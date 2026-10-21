---
title: Custom Path
articleKey: CustomPathObject3D
parent: "2D Paths"
nav_order: 3
description: Draw any flat shape point by point, with curves and straight lines, then turn it into a 3D part.
keywords: draw a shape, sketch, polygon, bezier, spline, freehand, profile, control points, edit points
---
# Custom Path

Draw your own 2D path with control points. This gives you complete freedom to create any 2D shape that can then be extruded or revolved into a 3D object.

<!-- IMAGE_NEEDED: Screenshot showing a custom path being edited in the Properties panel's path editor, with its toolbar (Reset Zoom, Sharp, Matched, Aligned, Free, Mirror, the X and Y boxes and the pop-out button) -->


## How to Use

1. Add **Custom Path** from the 2D Primitives folder (in the Library, or under **Add to Bed**)
2. Edit its points in the path editor in the Properties panel (see below)
3. Apply [Linear Extrude](../operations/path/linear-extrude.md) or other path operations to create a 3D object

## Editing the Path

The path editor in the Properties panel shows the path with its points and their curve handles:

- **Drag** a point or a handle to move it
- **Double-click** a segment to add a point there
- **Delete** removes the selected points
- **Ctrl + scroll** (⌘ + scroll on Mac) zooms; **Ctrl + drag** (⌘ + drag) pans. **Reset Zoom** (the home button) fits the path again
- Type an exact position, or a formula such as `=height`, in the **X** and **Y** boxes to place the selected point (see [Points That Follow a Formula](#points-that-follow-a-formula))

The four point buttons set how the selected point's handles behave:

- **Sharp** - a sharp corner with no handles
- **Matched** - handles in a straight line and of equal length, for a smooth curve
- **Aligned** - handles in a straight line, each its own length
- **Free** - handles move independently

**Mirror** turns on symmetry: edits are mirrored across the vertical line x = 0, so you only draw half of a symmetric shape. The pop-out button on the editor's toolbar moves the editor into its own window, for more room.

## Points That Follow a Formula

A corner or curve point's **X** and **Y** can each be a formula instead of a number, so the point moves when the value it reads changes:

1. Click the point in the path editor to select it
2. In the **X** or **Y** box on the editor's toolbar, type a formula starting with `=`, for example `=width` for a [Variable Sheet](../workspace/variable-sheet.md) cell, or `=Base.Width` for another part's setting (see [Object References](../workspace/object-references.md)), and press Enter

The point moves to the formula's value, and moves again whenever the value changes. Each box is separate: one axis can follow a formula while you still drag the point along the other. A dragged point doesn't move along an axis a formula sets. To hand an axis back to dragging, type a plain number in its box.

If a formula names something that isn't there, an orange **!** beside the box says what is wrong.

When the [AI](../getting-started/ai-tab.md) draws a path for you, it can give its corner and curve points formulas too. A circular arc it draws takes numbers only: its ends, center and radius are fixed when the arc is drawn, so draw a point that must follow a formula with a line or a curve.

## Open and Closed Paths

The **Closed** checkbox controls whether the path joins its last point back to its first.

- **Closed** (the default) makes the path outline a region. This is what [Linear Extrude](../operations/path/linear-extrude.md) and [Revolve](../operations/path/revolve.md) fill.
- **Open** makes the path a line. A line encloses nothing, so it shows in the scene as a thin ribbon along its length rather than as a filled shape. Use [Inflate Path](../operations/path/inflate-path.md) to give it a width and turn it back into something solid.

Two things to know before you uncheck **Closed**:

- **Re-closing is not an undo.** Opening a path throws away its closing segment. If that segment was curved, checking **Closed** again brings back a straight line, not the curve. Use Ctrl+Z instead - undo restores the original path exactly.
- **Some contours refuse to open.** A contour that would be left with fewer than two points - a teardrop drawn as a single point and a curve looping back to it - stays closed rather than collapsing into something you could no longer see or click. So does a contour holding a quadratic curve, which an imported SVG can contain: opening it would flatten the curve into a corner. The refusal is per contour, so the rest of the path still opens.

If a path has several contours and they do not agree, the checkbox reads as open. Checking it brings every contour into line.

Operations that need a region will close an open path for you rather than refuse it. Linear Extrude, Revolve, Subtract and the other boolean operations all do this, so an open path extrudes to the same solid its closed version would.

## Tips

- Use Custom Path when none of the built-in path shapes match what you need
- For importing shapes from external vector editors, see [SVG Object](../primitives/svg-object.md)
- To draw a line and turn it into a part, uncheck **Closed**, apply [Inflate Path](../operations/path/inflate-path.md) to give it a thickness, then [Linear Extrude](../operations/path/linear-extrude.md) to give it height

## Related

- [Circle Path](circle-path.md) - A ready-made circle
- [Box Path](box-path.md) - A ready-made rectangle
- [SVG Object](../primitives/svg-object.md) - Import vector paths from SVG files
- [Linear Extrude](../operations/path/linear-extrude.md) - Give paths height
