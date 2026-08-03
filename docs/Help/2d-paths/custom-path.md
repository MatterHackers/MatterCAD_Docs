---
title: Custom Path
articleKey: CustomPathObject3D
parent: "2D Paths"
nav_order: 3
---
# Custom Path

Draw your own 2D path with control points. This gives you complete freedom to create any 2D shape that can then be extruded or revolved into a 3D object.

<!-- Screenshot showing a custom path being edited with control points -->
![20260506 080247 paste 20260506 080247](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080247-paste-20260506-080247.jpg)


## How to Use

1. Add a **Custom Path** from the 2D Paths library
2. Edit the control points to define your shape
3. Apply [Linear Extrude](../operations/path/linear-extrude.md) or other path operations to create a 3D object

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
