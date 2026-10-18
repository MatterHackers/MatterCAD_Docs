---
title: Fit to Bounds
articleKey: FitToBoundsObject3D_4
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 3
---
# Fit to Bounds

Fit to Bounds scales an object to fit within specified width, depth, and height dimensions. You can control how the object stretches and aligns within the target bounds.

<!--  Screenshot showing an object being fit to specific bounding dimensions -->
![20260506 154930 paste 20260506 154930](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154930-paste-20260506-154930.jpg)

## How to Use

1. Select an object
2. Click **Fit to Bounds** in the Placement group of the toolbar
3. Enter the target **Width**, **Depth** and **Height**
4. Choose the proportion locking and how each axis stretches

## Parameters

- **Lock Proportion** - Which axes keep their proportions:
  - **None** (default) - Each axis fits on its own
  - **X Y** - Width and Depth scale together
  - **X Y Z** - All three scale together, keeping the part's shape
- **Width** - Target width (X), in mm
- **Depth** - Target depth (Y), in mm
- **Height** - Target height (Z), in mm. Not shown for a 2D path, which has no height

Each **Stretch** row chooses how the part fits:

- **Inside** - Shrink if needed to fit, but never grow
- **Expand** (default) - Grow (or shrink) to fill the bounds

The rows that show depend on Lock Proportion:

- **Group** section (X Y or X Y Z) - One **Stretch** for the locked axes
- **X Axis** and **Y Axis** sections (None) - A **Stretch** for each axis
- **Z Axis** section (None or X Y) - A **Stretch** for the height. For a 2D path the Z Axis Stretch and Align rows are hidden, since a path has no height

Whenever an axis's Stretch is **Inside**, an **Align** row appears for it: **Min**, **Center** (default) or **Max**, where the part sits within the bounds on that axis, since it may not fill them.

## Tips

- Use this to resize imported models to exact target dimensions
- Lock all proportions for uniform scaling that maintains the original shape
- Use per-axis control when you need to fit a specific width but don't care about the other dimensions

## Related

- [Scale](../transform/scale.md) - Scale by ratio or percentage instead of target size
- [Fit to Cylinder](fit-to-cylinder.md) - Fit within a cylindrical boundary
- [Align](align.md) - Position objects relative to each other
