---
title: Array
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 1
---
# Array

Array creates multiple copies of an object arranged in a pattern. Select a mode from the buttons at the top — **Linear**, **Radial**, or **Transform** — to switch between pattern types.

<!--  Screenshot of the Array operation panel showing the mode buttons at the top (Linear | Radial | Transform) -->
![20260506 080647 paste 20260506 080647](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080647-paste-20260506-080647.jpg)


## How to Use

1. Select an object
2. Apply the **Array** operation from the Duplication menu
3. Choose a mode (Linear, Radial, or Transform)
4. Adjust the parameters for the chosen mode

## Mode: Linear

Linear mode places copies along a direction with optional rotation and scale progression.

**Count** — Number of copies (integer or expression). The source object is the first copy; additional copies are offset from it.

**Offset Method** — How spacing is calculated:
- **Relative** — Offset is multiplied by the object's bounding box size. A Relative Offset of (1, 0, 0) spaces copies exactly one object-width apart along X.
- **Offset** — Fixed world-space distance in mm per copy.
- **Endpoint** — Set the position of the last copy; spacing is divided evenly between copies.

**Relative Offset** / **Offset** / **Endpoint** — The spacing vector, depending on the selected Offset Method.

**Rotation Mode** — How rotation accumulates across copies:
- **Local** — Each copy rotates in place at its own center; the offset direction stays in world axes.
- **Compounding** — Rotation accumulates and steers the offset, producing spirals, fans, and helices.

**Rotation** — Per-copy rotation in degrees on each axis.

**Scale** — Per-copy cumulative scale on each axis. Values less than 1 shrink copies; values greater than 1 grow them.

**Scale Affects Offset** — When on, the spacing between copies also scales with each step. Use this for tightening spirals and geometric progressions (nautilus shells, stacked nail-shell curves).

## Mode: Radial

Radial mode distributes copies evenly around a central axis at a fixed radius.

<!--  Screenshot of Array in Radial mode showing 6 copies arranged in a circle, with Radius and Central Axis parameters visible -->
![20260506 092618 paste 20260506 092618](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-092618-paste-20260506-092618.jpg)


**Count Method** — How the number of copies is determined:
- **Count** — Explicit number of copies.
- **Distance** — Angular gap between copies in degrees; count is calculated to fill the sweep.

**Count** / **Angular Distance** — Number of copies (Count mode) or angular spacing in degrees (Distance mode). Supports expressions.

**Central Axis** — The axis to rotate around (default: Z).

**Circle Segment** — Whether copies span a full 360° circle (**Full**) or a partial arc (**Arc**).

**Radius** — Distance from the central axis to each copy.

**Sweep Angle** — Degrees of arc to fill (shown when Circle Segment is Arc). Supports expressions.

**Align Rotation** — Rotate each copy so its forward axis points outward from the center.

**Forward Axis** — Which axis of the copy is treated as "forward" for alignment (shown when Align Rotation is on).

## Mode: Transform

Transform mode steps copies using a manual transform or by following another object's transform.

**Count** — Number of copies (integer or expression).

**Transform Reference** — Where the per-step transform comes from:
- **Input** — You specify translation, rotation, and scale directly.
- **Object** — The transform is read from a named sibling object.

**Translation** — Per-step world-space offset in mm (shown when Reference is Input).

**Rotation** — Per-step rotation in degrees per axis (shown when Reference is Input).

**Scale** / **Scale Axes** — Uniform and per-axis scale applied at each step (shown when Reference is Input).

**Transform Name** — Name of the sibling object whose transform is used as the per-step increment (shown when Reference is Object).

**Relative Space** — When on, each copy's transform compounds in the local frame of the previous copy; when off, each step is applied in world space (shown when Reference is Object).

## Randomize

Enable **Randomize** to add variation to all copies.

- **Random Offset** — Maximum random position offset per axis in mm.
- **Random Rotation** — Maximum random rotation per axis in degrees.
- **Random Scale Axes** — Maximum random scale variation per axis.
- **Exclude First** — Keep the first copy at its exact computed position (default: on).
- **Exclude Last** — Keep the last copy at its exact computed position.
- **Random Seed** — Change this to get a different random arrangement. Supports expressions.

## Merge

- **Create Single Mesh** — Combine all copies into one merged mesh object.
- **Merge Vertices** — Weld vertices within the merge distance threshold (shown when Create Single Mesh is on).
- **Distance** — Merge threshold in mm (shown when Merge Vertices is on).

## Tips

- Use expressions for Count, Rotation, or Endpoint to create parametric patterns
- For circular patterns, use Radial mode — set Radius to control the circle size and enable Align Rotation if copies should face outward
- Compounding rotation in Linear mode creates spirals and fans without manually calculating angle offsets
- Scale Affects Offset creates nautilus-shell and geometric-progression layouts naturally
- Combine Array with [Select Child](select-child.md) to create patterns where each copy shows a different variant

## Related

- [Align](../placement/align.md) - Position objects relative to each other
- [Select Child](select-child.md) - Pick a specific copy from an array by index or name
