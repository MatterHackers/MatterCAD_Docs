---
title: Revolve
articleKey: RevolveObject3D_2, RevolveObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 6
---
# Revolve

Revolve spins a 2D path around an axis to create a 3D solid of revolution. This is how you create vases, bowls, wheels, and other rotationally symmetric objects.

<!--  Before and after showing a profile path being revolved into a vase shape -->
![20260506 102004 paste 20260506 102004](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-102004-paste-20260506-102004.jpg)


## How to Use

1. Select a 2D path
2. Apply **Revolve** from the Path operations menu
3. Adjust the rotation range, axis position, and number of sides

## Where the Axis Is

The axis is the path's own **x = 0** line: the vertical line through the path's origin (the origin the path editor shows). Draw the profile to the right of that line, at the radius you want - a point 10 mm right of the origin ends up 10 mm from the axis. Anything drawn left of the line is folded across it, so keep the profile on one side.

On the bed (the default plane) the path's up direction is the world **Y** axis, so a revolved part lies on its side along Y. Rotate it afterwards to stand it up.

## Parameters

- **Rotation** - Total rotation angle for the revolve (default: 0, range: 0-360). Set to 360 for a complete revolution.
- **Axis Offset** - Moves the axis away from the path's x = 0 line (default: 0, range: -30 to 30). Positive values move it in +X, closer to a profile drawn right of the origin, which shrinks the part.
- **Starting Angle** - Where the revolution begins (default: 0)
- **Ending Angle** - Where the revolution ends (default: 360, a full revolution).
- **Sides** - Number of segments around the revolution (default: 40, the same as Sphere and Cylinder). More = smoother surface, but a slower rebuild.


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
