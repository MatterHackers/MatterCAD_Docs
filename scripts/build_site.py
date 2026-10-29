# Builds what GitHub Pages publishes from this repository (`_site/`). MatterCAD's help is read
# at https://mattercad.com/help/, so the Pages site no longer shows articles. It keeps two kinds
# of files that MatterCAD reads from it, at the same addresses:
#
# - `assets/**`: the help pictures. Articles embed them by their absolute Pages address, and the
#   desktop app, mattercad.com/help and every earlier MatterCAD version load them from there.
# - `help-docs.zip`: every help article (and translation) that MatterCAD downloads to show its
#   Help offline. Installed apps fetch it from this address.
#
# Every address where the old site showed an article now holds a small page that sends the
# visitor to the same article on mattercad.com/help, keeping the `#section` they linked to, so
# old links and bookmarks still land. The old site turned `Help/x/y.md` into `Help/x/y.html`
# (which Pages also serves at `Help/x/y`), a folder's `index.md` into `<folder>/index.html`
# (served at `<folder>/`), and the root `docs/index.md` into the site's front page.
#
# Usage: python3 scripts/build_site.py [--out _site]   (run from anywhere; paths are taken
# relative to this repository). scripts/test_build_site.py tests it.

import argparse
import html
import os
import shutil
import sys
import zipfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Where help is read now. Its addresses mirror the articles' paths under Help/:
# `Help/<path>.md` is `<HELP_SITE><path>`, a folder's index is `<HELP_SITE><folder>/`.
HELP_SITE = "https://mattercad.com/help/"

MOVED_TEXT = "MatterCAD's help has moved to mattercad.com/help."


def front_matter_title(md_path):
    """The `title:` from a Markdown file's front matter, or None when it has none."""
    with open(md_path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("title:"):
            value = line[len("title:"):].strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            return value or None
    return None


def redirect_target(rel_md):
    """The mattercad.com/help address for a page the old site published from `docs/<rel_md>`
    (a forward-slash path such as "Help/primitives/cube.md")."""
    if not rel_md.startswith("Help/"):
        # The old front page (and anything else outside Help/) goes to the help index.
        return HELP_SITE
    page = rel_md[len("Help/"):-len(".md")]
    if page == "index":
        return HELP_SITE
    if page.endswith("/index"):
        return HELP_SITE + page[: -len("index")]
    return HELP_SITE + page


def output_path(rel_md):
    """Where the old site wrote the page for `docs/<rel_md>`, relative to the site root."""
    if rel_md == "index.md":
        return "index.html"
    return rel_md[: -len(".md")] + ".html"


def redirect_page(title, target):
    """The HTML that sends a visitor to `target`, carrying their `#anchor` along."""
    t = html.escape(target, quote=True)
    heading = html.escape(title if title else "MatterCAD Help", quote=False)
    # json-style string literal for the script: the target is a plain https address, but escape
    # it anyway so nothing in it can end the script.
    js_target = target.replace("\\", "\\\\").replace('"', '\\"').replace("<", "\\u003c")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{heading} - MatterCAD Help</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{t}">
<meta http-equiv="refresh" content="0; url={t}">
<script>
// The refresh above drops the #section the visitor linked to; go with it instead.
location.replace("{js_target}" + location.hash);
</script>
</head>
<body>
<h1>{heading}</h1>
<p>{MOVED_TEXT} <a href="{t}">Read this page there</a>.</p>
</body>
</html>
"""


def published_markdown(docs_root):
    """Every Markdown file the old site turned into a page, as forward-slash paths relative to
    `docs/`, sorted. Folders whose names start with `_` or `.` held the theme's files, not pages."""
    pages = []
    for root, dirs, files in os.walk(docs_root):
        dirs[:] = sorted(d for d in dirs if not d.startswith(("_", ".")))
        for fname in sorted(files):
            if fname.lower().endswith(".md"):
                rel = os.path.relpath(os.path.join(root, fname), docs_root)
                pages.append(rel.replace("\\", "/"))
    return sorted(pages)


def write_redirects(docs_root, out_dir):
    """Writes one redirect page per published article; returns {output path: target}."""
    written = {}
    for rel_md in published_markdown(docs_root):
        target = redirect_target(rel_md)
        title = front_matter_title(os.path.join(docs_root, rel_md))
        out_rel = output_path(rel_md)
        out_file = os.path.join(out_dir, *out_rel.split("/"))
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        with open(out_file, "w", encoding="utf-8", newline="\n") as f:
            f.write(redirect_page(title, target))
        written[out_rel] = target
    return written


def copy_assets(docs_root, out_dir):
    """Copies `docs/assets/` to `<out>/assets/` byte for byte."""
    source = os.path.join(docs_root, "assets")
    if os.path.isdir(source):
        shutil.copytree(source, os.path.join(out_dir, "assets"))


def build_help_zip(repo_root, zip_path):
    """Writes help-docs.zip: every .md and .json under docs/Help/ as `Help/...`, then each
    translation's `<lang>/Help/**.md`. The app builds its help tree from the zip's folders and
    reads article titles from their front matter, so no table of contents is needed. Entries are
    in sorted folder-walk order so the zip is the same from one build to the next."""
    docs_root = os.path.join(repo_root, "docs")
    help_root = os.path.join(docs_root, "Help")
    translations_root = os.path.join(repo_root, "translations")
    included_extensions = {".md", ".json"}
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(help_root):
            dirs.sort()
            for fname in sorted(files):
                if os.path.splitext(fname)[1].lower() in included_extensions:
                    full_path = os.path.join(root, fname)
                    # Entry path relative to docs/, e.g. "Help/operations/array-linear.md"
                    arc_name = os.path.relpath(full_path, docs_root).replace("\\", "/")
                    zf.write(full_path, arc_name)

        # Translated articles live outside docs/ and are never pages of their own. Each language
        # contributes "<lang>/Help/..." entries alongside the English tree.
        if os.path.isdir(translations_root):
            for lang in sorted(os.listdir(translations_root)):
                lang_help = os.path.join(translations_root, lang, "Help")
                if not os.path.isdir(lang_help):
                    continue
                for root, dirs, files in os.walk(lang_help):
                    dirs.sort()
                    for fname in sorted(files):
                        if os.path.splitext(fname)[1].lower() == ".md":
                            full_path = os.path.join(root, fname)
                            # Entry path relative to translations/, e.g. "de/Help/operations/array-linear.md"
                            arc_name = os.path.relpath(full_path, translations_root).replace("\\", "/")
                            zf.write(full_path, arc_name)
        return len(zf.namelist())


def build_site(repo_root, out_dir):
    """Builds the whole published site into `out_dir` (emptied first); returns the redirects."""
    if os.path.isdir(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir)
    docs_root = os.path.join(repo_root, "docs")
    copy_assets(docs_root, out_dir)
    entries = build_help_zip(repo_root, os.path.join(out_dir, "help-docs.zip"))
    redirects = write_redirects(docs_root, out_dir)
    print(f"Generated help-docs.zip with {entries} entries and {len(redirects)} redirect pages")
    return redirects


def main(argv):
    parser = argparse.ArgumentParser(description="Build the GitHub Pages site into _site/.")
    parser.add_argument("--out", default=os.path.join(REPO_ROOT, "_site"))
    args = parser.parse_args(argv)
    build_site(REPO_ROOT, os.path.abspath(args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
