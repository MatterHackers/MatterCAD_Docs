---
title: 2D Paths
has_children: true
nav_order: 1
description: Find the flat 2D shapes you can extrude, revolve or sweep into 3D parts.
keywords: 2d shapes, sketches, flat shapes, profiles, outlines, 2d primitives
---
# 2D Paths

2D paths are flat shapes that you can use as the starting point for 3D objects. Add them from the **2D Primitives** folder (in the Library, or under **Add to Bed**). Use [Linear Extrude](../operations/path/linear-extrude.md) to give a path height, or [Revolve](../operations/path/revolve.md) to spin a path around an axis to create a 3D form.

<!-- AUTO_IMAGE: type=shot id=2d-index-extrude -->
![A flat Star path at the left and the same Star given height by Linear Extrude at the right, the Linear Extrude selected beside its Properties panel: Height and Bevel Top](https://matterhackers.github.io/MatterCAD_Docs/assets/2d-index-extrude.png)


## Available Paths

In the order the 2D Primitives folder lists them:

- [Box](box-path.md) - A rectangle, with optional rounded corners
- [Custom Path](custom-path.md) - Draw your own 2D path with control points
- **Text 2D** - Flat letter outlines: the [Text](../primitives/text.md) object with its Output set to 2D
- [Circle](circle-path.md) - A circle (or a regular polygon, with few sides)
- [Ring](ring-path.md) - A circle with a hole
- [Star](star-path.md) - A star with any number of points

## The Plane a Path Is Drawn On

Every one of these paths has a **Plane** in its Properties panel — a [construction plane](../workspace/construction-planes.md) that decides where the flat shape lives. By default it is XY, flat on the bed.

Change it and the shape stands somewhere else without any of its own dimensions changing:

- Click the **XZ** or **YZ** tab to stand the path upright, and **Flip** to face it the other way
- Click **Custom** to show the plane's values (under **Plane Values**), then type an **Origin** to move the whole path, a **Normal** to tilt it, or an **X Direction** to turn it within the plane, each one driven by an [expression](../workspace/expressions.md) if you want it to follow the rest of the design
- Click **Pick Face** and then a flat face of a model, to draw on that face's plane

Operations that consume paths flatten their inputs onto one plane before they work, so putting several paths on different planes is worth doing deliberately — see [Construction Planes](../workspace/construction-planes.md) for how each operation chooses.

## Softening Corners

Any of these paths can have its corners rounded or cut before you give it height. Use [Fillet](../operations/reshape/fillet.md) to round chosen corners to an exact radius, [Chamfer](../operations/reshape/chamfer.md) to cut them off flat, or [Smooth Path](../operations/path/smooth-path.md) to soften the whole path at once.
