---
title: Half Cylinder
articleKey: HalfCylinderObject3D
parent: "Primitives"
nav_order: 6
description: Add a shape with a flat bottom and a round top, half of a cylinder lying along its length.
keywords: half round, semicircle, rounded top, half pipe, tunnel
---
# Half Cylinder

A solid cylinder cut in half lengthwise: a flat bottom with a round top, lying along Y. Its height is half its Width.

<!-- AUTO_IMAGE: type=shot id=primitives-half-cylinder -->
![A Half Cylinder lying along Y, its round side toward you, selected beside its Properties panel: Width, Depth and Sides](https://matterhackers.github.io/MatterCAD_Docs/assets/primitives-half-cylinder.png)


## Parameters

- **Width** - The size across the flat bottom (X), which is also the diameter of the curve, in mm (default 20)
- **Depth** - The length along Y, in mm (default 20)
- **Sides** - Number of segments around the curved surface (default 20; 3 to 180)
- **Grow From** - Which side of the part stays where it is when you change its size: **Center** (the default) grows it the same amount on every side, **Front Left** keeps its front and left sides in place so it grows toward the back and right, and **Back Right** keeps its back and right sides in place so it grows toward the front and left. The sides are the part's own, so a part you have turned grows along its own sides. The bottom always stays where it is. It applies when **Width** or **Depth** changes, whether you type it or a formula changes it; other settings don't use it. It is the last row in the panel

## Tips

- Useful for rounded tops, bumps and ridges. For a hollow channel or gutter, [Subtract](../operations/boolean/subtract.md) a smaller Half Cylinder from a larger one
- Rotate to use as an arch or tunnel cross-section
- Combine with a [Cube](cube.md) for objects with one rounded side

## Related

- [Cylinder](cylinder.md) - A full round column
- [Half Sphere](half-sphere.md) - A dome shape
- [Half Wedge](half-wedge.md) - A ridge with sloped sides
