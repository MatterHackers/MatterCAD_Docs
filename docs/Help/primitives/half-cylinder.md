---
title: Half Cylinder
articleKey: HalfCylinderObject3D
parent: "Primitives"
nav_order: 6
---
# Half Cylinder

A solid cylinder cut in half lengthwise: a flat bottom with a round top, lying along Y. Its height is half its Width.

<!--  Screenshot of a Half Cylinder primitive on the workspace -->
![20260318 183306 paste 20260318 183306](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183306-paste-20260318-183306.jpg)


## Parameters

- **Width** - The size across the flat bottom (X), which is also the diameter of the curve, in mm (default 20)
- **Depth** - The length along Y, in mm (default 20)
- **Sides** - Number of segments around the curved surface (default 20; 3 to 180)

## Tips

- Useful for rounded tops, bumps and ridges. For a hollow channel or gutter, [Subtract](../operations/boolean/subtract.md) a smaller Half Cylinder from a larger one
- Rotate to use as an arch or tunnel cross-section
- Combine with a [Cube](cube.md) for objects with one rounded side

## Related

- [Cylinder](cylinder.md) - A full round column
- [Half Sphere](half-sphere.md) - A dome shape
- [Half Wedge](half-wedge.md) - A ridge with sloped sides
