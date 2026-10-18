---
title: Cube
articleKey: CubeObject3D
parent: "Primitives"
nav_order: 4
---
# Cube

A rectangular box shape with adjustable width, depth, height, and optional rounded edges. The Cube is one of the most commonly used primitives for building designs.

<!--  Screenshot of a Cube primitive on the workspace -->
![20260318 183230 paste 20260318 183230](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183230-paste-20260318-183230.jpg)


## Parameters

- **Width** - Size along the X axis (default: 20mm)
- **Depth** - Size along the Y axis (default: 20mm)
- **Height** - Size along the Z axis (default: 20mm)
- **Round** - Off by default. Turn it on to round every edge
- **Radius** - The size of the rounding, in mm (default 3; the slider runs 0 to 20). Shown only with Round on
- **Round Segments** - How many steps make each rounded edge (default 9; 1 to 20). More is smoother. Shown only with Round on

## Tips

- Use a Cube as the starting point for boxes, plates, brackets, and enclosures
- Enable Round for smooth, professional-looking edges
- The Radius cannot exceed half of the smallest dimension
- Combine a Cube with [Subtract](../operations/boolean/subtract.md) to create rectangular cutouts and slots

## Related

- [Cylinder](cylinder.md) - Round column shape
- [Pyramid](pyramid.md) - Tapered four-sided shape
- [Hole](hole.md) - A cube pre-configured for boolean subtraction
