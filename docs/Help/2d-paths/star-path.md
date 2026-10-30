---
title: Star Path
articleKey: StarPathObject3D
parent: "2D Paths"
nav_order: 5
description: Draw a flat star with as many points as you like and extrude it into a 3D star.
keywords: star shape, 2d star, starburst, pointed shape
---
# Star Path

A star-shaped 2D path, added as **Star** from the 2D Primitives. You choose how many points it has and how far its points and valleys are from the center. Use with [Linear Extrude](../operations/path/linear-extrude.md) to create 3D star shapes.

<!-- AUTO_IMAGE: type=shot id=2d-star -->
![A flat Star path selected on the bed, its point and valley circles showing, beside its Properties panel: Plane, Points, Point Radius and Valley Radius](https://matterhackers.github.io/MatterCAD_Docs/assets/2d-star.png)


## Parameters

- **Plane** - The [construction plane](../workspace/construction-planes.md) the star is drawn on (default XY, flat on the bed)
- **Points** - How many points the star has (default 5; 3 to 20)
- **Point Radius** - The distance from the center to the tip of each point, in mm (default 40)
- **Valley Radius** - The distance from the center to the valleys between the points, in mm (default 15)

## Tips

- The Valley Radius compared with the Point Radius sets how pointy the star is: a small Valley Radius makes long, sharp points
- For a six-pointed star like the Star of David, set Points to 6 and the Valley Radius to about 0.58 times the Point Radius (23 with the default Point Radius of 40)
- Use [Fillet](../operations/reshape/fillet.md) on a star to round its tips and valleys

## Related

- [Circle Path](circle-path.md) - A smooth circle
- [Involute Gear](../mechanical/gears.md) - A proper gear profile, with **Output** set to **2D**
- [Linear Extrude](../operations/path/linear-extrude.md) - Give paths height
