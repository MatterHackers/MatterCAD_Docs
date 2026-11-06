---
title: Clone
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 0
description: Make a linked copy of a part that stays the same as the original, or cut a test-fit piece that follows every change.
keywords: linked copy, linked duplicate, instance, mirror changes, test fit, test piece, fit check, print a section
---
# Clone

Clone makes a linked copy of a part. The copy and the original stay the same: change a setting on either one, such as a width or a hole size, and the other changes to match. Each copy keeps its own place, so you can move and turn the copies freely. Use it for parts that repeat in a design, like the legs of a table, so one change updates every leg.

## How to Use

1. Select a single part
2. Click **Clone** in the Duplication group of the toolbar
3. The linked copy appears in the same spot as the original and is selected, so move it where you want it

Clone more of the same part to add more linked copies; every copy in the group follows the others. The Properties panel shows which copy is selected, as **Clone - 1 of 3**, and its **Unclone** button makes that copy an ordinary part again, no longer linked.

## Test-Fit Pieces

Printing a whole part just to check how one area fits, such as a snap, a hinge or a hole for a bolt, takes time and material. A test-fit piece is just that area, cut out of the part so you can print it on its own in a few minutes.

1. Select the part and click **Clone**. The linked copy sits exactly on top of the part.
2. Add a **Cube** and size and place it so it covers only the area you want to test.
3. Select the linked copy and the cube, and click **Intersect**. What is left is the piece of the part inside the cube.
4. Move the piece aside and print it.

Because the piece is cut from a linked copy, it follows every later change to the part. If the test shows the fit is too tight and you widen the hole on the part, the piece updates with it, so you can print it again right away without remaking it.

## Tips

- A copy made with **Duplicate** is not linked; use Clone when the copies should stay the same
- To make many copies in a row or a circle that change together, use [Array](array.md) instead

## Related

- [Array](array.md) - Make many copies of a part in a pattern
- [Intersect](../boolean/intersect.md) - Keep only where parts overlap
