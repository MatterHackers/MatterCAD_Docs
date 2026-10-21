---
title: Pinch
articleKey: PinchObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 4
description: Taper a part so it narrows (or widens) from front to back.
keywords: taper, narrow, squeeze, slim
---
# Pinch

Pinch tapers a part from front to back. The front (the side nearest you in the Front view, lowest Y) keeps its width; moving toward the back (highest Y) the part narrows (or widens) toward its center line along X, reaching the **Back Ratio** at the back. The height (Z) is not changed.

<!--  Before and after showing an object being pinched -->
![20260506 155449 paste 20260506 155449](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155449-paste-20260506-155449.jpg)

## How to Use

1. Select an object
2. Click **Pinch** in the Deform group of the toolbar
3. Set **Back Ratio** in the Properties panel

## Parameters

- **Back Ratio** - The width of the back as a percentage of its original width (default 50; 0 to 300). 100 leaves the part unchanged, below 100 narrows the back (0 squeezes it to a line), above 100 flares it wider

## Tips

- To taper along a different direction, rotate the part first, pinch it, then rotate the result back
- Use this to create tapered, narrowing shapes from rectangular or cylindrical objects
- For radial (all-around) compression, use [Radial Pinch](radial-pinch.md) instead

## Related

- [Radial Pinch](radial-pinch.md) - Pinch radially around a center point
- [Twist](twist.md) - Rotate along height
- [Curve](curve.md) - Bend into an arc
