---
title: Array
articleKey: ArrayObject3D_3, ArrayObject3D_2
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 1
description: Make many copies of a part in a row, a grid, a circle or along a path, all in one editable pattern.
keywords: copies, repeat, pattern, circular pattern, polar array, copies in a circle, grid of copies
---
# Array

Array creates multiple copies of an object arranged in a pattern. Select a mode from the buttons at the top — **Linear**, **Radial**, or **Transform** — to switch between pattern types.

<!-- IMAGE_NEEDED: Screenshot of the Array operation panel showing the mode buttons at the top (Linear | Radial | Transform) -->


## How to Use

1. Select one part
2. Click **Array** in the Duplication group of the toolbar
3. Choose a mode (Linear, Radial, or Transform)
4. Adjust the parameters for the chosen mode

## Mode: Linear

Linear mode places copies along a direction with optional rotation and scale progression.

**Count** — Number of copies, the source included (default 3; the slider runs 1 to 200). The source object is the first copy; additional copies are offset from it.

**Offset Method** — How spacing is calculated:
- **Relative** (default) — Offset is multiplied by the object's bounding box size. A Relative Offset of (1, 0, 0), the default, spaces copies exactly one object-width apart along X.
- **Offset** — Fixed world-space distance in mm per copy (default 10, 0, 0).
- **Endpoint** — Set the position of the last copy relative to the first (default 100, 0, 0); spacing is divided evenly between copies.

**Relative Offset** / **Offset** / **Endpoint** — The spacing vector, depending on the selected Offset Method.

**Rotation Mode** — How rotation accumulates across copies:
- **Local** (default) — Each copy rotates in place at its own center; the offset direction stays in world axes.
- **Compounding** — Rotation accumulates and steers the offset, producing spirals, fans, and helices.

**Rotation** — Per-copy rotation in degrees on each axis (default 0, 0, 0).

**Scale** — Per-copy cumulative scale on each axis (default 1, 1, 1). Values less than 1 shrink copies; values greater than 1 grow them.

**Scale Affects Offset** — On by default. When on, the spacing between copies also scales with each step. Use this for tightening spirals and geometric progressions (nautilus shells, stacked nail-shell curves).

## Mode: Radial

Radial mode distributes copies evenly around a central axis at a fixed radius.

<!-- IMAGE_NEEDED: Screenshot of Array in Radial mode showing 6 copies arranged in a circle, with Radius and Central Axis parameters visible -->


**Count Method** — How the number of copies is determined:
- **Count** (default) — Explicit number of copies.
- **Distance** — Angular gap between copies in degrees; count is calculated to fill the sweep.

**Count** / **Angular Distance** — Number of copies (Count mode, default 3) or angular spacing in degrees (Distance mode, default 30; 1 to 360). Supports expressions.

**Central Axis** — The axis the copies circle, given as a [construction plane](../../workspace/construction-planes.md): its normal is the axis and its origin is the centre of the circle. The origin starts at the centre of the source object's bounding box, and the axis is drawn in the viewport while the Array is selected.

- **XY / XZ / YZ / Custom** — The tabs choose the axis: **XY** circles about Z (the default), **XZ** about Y, **YZ** about X. **Custom** shows the plane's values for an axis none of the tabs describe. Choosing a tab re-aims the axis and leaves the origin where it is.
- **Flip** — Reverses the axis, which reverses the direction copies are laid out in.
- **Origin** — The centre of the circle. Supports expressions per component.
- **Normal** — The axis itself; any length will do.
- **X Direction** — Not used by Array. An axis has no need of a sideways direction.
- **Pick Face** — Click the button, then click a flat face anywhere in the scene to circle about that face's normal. Press Esc to cancel.

**Circle Segment** — Whether copies span a full 360° circle (**Full**, the default) or a partial arc (**Arc**).

**Radius** — Distance from the central axis to each copy, in mm (default 30; the slider runs 0 to 500).

**Sweep Angle** — Degrees of arc to fill (default 90; -360 to 360; shown when Circle Segment is Arc). Supports expressions.

