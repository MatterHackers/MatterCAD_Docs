---
title: Half Sphere
articleKey: HalfSphereObject3D
parent: "Primitives"
nav_order: 7
description: Add a dome, the top half of a ball, for rounded caps, covers and lenses.
keywords: dome, hemisphere, cap, half ball, rounded cover
---
# Half Sphere

The top hemisphere of a sphere -- a dome shape. Useful for creating domed tops, lens shapes, and rounded covers.

<!--  Screenshot of a Half Sphere primitive on the workspace -->
![20260318 183343 paste 20260318 183343](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183343-paste-20260318-183343.jpg)


## Parameters

- **Diameter** - The width across the base of the dome (default: 20mm)
- **Longitude Sides** - Number of segments around the perimeter (default: 40)
- **Latitude Sides** - Number of segments from base to top (default: 10). More = smoother dome
- **Grow From** - Which side of the part stays where it is when you change its size: **Center** (the default) grows it the same amount on every side, **Front Left** keeps its front and left sides in place so it grows toward the back and right, and **Back Right** keeps its back and right sides in place so it grows toward the front and left. The sides are the part's own, so a part you have turned grows along its own sides. The bottom always stays where it is. It applies when **Diameter** changes, whether you type it or a formula changes it; other settings don't use it. It is the last row in the panel

## Tips

- Combine two half spheres with a cylinder for a capsule shape
- Place on top of a cylinder to create a domed lid or button
- Use with [Subtract](../operations/boolean/subtract.md) to create dome-shaped cavities

## Related

- [Sphere](sphere.md) - A full ball shape
- [Half Cylinder](half-cylinder.md) - A cylinder cut in half
