---
title: Translate
articleKey: TranslateObject3D
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 4
description: Move a part by an exact distance along X, Y and Z.
keywords: move by distance, exact position, shift, move exactly
---
# Translate

Translate moves an object by a specific distance along the X, Y, and/or Z axes. Unlike dragging an object with the mouse, Translate lets you enter exact offset values.

<!--  Screenshot showing the Translate operation properties with X, Y, Z offset fields -->
<!-- AUTO_IMAGE: type=shot id=translate -->
![A text moved off the world origin by Translate, a grey copy left where it started at the crossing of the bed's X and Y axes, beside its Properties panel: the X, Y and Z of the move](https://matterhackers.github.io/MatterCAD_Docs/assets/translate.png)


## How to Use

1. Select an object
2. Click **Translate** in the Transform group of the toolbar
3. Enter the desired offset values for X, Y, and Z in the Properties panel

## Parameters

- **X, Y, Z** (Translation) - The distance to move the object along each axis, in millimeters. Supports [expressions](../../workspace/expressions.md) for calculated values.

## Tips

- Use Translate when you need precise, repeatable positioning that you can adjust later
- The translation values are relative to the object's current position -- entering 10 for X moves it 10mm to the right from where it is
- For quick repositioning, you can also drag objects directly in the viewport. See [Editing Objects](../../getting-started/editing-objects.md)

## Related

- [Rotate](rotate.md) - Rotate an object by a specific angle
- [Scale](scale.md) - Resize an object precisely
- [Align](../placement/align.md) - Position objects relative to each other