**Align Rotation** — On by default: each copy turns with its place around the circle, so every copy faces the center the way the original does. Off: every copy keeps the original's direction.

## Mode: Transform

Transform mode steps copies using a manual transform or by following another object's transform.

**Count** — Number of copies (integer or expression).

**Transform Reference** — Where the per-step transform comes from:
- **Input** (default) — You specify the translation, rotation and scale directly.
- **Object** — The transform is read from a named sibling object.

**Transform Translation** — Per-step offset in mm (default 10, 0, 0; shown when Reference is Input).

**Transform Rotation** — Per-step rotation in degrees per axis (default 0, 0, 0; shown when Reference is Input).

**Scale** — How much bigger or smaller each copy is than the one before, the same on every axis (default 1; shown when Reference is Input). 2 doubles the size at each step, so three copies are 1×, 2× and 4× the size of the original; 0.5 halves it at each step. Scale multiplies **Scale Axes**: a Scale of 2 with Scale Axes of 1.5, 1, 1 makes each copy 3 times as long along X as the one before, and twice as big along Y and Z. Supports expressions.

**Scale Axes** — The same step-by-step size change, set separately for X, Y and Z (default 1, 1, 1; shown when Reference is Input). 1 keeps that axis the size of the copy before.

**Transform Name** — Name of the sibling object whose transform is used as the per-step increment (shown when Reference is Object).

**Relative Space** — On by default (shown when Reference is Object). When on, each step uses the named object's own move, turn and scale relative to the group it is in. When off, it uses where that object really sits in the design, so the moves of every group it is inside count too. Either way the steps add up from copy to copy the same way.

## Randomize

Turn on **Randomize** (off by default) to add variation to the copies. Every random amount starts at 0.

- **Random Offset** — Maximum random position offset per axis in mm.
- **Random Rotation** — Maximum random rotation per axis in degrees.
- **Random Scale Axes** — How much each copy's size can randomly change along each axis, as a fraction of its size: 0.2 lets a copy grow or shrink by up to 20% along that axis.
- **Exclude First** — Keep the first copy at its exact computed position (default: on).
- **Exclude Last** — Keep the last copy at its exact computed position.
- **Random Seed** — Change this to get a different random arrangement (default 0). Supports expressions.

## Merge

- **Create Single Mesh** — Off by default. Combine all copies into one merged mesh object.
- **Merge** — Off by default. Weld points of the copies that lie within **Distance** of each other (shown when Create Single Mesh is on).
- **Distance** — How close two points must be to be welded, in mm (default 0.01; the slider runs 0 to 1; shown when Merge is on).

## Older files

An Array created before construction planes shipped keeps its original **Central Axis** control — a direction vector with an axis dropdown — and keeps working exactly as it did. New Array operations get the construction plane described above. To move an old one over, delete it and apply Array again.

A Transform array saved by an earlier version of MatterCAD with its **Scale** set to anything other than 1 builds without Scale, so the design keeps the shape it was saved with, and its Scale row is hidden. To change the size of its copies, use **Scale Axes**.

## Tips

- Use expressions for Count, Rotation, or Endpoint to create parametric patterns
- For circular patterns, use Radial mode — set Radius to control the circle size and enable Align Rotation if copies should face outward
- Compounding rotation in Linear mode creates spirals and fans without manually calculating angle offsets
- Scale Affects Offset creates nautilus-shell and geometric-progression layouts naturally
- Combine Array with [Select Child](select-child.md) to create patterns where each copy shows a different variant
- Inside an Array, `[index]` in an expression is the copy's own position counting from 0 — pair it with `index()` to give every copy its own row of a [Variable Sheet](../../workspace/variable-sheet.md), as in `=index("A", [index]+2)`

## Related

- [Construction Planes](../../workspace/construction-planes.md) - Presets, expressions, and Pick Face for the Central Axis
- [Align](../placement/align.md) - Position objects relative to each other
- [Select Child](select-child.md) - Pick a specific copy from an array by index or name
- [Expressions](../../workspace/expressions.md) - Drive each copy from `[index]` and sheet values
