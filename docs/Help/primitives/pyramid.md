---
title: Pyramid
articleKey: PyramidObject3D
parent: "Primitives"
nav_order: 11
---
# Pyramid

A four-sided pyramid shape with an adjustable rectangular base and height.

<!--  Screenshot of a Pyramid primitive on the workspace -->
![20260318 183743 paste 20260318 183743](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183743-paste-20260318-183743.jpg)


## Parameters

- **Width** - Base size along the X axis (default: 20mm)
- **Depth** - Base size along the Y axis (default: 20mm)
- **Height** - How tall the pyramid is from base to apex (default: 20mm)
- **Grow From** - Which side of the part stays where it is when you change its size: **Center** (the default) grows it the same amount on every side, **Front Left** keeps its front and left sides in place so it grows toward the back and right, and **Back Right** keeps its back and right sides in place so it grows toward the front and left. The sides are the part's own, so a part you have turned grows along its own sides. The bottom always stays where it is, so a taller part grows upward. It applies when **Width** or **Depth** changes, whether you type it or a formula changes it; other settings don't use it. It is the last row in the panel

## Tips

- Set Width and Depth to the same value for a regular square-base pyramid
- Use different Width and Depth values for a rectangular-base pyramid
- Useful for decorative elements, rooflines, and pointed features

## Related

- [Cone](cone.md) - A round-base pointed shape
- [Wedge](wedge.md) - A triangular prism (like half a cube)
