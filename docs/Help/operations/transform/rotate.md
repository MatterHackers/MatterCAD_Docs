---
title: Rotate
articleKey: RotateObject3D_3, RotateObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 2
---
# Rotate

Rotate turns an object around an axis by a given angle. The axis is a [construction plane](../../workspace/construction-planes.md): the plane's normal is what the object turns around, and the plane's origin is the point it turns about.

<!--  Screenshot showing the Rotate operation with the rotation gizmo visible in the viewport -->
![20260506 160726 paste 20260506 160726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160726-paste-20260506-160726.jpg)

## How to Use

1. Select an object
2. Apply the **Rotate** operation from the Transform menu
3. Set the rotation angle in the Properties panel
4. Choose the axis under **Rotate About** — a preset, typed values, or a face picked off a model

You can also rotate objects directly in the viewport by clicking the rotate corner controls on a selected object. Moving your mouse over the angle indicators snaps to 45-degree increments.

## Parameters

- **Angle** - The rotation angle in degrees (range: 3-360). Supports [expressions](../../workspace/expressions.md).
- **Rotate About** - The construction plane whose normal is the axis of rotation and whose origin is the centre of rotation.

### Rotate About

The plane is shown in the viewport while the Rotate is selected, so you can see the axis you are turning around.

- **Preset** - **XY** turns about +Z, **XZ** about -Y, **YZ** about +X. The **Flipped** presets reverse each of those, so the same positive angle turns the other way. Choosing a preset also resets the Origin to the object's own zero, so re-enter your pivot point afterwards if you had moved it.
- **Origin** - The point the object pivots about. It starts at the centre of the object's bounding box.
- **Normal** - The axis itself. Type any direction; it does not need to be unit length.
- **X Direction** - Not used by Rotate. An axis has no need of a sideways direction, so leave it alone.
- **Pick Face** - Click the button, then click a flat face anywhere in the scene to turn about that face's normal. Press Esc to cancel.

Each of Origin and Normal takes [expressions](../../workspace/expressions.md) per component, so the axis can be driven by the rest of the design.

## Older files

A Rotate created before construction planes shipped keeps its original **Rotate About** control — a Direction Axis with an axis dropdown — and keeps working exactly as it did. New Rotate operations get the construction plane described above. To move an old one over, delete it and apply Rotate again.

## Tips

- The rotation is centered on the object's bounding box center by default
- For 90-degree rotations, the snap indicators make it easy to get exact values
- Use the Rotate operation (rather than viewport controls) when you need a precise angle that isn't a multiple of 45 degrees
- You can change the rotation axis after applying the operation by editing the Rotate About property
- To turn about a slanted feature of your model, use Pick Face rather than working the direction out by hand

## Related

- [Construction Planes](../../workspace/construction-planes.md) - Presets, expressions, and Pick Face in full
- [Translate](translate.md) - Move an object by a specific distance
- [Scale](scale.md) - Resize an object
- [Mirror](mirror.md) - Create a mirrored reflection
