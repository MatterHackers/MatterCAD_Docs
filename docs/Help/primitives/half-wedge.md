---
title: Half Wedge
articleKey: HalfWedgeObject3D
parent: "Primitives"
nav_order: 8
description: Add a ridge shaped like a roof, with two slopes meeting at a peak.
keywords: roof, ridge, peak, triangular prism, gable, a-frame
---
# Half Wedge

A ridge: a triangular prism whose two sloped sides meet at a peak centered across its Width, like a roof. Useful for roof shapes, ridges and pointed features.

<!-- AUTO_IMAGE: type=shot id=primitives-half-wedge -->
![A Half Wedge selected in the 3D view beside its Properties panel: Width, Depth and Height](https://matterhackers.github.io/MatterCAD_Docs/assets/primitives-half-wedge.png)


## Parameters

- **Width** - Size along the X axis, across the two slopes, in mm (default 20)
- **Depth** - Size along the Y axis, the length of the ridge, in mm (default 20)
- **Height** - How tall the peak is, in mm (default 10)
- **Grow From** - Which side of the part stays where it is when you change its size: **Center** (the default) grows it the same amount on every side, **Front Left** keeps its front and left sides in place so it grows toward the back and right, and **Back Right** keeps its back and right sides in place so it grows toward the front and left. The sides are the part's own, so a part you have turned grows along its own sides. The bottom always stays where it is, so a taller part grows upward. It applies when **Width** or **Depth** changes, whether you type it or a formula changes it; other settings don't use it. It is the last row in the panel

## Tips

- For a single slope, like a ramp, use a [Wedge](wedge.md)
- Combine with other shapes to create angled transitions

## Related

- [Wedge](wedge.md) - A full triangular prism
- [Pyramid](pyramid.md) - A four-sided pointed shape
- [Half Cylinder](half-cylinder.md) - A cylinder cut in half
