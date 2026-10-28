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

Array makes many copies of a part and arranges them in a pattern: a row, a ring, or a series of steps that each move, turn and grow a little more. The copies stay one editable part, so changing a setting rearranges all of them at once.

<!-- IMAGE_NEEDED: Screenshot of the Array panel showing the Mode tabs at the top (Line | Circle | Transform) -->


## How to Use

1. Select the part you want copies of
2. Click **Array** in the Duplication group of the toolbar
3. Choose a **Mode** on the tabs at the top of the panel: **Line**, **Circle** or **Transform**
4. Adjust the settings for that mode, or drag the handles in the 3D view

The copies appear at once. Undo takes the whole Array back in one step and leaves your part as it was.

## Mode: Line

Line places copies in a row, each one further along than the last, with optional turning and growing as the row goes.

**Count** — Number of copies, the original included (default 3). The original is the first copy; the others are offset from it.

**Offset Method** — How the spacing is set:
- **Relative** (default) — The spacing is a share of the part's own size. A **Relative Offset** of (1, 0, 0), the default, puts the copies side by side along X.
- **Offset** — A fixed distance in mm from each copy to the next (default 10, 0, 0).
- **Endpoint** — Where the last copy goes, measured from the first (default 100, 0, 0); the copies are spaced evenly between.

**Relative Offset** / **Offset** / **Endpoint** — The spacing itself, for the chosen Offset Method.

**Rotation Mode** — How turning adds up along the row:
- **Local** (default) — Each copy turns in place about its own center; the row stays straight.
- **Compounding** — The turns add up and steer the row, so it curls into arcs, fans, spirals and helices.

**Rotation** — How many degrees each copy turns more than the one before, on each axis (default 0, 0, 0).

**Scale** — How much each copy grows or shrinks compared with the one before, on each axis (default 1, 1, 1). Below 1 shrinks, above 1 grows.

**Scale Affects Offset** — On by default. The spacing grows or shrinks with the copies, so they keep touching. Use it for nautilus shells and other rows that tighten as they go.

## Mode: Circle

Circle places copies evenly around an axis, at a set distance from it.

<!-- IMAGE_NEEDED: Screenshot of Array in Circle mode showing 6 copies arranged in a circle, with the Radius and Central Axis rows visible -->


**Count Method** — How the number of copies is set:
- **Count** (default) — You give the number of copies.
- **Distance** — You give the angle between copies, and as many copies as fit are made.

**Count** / **Angular Distance** — The number of copies (default 3), or the angle between copies in degrees (default 30). Both take expressions.

**Central Axis** — The axis the copies go around, picked on its tabs: **XY** goes around Z (the default), **XZ** around Y and **YZ** around X. The ring is centered on your part. **Custom** shows two more rows for any other axis: **Origin**, the center of the ring, and **Normal**, the direction of the axis (any length will do). See [Construction Planes](../../workspace/construction-planes.md).

**Flip** — Reverses the axis, so the copies are laid out the other way around.

**Circle Segment** — **Full** (default) spreads the copies all the way around; **Arc** spreads them over part of the circle.

**Radius** — How far each copy is from the axis, in mm (default 30).

**Sweep Angle** — How many degrees of arc to fill (default 90; shown when Circle Segment is Arc). Takes expressions.

**Align Rotation** — On by default: each copy turns with its place around the circle, so every copy faces the center the way the original does. Off: every copy keeps the original's direction.

## Mode: Transform

Transform steps each copy on from the one before, by a move, a turn and a size change you give, or by copying another part's move.

**Count** — Number of copies.

**Transform Reference** — Where each step comes from:
- **Input** (default) — You type the step in the rows below.
- **Object** — Each step is the move of another part in your design, found by its name.

**Transform Translation** — How far each copy moves on from the one before, in mm (default 10, 0, 0; shown when Reference is Input).

**Transform Rotation** — How many degrees each copy turns more than the one before, per axis (default 0, 0, 0; shown when Reference is Input).

**Scale** — How much bigger or smaller each copy is than the one before, the same on every axis (default 1; shown when Reference is Input). 2 doubles the size at each step, so three copies are 1×, 2× and 4× the size of the original; 0.5 halves it. Scale multiplies **Scale Axes**: a Scale of 2 with Scale Axes of 1.5, 1, 1 makes each copy 3 times as long along X as the one before, and twice as big along Y and Z. Takes expressions.

