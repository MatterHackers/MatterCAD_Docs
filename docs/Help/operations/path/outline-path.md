---
title: Outline Path
articleKey: OutlinePathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 5
description: Turn a filled 2D shape into just its outline, a band of the width you choose.
keywords: border, rim, frame, edge band, hollow outline, stroke
---
# Outline Path

Outline Path creates an outline version of a filled path, converting a solid shape into just its boundary ring with a specified thickness.

<!--  Before and after showing a solid circle path converted to a ring outline -->
<!-- AUTO_IMAGE: type=shot id=outline-path -->
![Outline Path: a filled star at the left, and at the right only its outline, a band 7.5 mm wide with round corners, beside Outline Width, Offset, Inner Style and Outer Style](https://matterhackers.github.io/MatterCAD_Docs/assets/outline-path.png)

## How to Use

1. Select a 2D path
2. Click **Outline Path** in the Path group of the toolbar
3. Set **Outline Width**

## Parameters

- **Outline Width** - How wide the outline band is, in mm (default 0.5; the slider runs 0.1 to 10)
- **Offset** - Where the band sits on the path's edge, as a share of its width (default 0.5; 0 to 1): how much of the band lies outside the original edge. 0.5 centers the band on the edge. An open line is always outlined down its middle
- **Inner Style** - How the inside corners of the band are drawn: **Flat**, **Round** or **Sharp** (default)
- **Outer Style** - How the outside corners of the band are drawn: **Flat**, **Round** or **Sharp** (default)

## Tips

- Use this to create frame-like shapes from solid paths
- Combine with [Linear Extrude](linear-extrude.md) to create 3D frames and borders
- An outlined [Circle Path](../../2d-paths/circle-path.md) makes the same shape as a [Ring Path](../../2d-paths/ring-path.md)

## Related

- [Inflate Path](inflate-path.md) - Expand a path outward
- [Border Path](border-path.md) - Add a border offset
- [Ring Path](../../2d-paths/ring-path.md) - A ready-made ring shape
