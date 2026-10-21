---
title: Revolve
articleKey: RevolveObject3D_2, RevolveObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 6
description: Spin a flat profile around an axis to make round parts like vases, bowls, knobs and wheels.
keywords: lathe, spin, rotate profile, vase, bowl, turned part, round part
---
# Revolve

Revolve spins a 2D path around an axis to create a 3D solid of revolution. This is how you create vases, bowls, wheels, and other rotationally symmetric objects.

<!-- IMAGE_NEEDED: Before and after showing a profile path being revolved into a vase shape, with the Revolve's Properties panel (Rotation, Axis Offset, Starting Angle, Ending Angle, Sides) -->


## How to Use

1. Select a 2D path
2. Click **Revolve** in the Path group of the toolbar
3. Adjust the Starting and Ending Angle, the Axis Offset and the number of Sides

## Where the Axis Is

The axis is the path's own **x = 0** line: the vertical line through the path's origin (the origin the path editor shows). Draw the profile to the right of that line, at the radius you want - a point 10 mm right of the origin ends up 10 mm from the axis. Anything drawn left of the line is folded across it, so keep the profile on one side.

On the bed (the default plane) the path's up direction is the world **Y** axis, so a revolved part lies on its side along Y. Rotate it afterwards to stand it up.

## Parameters

- **Rotation** - Turns the axis within the path's plane, about the path's origin, in degrees (default 0; 0 to 360). At 0 the axis is the path's vertical x = 0 line; at 90 it runs across the path instead. It does not change how far the profile is spun: that is the Starting and Ending Angle
- **Axis Offset** - Moves the axis away from the path's x = 0 line, in mm (default 0; the slider runs -30 to 30). Positive values move it in +X, closer to a profile drawn right of the origin, which shrinks the part
- **Starting Angle** - Where the spin begins, in degrees (default 0; 0 to 360)
- **Ending Angle** - Where the spin ends, in degrees (default 360, a full turn)
- **Sides** - Number of segments around the spin (default 40; 3 to 360). More is a smoother surface, but a slower rebuild


## Projection Plane

The **Projection Plane** section says which flat surface the profile is flattened onto before it is spun -- by default the plane the profile was drawn on. See [Construction Planes](../../workspace/construction-planes.md).

## Tips

- Use Axis Offset to control the inner diameter of the revolved shape
- Set Starting and Ending Angle to less than 360 to create partial revolutions (arches, gutters)
- Draw a profile path of your vase or bowl shape, then revolve it for perfect symmetry
- A [Circle Path](../../2d-paths/circle-path.md) revolved creates a torus

## Related

- [Linear Extrude](linear-extrude.md) - Extrude straight up instead of revolving
- [Sweep](sweep.md) - Carry a profile along a 3D curve instead of around an axis
- [Loft](loft.md) - Blend between stacked sections
- [2D Paths](../../2d-paths/index.md) - Create profile paths to revolve
- [Torus](../../primitives/torus.md) - A ready-made revolved ring shape
