---
title: Scale
articleKey: ScaleObject3D_3
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 3
---
# Scale

Scale resizes an object with precise control over dimensions, proportions, and unit conversion. You can scale uniformly, lock specific axes together, or resize each axis independently.

<!--  Screenshot showing the Scale operation properties with dimension fields and lock proportion options -->
![20260506 160759 paste 20260506 160759](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160759-paste-20260506-160759.jpg)

## How to Use

1. Select an object
2. Click **Scale** in the Transform group of the toolbar
3. Choose a **Scale Type**, then enter the sizes or percentages you want

You can also scale objects in the viewport by clicking and dragging the scale corner controls on a selected object.

## Parameters

### Scale Type

Choose your own size, or one of four unit conversions:

- **Custom** (default) - Enter your own sizes or percentages. Choosing Custom again puts the part back to its original size, ready for new values
- **Inches to mm** - Makes the part 25.4 times bigger: for a model drawn in inches that came in too small
- **mm to Inches** - Divides the size by 25.4
- **mm to cm** - Makes the part a tenth the size
- **cm to mm** - Makes the part 10 times bigger

With a conversion chosen, the panel shows the resulting **Width Percent**, **Depth Percent** and **Height Percent** as read-only values, and the rows below are hidden.

### Scale Method (Custom only)

- **Direct** (default) - Enter the Width, Depth and Height you want, in mm
- **Percentage** - Enter **Width Percent**, **Depth Percent** and **Height Percent** of the original size

### Lock Proportion (Custom only)

- **None** - Scale freely: each axis changes on its own
- **X Y** - Width and Depth stay locked together; Height changes on its own
- **X Y Z** (default) - Width, Depth and Height all change together, keeping the part's proportions

### Dimensions

- **Width** - Size along the X axis
- **Depth** - Size along the Y axis
- **Height** - Size along the Z axis

## Tips

- Use "Inches to mm" if you imported an STL file that was designed in inches and appears too small
- With Lock Proportion on **X Y Z**, changing any one dimension updates them all
- The object's base position is maintained during scaling so it stays on the workspace surface
- You can type exact values for precise sizing, or use the sliders for quick adjustments

## Related

- [Translate](translate.md) - Move an object
- [Rotate](rotate.md) - Rotate an object
- [Fit to Bounds](../placement/fit-to-bounds.md) - Scale to fit within a specific size
