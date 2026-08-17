---
title: Twist
articleKey: TwistObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 7
---
# Twist

Twist rotates the top of an object relative to the bottom, creating a spiral or twisted effect along the height. By default the rotation progresses evenly from bottom to top; under Advanced you can draw where along the height the turning actually happens.

<!--  Before and after showing a cube being twisted into a spiral column -->
![20260506 155620 paste 20260506 155620](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155620-paste-20260506-155620.jpg)

## How to Use

1. Select an object
2. Apply the **Twist** operation from the Reshape menu
3. Set the twist angle and adjust slicing for smoothness
4. Turn on **Advanced** if you want to draw how the twist is spread up the part

## The Twist Profile

Under Advanced, the **Twist Profile** curve decides where the twist happens. The total amount of twist is still set by the Angle (or Rotation Distance) control - the curve only spreads it:

- **Up the curve** is the height on the part in percent - 0 at the bottom, 100 at the top. A guide line across the editor marks 100 percent and is labeled with the part's real height in mm.
- **Across the curve** is the percent of the total twist reached by that height - 0 for none of it, 100 for all of it.

A new Twist starts with a straight diagonal from 0 to 100, which is the plain even twist you get without Advanced at all.

A flat run in the curve is a band of the part that does not twist. Where the curve does not cover the full height, the nearest end of it is held, so a curve drawn only between 40 and 60 percent leaves the part rigid below and above it - that is how you start and stop a twist part way up.

A run that falls back as it goes up unwinds: that band of the part turns the other way, back toward where it started. Drawing the profile up past 100 and then back down is how you overshoot the total and return to it.

## Parameters

- **Rotation Type** - Choose between:
  - **Angle** - Specify the total twist angle in degrees (3-360)
  - **Distance** - Specify the twist as a distance along the circumference
- **Rotation Slices** - Number of horizontal cuts added for smooth twisting. More slices = smoother twist
- **Twist Right** - Direction of twist: right (clockwise) or left (counterclockwise)
- **Prefered Radius** - Read-only: the radius the part itself reports, or the one implied by its shape, which is what a twist distance is measured around (Distance mode only)
- **Edit Radius** - Turn off the reported radius so you can set your own (Distance mode only, and only when the part reports one)
- **Override Radius** - Custom radius for the twist calculation (Distance mode only)

### Advanced Parameters

- **Twist Profile** - The curve editor described above: the percent of the total twist reached at each height in percent
- **Rotation Offset** - Shift the center the part is turned about, away from the middle of the part

## Tips

- Higher Rotation Slices values produce smoother results but generate more geometry
- Draw the profile flat at the bottom and rising after that to leave a straight base under a twisted column
- A 90-degree twist on a square column creates an elegant architectural effect
- Draw two flat runs joined by a short climb to wind the middle of the part and leave both ends rigid

## Related

- [Curve](curve.md) - Bend an object into an arc
- [Pinch](pinch.md) - Compress toward center
- [Radial Pinch](radial-pinch.md) - Shape the profile with a curve the same way
