---
title: Slice to Path
articleKey: FindSliceObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 12
---
# Slice to Path

Slice to Path cuts a solid with a horizontal plane and hands you the outline where the plane crossed it, as a 2D path. It is how you get a real cross section of a part out as something you can go on building with -- extrude it, offset it, or use it as the profile of a [Sweep](../path/sweep.md).

<!-- IMAGE_NEEDED: Screenshot of a Slice to Path applied to a solid, showing the flat outline path where the slice plane crossed the part -->

Nothing is removed from the source. The solid goes in and a flat outline comes out; the original is kept underneath and hidden, so you can change the height and take a different section at any time.

## How to Use

1. Select a solid
2. Click **Slice to Path** in the Reshape group of the toolbar
3. Set **Slice Height** to the level you want the section taken at
4. Apply a path operation to the result -- [Linear Extrude](../path/linear-extrude.md) is the usual next step

The operation is enabled for anything with a mesh.

The plane is horizontal (perpendicular to Z) and sits at Slice Height in the object's own space -- so it is measured from where the Slice to Path sits, not from the bed. Rotate the Slice to Path to take a section on a different axis.

## Parameters

- **Slice Height** - How far up to take the section (default 10). A height above or below the part gives you an empty path
- **Fill Type** - How overlapping loops in the section are read, when a slice comes back with more than one outline:
  - **Even Odd** - Alternating. The first loop is solid, a loop inside it is a hole, a loop inside that is solid again. This is the default and matches how most parts read
  - **Non Zero** - A region is solid if the loops around it wind a net non-zero number of times. Overlapping outlines merge rather than cancelling
  - **Positive** - Keeps regions wound counterclockwise
  - **Negative** - Keeps regions wound clockwise

If the object being sliced has several visible parts, each is sliced and the results are unioned together under the fill rule you chose.

## Tips

- Use it to lift a profile off an imported STL you cannot otherwise edit: slice it, then extrude the outline to a height you control
- A slice exactly at the top or bottom face of a part is a coin toss. Move the height a fraction into the solid
- **Apply** turns the result into an editable [Custom Path](../../2d-paths/custom-path.md), which you can then reshape point by point
- Two slices at two heights give you two sections you can [Loft](../path/loft.md) between, which is a quick way to simplify an organic shape
- Slice to Path is not [Plane Cut](plane-cut.md). Plane Cut keeps the solid and throws away what is above (or below) the plane; Slice to Path throws away the solid and keeps the outline

## Related

- [Plane Cut](plane-cut.md) - Cut a solid at a height and keep the solid
- [Linear Extrude](../path/linear-extrude.md) - Give the sliced outline a new height
- [Loft](../path/loft.md) - Blend between two sections taken at two heights
- [Custom Path](../../2d-paths/custom-path.md) - What an applied slice becomes
- [Border Path](../path/border-path.md) - Offset the sliced outline outward
