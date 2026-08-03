---
title: Inflate Path
articleKey: InflatePathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 2
---
# Inflate Path

Inflate Path expands a 2D path outward, making the shape larger while maintaining its overall form. This is similar to applying a uniform offset to all edges.

<!--  Before and after showing a path inflated outward -->
![20260506 100652 paste 20260506 100652](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100652-paste-20260506-100652.jpg)


## How to Use

1. Select a 2D path
2. Apply **Inflate Path** from the Path operations menu
3. Adjust the inflation amount

## Inflating an Open Line

Inflate is how you turn a line into a shape. Uncheck **Closed** on a [Custom Path](../../2d-paths/custom-path.md) to draw an open line, then inflate it: the result is a filled ribbon as wide either side of the line as the amount you set. From there it extrudes like any other path.

**Style** sets how the two ends of the line are capped, as well as how its corners are joined:

- **Flat** stops the ribbon square at each end point
- **Round** adds a half circle past each end point
- **Sharp** adds a square past each end point

An open line has no inside to shrink into, so a zero or negative amount would leave nothing at all. Inflate clamps the value up to a small positive number in that case and writes the clamped number back so you can see what happened. Closed paths still shrink on negative values as they always have.

## Tips

- Use negative values to shrink the path inward instead of expanding
- Inflate is useful for creating tolerance offsets around shapes
- Combine with [Outline Path](outline-path.md) for creating borders with specific widths

## Related

- [Outline Path](outline-path.md) - Create an outline from a path
- [Border Path](border-path.md) - Add a border offset
- [Smooth Path](smooth-path.md) - Round the corners of a path
