---
title: Loft
articleKey: LoftObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 10
---
# Loft

Loft skins a solid between two or more flat sections stacked at different heights. Each section is a 2D path, and the surface runs smoothly from one to the next -- a square at the bottom blending into a circle at the top, a rectangular base tapering to a slot.

<!-- IMAGE_NEEDED: Screenshot of a Loft in the 3D view, showing a square section at the bed and a circle section above it with the skinned surface between them -->

Where [Linear Extrude](linear-extrude.md) gives one profile a constant height, Loft lets the profile change as it rises. Where [Sweep](sweep.md) carries one profile along a route you draw, Loft keeps the sections where you put them and fills the space between.

## How to Use

1. Select two or more 2D paths (Shift-click or Ctrl-click to multi-select)
2. Click **Loft** in the Path group of the toolbar
3. Move each section up or down to change where the blend happens
4. Edit any section's own path to change the shape at that height

The operation is enabled for anything that presents a path rather than a solid. The Path group is hidden on the toolbar by default -- see [Path Operations](index.md) for how to turn it on, or use the right-click **Modify** menu instead. An object that carries its own mesh -- an existing Linear Extrude, Revolve or Sweep, all of which keep their source path as a child -- is not offered as a section.

**Loft has no properties of its own.** You shape the result entirely by editing and moving the sections, which is why the Properties panel for a Loft is bare.

## How the Sections Are Chosen

- **Each selected item becomes one section.** A multi-select is unpacked, so two selected paths make two sections rather than being flattened into one
- **A child holding several paths becomes one section.** Group three circles and they contribute a single cross section at that group's height, not three stations
- **Sections stack by height, not by child order.** Each section's station is where its matrix puts its origin in Z, and they are sorted bottom to top before skinning. Two at the same height keep their child order
- **A hidden child contributes nothing.** Hiding a section is how you take it out of the loft without deleting it

### When Two Sections Share a Height

Two paths drawn on the bed are both at Z 0, and lofting between coplanar sections would make a solid with no height at all. So when a Loft is created, any section that lands on a station an earlier one already holds is lifted 20mm, and each further collision lifts it another 20mm. Several paths on the bed therefore spread into an evenly spaced stack you can then adjust.

Sections you have already stacked yourself are left exactly where they are.

### When You Only Select One Section

One section has nothing to skin between, so a copy of it is placed 20mm directly above, keeping the same X and Y. The first result is a straight prism you can then reshape by editing the top section.

### When a 3D Curve Is in the Selection

A [3D Curve](curve-3d.md) in the selection says you want the profiles carried *along* the curve, which is a [Sweep](sweep.md), not a loft. MatterCAD builds a Sweep for you instead, with the curve as the rail. Lofting would have silently dropped the curve -- it is not a path, so it is no section -- and handed back a straight prism with the curve dangling inside it.

Only a curve you actually selected counts. A curve buried inside a selected solid (an existing Sweep keeps its rail as a child) is that solid's own business.

## Tips

- Give each section a meaningful name in the design tree. On a loft with four or five sections, "Base", "Waist" and "Rim" beat "Circle", "Circle" and "Circle"
- Move a section in Z to change where the transition happens; move it in X and Y to lean the solid over
- More sections mean more control over the profile of the blend. Two sections give you a straight taper; three let you put a waist in it
- Sections do not have to have the same number of points or the same kind of path -- a star can blend into a circle
- A loft takes its colour from the first section when it has none of its own

## Related

- [Sweep](sweep.md) - Carry one profile along a 3D curve instead of blending between stacked ones
- [Linear Extrude](linear-extrude.md) - Give one profile a constant height
- [Revolve](revolve.md) - Spin a profile around an axis
- [3D Curve](curve-3d.md) - Selecting one alongside your paths turns a Loft into a Sweep
- [2D Paths](../../2d-paths/index.md) - The path shapes you can use as sections
