---
title: Cone
articleKey: ConeObject3D
parent: "Primitives"
nav_order: 3
---
# Cone

A tapered cylinder that comes to a point at the top. Useful for creating pointed features, funnels, and chamfers.

<!--  Screenshot of a Cone primitive on the workspace -->
![20260318 183159 paste 20260318 183159](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183159-paste-20260318-183159.jpg)


## Parameters

- **Diameter** - The width across the base (default: 20mm)
- **Height** - How tall the cone is (default: 20mm)
- **Sides** - Number of segments around the perimeter (default: 40)
- **Grow From** - Which side of the part stays where it is when you change its size: **Center** (the default) grows it the same amount on every side, **Front Left** keeps its front and left sides in place so it grows toward the back and right, and **Back Right** keeps its back and right sides in place so it grows toward the front and left. The sides are the part's own, so a part you have turned grows along its own sides. The bottom always stays where it is, so a taller part grows upward. It applies when **Diameter** changes, whether you type it or a formula changes it; other settings don't use it. It is the last row in the panel

## Tips

- For a truncated cone (flat top instead of a point), use a [Cylinder](cylinder.md) with Advanced mode and set different Diameter and Diameter Top values
- Cones are useful for creating chamfered edges when combined with [Subtract](../operations/boolean/subtract.md)

## Related

- [Cylinder](cylinder.md) - A round column without taper
- [Pyramid](pyramid.md) - A four-sided pointed shape
