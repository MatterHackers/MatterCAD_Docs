---
title: Circle Path
articleKey: CirclePathObject3D
parent: "2D Paths"
nav_order: 2
---
# Circle Path

A circular 2D path, added as **Circle** from the 2D Primitives. Use with [Linear Extrude](../operations/path/linear-extrude.md) to create cylinders, or [Revolve](../operations/path/revolve.md) to create torus-like shapes.

<!-- Screenshot of a Circle Path on the workspace -->
![20260506 080110 paste 20260506 080110](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080110-paste-20260506-080110.jpg)


## Parameters

- **Plane** - The [construction plane](../workspace/construction-planes.md) the circle is drawn on (default XY, flat on the bed)
- **Diameter** - The width from one side to the opposite side, in mm (default 20)
- **Sides** - How many straight segments make the circle (default 40; 3 to 360). More is smoother; 3 makes a triangle, 6 a hexagon

## Tips

- A Circle Path combined with Linear Extrude produces a cylinder, similar to the [Cylinder](../primitives/cylinder.md) primitive but with more flexibility in how you build up from it
- Move it away from the axis and use [Revolve](../operations/path/revolve.md) to make a ring shape

## Related

- [Box Path](box-path.md) - A rectangular 2D path
- [Ring Path](ring-path.md) - A circle with a hole
- [Linear Extrude](../operations/path/linear-extrude.md) - Give paths height
