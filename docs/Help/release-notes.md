---
title: Release Notes
nav_order: 104
---
# MatterCAD 2.2026.8 (August 10, 2026)
[Windows Download](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## New Features

* **Edit Children**
  * Double-click an object on the bed or in the Scene Tree to step inside it and edit the parts it is built from — no separate window or tab
  * For operations like Subtract, you edit the source parts and the result rebuilds when you come back out
  * A breadcrumb across the top of the Scene Tree shows the full path; clicking a level folds your edits in as one undoable step, and each level keeps its own undo history
  <!-- IMAGE: gif — Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->

* **One Boolean Tool**
  * Combine, Subtract, Intersect, and Subtract and Replace are now a single operation with an icon row at the top of its panel — switch modes with a click instead of deleting and re-applying
  * The same operation handles both 3D meshes and 2D paths, and shows progress while a heavy boolean runs
  * Designs saved with the older separate boolean objects continue to open normally
  <!-- IMAGE: static — Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->

* **Booleans That Just Work**
  * Booleans run on a new native engine that is faster and succeeds on meshes that previously failed
  * Combine repairs parts with holes automatically: clean repairs join the union, parts that cannot be safely merged are kept beside it and named for you, and a part that could not be repaired keeps your original geometry
  * Plane Cut is now a true solid intersection, so the result is watertight and printable instead of an open shell
  * New Keep Inside Out Geometry and Repair Winding Order options for troublesome imported meshes
  <!-- IMAGE: gif — Combine on a holey imported model: fails before, completes after with leftover parts named. ~700x400px -->

* **Sweep**
  * Sweep a 2D profile along a 3D Curve rail to build tubes, handles, rails, and trim
  * Drag the Scale and Twist handles directly in the 3D view to taper and twist the shape by eye
  * Applying Sweep with no rail adds a default S-curve rail so you can start shaping immediately
  <!-- IMAGE: gif — Apply Sweep to a circle and a 3D Curve, then drag a scale sphere to taper it. ~700x450px -->

* **Loft**
  * Skin a solid between stacked 2D cross-sections — each path child contributes a section at its Z height
  * Applying Loft to a selection that includes a 3D Curve creates a Sweep instead, since that is what the curve was for
  <!-- IMAGE: gif — Stack three profiles at different heights and apply Loft. ~700x450px -->

* **Open Paths**
  * 2D paths can now be open lines as well as closed regions, with a Closed checkbox
  * Open contours draw as a thin ribbon and can be inflated with end-cap styles
  <!-- IMAGE: static — A path with Closed unchecked, shown as an open ribbon on the bed. ~500x350px -->

## Improvements

* **2D Path Editor**
  * Four point modes — Sharp, Symmetric, Aligned, and Free — applied with one click, in both the 2D editor and the 3D view
  * Mirror is now a live symmetry mode: edits mirror across the center as you make them, and dragging a mirrored pair onto the axis merges it to a single point
  * Drag-select points with a rubber band, move them as a group, snap to the grid, and press Esc to cancel a drag
  * Smooth fits a curve through your clicked-out points in one step
  <!-- IMAGE: gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->

* **Viewing and Navigation**
  * Press Z with a flat path selected to animate to a straight-down editing view fitted to the path
  * The Scene Tree header is now one row: a breadcrumb that names the document and grows into a clickable path as you drill in
  * The 3D view renders fully anti-aliased on the first frame instead of converging over many frames, and thumbnails have smoother edges
  * Sub-pixel text rendering is now on automatically when your display supports it, and can still be turned on or off under Advanced settings

* **Modeling**
  * Linear Extrude can bevel the bottom edge with its own style, radius, and segment count
  * Editor-only objects (3D Curve, Measure Tool, Description, Sheet) still display but are excluded from export

* **Errors You Can See**
  * Failed saves, failed background tasks, and cloud problems now appear as dismissible notifications instead of being silently swallowed

* **Print Farm and Job Manager**
  * Faster repeat upload passes, a working Stop button, and recovery when a print-farm credential is rotated or revoked

## Top Bug Fixes

* **Save Reliability**
  * A save that failed part-way could truncate the file it was replacing while reporting success. Saves now complete fully, then replace the destination atomically — the same protection covers library saves and exports
  * A failed save leaves the design marked unsaved, so closing the app cannot silently discard your work

* **Align**
  * Every rebuild snapped children back on all three axes, erasing any move you made on an axis Align was not controlling. Align now only resets the axes it controls

* **Cloud and GitHub Libraries**
  * A rate-limit or not-found response from GitHub crashed the library folder; errors now appear as a message on the folder instead
  * Saving a cloud item to disk kept the old tab name and lost the tab on restart

* **Booleans and Selection**
  * The Part(s) to Subtract radios could show two parts selected and refuse to let you pick just one
  * 2D Subtract dropped every kept part after the first

* **File Loading**
  * Fixed 3MF sub-models being silently dropped on load, and 3MF files loaded at the same time contaminating each other

* **Image Converter**
  * Fixed crashes, a broken histogram filter, and copies of an image part not staying in sync with the original

* **Path Editing**
  * Fixed a crash when deleting a curve point, and points at a closed path's seam reverting the mode you chose

* **Interface**
  * Fixed a crash when dragging the Text Size slider in Application Settings
  * The Stop button on a running task is now clickable and actually cancels

---

# MatterCAD 2.2026.5 (May 8, 2026)
[Windows Download](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## New Features

* **Redesigned Array Tool**
  * Single unified Array operation replaces the old Linear Array, Radial Array, and Advanced Array
  * **Linear** mode: copies along a direction with optional rotation and progressive scale
  * **Radial** mode: copies around a central axis with configurable radius, sweep angle, and arc or full-circle patterns
  * **Transform** mode: step copies using a manual transform or a named sibling object's transform
  * Compounding rotation mode in Linear creates spirals, fans, and helices naturally
  * Scale Affects Offset option for nautilus-shell and geometric-progression layouts
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **Library Favorites**
  * Star any library item to add it to a persistent Favorites folder
  * Quickly access your most-used primitives, generators, and saved parts from one place
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## Improvements

* **Align**
  * Stacked alignment is now a direct mode button instead of a dropdown option
  * Added clearer Simple, Offset, and Stacked modes for lining up edges, adding precise gaps, and building ordered stacks
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **File Support**
  * Added support for WEBP image format in image-based operations
  * Improved SVG file parsing for more reliable imports

* **Reliability**
  * Improved 3MF file loading speed and reliability
  * Better tab restoration between sessions

## Top Bug Fixes

* **Login and Cloud Library Access**
  * Login and Cloud Library access are restored after a backend server upgrade broke sign-in.
  * MatterCAD now prompts you to sign in again when cloud access finds expired or invalid credentials.

* **Scene Tree Selection**
  * Fixed inconsistent selection behavior when choosing objects from the scene tree.

* **Help Navigation**
  * Fixed navigation issues in the bundled help and release documentation.

* **Library Right-Click**
  * Fixed right-click behavior in the library tree view.

* **Sheets**
  * Fixed a crash that could happen while working with sheets.

---

# MatterCAD 2.2026.3 (March 12, 2026)
[Windows Download](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## New Features

* **All-New Direct3D 11 Rendering Engine**
  * Complete migration from OpenGL to Direct3D 11 for dramatically better performance
  * FXAA anti-aliasing for crisp, clean edges
  * Dual depth peeling for correct order-independent transparency
  * Hardware-accelerated bed shadows
  * Improved object outlines and selection visuals
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **Object Transparency**
  * Set alpha/transparency on any individual object in the scene
  * Per-face color meshes support alpha without color damage
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **Lock & Hide Objects**
  * Lock objects to prevent accidental selection or editing
  * Hide objects to reduce visual clutter while working on specific parts
  * Unhide All and Unlock All commands to quickly restore visibility
  * Locked and hidden objects are correctly excluded from ray-based selection
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **Improved Boolean Subtract**
  * Multi-subtract operations are significantly more reliable and accurate

## Improvements

* **File Handling**
  * Projects now save as 3MF by default instead of STL, preserving colors, materials, and design history
  * Enhanced drag-and-drop support for files and folders into the 3D view

* **Workflow**
  * Save As and Move dialogs remember your last folder location
  * Expression fields now support `pi`, `tau`, `e`, and `count`
  * Esc key performs undo in design editing contexts
  * 3D controls remain visible when mouse leaves the scene

* **Performance & Stability**
  * Fixed startup crashes and recursive load issues
  * Fixed lighting and mipmapping rendering bugs
  * Improved library tree view updates
  * Dynamic near/far plane calculations for better zoom behavior
  * Upgraded to .NET 10

---

# MatterCAD 2.2025.6 (June 20, 2025)
[Windows Download](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## New Features

* **SVG File Support**  
  * Full drag-and-drop support for SVG files
  * Direct conversion from SVG graphics to 3D objects
  * Seamless integration with existing CAD workflows

* **Advanced OBJ File Handling**  
  * Support for loading materials from ZIP archives
  * Enhanced OBJ file parsing and material handling
  * Better support for complex 3D models with multiple materials

* **Enhanced Tab Management System**
  * Cloud library tabs now persist correctly - your work stays exactly where you left it
  * Improved tab organization and navigation
  * Automatic restoration of open tabs between sessions

## User Experience Enhancements

* **Streamlined Interface**
  * Reorganized Recent menu for faster access
  * Better visual feedback during long operations
  * Improved application startup time and responsiveness

* **Reliability**
  * Fixed critical crashes in 3D scene interactions
  * Resolved memory management issues
  * Improved application stability across all platforms

---

# MatterCAD 2.21.5 (Feb 13, 2025)

[Windows Download](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# Existing Features

*The following features represent the foundation that MatterCAD builds upon from MatterControl's heritage:*

* Added Hollow Feature  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* Added Polygon Reduce  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* Added Mesh Repair  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* Put in fully automatic support (legacy support) as an opption in additon to new manual support option
* Added Support for gsSlicer (Experimental new slicing engine)
* Fixed bugs

## Changes

* Improved ungrouping of mesh (splitting into multiple meshes)
    * Discard degenerate faces
    * Discard microscopic discrete features

## Changes

* Added search bar for application
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* Improved design tool bar
    * Added grouping to some items
    * Added dual align button
    * Added Arrange All button
* Nudge items on the bed with arrow keys
* Downloads folder is sorted by date

## Changes

* UI improvements
    * Faster updates in Cloud Library folders
    * Restore UI on re-open
    * Better Keyboard navigation support
* New error detection and warning system
    * More hardware errors handled
* Design tools improvements and optimizations
    * New Twist tools 
    * Improved Curve tool
    * Improved Align


## Changes

* Improved flatten
* Improved Undo support
* Improved design history

## Changes
* Versioning: Moving to a (version).(year).(month) version number. Easier to read and more informative.
* New State-of-the-art Subtract, Combine and Intersection (Window only)
* We now start up with a 'Feature Tour' to help new users find their way

## Changes
* Design Tools - The ability to 3D model with a complete set of modeling primitives
* Use a primitive to create your own customized supports
* Design Apps - Design Apps: sophisticated customizable designs
* 64-bit Processing