---
title: Sphere
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
description: Add a ball of any diameter, as smooth as you like.
keywords: ball, globe, orb, round ball, bead
---
# Sphere

A round ball shape with adjustable diameter and detail level.

<!-- AUTO_IMAGE: type=shot id=primitives-sphere -->
![A Sphere selected in the 3D view beside its Properties panel: Diameter, Sides and Advanced, with the line saying Advanced gives more options](https://matterhackers.github.io/MatterCAD_Docs/assets/primitives-sphere.png)


## Parameters

- **Diameter** - The width across the sphere, in mm (default 20)
- **Sides** - Number of segments around the sphere (default 40; 3 to 360). More is smoother. Without Advanced, the same number is used from top to bottom
- **Grow From** - Which side of the part stays where it is when you change its size: **Center** (the default) grows it the same amount on every side, **Front Left** keeps its front and left sides in place so it grows toward the back and right, and **Back Right** keeps its back and right sides in place so it grows toward the front and left. The sides are the part's own, so a part you have turned grows along its own sides. The bottom always stays where it is. It applies when **Diameter** changes, whether you type it or a formula changes it; other settings don't use it. It is the last row in the panel, below the Advanced rows, and shows whether Advanced is on or off
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
