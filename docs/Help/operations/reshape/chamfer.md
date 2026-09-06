---
title: Chamfer
articleKey: ChamferObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 9
---
# Chamfer

Chamfer cuts the edges you pick flat, leaving a 45 degree face where the edge was. On a 2D path it cuts the corners off instead.

<!-- AUTO_IMAGE: type=from_mcx file=reshape_chamfer -->
![reshape_chamfer](https://matterhackers.github.io/MatterCAD_Docs/assets/reshape_chamfer.png)

Chamfer and [Fillet](fillet.md) are the same tool with two different profiles -- Chamfer leaves a flat cut, Fillet leaves an arc. Picking edges, the one size a whole feature is cut at, and the messages the panel shows work identically in both, and are described in full on the [Fillet](fillet.md) page.

## How to Use

1. Select a part, or a 2D path
2. Click **Chamfer** in the Reshape group of the toolbar
3. Click an edge (or, on a path, a corner) in the 3D view to add it
4. Set **Distance** in the Properties panel

Nothing is cut until you pick something. A fresh Chamfer on a solid is the part unchanged, waiting for a click.

**One Chamfer, one distance.** Every edge a Chamfer selects is cut back by the same amount. If part of your shape needs a different distance, apply a second Chamfer on top of the first and pick those edges there.

## Picking Edges

Hover the part and the edge under the cursor lights up white; click to add it, click it again to remove it. **One click can mean several things** -- the edge alone, the loop it belongs to, or that loop read more coarsely so it does not stop at the facets of a curved wall. A small badge beside the hovered edge names the reading on offer -- "1 edge", "40 edges, chain" -- with an arrow each side for the reading next door. The arrows only show you a reading; a normal click commits it.

Every committed selection becomes a row in the **Edges** list with its own accent colour, a button that lights it up in the 3D view, a remove button, and a reading dropdown offering that pick's other readings. Choosing one of them replaces that group in its own slot rather than adding a second, and can be undone. There is no segment count anywhere on a Chamfer: a flat cut is one straight step across, and a second step would only put a point on a line.

<!-- IMAGE_NEEDED: Screenshot of the Properties panel for a Chamfer with three groups in the Edges list, showing the colour swatches, highlight buttons and remove buttons -->

On a 2D path the panel shows **Corners** and **Corner Threshold** instead. Small balls appear at each corner; click one to cut it, click it again to leave it sharp. With no corners selected every corner is cut, which is what a new Chamfer on a path starts out doing.

## Parameters

- **Distance** - How far back from the edge the cut starts, measured along *each* of the two faces the edge joins. Every edge this Chamfer selects is cut back by it; for a second distance, apply a second Chamfer
- **Edges** - The list of selections on a solid
- **Corners** - The same list for a 2D path. Empty means every corner
- **Corner Threshold** - 2D only. How far a corner has to bend from straight before it counts as a corner at all

On a 2D path the distance is the setback along each edge from the corner, not a radius. That is deliberate: one radius applied to corners of different angles would set each of them back by a different amount, which is not what the number you typed into Distance means.

## When It Refuses

A chamfer that does not fit is skipped with a warning triangle on its row and a sentence saying why -- MatterCAD never quietly shrinks a size you typed. The messages that can are worded to tell you what would have fitted:

> A size of 5 reaches further across the face at (10, 0, 20) than the face is wide. The most that fits there is about 3.2.

Type that number or less. Everything on the [Fillet](fillet.md) page under "When It Refuses" -- the other refusals, the inside-out advisory and the silent weld of unwelded imports -- applies to Chamfer word for word.

## Tips

- A chamfer is the cheaper edge break: it adds two triangles per edge where a fillet adds a whole arc's worth
- On a part you plan to 3D print, a chamfer on the bottom edge is often easier to print cleanly than a fillet of the same size
- Distance is measured along the faces, not across the cut. A 2 mm chamfer takes 2 mm off each face and leaves a cut face about 2.8 mm wide
- Chamfer and Fillet can be stacked: chamfer one set of edges, then fillet the result's new edges
- If every outside edge should be broken at one size and you do not care whether it is round, [Round All Edges](round-all-edges.md) needs no picking

## Related

- [Fillet](fillet.md) - The same tool with a round instead of a flat cut, and the full description of edge picking
- [Round All Edges](round-all-edges.md) - Round every outside edge at one radius, with nothing to pick
- [Plane Cut](plane-cut.md) - Cut a whole part flat rather than one edge
- [Repair](../mesh/repair.md) - Fix an imported mesh before beveling it
