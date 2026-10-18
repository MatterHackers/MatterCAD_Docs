---
title: Dual Extrusion Align
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 2
---
# Dual Extrusion Align

![20260506 160531 paste 20260506 160531](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160531-paste-20260506-160531.jpg)


Dual Extrusion Align puts two or more selected parts back where they sit relative to each other in the files they came from. Every part is set to the same position: the first part stays where it is, and each other part ends up the same distance from its own file position as the first, so parts that were modeled together line up again. It also clears each part's rotation and scale.

<!--  Screenshot showing two parts before and after Dual Extrusion Align -->
|![20260506 160417 paste 20260506 160417](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160417-paste-20260506-160417.jpg)
|![20260506 160501 paste 20260506 160501](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160501-paste-20260506-160501.jpg)
|

## How to Use

1. Select two or more objects
2. Apply **Dual Extrusion Align** from the Placement group on the toolbar

## When to Use

Use this operation when parts that were made to fit together, such as the pieces of a multi-part model exported in shared coordinates, have been moved apart. Because it clears rotation and scale, apply it before you rotate or scale the parts. It is a single undo step.

## Related

- [Align](align.md) - Position objects relative to each other along any axis
- [Fit to Bounds](fit-to-bounds.md) - Scale an object to fit within a rectangular boundary
