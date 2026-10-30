---
title: Linear Extrude
articleKey: LinearExtrudeObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 3
description: Give a flat 2D shape height to turn it into a solid, with an optional bevel on its edge.
keywords: extrusion, pull up, add height, 2d to 3d, raise, make solid
---
# Linear Extrude

Linear Extrude gives a 2D path height, turning a flat shape into a 3D solid. This is the primary way to convert paths into 3D objects.

<!-- AUTO_IMAGE: type=shot id=linear-extrude -->
![Linear Extrude: a flat star path at the left, and at the right the same star extruded into a solid, with its Height, Direction and Bevel Top settings](https://matterhackers.github.io/MatterCAD_Docs/assets/linear-extrude.png)


## How to Use

1. Select a 2D path or path-based object
2. Click **Linear Extrude** in the Path group of the toolbar
3. Set the desired height

## Parameters

- **Height** - How tall the extrusion is, in mm (default 5; the slider runs 0.1 to 50)
- **Direction** - Which side of the sketch the solid grows to. **Up** (the default) stands it on the sketch, **Center** puts half the height above the sketch and half below, and **Down** hangs it below the sketch. Bevel Top always rounds the top face and Bevel Bottom the bottom face, whichever way it grows. The height handle sits on the top face (with **Down**, on the bottom face): drag it away from the part to make it taller
- **Bevel Top** - Off by default. Rounds the top edge of the extrusion
- **Bevel Bottom** - Off by default. Rounds the bottom edge. It has its own size, so a part can have a large round at the bottom and a small one on top

### Bevel Parameters

Shown when **Bevel Top** is on:

- **Style** - How the corners of the shape are drawn as the edge rounds in: **Flat**, **Round** or **Sharp** (default)
- **Radius** - How far the round reaches, in mm (default 3; the slider runs 0 to 20)
- **Segments** - How many steps make the round (default 9; 1 to 20). More is smoother

Shown when **Bevel Bottom** is on: **Bottom Style**, **Bottom Radius** and **Bottom Segments**, the same settings for the bottom edge (defaults Sharp, 3 and 9).


## Projection Plane

Every path operation carries a **Projection Plane** section that says which flat surface its input paths are flattened onto -- by default the plane the first input was drawn on. Leave it on **Auto** unless the panel warns that your paths are not coplanar. See [Construction Planes](../../workspace/construction-planes.md).

## Tips

- This works with any 2D path: [Circle](../../2d-paths/circle-path.md), [Box](../../2d-paths/box-path.md), [Star](../../2d-paths/star-path.md), [SVG](../../primitives/svg-object.md), and [Custom](../../2d-paths/custom-path.md) paths
- Enable Bevel Top for a more polished, professional look
- Use **Down** to cut a pocket into a part: draw the shape on the part's top face, extrude it Down and subtract it
- For revolving a path around an axis instead of extruding straight up, see [Revolve](revolve.md)
- For a profile that follows a route through space, see [Sweep](sweep.md); for one that changes shape as it rises, see [Loft](loft.md)

## Related

- [Revolve](revolve.md) - Spin a path around an axis
- [Sweep](sweep.md) - Carry a path along a 3D curve
- [Loft](loft.md) - Blend between two or more stacked paths
- [2D Paths](../../2d-paths/index.md) - Available path shapes
- [Text](../../primitives/text.md) - Text is automatically extruded
