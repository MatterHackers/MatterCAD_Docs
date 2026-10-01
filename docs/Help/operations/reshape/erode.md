---
title: Erode
articleKey: ErodeObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 14
---
# Erode

Erode shrinks a solid inward by at least the radius you set, never less. Flat faces move inward. Inside corners become rounded, holes become larger, and thin features can disappear or split the part into separate pieces. All surviving pieces are kept.

<!-- AUTO_IMAGE: type=from_mcx file=reshape_erode -->
![An L-shaped solid after erode](https://matterhackers.github.io/MatterCAD_Docs/assets/reshape_erode.png)

## How to Use

1. Select a solid part
2. Click **Erode** in the Round & Offset group of the toolbar
3. Set **Radius** to the smallest distance to shrink
4. Wait for the operation to finish; use **Cancel** in the task area to keep the previous result

While you drag the **Radius** slider on a detailed part, MatterCAD shows a quick, see-through preview, and a **Preview** row appears in the task area. Let go to build the exact result; it replaces the preview, with a progress bar and the time left. Grab the slider again to stop that build and return to the preview. The preview is approximate, so its edges look a little softer; the final result is exact. Small parts skip the preview because the exact result is already quick.

## Parameters

- **Radius** - The least distance surfaces move inward (default: 1 mm). Must be greater than zero. Some faces can move a little further, never less
- **Segments** - The detail of the rounding ball (default: 16). More segments produce finer curves and bring the result closer to exactly the radius set, but take longer, especially on parts with pockets or notches

## When It Refuses

The radius must be smaller than half the source bounding box's smallest side, and a little smaller still because the rounding ball reaches slightly past the radius. That is an upper bound, not a guarantee that the ball fits inside the shape. If the radius is too large, the message tells you the largest radius that works; set **Radius** below it. If no solid remains after erosion, the operation refuses the result and leaves the source visible. A thin feature disappearing is allowed as long as some solid remains.

Convex parts, such as boxes with no pockets or notches, use a fast exact erosion. Parts with inside corners take longer.

## Tips

- This changes the whole part's dimensions. To round edges while broadly preserving the original dimensions, use one of the Round operations below
- Radius is measured in the source part's own coordinates. Non-uniform scaling applied afterward also stretches the rounding
- These operations require a solid. Use [Inflate Path](../path/inflate-path.md) to grow or shrink a 2D path

## Related

- [Dilate](dilate.md) - Grow a solid outward
- [Round All Edges](round-all-edges.md) - Erode followed by Dilate at the same radius
- [Round Inside Edges](round-inside-edges.md) - Dilate followed by Erode at the same radius
- [Fillet](fillet.md) - Round only the edges you pick
