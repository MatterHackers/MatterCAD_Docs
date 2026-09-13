---
title: Plane Cut
articleKey: PlaneCutObject3D_2, PlaneCutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 5
---
# Plane Cut

Plane Cut slices an object with a [construction plane](../../workspace/construction-planes.md) and keeps the part behind it -- everything on the far side of the way the plane faces. The cut surface is capped with a flat face, so the result is still a solid you can go on building with.

<!--  Before and after showing an object being sliced at a specific height -->
![20260506 155526 paste 20260506 155526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155526-paste-20260506-155526.jpg)

## How to Use

1. Select an object
2. Apply the **Plane Cut** operation from the Reshape menu
3. Put the plane where you want the cut -- drag its handles in the viewport, or type the values into the **Plane** row

The plane starts level, facing up, 10mm above the object's own zero, which is where the old Cut Height slider started.

## The Plane

The **Plane** row is the construction plane the cut is made on:

- **XY / XZ / YZ** -- the three level and upright presets. **Custom** opens the values for editing
- **Flip** -- turns the plane around, so the half that was thrown away is the half that is kept
- **Pick Face** -- click a flat face on any model in the scene and the plane lands on it
- **Plane Values** -- **Origin** (where the plane sits), **Normal** (which way it faces, and so which side is cut off) and **X Direction** (how the plane is spun within itself; it makes no difference to a cut)

In the viewport the selected Plane Cut draws its plane over the part, and the standard selection handles edit that plane rather than the operation: the up arrow moves the plane up and down in world Z, and the three curved rotate arrows tilt it. The Plane row follows along - the tab flips to Custom as soon as the plane is tilted, and Origin Z tracks the arrow. Every value can also be driven by an [expression](../../workspace/expressions.md).

## Tips

- Use Plane Cut to flatten the top of a model at a specific height, or to trim an imported model down to a flat base
- A tilted cut is direct: turn the plane, do not rotate the object
- For cutting with a non-planar shape, use [Subtract](../boolean/subtract.md) with another object instead
- To get the cross section itself as a 2D path instead of a cut solid, use [Slice to Path](slice-to-path.md)

## Related

- [Construction Planes](../../workspace/construction-planes.md) - the plane the cut is made on
- [Slice to Path](slice-to-path.md) - Keep the outline where the plane crosses, rather than the solid
- [Intersect](../boolean/intersect.md) - Keep only where objects overlap
- [Subtract](../boolean/subtract.md) - Cut with any shape, not just a plane
- [Hollow Out](hollow-out.md) - Create a hollow shell
