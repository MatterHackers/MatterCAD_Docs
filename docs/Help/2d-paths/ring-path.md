---
title: Ring Path
articleKey: RingPathObject3D
parent: "2D Paths"
nav_order: 4
---
# Ring Path

A 2D ring shape -- a circle with a circular hole in the center -- added as **Ring** from the 2D Primitives. Use with [Linear Extrude](../operations/path/linear-extrude.md) to create tube or washer shapes.

<!-- Screenshot of a Ring Path on the workspace -->
![20260506 080211 paste 20260506 080211](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080211-paste-20260506-080211.jpg)

## Parameters

- **Plane** - The [construction plane](../workspace/construction-planes.md) the ring is drawn on (default XY, flat on the bed)
- **Outer Diameter** - The outer diameter of the ring, in mm (default 20)
- **Inner Diameter** - The diameter of the hole in the center, in mm (default 15)
- **Sides** - How many straight segments make each circle (default 40; 3 to 360)
- **Advanced** - Off by default. Turn it on for Starting Angle and Ending Angle
- **Starting Angle** - Where the ring begins around its center, in degrees (default 0). Shown only with Advanced on
- **Ending Angle** - Where the ring ends, in degrees (default 360). Less than 360 leaves a gap, like a C shape. Shown only with Advanced on

## Tips

- The wall thickness of the ring is (Outer Diameter - Inner Diameter) / 2
- Extruding a Ring Path creates a tube like the [Tube](../primitives/ring.md) primitive

## Related

- [Circle Path](circle-path.md) - A solid circle (no hole)
- [Tube](../primitives/ring.md) - A ready-made 3D tube shape
- [Linear Extrude](../operations/path/linear-extrude.md) - Give paths height
