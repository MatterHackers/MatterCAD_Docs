---
title: Dilate
articleKey: DilateObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 13
---
# Dilate

Dilate grows a solid outward by at least the radius you set, never less. Flat faces move outward. Outside edges and corners become rounded, holes become smaller, and nearby features can join.

<!-- AUTO_IMAGE: type=from_mcx file=reshape_dilate -->
![An L-shaped solid after dilate](https://matterhackers.github.io/MatterCAD_Docs/assets/reshape_dilate.png)

## How to Use

1. Select a solid part
2. Click **Dilate** in the Round & Offset group of the toolbar
3. Set **Radius** to the smallest distance to grow
4. Wait for the operation to finish; use **Cancel** in the task area to keep the previous result

While you drag the **Radius** slider on a detailed part, MatterCAD shows a quick, see-through preview, and a **Preview** row appears in the task area. Let go to build the exact result; it replaces the preview, with a progress bar and the time left. Grab the slider again to stop that build and return to the preview. The preview is approximate, so its edges look a little softer; the final result is exact. Small parts skip the preview because the exact result is already quick.

## Parameters

- **Radius** - The least distance surfaces move outward (default: 1 mm). Must be greater than zero. Some faces can move a little further, never less
- **Segments** - The detail of the rounding ball (default: 16). More segments produce finer curves and bring the result closer to exactly the radius set, but take longer, especially on parts with pockets or notches

## Tips

- This changes the whole part's dimensions. To round edges while broadly preserving the original dimensions, use one of the Round operations below
- Radius is measured in the source part's own coordinates. Non-uniform scaling applied afterward also stretches the rounding
- These operations require a solid. Use [Inflate Path](../path/inflate-path.md) to grow or shrink a 2D path

## Related

- [Erode](erode.md) - Shrink a solid inward
- [Round All Edges](round-all-edges.md) - Erode followed by Dilate at the same radius
- [Round Inside Edges](round-inside-edges.md) - Dilate followed by Erode at the same radius
- [Fillet](fillet.md) - Round only the edges you pick
