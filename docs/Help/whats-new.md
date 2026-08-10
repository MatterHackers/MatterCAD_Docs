---
title: What's New
nav_order: 105
---
# MatterCAD 2.2026.8

<!-- HERO_IMAGE: GIF — Double-click a Subtract on the bed to drill into it, move a source part, then click the document name in the breadcrumb to return and see the result update. ~800x450px -->

# What's New

* **Edit Children**
  * Double-click any object to step inside it and edit the parts it is built from, right on the bed
  * A breadcrumb shows where you are — click any level to fold your edits back in
  <!-- IMAGE: gif — Drill two levels into a nested group, edit a cube, then click back out through the breadcrumb. ~700x450px -->

* **One Boolean Tool**
  * Combine, Subtract, Intersect, and Subtract and Replace are now one operation — switch modes with a click instead of deleting and re-applying
  <!-- IMAGE: static — Boolean property panel showing the four-icon operation row with Subtract selected. ~500x350px -->

* **Booleans That Just Work**
  * A new engine is faster and succeeds on meshes that used to fail
  * Combine repairs parts with holes automatically and names anything it could not merge; Plane Cut now leaves a watertight, printable solid
  <!-- IMAGE: gif — Combine on a holey imported model: fails before, completes after. ~700x400px -->

* **Sweep and Loft**
  * Sweep a 2D profile along a 3D Curve to make tubes, handles, and rails; Loft skins a solid between stacked cross-sections
  * Drag the Sweep's scale and twist handles in the 3D view to taper and twist by eye
  <!-- IMAGE: gif — Apply Sweep to a circle plus a 3D Curve, then drag a scale sphere to taper the tube. ~700x450px -->

* **Better 2D Path Editing**
  * Point modes, live Mirror symmetry, grid snapping, drag-select, and Esc to cancel a drag
  * Paths can now be open lines as well as closed regions
  <!-- IMAGE: gif — Turn on Mirror, drag a point and watch its partner follow, then drag it onto the axis to merge. ~700x450px -->

## Improvements

* **Sharper Views** — The 3D view is fully anti-aliased on the first frame, and thumbnails have clean edges
* **Errors You Can See** — Failed saves, tasks, and cloud problems now appear as notifications instead of failing silently
* **Navigation** — Press Z with a 2D path selected for a top-down editing view
* **Crisper Text** — Sub-pixel text rendering is now on automatically when your display supports it

## Top Bug Fixes

* **Save Reliability** — A failed save can no longer damage the file it was replacing, and it tells you it failed
* **Align** — Moving a part on an axis Align isn't controlling is no longer erased
* **Cloud Library** — Library folders explain themselves when GitHub limits requests instead of crashing
* **Subtract** — The Part(s) to Subtract selector now picks exactly one part
* **File Loading** — Fixed 3MF parts being silently dropped on load

## You can view the full release notes [Here](release-notes.md).
