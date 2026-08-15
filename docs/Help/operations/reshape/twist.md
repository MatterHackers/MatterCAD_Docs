---
title: Twist
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 7
---
# Twist

Twist rotates an object about its vertical axis, turning each height by the amount you draw on a curve. A curve that rises steadily from bottom to top gives the classic spiral column; a curve that is flat over part of the height leaves that part alone.

<!--  Before and after showing a cube being twisted into a spiral column -->
![20260506 155620 paste 20260506 155620](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155620-paste-20260506-155620.jpg)

## How to Use

1. Select an object
2. Apply the **Twist** operation from the Reshape menu
3. Edit the **Twist** curve to set how far the part is turned at each height
4. Adjust **Rotation Slices** for smoothness

<!-- IMAGE_NEEDED: The Twist properties panel showing the curve editor with the default 0 to 45 degree line, and the guide line marking the top of the part -->

## The Twist Curve

The curve is read as a function of height:

- **Up the curve** is the height on the part in percent - 0 at the bottom, 100 at the top. A guide line across the editor marks 100 percent and is labeled with the part's real height in mm.
- **Across the curve** is the twist in degrees at that height. Positive turns one way, **negative turns the other way** - a curve that crosses zero turns the bottom of the part one way and the top the other.

A new Twist starts with a straight line from 0 degrees at the bottom to 45 degrees at the top.

Where the curve does not cover the full height, the nearest end of it is held. So a curve drawn only between 40 and 60 percent still decides what happens above and below: everything under it is turned by the curve's bottom value and everything over it by the curve's top value. That is how you start and stop a twist part way up the part - the ends stay rigid instead of continuing to wind.

## Parameters

- **Twist** - The curve editor described above: the twist in degrees at each height in percent
- **Rotation Slices** - Number of horizontal cuts added through the part so it can bend smoothly. More slices = smoother twist

### Advanced Parameters

- **Rotation Offset** - Shift the center the part is turned about, away from the middle of the part

## Tips

- Higher Rotation Slices values produce smoother results but generate more geometry
- Draw the curve flat at the bottom and rising after that to leave a straight base under a twisted column
- A 90-degree twist on a square column creates an elegant architectural effect
- Drag the curve into an S shape for a twist that winds one way and then back the other

## Related

- [Curve](curve.md) - Bend an object into an arc
- [Pinch](pinch.md) - Compress toward center
- [Radial Pinch](radial-pinch.md) - Shape the profile with a curve the same way
