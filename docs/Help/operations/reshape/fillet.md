---
title: Fillet
articleKey: FilletObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 8
---
# Fillet

Fillet rounds the edges you pick. On a solid it rolls a ball of the radius you give along each selected edge and leaves the surface that ball sweeps out. On a 2D path it rounds the corners instead.

<!-- AUTO_IMAGE: type=from_mcx file=reshape_fillet -->
![reshape_fillet](https://matterhackers.github.io/MatterCAD_Docs/assets/reshape_fillet.png)

Fillet and [Chamfer](chamfer.md) are the same tool with two different profiles -- Fillet leaves an arc, Chamfer leaves a flat cut -- so everything on this page about picking edges and the messages the panel shows is true of both. If you want every outside edge of a part rounded at one radius and do not want to pick anything, use [Round All Edges](round-all-edges.md) instead.

## How to Use

1. Select a part, or a 2D path
2. Click **Fillet** in the Reshape group of the toolbar
3. Click an edge (or, on a path, a corner) in the 3D view to add it
4. Set **Radius** in the Properties panel

Nothing is rounded until you pick something. A fresh Fillet on a solid is the part unchanged, waiting for a click.

**One Fillet, one radius.** Every edge a Fillet selects is rounded at the same radius, the way every mainstream CAD package models the feature. If part of your shape needs a different radius, apply a second Fillet on top of the first and pick those edges there.

## Picking Edges on a Solid

Move the mouse over the part with the Fillet selected and the edge under the cursor lights up in white. Click it to add it. Click an edge that is already selected and it is removed again.

**Shift-click cycles what the click means.** The same click can honestly mean several different things, and MatterCAD offers all of them rather than guessing:

- **the edge on its own** -- just what you clicked
- **the loop it belongs to** -- the run of edges that continues smoothly from it, the way most CAD packages extend a picked edge
- **that loop read more coarsely** -- the same walk with the surface treated as smoother, so it does not stop at the facets of a curved wall. There are two steadily coarser readings of it, though on a shape where they come to the same edges you will only be offered one

Shift-click steps to the next reading and shows it without committing anything. When the one you want is lit, click normally to keep it. This matters most on rounded shapes: the rim of a tessellated cylinder is a single flat facet at the tightest reading and the whole circle at the loosest.

<!-- IMAGE_NEEDED: Screenshot of the 3D view with a Fillet selected, showing an edge highlighted in white under the cursor and two already-picked groups drawn in their own accent colors -->

Each selection you commit becomes a row in the **Edges** list, labelled with what it is and how many edges it came to -- "1. Edge, 1 edge", "2. Chain, 64 edges", "3. Face Group, 4 edges". The list is what you have selected, not how big the round is; every row carries:

- a colour swatch showing the colour that group's edges are drawn in
- a button that lights the group up in the 3D view, so you can tell which row means which edges
- a remove button, which stops beveling those edges

You can also drag the size handle that sits on each selected run in the 3D view to set the radius by eye. There is one number, so every handle moves together and any of them will do. Press **Esc** during the drag to cancel it.

## Picking Corners on a 2D Path

When the thing you filleted is a 2D path, the panel shows **Corners** and **Corner Threshold** instead of **Edges**, and a small ball appears at every corner of the path. Click a ball to round that corner; click it again to leave it sharp.

There is no shift-click here -- a corner is a corner, where an edge could also have meant its loop.

**With no corners selected, every corner is rounded.** That is the default a new Fillet on a path starts in, and it is what designs saved before corner picking existed still ask for. Pick a corner and you have narrowed it to just the corners you pick.

<!-- AUTO_IMAGE: type=from_mcx file=reshape_fillet_2d -->
![reshape_fillet_2d](https://matterhackers.github.io/MatterCAD_Docs/assets/reshape_fillet_2d.png)

*The original star path on the left, the same path with a 1.5 mm Fillet on every corner on the right.*

## Parameters

- **Radius** - The radius every edge and corner this Fillet selects is rounded at. It is the radius of the largest ball that would roll along the edge. One Fillet has one radius; for a second radius, apply a second Fillet
- **Segments** - How many straight steps each arc is drawn with. More segments make a smoother curve and a heavier mesh. 8 is plenty for most parts
- **Edges** - The list of selections on a solid (see above)
- **Corners** - The same list for a 2D path. Empty means every corner
- **Corner Threshold** - 2D only. How far a corner has to bend from straight before it counts as a corner at all. Vertices straighter than this are left alone, which keeps a curve made of many short segments from being "rounded" segment by segment

## When It Refuses

A fillet either fits or it does not, and MatterCAD will not quietly shrink one to make it fit -- a radius you typed is a dimension, and silently changing it would make the part lie about itself. So a selection that does not fit is skipped, with a warning triangle on its row and a sentence saying why.

The most useful ones tell you the largest size that *would* have fitted:

> A size of 5 reaches further across the face at (10, 0, 20) than the face is wide. The most that fits there is about 3.2.

> A size of 4 runs into the bevel coming the other way across the face at (0, 12, 5), so the two of them do not both fit. The most that fits there is about 1.9.

Read those as "type this number or less". The point named in the message is where the problem is, so you can find it on the part.

Others describe a shape the round cannot be swept along at all:

- *"The two faces along this edge lie in the same plane, so there is no corner to bevel."* -- the edge is a triangulation seam across a flat area, not a real edge
- *"The faces along this edge meet at N degrees, which is too sharp/flat to bevel."* -- a knife edge or a nearly flat join
- *"The group resolved to no edges at all."* -- the shape changed under the Fillet and the edge that was picked is no longer there. Pick it again
- *"The cut removed the whole part, so nothing was left to keep."* -- shown above the list rather than on a row, because it is about the operation and not any one group. The sizes are far too big for the part
- *"This tangent chain never grew past the edge that was picked..."* -- you picked a loop on a curved surface at the tightest reading, so the walk stopped at the first facet. Pick the edge again and shift-click to a coarser reading, as the message says

The panel also shows **advisories** above the list, in a different colour and with a different glyph. Nothing failed; they tell you about a repair that was made to your source so the fillet could run:

> This source mesh is inside out - every one of its faces points into the solid rather than out of it. It has been turned right way out to bevel it; the source itself is unchanged.

Only the working copy is changed, never your model. If you would rather fix it once and for all, use [Repair](../mesh/repair.md) on the source.

One repair is made silently. A mesh made of loose, unwelded triangles -- which many STL files are -- has no shared edges at all, so the first look for edges finds none; when that happens the working copy is welded and the look is repeated. Putting back topology the file never carried does not change what the part is, which is why it needs no advisory. If a part still shows no edges to pick after that, there really are none to find.

## Tips

- Fillet last. Round the edges of a shape after you have finished cutting and combining it, so you do not have to re-pick edges every time the shape changes
- Selections survive a rebuild. They are stored as geometry, not as edge numbers, so changing the size of the box under a Fillet keeps the same edges rounded
- If a whole rim should be rounded, click one edge of it and shift-click once -- that is nearly always faster and more robust than picking edges one at a time
- Keep segments low while you work and raise them at the end. Every segment is mesh
- Two radii on one part are two Fillets. Round the edges that share a radius, then apply another Fillet for the rest -- the same way you would in any other CAD package
- Concave edges get a bead of material added into the corner rather than material cut away, which is what a fillet means on the inside of a shape
- If every edge of the part should be rounded at one radius, [Round All Edges](round-all-edges.md) needs no picking at all

## Related

- [Chamfer](chamfer.md) - The same tool with a flat cut instead of a round
- [Round All Edges](round-all-edges.md) - Round every outside edge at one radius, with nothing to pick
- [Repair](../mesh/repair.md) - Fix an imported mesh before beveling it
- [Smooth Path](../path/smooth-path.md) - Smooth a 2D path as a whole rather than rounding chosen corners
- [Linear Extrude](../path/linear-extrude.md) - Give a filleted 2D path some height
