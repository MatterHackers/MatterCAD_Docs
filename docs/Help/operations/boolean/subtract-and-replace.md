---
title: Subtract and Replace
articleKey: SubtractAndReplaceObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 4
---
# Subtract and Replace

Subtract and Replace subtracts the parts you choose out of the parts you did not, but keeps the piece that was cut away as its own part instead of discarding it. Use **Part(s) to Subtract** to pick the cutting shapes; everything else is the base that gets cut.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->
![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)

[Combine](combine.md), [Subtract](subtract.md), [Intersect](intersect.md) and Subtract and Replace are all performed by one Boolean object -- the toolbar button creates it with Subtract & Replace already selected, and you can switch to any of the other three at any time from the **Operation** icon row at the top of the Properties panel.

Subtract & Replace is not offered for 2D paths -- a region has no removed volume to hand back.

## How to Use

1. Select two or more objects
2. Click **Subtract & Replace** in the toolbar
3. Use **Part(s) to Subtract** to choose which children are the cutting shapes
4. Change your mind at any time by clicking a different icon in the **Operation** row at the top of the Properties panel -- the shape rebuilds with the new operation

## Parameters

- **Operation** - Which boolean to perform. Shown as an icon row at the top of the panel
- **Part(s) to Subtract** - Which children are the cutting shapes
- **Keep Inside Out Geometry** - Treat an inside-out shell as solid material instead of letting it cancel out the volume around it. Turn this on when a model that should be solid comes back with parts missing. It forces the slower, exact boolean engine
- **Repair Winding Order** - Rewind each part's inside-out shells before the boolean runs. This fixes the geometry once rather than changing what every later operation counts as solid, and is usually the better of the two answers to an inside-out model

## Tips

- The two parts fit together exactly, because they came out of the same operation
- Use it for multi-color designs, interlocking assemblies, and inlays
- If a result looks wrong, check that the source objects are watertight. **Repair Winding Order** fixes inside-out shells; [Repair](../mesh/repair.md) fixes broader damage in imported models

## Related

- [Combine](combine.md) - Merge multiple objects into a single solid shape
- [Subtract](subtract.md) - Cut one shape out of another
- [Intersect](intersect.md) - Keep only the volume where objects overlap
- [Plane Cut](../reshape/plane-cut.md) - Cut with a flat plane instead of another shape
- [Repair](../mesh/repair.md) - Fix damaged imported meshes before a boolean

This page also covers the older Subtract and Replace objects still found in designs saved before the operations were merged. They keep working exactly as they did; new designs use the shared Boolean object with the Subtract & Replace operation selected.
