---
title: What's New
nav_order: 105
---
# MatterCAD 2.2026.8

# What's New

* **Edit Children**
  * Double-click any object to step inside it and edit the parts it is built from, right on the bed
  * A breadcrumb shows where you are — click any level to fold your edits back in
  * ![MatterCAD 2.2026.8](https://www.matterhackers.com/r/qgG4VA)

* **One Boolean Tool**
  * Combine, Subtract, Intersect, and Subtract and Replace are now one operation — switch modes with a click instead of deleting and re-applying
  <!-- Boolean property panel showing the four-icon operation row with Subtract selected. ~500x350px -->
  * ![One Boolean Tool](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)

* **Booleans That Just Work**
  * A new engine is faster and succeeds on meshes that used to fail
  * Combine repairs parts with holes automatically and names anything it could not merge; Plane Cut now leaves a watertight, printable solid

* **Better 2D Path Editing**
  * Point modes, live Mirror symmetry, grid snapping, drag-select, and Esc to cancel a drag
  <!-- Turn on Mirror, drag a point and watch its partner follow, then drag it onto the axis to merge. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

## Improvements

* **Navigation** — Press Z with a 2D path selected for a top-down editing view
* **Crisper Text** — Sub-pixel text rendering is now on automatically when your display supports it
* **Modeling** — Linear Extrude can bevel the bottom edge with its own style, radius, and segment count

## Top Bug Fixes

* **Save Reliability** — A failed save can no longer damage the file it was replacing, and it tells you it failed
* **Cloud Library** — Saving a cloud item to disk keeps its tab name, and the tab survives a restart
* **File Loading** — Fixed 3MF parts being silently dropped on load
* **Path Editing** — Fixed a crash when deleting a curve point, and seam points reverting the mode you chose
* **Background Tasks** — The Stop button on a running task is now clickable and actually cancels

## You can view the full release notes [Here](release-notes.md).
