---
title: Wedge
articleKey: WedgeObject3D_2
parent: "Primitives"
nav_order: 18
---
# Wedge

A triangular prism shape -- like a cube cut diagonally from one edge to the opposite edge. Useful for ramps, supports, and angled surfaces.

<!--  Screenshot of a Wedge primitive on the workspace -->
![20260318 184625 paste 20260318 184625](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184625-paste-20260318-184625.jpg)


## Parameters

- **Width** - Size along the X axis (default: 20mm)
- **Depth** - Size along the Y axis (default: 20mm)
- **Height** - How tall the wedge is at its tallest point (default: 20mm)
- **Round** - Shapes the sloped face: **None** (default) keeps it flat, **Up** bulges it outward in a curve, **Down** curves it inward
- **Round Segments** - How many steps make the curved face (default 15; 2 to 90). More is smoother. Shown only with Round set to Up or Down

## Tips

- Wedges are great for creating ramps, angled brackets, and support structures
- Use Round **Down** for a curved ramp, or **Up** for a quarter-round molding

## Related

- [Half Wedge](half-wedge.md) - A ridge with two sloped sides
- [Pyramid](pyramid.md) - A four-sided pointed shape
- [Cube](cube.md) - A rectangular box
