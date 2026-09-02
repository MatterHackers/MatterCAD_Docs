---
title: Combine
articleKey: CombineObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 1
---
# Combine

Combine merges everything into a single solid. Internal faces where the shapes overlapped are removed, so the result is one continuous mesh rather than overlapping shells.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->
![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)

Combine, [Subtract](subtract.md), [Intersect](intersect.md) and [Subtract and Replace](subtract-and-replace.md) are all performed by one Boolean object -- the toolbar button creates it with Combine already selected, and you can switch to any of the other three at any time from the row of operation icon tabs at the top of the Properties panel.

Combine works on solids and on 2D paths. It looks at what you gave it and does the right kind of operation, so combining two paths produces one path and combining two meshes produces one solid.

## How to Use

1. Select two or more objects
2. Click **Combine** in the toolbar
3. Change your mind at any time by clicking a different operation tab at the top of the Properties panel (each tab shows the operation's icon, hover for its name) -- the shape rebuilds with the new operation

## Parameters

- **Operation** - Which boolean to perform. Shown as a row of icon tabs at the top of the panel
- **Keep Inside Out Geometry** - Treat an inside-out shell as solid material instead of letting it cancel out the volume around it. Turn this on when a model that should be solid comes back with parts missing. It forces the slower, exact boolean engine
- **Repair Winding Order** - Rewind each part's inside-out shells before the boolean runs. This fixes the geometry once rather than changing what every later operation counts as solid, and is usually the better of the two answers to an inside-out model

## Tips

- Combine will still join non-overlapping objects into one mesh, but they stay visually separate
- Combine handles Hole objects for you: anything marked as a hole is subtracted from the result rather than added to it
- Combine carries per-face colors through from the original objects
- If a result looks wrong, check that the source objects are watertight. **Repair Winding Order** fixes inside-out shells; [Repair](../mesh/repair.md) fixes broader damage in imported models

## Related

- [Subtract](subtract.md) - Cut one shape out of another
- [Intersect](intersect.md) - Keep only the volume where objects overlap
- [Subtract and Replace](subtract-and-replace.md) - Subtract one shape and keep the piece that was cut away
- [Plane Cut](../reshape/plane-cut.md) - Cut with a flat plane instead of another shape
- [Hole](../../primitives/hole.md) - A cube pre-configured to subtract
- [Repair](../mesh/repair.md) - Fix damaged imported meshes before a boolean

This page also covers the older Combine objects still found in designs saved before the operations were merged. They keep working exactly as they did; new designs use the shared Boolean object with the Combine operation selected.
