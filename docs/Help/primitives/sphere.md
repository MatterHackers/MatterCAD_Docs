---
title: Sphere
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
---
# Sphere

A round ball shape with adjustable diameter and detail level.

<!--  Screenshot of a Sphere primitive on the workspace -->
![20260318 183909 paste 20260318 183909](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183909-paste-20260318-183909.jpg)


## Parameters

- **Diameter** - The width across the sphere, in mm (default 20)
- **Sides** - Number of segments around the sphere (default 40; 3 to 360). More is smoother. Without Advanced, the same number is used from top to bottom
- **Advanced** - Off by default. Turn it on for the options below

### Advanced Parameters

- **Starting Angle** - Where the sphere begins around its vertical axis, in degrees (default 0)
- **Ending Angle** - Where the sphere ends, in degrees (default 360). Less than 360 cuts out a wedge, like an orange with segments removed
- **Latitude Sides** - Number of segments from top to bottom (default 30; 3 to 180). More is smoother

## Tips

- 40 sides is smooth enough for most parts. Higher values create smoother surfaces but larger files
- Starting and Ending Angle cut the sphere from top to bottom, like orange segments. For a dome, use a [Half Sphere](half-sphere.md)
- Combine with [Subtract](../operations/boolean/subtract.md) to create spherical cavities

## Related

- [Half Sphere](half-sphere.md) - Just the top hemisphere
- [Torus](torus.md) - A donut shape
