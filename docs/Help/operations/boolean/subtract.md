---
title: Subtract
articleKey: SubtractObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 2
---
# Subtract

Subtract cuts the parts you choose out of the parts you did not. Use **Part(s) to Subtract** to pick the cutting shapes; everything else is the base that gets cut.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->
![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)

[Combine](combine.md), Subtract, [Intersect](intersect.md) and [Subtract and Replace](subtract-and-replace.md) are all performed by one Boolean object -- the toolbar button creates it with Subtract already selected, and you can switch to any of the other three at any time from the row of operation icon tabs at the top of the Properties panel.

Subtract works on solids and on 2D paths. It looks at what you gave it and does the right kind of operation, so subtracting one path from another produces a path and subtracting one mesh from another produces a solid.

## How to Use

1. Select two or more objects
2. Click **Subtract** in the toolbar -- a default part to cut away is picked for you so it does something right away
3. Use **Part(s) to Subtract** to choose which children are the cutting shapes
4. Change your mind at any time by clicking a different operation tab at the top of the Properties panel (each tab shows the operation's icon, hover for its name) -- the shape rebuilds with the new operation

## Parameters

- **Operation** - Which boolean to perform. Shown as a row of icon tabs at the top of the panel
- **Keep Inside Out Geometry** - Treat an inside-out shell as solid material instead of letting it cancel out the volume around it. Turn this on when a model that should be solid comes back with parts missing. It forces the slower, exact boolean engine
- **Repair Winding Order** - Rewind each part's inside-out shells before the boolean runs. This fixes the geometry once rather than changing what every later operation counts as solid, and is usually the better of the two answers to an inside-out model
- **Part(s) to Subtract** - Which children are the cutting shapes
- **Keep Subtracted Parts** - Leave the parts that were cut away in the scene rather than discarding them

## Tips

- Objects have to overlap for Subtract to do anything
- To cut a through-hole, make sure the cutting object passes completely through the base
- For a simple hole, the [Hole](../../primitives/hole.md) primitive is already set up to subtract
- The cutting objects stay in the design tree, so you can move or resize them and the cut updates
- If a result looks wrong, check that the source objects are watertight. **Repair Winding Order** fixes inside-out shells; [Repair](../mesh/repair.md) fixes broader damage in imported models

## Related

- [Combine](combine.md) - Merge multiple objects into a single solid shape
- [Intersect](intersect.md) - Keep only the volume where objects overlap
- [Subtract and Replace](subtract-and-replace.md) - Subtract one shape and keep the piece that was cut away
- [Plane Cut](../reshape/plane-cut.md) - Cut with a flat plane instead of another shape
- [Hole](../../primitives/hole.md) - A cube pre-configured to subtract
- [Repair](../mesh/repair.md) - Fix damaged imported meshes before a boolean

This page also covers the older Subtract objects still found in designs saved before the operations were merged. They keep working exactly as they did; new designs use the shared Boolean object with the Subtract operation selected.
