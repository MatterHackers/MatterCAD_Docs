---
title: Boolean
articleKey: BooleanObject3D
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 1
---
# Boolean

Boolean builds a new shape out of the shapes you already have. One Boolean object performs all four operations -- Combine, Subtract, Intersect and Subtract & Replace -- and you switch between them with the icon row at the top of the Properties panel. The four toolbar buttons are shortcuts: each creates a Boolean with that operation already chosen.

Boolean works on solids and on 2D paths. It looks at what you gave it and does the right kind of operation, so combining two paths produces one path and combining two meshes produces one solid.

|Combine|Subtract|Intersect|Subtract & Replace|
| :--- | :--- | :--- | :--- |
|<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)|<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)|<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)|<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)|

## How to Use

1. Select two or more objects
2. Click **Combine**, **Subtract**, **Intersect** or **Subtract & Replace** in the toolbar
3. Change your mind at any time by clicking a different icon in the **Operation** row at the top of the Properties panel -- the shape rebuilds with the new operation

## The Operations

### Combine

Merges everything into a single solid. Internal faces where the shapes overlapped are removed, so the result is one continuous mesh rather than overlapping shells.

Combine handles Hole objects for you: anything marked as a hole is subtracted from the result rather than added to it.

### Subtract

Cuts the parts you choose out of the parts you did not. Use **Part(s) to Subtract** to pick the cutting shapes; everything else is the base that gets cut.

The cutting objects stay in the design tree, so you can move or resize them and the cut updates.

### Intersect

Keeps only the volume every object shares and discards the rest. With more than two objects it works down the list: the first two are intersected, then that result is intersected with the third, and so on.

If the objects do not actually overlap, the result is empty.

### Subtract & Replace

Subtracts as above, but keeps the piece that was cut away as its own part instead of discarding it. The two parts fit together exactly, because they came out of the same operation.

Use it for multi-color designs, interlocking assemblies, and inlays. Subtract & Replace is not offered for 2D paths -- a region has no removed volume to hand back.

## Parameters

- **Operation** - Which boolean to perform. Shown as an icon row at the top of the panel
- **Part(s) to Subtract** - Which children are the cutting shapes. Shown for Subtract and Subtract & Replace
- **Keep Subtracted Parts** - Leave the parts that were cut away in the scene rather than discarding them. Shown for Subtract
- **Keep Inside Out Geometry** - Treat an inside-out shell as solid material instead of letting it cancel out the volume around it. Turn this on when a model that should be solid comes back with parts missing. It forces the slower, exact boolean engine
- **Repair Winding Order** - Rewind each part's inside-out shells before the boolean runs. This fixes the geometry once rather than changing what every later operation counts as solid, and is usually the better of the two answers to an inside-out model

## Tips

- Objects have to overlap for Subtract and Intersect to do anything. Combine will still join non-overlapping objects into one mesh, but they stay visually separate
- To cut a through-hole, make sure the cutting object passes completely through the base
- For a simple hole, the [Hole](../../primitives/hole.md) primitive is already set up to subtract
- Boolean carries per-face colors through from the original objects
- If a result looks wrong, check that the source objects are watertight. **Repair Winding Order** fixes inside-out shells; [Repair](../mesh/repair.md) fixes broader damage in imported models

## Related

- [Plane Cut](../reshape/plane-cut.md) - Cut with a flat plane instead of another shape
- [Hole](../../primitives/hole.md) - A cube pre-configured to subtract
- [Repair](../mesh/repair.md) - Fix damaged imported meshes before a boolean
