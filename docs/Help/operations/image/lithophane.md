---
title: Lithophane
articleKey: LithophaneObject3D
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 3
---
# Lithophane

A lithophane is a thin panel where a picture is turned into varying thickness. With a light behind it, the thinner areas let more light through and the picture appears. It is a beautiful way to display photographs and artwork.

<!-- IMAGE_NEEDED: A Lithophane made from a photo, with the Lithophane's Properties panel (Pixels Per mm, Height, Width, Invert and the Update button) -->


## How to Use

1. Add a picture to the bed (drop an image file on the 3D view) and select it
2. Click **Lithophane** in the Image group of the toolbar
3. Set the size and detail, then click **Update** to rebuild. Changing a setting does not rebuild a lithophane on its own, because a detailed one can take a while to build

## Parameters

- **Pixels Per mm** - How many of the picture's pixels make each millimetre (default 1.5; 0.1 to 10). More gives finer detail, a heavier model and a longer build. It does not change the size: the panel stays **Width** wide
- **Height** - The thickness at the thickest point, in mm (default 2.5; the slider runs 0.5 to 3). The thinnest areas are 0.4 mm thick
- **Width** - The width of the panel, in mm (default 150). The height follows the picture's proportions
- **Invert** - On by default: dark parts of the picture are thick, so they block the light and look dark when lit from behind. Turn it off to make light parts thick instead

## Tips

- Try a low Pixels Per mm while you choose the size, then raise it for the final model
- A height of 2 to 3 mm works well for most lithophanes
- Portrait photos with good contrast work particularly well

## Related

- [Image Converter](image-converter.md) - Trace an image's shapes and extrude them, instead of turning brightness into thickness
- [Image to Path](image-to-path.md) - Trace image outlines as paths
