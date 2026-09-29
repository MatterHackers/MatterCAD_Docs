---
title: Bounds
articleKey: BoundsObject3D
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 5
---
# Bounds

Bounds replaces the selected parts with a solid box that exactly fills the space they take up (their bounding box, lined up with the X, Y and Z axes). The parts stay inside the Bounds, hidden, so the box follows them: move or resize a part and the box changes with it.

## How to Use

1. Select one or more parts
2. Choose **Bounds** from the Placement menu
3. Read the box's corners and size in the properties panel

## Values

These are measured for you and can't be typed over:

- **Min** - The low corner of the box (smallest X, Y and Z)
- **Max** - The high corner of the box (largest X, Y and Z)
- **Size** - The box's width, depth and height
- **Center** - The middle of the box

Formulas in other parts can read one part of a value by adding its letter: `=Bounds.Max.Z` is the height of the top of the box, and `=Bounds.Size.X` its width. Use the Bounds' own name in the scene tree in place of `Bounds` if you renamed it.

## In a Node Graph

Bounds is also a node (Add Node > Operations). Wire parts into its **Source**; its **Result** is the box, and its **Min**, **Max**, **Size** and **Center** are outputs you can wire into another card's settings - through Separate XYZ for a single number, or into an Inside Box node to round only the edges inside the box. See *Values Between Nodes* on the [Node Graphs](../../workspace/node-graphs.md) page.

## Tips

- Use Bounds to make a block exactly as big as another part, such as a base or a mold box
- Apply the Bounds to keep the box as a plain part and drop the parts it measured

## Related

- [Fit to Bounds](fit-to-bounds.md) - Scale a part to fit a box of the size you choose
- [Align](align.md) - Position parts relative to each other
- [Node Graphs](../../workspace/node-graphs.md) - Wire a Bounds' values into other nodes
