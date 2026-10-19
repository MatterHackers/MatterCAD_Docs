---
title: Radial Pinch
articleKey: RadialPinchObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
---
# Radial Pinch

Radial Pinch pushes each horizontal layer of a part in or out from its vertical center line, following a profile you draw. Unlike regular [Pinch](pinch.md), which tapers from front to back, Radial Pinch works all the way around the part. A new Radial Pinch starts with a profile at the part's own reach at the bottom and top, bulging out to one and a half times that reach through the middle.

<!-- IMAGE_NEEDED: Before and after showing an object with Radial Pinch applied, with its Properties panel showing the Pinch profile editor, Slices and Advanced -->

## How to Use

1. Select an object
2. Click **Radial Pinch** in the Deform group of the toolbar
3. Edit the **Pinch** profile to set how far the part is pushed in or out at each height
4. Raise **Slices** if the curve looks rough

## Parameters

- **Pinch** - The part's outline from bottom to top, drawn in the design's units (see [the units button](../../workspace/camera-controls.md#the-units-button)): the **X** box of a selected point is how far it reaches across and the **Y** box is how high it is, both in those units. Up is the height on the part; a guide line marks the top and is labelled with the part's height. Across is how far that layer reaches from the center line (the editor's origin line); a second guide line marks the part's own reach and is labelled with it. On that reach line a layer stays as it is; nearer the center pinches it in (0 collapses it onto the center line); farther out pushes it out
- **Slices** - How many horizontal cuts, spaced evenly up the part, give the mesh enough detail to follow the profile (default 20; the slider runs 0 to 50). More slices give a smoother result
- **Advanced** - Off by default. Turn it on for the options below

### Advanced Parameters

- **Pinch Type** - Which way the part is pinched:
  - **Radial** (default) - In or out equally on all sides
  - **X Axis** - Only along the X axis
  - **Y Axis** - Only along the Y axis
- **Rotation Offset** - Moves the center line the pinch works around, in mm

## Tips

- Use the profile editor to create hourglass, bottle, or vase-like shapes
- Radial pinch is ideal for creating organic, rounded forms from cylindrical objects
- Increase Slices for smoother curves, especially on tight pinch profiles
- When you change the design's units and choose to keep your numbers, so that every part changes size, the Pinch profile changes size with the part, both how far it reaches and how high it goes, and the part keeps its shape

## Related

- [Pinch](pinch.md) - A simple front-to-back taper
- [Twist](twist.md) - Spiral rotation along height
- [Curve](curve.md) - Bend into an arc
