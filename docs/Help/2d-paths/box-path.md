---
title: Box Path
articleKey: BoxPathObject3D
parent: "2D Paths"
nav_order: 1
---
# Box Path

A rectangular 2D path, added as **Box** from the 2D Primitives. Use with [Linear Extrude](../operations/path/linear-extrude.md) to create box shapes, or as a base for other path operations.

<!-- Screenshot of a Box Path on the workspace -->
![20260506 080026 paste 20260506 080026](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080026-paste-20260506-080026.jpg)


## Parameters

- **Width** - The size of the rectangle along X, in mm (default 20)
- **Depth** - The size of the rectangle along Y, in mm (default 20)
- **Round** - Off by default. Turn it on to round all four corners
- **Radius** - The corner radius, in mm (default 3; the slider runs 0 to 20). Shown only with Round on
- **Round Segments** - How many straight pieces make each rounded corner (default 9; the slider runs 1 to 30). More is smoother. Shown only with Round on
- **Plane** - The [construction plane](../workspace/construction-planes.md) the rectangle is drawn on (default XY, flat on the bed)

## Tips

- A Box Path plus Linear Extrude creates a shape similar to a [Cube](../primitives/cube.md), but you can apply path operations like [Inflate](../operations/path/inflate-path.md) or [Fillet](../operations/reshape/fillet.md) before extruding

## Related

- [Circle Path](circle-path.md) - A circular 2D path
- [Star Path](star-path.md) - A star-shaped 2D path
- [Linear Extrude](../operations/path/linear-extrude.md) - Give paths height
