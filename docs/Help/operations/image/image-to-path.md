---
title: Image to Path
articleKey: ImageToPathObject3D_2
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 2
description: Trace the outlines of a picture into flat 2D paths you can extrude, revolve or cut with.
keywords: trace, tracing, vectorize, outline from picture, bitmap to vector
---
# Image to Path

Image to Path traces the outlines of an image to create 2D paths. These paths can then be extruded, revolved, or used with any other path operation. This is ideal for converting logos, silhouettes, and simple graphics into 3D objects.

<!-- AUTO_IMAGE: type=shot id=image-to-path -->
![A logo traced by Image to Path, the traced outline drawn over the picture, beside its Properties panel: the Analysis Type tabs, the Select Range histogram and Min Surface Area](https://matterhackers.github.io/MatterCAD_Docs/assets/image-to-path.png)


## How to Use

1. Select an image object in your workspace
2. Click **Image to Path** in the Image group of the toolbar
3. Choose the analysis type and adjust the selection range

## Parameters

- **Analysis Type** - How the image is analyzed for tracing:
  - **Transparency** - Trace based on transparent vs opaque areas (best for PNGs with transparent backgrounds)
  - **Colors** - Trace based on color regions
  - **Intensity** - Trace based on brightness levels (best for most images)
- **Select Range** - A histogram control to select which brightness/color values to include in the trace
- **Min Surface Area** - Drops small traced loops, measured in the picture's pixels (default 1; the slider runs 0 to 150). A loop is kept only if its area is at least this number squared, in square pixels: 1 keeps loops of 1 square pixel or more, 10 needs 100 square pixels. Increase it to filter out small specks. When the trace finds only one loop, it is always kept

## Tips

- Clean, high-contrast images with simple shapes work best
- Use Transparency mode for PNG images with transparent backgrounds
- Use Intensity mode for photographs and images without transparency
- After tracing, apply [Linear Extrude](../path/linear-extrude.md) to give the path height
- Increase Min Surface Area to remove small unwanted details from the trace

## Related

- [Image Converter](image-converter.md) - The same trace, already wrapped in an extrude and an optional base
- [Lithophane](lithophane.md) - Create backlit image displays
- [SVG Object](../../primitives/svg-object.md) - Import vector graphics directly (no tracing needed)
- [Linear Extrude](../path/linear-extrude.md) - Give the traced path height
