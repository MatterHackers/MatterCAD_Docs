---
title: Measure Tool
articleKey: MeasureToolObject3D
parent: "Workspace"
nav_order: 7
---
# Measure Tool

The Measure Tool lets you measure distances between points in your design. Place measurement points anywhere in the 3D viewport to check dimensions.

<!--  Screenshot showing the Measure Tool with a distance measurement displayed between two points -->
![20260318 192711 paste 20260318 192711](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-192711-paste-20260318-192711.jpg)


## How to Use

1. Open the Tools group in the library and drag **Measure Tool** onto the bed
2. Drag the two spheres to the locations you want to measure between
3. The distance is drawn in the viewport, on the line between them

## Parameters

- **Distance** - The straight-line distance between the two points, shown read-only in the Properties panel. It is the same number the viewport draws
- **Reset** - A button that puts the two ends back to their starting positions and clears the reading

## Tips

- Use this to verify dimensions before exporting for 3D printing
- The Measure Tool measures the straight-line distance between the two spheres, whatever is in between
- Dragging a sphere is undoable, so you can step back to a previous measurement
- The Measure Tool does not print and is left out of exports, so you can leave it in your design

## Related

- [Description](description.md) - Place a Markdown note in the scene
- [Scale](../operations/transform/scale.md) - Resize objects to exact dimensions
- [Editing Objects](../getting-started/editing-objects.md) - View and edit object dimensions in the Properties panel