**Scale Axes** — The same step-by-step size change, set separately for X, Y and Z (default 1, 1, 1; shown when Reference is Input).

**Transform Name** — The name of the part whose move each step copies (shown when Reference is Object). Capitals don't matter. A name that matches nothing steps by the Input rows instead.

**Relative Space** — On by default (shown when Reference is Object). On: each step uses the named part's own move, turn and scale inside the group it is in. Off: it uses where that part really sits in the design, so the moves of every group it is inside count too.

## Randomize

Turn on **Randomize** (off by default) to vary the copies. Every random amount starts at 0.

- **Random Offset** — The most each copy can move at random, per axis, in mm.
- **Random Rotation** — The most each copy can turn at random, per axis, in degrees.
- **Random Scale Axes** — How much each copy's size can change at random along each axis, as a share of its size: 0.2 lets a copy grow or shrink by up to 20%.
- **Exclude First** — Keep the first copy exactly in place (on by default).
- **Exclude Last** — Keep the last copy exactly in place.
- **Random Seed** — Change it to get a different random arrangement (default 0). The same seed always gives the same copies. Takes expressions.

## Output

- **Create Single Mesh** — Off by default. Joins all the copies into one mesh.
- **Merge** — Off by default. Joins points of the copies that are closer than **Distance** (shown when Create Single Mesh is on).
- **Distance** — How close two points must be to be joined, in mm (default 0.01; shown when Merge is on).

## Handles in the 3D View

While the Array is selected, spheres in the 3D view let you change it by dragging instead of typing:

- **Line**, with Offset Method at **Offset** or **Endpoint**: a sphere sets the **Offset** or the **Endpoint**. Drag it and the copies follow.
- **Circle**: a sphere out from the center sets the **Radius**. With Circle Segment at **Arc**, a sphere on the circle sets the **Sweep Angle**; with Count Method at **Distance**, one sets the **Angular Distance**.

Let go and the change is one undo step; press **Esc** during a drag to put the value back. A handle hides while its setting is a formula, since dragging would replace the formula.

## How Array Is Built

Array is built as a [node graph](../../workspace/node-graphs.md): boxes wired together, each doing one step of making the copies. Turn on **Show Graph** in the panel to see how it works, and change it if you want something Array does not do, such as copies along a curve or random flips. The graph's settings are the rows above, so you never need to open it to use Array.

## Arrays in Older Designs

A design saved before Array became a node graph keeps its Array as it was, and it works exactly as before. Its panel differs a little:

- The modes are called **Linear**, **Radial** and **Transform**.
- Its **Central Axis** shows the full [construction plane](../../workspace/construction-planes.md): an **X Direction** row (not used by Array) and **Pick Face**, which aims the axis at a flat face you click in the scene (Esc cancels). An Array made before construction planes keeps a direction with an axis dropdown instead.
- Its join settings sit under a **Merge** heading.
- A Transform array saved with its **Scale** set to anything other than 1 builds without Scale, so the design keeps the shape it was saved with, and its Scale row is hidden. Use **Scale Axes** to change the size of its copies.
- Inside one of these Arrays, `[index]` in an expression is the copy's own position counting from 0. Pair it with `index()` to give every copy its own row of a [Variable Sheet](../../workspace/variable-sheet.md), as in `=index("A", [index]+2)`, and use [Select Child](select-child.md) to pick one copy out by its index or name.

## Tips

- Use expressions for Count, Rotation or Endpoint to make patterns that follow the rest of your design
- For a ring, use Circle mode: set Radius for the size of the circle, and keep Align Rotation on if the copies should face outward
- Compounding rotation in Line mode makes spirals and fans without working out each angle
- Scale Affects Offset makes nautilus-shell rows that tighten as they go

## Related

- [Node Graphs](../../workspace/node-graphs.md) - How the graph Array is built from works, and the Copies nodes it uses
- [Construction Planes](../../workspace/construction-planes.md) - The planes behind the Central Axis
- [Align](../placement/align.md) - Position objects relative to each other
- [Select Child](select-child.md) - Pick a specific copy from an older Array by index or name
- [Expressions](../../workspace/expressions.md) - Formulas in Array's settings
