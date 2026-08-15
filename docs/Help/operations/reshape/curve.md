---
title: Curve
articleKey: CurveObject3D_4
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 2
---
# Curve

Curve bends an object along its length by the amount you draw on a curve. A curve that rises steadily from one end to the other gives a plain arc; a curve that is flat over part of the length leaves that part of the part dead straight.

<!--  Before and after showing a straight bar being curved into an arc -->
![20260506 155243 paste 20260506 155243](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155243-paste-20260506-155243.jpg)

<!-- IMAGE_NEEDED: The before/after above was shot with the old angle/diameter Curve. Reshoot it with the bend curve editor visible beside the bent part. -->

## How to Use

1. Select an object
2. Apply the **Curve** operation from the Reshape menu
3. Edit the **Bend** curve to set how far the part has turned at each point along its length
4. Turn **Split Mesh** on (it is on by default) and adjust **Min Sides Per Rotation** for smoothness

<!-- IMAGE_NEEDED: The Curve properties panel showing the bend curve editor with the default 0 to 90 degree line, and the guide line marking the far end of the part -->

## The Bend Curve

The curve is read as a function of position along the part:

- **Up the curve** is the position along the part's length in percent - 0 at the left end, 100 at the right. A guide line across the editor marks 100 percent and is labeled with the part's real length in mm.
- **Across the curve** is the total bend in degrees that has accumulated by that point. Positive bends the part up, **negative bends it down**.

Because the value is the bend *so far*, it is the curve's slope that sets the tightness of the bend:

- A straight slanted line is the old uniform bend - one constant radius all the way along. The steeper the line, the tighter the radius.
- A flat run is a straight section: nothing has changed, so nothing turns there.
- A line that climbs and then falls back bends one way and then the other, which is how you draw an S bend.

A new Curve starts with a straight line from 0 degrees at the left to 90 degrees at the right - a quarter turn spread evenly along the part.

Where the curve does not cover the full length, the nearest end of it is held, so a curve drawn only between 40 and 60 percent still decides what happens outside it: everything before it keeps the curve's first value and everything after it keeps its last. That is how a bend starts and stops part way along - the ends stay rigid instead of continuing to curl. It is also what the old Start Bend Percent and End Bend Percent settings were for.

The bend keeps the length of the part's center line, so drawing 360 degrees wraps the part into a ring whose size follows from its own length. The left end of the part stays where it is and the rest curls away from it.

## Parameters

- **Bend** - The curve editor described above: the accumulated bend in degrees at each position in percent
- **Split Mesh** - Split the mesh so it has enough geometry to follow the bend smoothly (default: on)
- **Min Sides Per Rotation** - Minimum number of mesh segments per full 360 degrees of bend. Higher values = smoother curves. Only shown when Split Mesh is on

## Tips

- Use Curve to create arches, rings, and bent brackets from straight stock shapes
- Draw a straight line up to 360 degrees to wrap the object into a complete ring
- Draw the curve flat at the start and rising after that to leave a straight tab on the end of a bent bracket
- Draw two flat runs joined by a short steep climb for a sharp corner with straight legs either side
- Increase Min Sides Per Rotation for smoother results on tight bends

## Related

- [Twist](twist.md) - Rotate along height instead of bending
- [Torus](../../primitives/torus.md) - A ready-made ring shape
