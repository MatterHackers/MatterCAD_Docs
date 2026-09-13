---
title: Slice to Path
articleKey: FindSliceObject3D_2, FindSliceObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 12
---
# Slice to Path

Slice to Path cuts a solid with a [construction plane](../../workspace/construction-planes.md) and hands you the outline where the plane crossed it, as a 2D path. It is how you get a real cross section of a part out as something you can go on building with -- extrude it, offset it, or use it as the profile of a [Sweep](../path/sweep.md).

<!-- IMAGE_NEEDED: Screenshot of a Slice to Path applied to a solid, showing the flat outline path where the slice plane crossed the part -->

Nothing is removed from the source. The solid goes in and an outline comes out; the original is kept underneath and hidden, so you can move the plane and take a different section at any time.

The section is drawn on the plane it was taken on, not flattened back onto the bed. Anything built over it -- an [Outline](../path/outline-path.md), a [Linear Extrude](../path/linear-extrude.md) -- stands where the section actually lies.

## How to Use

1. Select a solid
2. Click **Slice to Path** in the Reshape group of the toolbar
3. Put the plane through the part where you want the section -- drag its handles in the viewport, or type the values into the **Plane** row
4. Apply a path operation to the result -- [Linear Extrude](../path/linear-extrude.md) is the usual next step

The operation is enabled for anything with a mesh. The plane starts level, facing up, 10mm above the object's own zero -- measured from where the Slice to Path sits, not from the bed.

## The Plane

The **Plane** row is the construction plane the section is taken on:

- **XY / XZ / YZ** -- the three level and upright presets. **Custom** opens the values for editing
- **Flip** -- turns the plane around. The section is the same, but the path is seen from the other side
- **Pick Face** -- click a flat face on any model in the scene and the plane lands on it
- **Plane Values** -- **Origin** (where the plane sits), **Normal** (which way it faces) and **X Direction** (which way is "right" on the plane, and so how the resulting path is spun)

In the viewport the selected Slice to Path draws its plane through the part, and the standard selection handles edit that plane rather than the operation: the up arrow moves the plane up and down in world Z, and the three curved rotate arrows tilt it. The Plane row follows along - the tab flips to Custom as soon as the plane is tilted, and Origin Z tracks the arrow. Every value can also be driven by an [expression](../../workspace/expressions.md).

## Parameters

- **Fill Type** - How overlapping loops in the section are read, when a slice comes back with more than one outline:
  - **Even Odd** - Alternating. The first loop is solid, a loop inside it is a hole, a loop inside that is solid again. This is the default and matches how most parts read
  - **Non Zero** - A region is solid if the loops around it wind a net non-zero number of times. Overlapping outlines merge rather than cancelling
  - **Positive** - Keeps regions wound counterclockwise
  - **Negative** - Keeps regions wound clockwise

If the object being sliced has several visible parts, each is sliced and the results are unioned together under the fill rule you chose.

## Tips

- Use it to lift a profile off an imported STL you cannot otherwise edit: slice it, then extrude the outline to a height you control
- A slice exactly on the top or bottom face of a part is a coin toss. Move the plane a fraction into the solid
- A tilted section is direct: turn the plane, do not rotate the object
- **Apply** turns the result into an editable [Custom Path](../../2d-paths/custom-path.md) on the same plane, which you can then reshape point by point
- Two slices on two planes give you two sections you can [Loft](../path/loft.md) between, which is a quick way to simplify an organic shape
- Slice to Path is not [Plane Cut](plane-cut.md). Plane Cut keeps the solid and throws away what is on the other side of the plane; Slice to Path throws away the solid and keeps the outline

## Related

- [Construction Planes](../../workspace/construction-planes.md) - the plane the section is taken on
- [Plane Cut](plane-cut.md) - Cut a solid with a plane and keep the solid
- [Linear Extrude](../path/linear-extrude.md) - Give the sliced outline a new height
- [Loft](../path/loft.md) - Blend between two sections
- [Custom Path](../../2d-paths/custom-path.md) - What an applied slice becomes
- [Border Path](../path/border-path.md) - Offset the sliced outline outward
