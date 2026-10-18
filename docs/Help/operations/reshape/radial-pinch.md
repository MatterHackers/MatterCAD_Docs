---
title: Radial Pinch
articleKey: RadialPinchObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
---
# Radial Pinch

Radial Pinch pushes each horizontal layer of a part in or out from its vertical center line, following a profile you draw. Unlike regular [Pinch](pinch.md), which tapers from front to back, Radial Pinch works all the way around the part. A new Radial Pinch starts with an S-shaped profile that bulges the middle of the part outward.

<!-- IMAGE_NEEDED: Before and after showing an object with Radial Pinch applied, with its Properties panel showing the Pinch profile editor, Slices and Advanced -->

## How to Use

1. Select an object
2. Click **Radial Pinch** in the Deform group of the toolbar
3. Edit the **Pinch** profile to set how far the part is pushed in or out at each height
4. Raise **Slices** if the curve looks rough

## Parameters

- **Pinch** - A profile editor. Up the profile is the height of the part (in percent, bottom to top); across it is how far that layer is pushed, in mm. Points toward the center line pull the part in; points away from it push the part out
- **Slices** - How many horizontal cuts, spaced evenly up the part, give the mesh enough detail to follow the profile (default 20; the slider runs 0 to 50). More slices give a smoother result
- **Advanced** - Off by default. Turn it on for the options below

### Advanced Parameters

- **Pinch Type Value** - Which way the part is pushed:
  - **Radial** (default) - In or out equally on all sides
  - **X Axis** - Only along the X axis
  - **Y Axis** - Only along the Y axis
- **Rotation Offset** - Moves the center line the pinch works around, in mm

## Tips

- Use the profile editor to create hourglass, bottle, or vase-like shapes
- Radial pinch is ideal for creating organic, rounded forms from cylindrical objects
- Increase Slices for smoother curves, especially on tight pinch profiles

## Related

- [Pinch](pinch.md) - A simple front-to-back taper
- [Twist](twist.md) - Spiral rotation along height
- [Curve](curve.md) - Bend into an arc
