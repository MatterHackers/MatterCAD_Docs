---
title: Image Converter
articleKey: 4D9BD8DB-C544-4294-9C08-4195A409217A
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 1
description: Turn a picture or logo into a raised solid part, with an optional base, ready to export.
keywords: picture to 3d, logo, photo to model, silhouette, image to stl, stencil, emblem
---
# Image Converter

Image Converter turns a picture into a solid part. It traces the shapes in the picture into an outline, smooths it, and raises it to a height you choose, so a logo becomes a raised solid with the logo's silhouette, not a relief carved from brightness. It can also put a base plate under the shape.

<!-- AUTO_IMAGE: type=shot id=image-converter-panel -->
![A logo made a raised solid by Image Converter, beside its Properties panel: the picture, the Analysis Type tabs and the Select Range histogram](https://matterhackers.github.io/MatterCAD_Docs/assets/image-converter-panel.png)

## How to Use

1. Add your picture to the bed (drag the file in, or use an [Image](../../primitives/image-object.md))
2. Select the picture
3. Click **Image Converter** in the Image group of the toolbar. The picture is replaced by a solid traced from it, in the same place. The button is only enabled while a picture is selected
4. Pick the **Analysis Type** that separates your subject from its background, if the one it chose does not
5. Adjust **Select Range** or **Colors** until only the shapes you want are traced
6. Set the **Height** under Main Extrude

Undo brings back the picture in one step.

You can also start without a picture: **Image Converter (Nodes)** in the Library's **My Tools** starts from a sample picture you then replace, and **Image Converter** in the **3D Primitives** folder adds the older Image Converter described at the end of this page.

## Settings

### Image

- **Image Search** - Searches Google for a picture to use. Make sure you have permission to use anything you find
- The picture itself, which the whole part is traced from
- **Invert** - Swaps the light and dark parts of the picture before it is traced
- **Open new image** - Replaces the picture. The trace, the smoothing, the height and the base all rebuild from the new one

### Analysis Type

Chooses how the tracer decides which pixels are part of the shape. A new Image Converter looks at the picture and starts on the type that suits it; pick another tab to change it.

- **Transparency** - Uses the picture's own see-through areas. Transparent pixels are left out and only solid pixels count as the shape. Best for a PNG cut out on a transparent background. The panel says so under the tabs
- **Colors** - Separates the shape by colour: tick the colours in **Colors** that should become the shape
- **Intensity** - Separates the shape by brightness. The right choice for most photographs and black-on-white logos

### Select Range

Shown for Intensity. The histogram is where you decide how much of the picture becomes shape. Drag its handles to move the threshold; the preview picture above it shows which pixels are kept before the part rebuilds.

- **Min Surface Area** - The smallest area, in mm², a traced shape must have to be kept (default 1). Raise it to drop specks, dust and JPEG noise that would otherwise each become a tiny island of plastic

### Main Extrude

How the traced shape is raised:

- **Height** - How tall the shape stands (default 5mm)
- **Bevel Top** / **Bevel Bottom** - Round or cut the top or bottom edge, each with its own **Style**, **Radius** and **Segments**

### Border (the base)

A base is off until you ask for one. **Base Type** chooses its shape:

- **None** - No base. This is what a new Image Converter starts as, and the panel says so
- **Rectangle** - A rectangular plate around the shape, with **Radius** and **Segments** to round its corners
- **Circle** - A round plate, with **Centering** choosing whether it is centred on the shape's bounding box (Bounds) or on where the shape's area actually sits (Weighted)
- **Outline** - A plate that follows the shape's own outline, with **Style** choosing how its corners are made and **Infill Amount** closing gaps between nearby parts of the shape

With a base chosen, one more setting appears:

- **Expand** - How far the base reaches past the traced shape (default 3mm). This is the visible margin around your part

### Base Extrude

The base's thickness, shown once Base Type is something other than None:

- **Height** - How thick the base plate is
- **Bevel Top** / **Bevel Bottom** - The same bevel settings as the main extrude, for the plate

## How Image Converter Is Built

Image Converter is built as a [node graph](../../workspace/node-graphs.md): boxes wired together that make a mask of the picture, trace it, smooth it, raise it and add the base. Turn on **Show Graph** in the panel to see how it works, and change it if you want something it does not do. The graph's settings are the ones above, so you never need to open it to use Image Converter.

## Tips

- High-contrast pictures with clear silhouettes trace best. A busy photograph traces into hundreds of shapes
- If the result has specks, raise **Min Surface Area** before changing the histogram: it is usually noise, not the threshold
- The base sits under the main extrude by itself. Give it a small **Height** and a modest **Expand** for a stable part

## Older Image Converters

Designs saved before Image Converter became a node graph keep their Image Converter, which works as before. So does one added from the **3D Primitives** folder, one the AI makes, and one made from a QR code or another image source that is not a stored picture. It is a [component](../../workspace/components.md) built from parts you could assemble yourself: an [Image](../../primitives/image-object.md), an [Image to Path](image-to-path.md) that traces it, a [Smooth Path](../path/smooth-path.md) and a [Linear Extrude](../path/linear-extrude.md) named **Main Extrude**, beside a [Border Path](../path/border-path.md) extruded as **Base Extrude**, held together by an [Align](../placement/align.md). Its settings are the same as above, with these differences:

- To reach the settings it does not show, such as the Smooth Path's, expand it in the design tree
- **Cancel** on the component removes it and leaves the original picture behind, so you can start over from it

## When to use something else

- If you only want the traced outline as a 2D path to feed into your own operations, use [Image to Path](image-to-path.md)
- If you want brightness to become height, as in a backlit picture with light and dark shading, use [Lithophane](lithophane.md). That is the height-map tool; Image Converter is not

## Related

- [Node Graphs](../../workspace/node-graphs.md) - How the graph Image Converter is built from works
- [Image to Path](image-to-path.md) - The trace on its own, without the extrude and base
- [Lithophane](lithophane.md) - Turn brightness into thickness for a backlit picture
- [Image Object](../../primitives/image-object.md) - The picture itself, which every image operation reads from
- [Linear Extrude](../path/linear-extrude.md) - The operation that gives a traced path its height
- [Border Path](../path/border-path.md) - The operation that builds the base outline
- [Components](../../workspace/components.md) - How an older Image Converter shows a chosen set of settings
