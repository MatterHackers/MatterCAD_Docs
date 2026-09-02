---
title: Sweep
articleKey: SweepObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 9
---
# Sweep

Sweep carries a flat profile along a curve through space. The profile is a 2D path -- a circle, a star, an SVG outline -- and the curve is a [3D Curve](curve-3d.md), called the rail. The result is a solid tube with your profile as its cross section, following wherever the rail goes.

<!-- IMAGE_NEEDED: Screenshot of a Sweep selected in the 3D view, showing a circle profile swept along an S shaped rail, with the rail's control point spheres visible -->

Where [Linear Extrude](linear-extrude.md) pushes a profile straight up and [Revolve](revolve.md) spins it around an axis, Sweep lets you draw the route yourself. It is the tool for handles, tubing, pipes, wire runs and trim that follows a path.

## How to Use

1. Select a 2D path
2. Click **Sweep** in the Path group of the toolbar
3. A rail is created for you -- an S curve about twice as long as the profile is wide, starting at the profile
4. Select the **3D Curve** in the design tree and drag its control points to shape the route
5. Adjust **Rail Segments** if the result looks faceted

The operation is only enabled when the selected item is a path. The Path group is hidden on the toolbar by default -- see [Path Operations](index.md) for how to turn it on, or use the right-click **Modify** menu instead.

You can also build one the other way round: select a path *and* a 3D Curve together and choose **Loft**. A curve in the selection means you want the profile carried along it, so MatterCAD makes a Sweep instead of a loft, with the curve as the rail and everything else as the profile.

## The Children

A Sweep holds two kinds of child, and it tells them apart by type rather than by order:

- **The profile** - every path child. Several path children combine into a single cross section
- **The rail** - the [3D Curve](curve-3d.md) child. There is one, and it is not treated as part of the profile

Delete the rail and the sweep has nothing to follow, so it builds no geometry until you add one back. Hide or replace the profile and the cross section changes with it.

The cross section is centred on the profile's own bounds before the sweep runs, and the default rail starts at that same centre -- so a circle you drew off to one side still rides *on* the rail rather than orbiting it at a distance.

A Sweep with no colour of its own takes the profile's colour, so sweeping a red path gives you a red solid. The rail's colour is ignored; it is editor geometry, not part of the model.

## Parameters

- **Rail Segments** - How many straight steps each span of the rail is broken into (default 20, range 2-100). More segments make a smoother tube and a heavier mesh
- **Cap Ends** - Close the two ends of the sweep (default on). Hidden when the rail is closed, because a closed rail has no ends to cap
- **Scale** - A small graph that sets the size of the profile as the sweep advances. Up the graph is position along the rail in percent (0 at the start, 100 at the end); across it is the size in percent, so 100 leaves the profile exactly as drawn. Draw it sloping down and the tube tapers
- **Twist** - The same kind of graph for rotation of the profile about the rail, in degrees. Positive twists one way, negative the other. Hidden when the rail is closed: a closed rail has no start and end for the twist to run between, and forcing the whole difference onto the closing segment folds the surface through itself

Both graphs start flat -- 100 percent scale and 0 twist the whole way -- which is the same as not using them at all.

When a Sweep is selected, a control sphere sits on the solid for every point of the Scale graph, and of the Twist graph when the rail is open, so you can shape those functions against the shape they are shaping.

## Tips

- Shape the rail first, then the profile. The rail decides where the part goes; the profile only decides what its section looks like
- Keep **Rail Segments** low while you are shaping the rail and raise it when you are done. Every segment is mesh
- A closed rail makes a closed loop -- a ring, a gasket, a torus with your own cross section -- and neither Cap Ends nor Twist applies to it
- On a closed rail, a Scale graph that does not come back to where it started leaves a visible step at the seam. That is honest, not a bug: the two ends of the graph meet there
- To sweep several separate profiles as one shape, group them first, or add them all as children of the Sweep

## Related

- [3D Curve](curve-3d.md) - The rail a Sweep follows, and how to edit it
- [Loft](loft.md) - Blend between stacked sections instead of carrying one along a curve
- [Linear Extrude](linear-extrude.md) - Push a profile straight up
- [Revolve](revolve.md) - Spin a profile around an axis
- [2D Paths](../../2d-paths/index.md) - The path shapes you can use as a profile
