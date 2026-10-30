---
title: Align in Place
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 2
description: Put parts from separate files back where they fit together, as their files placed them.
keywords: assembly, fit together, original position, restore position, multi-part file, reassemble
---
# Align in Place

Align in Place puts two or more selected parts back where their own files placed them relative to each other, so parts that were made to fit together line up again. The first part you selected stays where it is; every other part moves so it sits relative to the first exactly as it did in the files they came from. It also clears each part's rotation and scale.

<!--  Two parts before and after Align in Place -->
|<!-- AUTO_IMAGE: type=shot id=align-in-place-before -->![The parts of one model, made as separate files that share coordinates, scattered on the bed](https://matterhackers.github.io/MatterCAD_Docs/assets/align-in-place-before.png)
|<!-- AUTO_IMAGE: type=shot id=align-in-place-after -->![The same parts after Align in Place: put back together where their files placed them](https://matterhackers.github.io/MatterCAD_Docs/assets/align-in-place-after.png)
|

## How to Use

1. Select two or more parts
2. Click **Align in Place** in the Placement group of the toolbar (also in the right-click **Modify** menu)

## When to Use

Use it when the pieces of one model, exported as separate files that share the same coordinates, have been moved apart: for example the pieces of a multi-part figure, or the parts of a model split for different colors. Because it clears rotation and scale, use it before you rotate or scale the parts. It is a single undo step.

## Related

- [Align](align.md) - Position objects relative to each other along any axis
- [Fit to Bounds](fit-to-bounds.md) - Scale an object to fit within a rectangular boundary
