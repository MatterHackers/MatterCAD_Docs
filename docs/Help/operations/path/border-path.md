---
title: Border Path
articleKey: BorderPathObject3D_2
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 1
---
# Border Path

Border Path makes a flat base shape around a 2D path: by default a rounded rectangle 3 mm bigger than the path on every side. Extrude it to make a plate, a tag or a backing for raised text. In the Design tree it is named **Border**.

<!--  Before and after showing a path with a border added -->
![20260506 100533 paste 20260506 100533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100533-paste-20260506-100533.jpg)


## How to Use

1. Select a 2D path
2. Click **Border Path** in the Path group of the toolbar
3. Pick a **Base Type** and set **Expand**

## Parameters

- **Base Type** - The shape of the border, as tabs:
  - **None** - No border is made (the panel says so)
  - **Rectangle** (default) - The rectangle around the path's bounds, grown by Expand, with rounded corners
  - **Circle** - The smallest circle around the path, grown by Expand
  - **Outline** - The path's own outline, grown by Expand
- **Expand** - How far the border reaches past the path, in mm (default 3; the slider runs 0 to 30). Not shown for None
- **Infill Amount** - Outline only. Fills in notches and gaps in the outline so the border's edge is smoother, in mm (default 3; 0 to 10). The bigger the amount, the wider the gaps it bridges; 0 just grows the outline by Expand
- **Style** - Outline only. How the grown outline's corners are drawn: **Flat**, **Round** (default) or **Sharp**
- **Centering** - Circle only. **Bounds** centers the circle on the path's bounding box; **Weighted** (default) centers it on the middle of the path's outer outlines
- **Radius** - Rectangle only. The corner radius, in mm (default 3; the slider runs 0 to 20)
- **Segments** - Rectangle only. How many straight pieces make each rounded corner (default 9; 1 to 30)

## Tips

- Set Radius to 0 for a square-cornered rectangle
- Duplicate the path first, then [Subtract](../boolean/subtract.md) the copy from the border to make a frame shape
- To grow the path itself without a separate base shape, use [Inflate Path](inflate-path.md)

## Related

- [Inflate Path](inflate-path.md) - Expand a path outward
- [Outline Path](outline-path.md) - Create an outline from a filled path
- [Linear Extrude](linear-extrude.md) - Give the bordered path height
