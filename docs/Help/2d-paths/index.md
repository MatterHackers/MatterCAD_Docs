---
title: 2D Paths
has_children: true
nav_order: 1
---
# 2D Paths

2D paths are flat shapes that you can use as the starting point for 3D objects. Use [Linear Extrude](../operations/path/linear-extrude.md) to give a path height, or [Revolve](../operations/path/revolve.md) to spin a path around an axis to create a 3D form.

<!--  Screenshot showing a 2D path being extruded into a 3D shape -->
![20260506 093625 paste 20260506 093625](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-093625-paste-20260506-093625.jpg)


## Available Paths

- [Circle Path](circle-path.md) - A circular 2D outline
- [Box Path](box-path.md) - A rectangular 2D outline
- [Ring Path](ring-path.md) - A 2D ring (circle with a hole)
- [Star Path](star-path.md) - A star-shaped 2D outline with configurable points
- [Custom Path](custom-path.md) - Draw your own 2D path with control points

## The Plane a Path Is Drawn On

Every one of these paths has a **Plane** in its Properties panel — a [construction plane](../workspace/construction-planes.md) that decides where the flat shape lives. By default it is XY, flat on the bed, which is how paths have always behaved and what older files get when they are opened.

Change it and the shape stands somewhere else without any of its own dimensions changing:

- Pick **XZ** or **YZ** from the preset dropdown to stand the path upright
- Type an **Origin** to move the whole path, or a **Normal** to tilt it, either one driven by an [expression](../workspace/expressions.md) if you want it to follow the rest of the design
- Click **Pick Face** and then a flat face of a model, to draw on that face's plane

Operations that consume paths flatten their inputs onto one plane before they work, so putting several paths on different planes is worth doing deliberately — see [Construction Planes](../workspace/construction-planes.md) for how each operation chooses.

## Softening Corners

Any of these paths can have its corners rounded or cut before you give it height. Use [Fillet](../operations/reshape/fillet.md) to round chosen corners to an exact radius, [Chamfer](../operations/reshape/chamfer.md) to cut them off flat, or [Smooth Path](../operations/path/smooth-path.md) to soften the whole path at once.
