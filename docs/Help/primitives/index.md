---
title: Primitives
has_children: true
nav_order: 7
description: "Find the basic 3D shapes to build designs from: boxes, cylinders, spheres, text and more."
keywords: shapes, basic shapes, building blocks, 3d shapes, solids
---
# Primitives

MatterCAD's 3D primitive shapes are the building blocks for your designs. Add one from the **3D Primitives** folder (in the Library, or under **Add to Bed**), or from the favorites bar down the left side of the design, then change its settings in the Properties panel to get the exact shape you need.

<!-- AUTO_IMAGE: type=shot id=primitives-index-library -->
![The Library's 3D Primitives folder: a thumbnail and name for each shape it holds, from Cube to Image Converter](https://matterhackers.github.io/MatterCAD_Docs/assets/primitives-index-library.png)



## 3D Primitives

In the order the 3D Primitives folder lists them:

- [Cube](cube.md) - A box shape with adjustable width, depth, height, and optional rounding
- [Hole](hole.md) - A cube that cuts away whatever it overlaps when combined
- [Pyramid](pyramid.md) - A four-sided pyramid with adjustable base and height
- [Wedge](wedge.md) - A triangular prism shape, a ramp
- [Half Wedge](half-wedge.md) - A ridge with two sloped sides
- [Text](text.md) - 3D lettering in MatterCAD's fonts
- [Cylinder](cylinder.md) - A round column with configurable diameter, height, and sides
- [Cone](cone.md) - A tapered cylinder that comes to a point
- [Half Cylinder](half-cylinder.md) - A cylinder cut in half lengthwise
- [Torus](torus.md) - A donut shape with inner and outer diameter control
- [Tube](ring.md) - A hollow cylinder with inner and outer diameters
- [Sphere](sphere.md) - A round ball with adjustable diameter and detail level
- [Half Sphere](half-sphere.md) - The top half of a sphere
- [Image Converter](../operations/image/image-converter.md) - Turn a picture into a solid shape
- [3D Curve](../operations/path/curve-3d.md) - A curve through points in space, for Sweep and other operations


## Where a Shape Sits

A new shape stands on the bed: its bottom is at Z 0. A [Translate](../operations/transform/translate.md) moves the whole shape by its **Translation**, so for a shape centered at X 0, Y 0, the Translation's X and Y say where the shape's center goes and its Z says how high its bottom sits.

When you change a shape's size, its bottom stays where it is and, by default, its center stays put in X and Y. On the Cube, Hole, Pyramid, Wedge, Half Wedge, Cylinder, Cone, Half Cylinder, Torus, Tube, Sphere and Half Sphere, the **Grow From** setting (the last row in the panel) can keep the shape's front-left or back-right sides in place instead.

## Other Shapes

These come from other places:

- [Braille](braille.md) and [Braille Card](braille-card.md) - Raised Braille, from **Included > Design Apps**
- [QR Code](qr-code.md) - A QR code picture plate, from **Included > Tools**
- [Image Object](image-object.md) - A picture you drop on the 3D view, the input for the image operations
- [SVG Object](svg-object.md) - What an .svg file opens as: solid parts or flat paths
