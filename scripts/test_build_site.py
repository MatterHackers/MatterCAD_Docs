# Tests scripts/build_site.py against the real docs/: every address the old help site published
# an article at still answers and sends the visitor to the same article on mattercad.com/help
# (with their #section), the pictures are published byte for byte, and help-docs.zip holds the
# same entries with the same contents as the zip the old deploy step wrote, since installed
# MatterCAD apps download both from the Pages site.
#
# Run: python3 -m unittest discover -s scripts -p 'test_*.py'   (from the repository root)

import filecmp
import os
import subprocess
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_site  # noqa: E402

REPO_ROOT = build_site.REPO_ROOT
DOCS_ROOT = os.path.join(REPO_ROOT, "docs")

# The help-docs.zip step the deploy workflow ran before the site was built by build_site.py,
# word for word except for where it writes the zip (it wrote into docs/). The new zip must match
# what it wrote, entry for entry.
OLD_ZIP_STEP = r'''
import os, zipfile

HELP_ROOT = "docs/Help"
TRANSLATIONS_ROOT = "translations"

included_extensions = {".md", ".json"}
with zipfile.ZipFile(OUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(HELP_ROOT):
        dirs.sort()
        for fname in sorted(files):
            if os.path.splitext(fname)[1].lower() in included_extensions:
                full_path = os.path.join(root, fname)
                arc_name = os.path.relpath(full_path, "docs").replace("\\", "/")
                zf.write(full_path, arc_name)

    if os.path.isdir(TRANSLATIONS_ROOT):
        for lang in sorted(os.listdir(TRANSLATIONS_ROOT)):
            lang_help = os.path.join(TRANSLATIONS_ROOT, lang, "Help")
            if not os.path.isdir(lang_help):
                continue
            for root, dirs, files in os.walk(lang_help):
                dirs.sort()
                for fname in sorted(files):
                    if os.path.splitext(fname)[1].lower() == ".md":
                        full_path = os.path.join(root, fname)
                        arc_name = os.path.relpath(full_path, TRANSLATIONS_ROOT).replace("\\", "/")
                        zf.write(full_path, arc_name)
'''


def all_markdown():
    """Every article source under docs/, forward-slash relative paths."""
    found = []
    for root, dirs, files in os.walk(DOCS_ROOT):
        dirs[:] = [d for d in dirs if not d.startswith(("_", "."))]
        for fname in files:
            if fname.endswith(".md"):
                found.append(os.path.relpath(os.path.join(root, fname), DOCS_ROOT).replace("\\", "/"))
    return sorted(found)


class BuildSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = os.path.join(cls.tmp.name, "_site")
        cls.redirects = build_site.build_site(REPO_ROOT, cls.out)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def read(self, rel):
        with open(os.path.join(self.out, *rel.split("/")), encoding="utf-8") as f:
            return f.read()

    def test_every_article_has_a_redirect_at_its_old_address(self):
        sources = all_markdown()
        self.assertGreater(len(sources), 100)
        for rel_md in sources:
            old_page = rel_md[: -len(".md")] + ".html" if rel_md != "index.md" else "index.html"
            with self.subTest(article=rel_md):
                self.assertTrue(os.path.isfile(os.path.join(self.out, *old_page.split("/"))), old_page)
                target = self.redirects[old_page]
                page = self.read(old_page)
                self.assertIn(f'<meta http-equiv="refresh" content="0; url={target}">', page)
                self.assertIn(f'<link rel="canonical" href="{target}">', page)
                self.assertIn('<meta name="robots" content="noindex">', page)
                self.assertIn(f'<a href="{target}">', page)
                self.assertIn(build_site.MOVED_TEXT, page)
        self.assertEqual(len(self.redirects), len(sources))

    def test_articles_go_to_the_same_path_on_mattercad_com(self):
        self.assertEqual(
            self.redirects["Help/operations/boolean/subtract.html"],
            "https://mattercad.com/help/operations/boolean/subtract",
        )
        self.assertEqual(
            self.redirects["Help/workspace/keyboard-shortcuts.html"],
            "https://mattercad.com/help/workspace/keyboard-shortcuts",
        )
        self.assertEqual(
            self.redirects["Help/primitives/cube.html"], "https://mattercad.com/help/primitives/cube"
        )

    def test_folder_indexes_go_to_the_folder_and_the_root_to_the_help_index(self):
        # Pages serves `<folder>/index.html` at `<folder>/` too, so old folder links land here.
        self.assertEqual(self.redirects["Help/primitives/index.html"], "https://mattercad.com/help/primitives/")
        self.assertEqual(
            self.redirects["Help/operations/boolean/index.html"],
            "https://mattercad.com/help/operations/boolean/",
        )
        self.assertEqual(self.redirects["Help/index.html"], "https://mattercad.com/help/")
        self.assertEqual(self.redirects["index.html"], "https://mattercad.com/help/")

    def test_pages_outside_help_go_to_the_help_index(self):
        self.assertEqual(build_site.redirect_target("other/page.md"), "https://mattercad.com/help/")

    def test_a_redirect_carries_the_visitors_section_anchor(self):
        page = self.read("Help/primitives/cube.html")
        self.assertIn('location.replace("https://mattercad.com/help/primitives/cube" + location.hash);', page)

    def test_a_redirect_shows_the_articles_title(self):
        self.assertIn("<h1>Subtract</h1>", self.read("Help/operations/boolean/subtract.html"))
        self.assertIn("<h1>Home</h1>", self.read("index.html"))

    def test_titles_are_escaped_for_html(self):
        page = build_site.redirect_page("Fish & <Chips>", "https://mattercad.com/help/x")
        self.assertIn("<h1>Fish &amp; &lt;Chips&gt;</h1>", page)
        self.assertNotIn("<Chips>", page)

    def test_no_theme_files_are_published(self):
        for name in ("_config.yml", "Gemfile", "_sass"):
            self.assertFalse(os.path.exists(os.path.join(self.out, name)), name)

    def test_pictures_are_published_byte_for_byte(self):
        source = os.path.join(DOCS_ROOT, "assets")
        names = sorted(os.listdir(source))
        self.assertGreater(len(names), 0)
        published = sorted(os.listdir(os.path.join(self.out, "assets")))
        self.assertEqual(published, names)
        match, mismatch, errors = filecmp.cmpfiles(
            source, os.path.join(self.out, "assets"), names, shallow=False
        )
        self.assertEqual((mismatch, errors), ([], []))

    def test_help_zip_matches_what_the_old_deploy_step_wrote(self):
        old_zip = os.path.join(self.tmp.name, "old-help-docs.zip")
        code = f"OUT_ZIP = {old_zip!r}\n" + OLD_ZIP_STEP
        subprocess.run([sys.executable, "-I", "-c", code], cwd=REPO_ROOT, check=True)
        with zipfile.ZipFile(old_zip) as old, zipfile.ZipFile(os.path.join(self.out, "help-docs.zip")) as new:
            self.assertEqual(new.namelist(), old.namelist())
            self.assertTrue(any(n.startswith("Help/") for n in new.namelist()))
            self.assertTrue(any("/Help/" in n and not n.startswith("Help/") for n in new.namelist()))
            for name in old.namelist():
                self.assertEqual(new.read(name), old.read(name), name)
                self.assertEqual(new.getinfo(name).compress_type, old.getinfo(name).compress_type, name)


if __name__ == "__main__":
    unittest.main()
