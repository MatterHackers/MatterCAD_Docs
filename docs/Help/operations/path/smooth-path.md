---
title: Smooth Path
articleKey: SmoothPathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 8
description: Even out jagged steps and bumps in a 2D path, such as an outline traced from a picture.
keywords: jagged, smoother, clean up outline, stair steps, rough edges, soften
---
# Smooth Path

Smooth Path evens out small bumps and jagged steps in a 2D path, such as the stair-steps of an outline traced from a picture. Each pass moves every point toward the average of itself and its neighbours, and no point ever moves further than **Smooth Distance** from where it started, so the overall shape stays the same. To round corners to a chosen size, use [Fillet](../reshape/fillet.md) instead.

<!-- AUTO_IMAGE: type=shot id=smooth-path -->
![Smooth Path: a letter M traced from a blocky picture at the left, the raw trace's edges in stair-steps, and at the right the same trace evened out, beside Smooth Distance and Iterations](https://matterhackers.github.io/MatterCAD_Docs/assets/smooth-path.png)


## How to Use

1. Select a 2D path
2. Click **Smooth Path** in the Path group of the toolbar
3. Raise **Smooth Distance** or **Iterations** until the bumps are gone

## Parameters

- **Smooth Distance** - The farthest any point may move, in mm (default 0.3; the slider runs 0.01 to 1)
- **Iterations** - How many smoothing passes to run (default 3; 1 to 10). More passes make a smoother line, up to the Smooth Distance limit

## Tips

- Use it on paths from [Image to Path](../image/image-to-path.md) to clean up the jagged edges of a traced picture before you extrude it
- Because no point moves further than Smooth Distance, sharp corners only soften slightly; [Fillet](../reshape/fillet.md) rounds them properly

## Related

- [Fillet](../reshape/fillet.md) - Round chosen corners to an exact radius instead of smoothing the whole path
- [Chamfer](../reshape/chamfer.md) - Cut chosen corners off flat
- [Inflate Path](inflate-path.md) - Expand a path outward
- [Outline Path](outline-path.md) - Create an outline from a path
- [Linear Extrude](linear-extrude.md) - Give the smoothed path height
