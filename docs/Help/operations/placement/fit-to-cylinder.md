---
title: Fit to Cylinder
articleKey: FitToCylinderObject3D
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 4
description: Change the settings of a Fit to Cylinder you find in an older design, which scales a part to a round size.
keywords: fit into cylinder, round boundary, diameter fit, older designs
---
# Fit to Cylinder

Fit to Cylinder scales an object to fit within a specified cylindrical boundary defined by a diameter and height.

There is no toolbar button or menu entry for Fit to Cylinder. You meet it in designs that already contain one, where you can select it and change its settings like any other operation. To fit a part into a size, use [Fit to Bounds](fit-to-bounds.md).

## How to Use

1. Select the Fit to Cylinder in the Design tree
2. Set the target Diameter and Height in the Properties panel

## Parameters

- **Alternate Centering** - Off by default. Normally the part is expanded to fill the cylinder; turn this on to center the part's weight in the cylinder instead
- **Diameter** - The diameter of the target cylinder, in mm
- **Height** - The height of the target cylinder, in mm
- **Stretch Z** - On by default. Scales the part to the cylinder's height too; turn it off to leave the height alone

## Related

- [Fit to Bounds](fit-to-bounds.md) - Fit within a rectangular bounding box instead
- [Align](align.md) - Position objects relative to each other
