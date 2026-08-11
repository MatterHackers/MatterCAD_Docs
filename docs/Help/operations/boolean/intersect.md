---
title: Intersect
articleKey: IntersectionObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 3
---
# Intersect

Intersect keeps only the volume every object shares and discards the rest.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->
![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)

[Combine](combine.md), [Subtract](subtract.md), Intersect and [Subtract and Replace](subtract-and-replace.md) are all performed by one Boolean object -- the toolbar button creates it with Intersect already selected, and you can switch to any of the other three at any time from the **Operation** icon row at the top of the Properties panel.

Intersect works on solids and on 2D paths. It looks at what you gave it and does the right kind of operation, so intersecting two paths produces one path and intersecting two meshes produces one solid.

## How to Use

1. Select two or more objects
2. Click **Intersect** in the toolbar
3. Change your mind at any time by clicking a different icon in the **Operation** row at the top of the Properties panel -- the shape rebuilds with the new operation

## Parameters

- **Operation** - Which boolean to perform. Shown as an icon row at the top of the panel
- **Keep Inside Out Geometry** - Treat an inside-out shell as solid material instead of letting it cancel out the volume around it. Turn this on when a model that should be solid comes back with parts missing. It forces the slower, exact boolean engine
- **Repair Winding Order** - Rewind each part's inside-out shells before the boolean runs. This fixes the geometry once rather than changing what every later operation counts as solid, and is usually the better of the two answers to an inside-out model

## Tips

- The objects have to overlap. If they do not actually overlap, the result is empty
- With more than two objects it works down the list: the first two are intersected, then that result is intersected with the third, and so on
- If a result looks wrong, check that the source objects are watertight. **Repair Winding Order** fixes inside-out shells; [Repair](../mesh/repair.md) fixes broader damage in imported models

## Related

- [Combine](combine.md) - Merge multiple objects into a single solid shape
- [Subtract](subtract.md) - Cut one shape out of another
- [Subtract and Replace](subtract-and-replace.md) - Subtract one shape and keep the piece that was cut away
- [Plane Cut](../reshape/plane-cut.md) - Cut with a flat plane instead of another shape
- [Repair](../mesh/repair.md) - Fix damaged imported meshes before a boolean

This page also covers the older Intersection objects still found in designs saved before the operations were merged. They keep working exactly as they did; new designs use the shared Boolean object with the Intersect operation selected.
