---
title: 3D Curve
articleKey: Curve3DObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 11
---
# 3D Curve

A 3D Curve is a Bezier spline you draw through space by dragging spheres in the 3D view. It is not a solid and it does not print -- it is a route. Its main job is to be the rail a [Sweep](sweep.md) carries a profile along.

<!-- IMAGE_NEEDED: Screenshot of a 3D Curve selected in the 3D view, showing the thick tube of the curve, the anchor spheres along it, and the two handle spheres of the point being edited -->

The curve is drawn as a thin octagonal tube so you can see it and click on it. That tube is editor geometry: it shows in the viewport and in thumbnails, but it is left out of exports and out of the below-the-bed check.

## How to Use

You get a 3D Curve two ways:

- **From the library.** Open the Primitives panel and drag **3D Curve** onto the bed. It arrives as a flattened spiral you can reshape
- **From a Sweep.** Applying [Sweep](sweep.md) to a path creates a curve for you -- an S shape about twice as long as the profile is wide, starting at the profile

Then shape it:

1. Select the curve (select it inside the Sweep, in the design tree, if that is where it lives)
2. Click an anchor sphere to select that point
3. Drag it to move the curve through it
4. Use the handle spheres either side of the selected point to change how the curve bends into and out of it

Handles only appear on the point you are editing, so the view does not fill up with spheres.

## Editing Points

- **Click** an anchor or handle sphere to select it. **Ctrl-click** adds it to the selection, or removes it if it was already selected
- **Drag** a selected sphere to move it. Dragging moves everything that is selected together
- **Insert** -- press the Insert key to add a point straight after the selection, or click the **Insert Point** button and then click the segment of the curve you want the new point on. The panel shows "Click a curve segment" while insert mode is waiting
- **Delete** or **Backspace** removes the selected anchor point. This takes priority over the ordinary object delete, so pressing Delete with a point picked removes the point, not the whole curve. With no point picked, Delete removes the curve as usual
- **Esc** backs out: first it cancels insert mode, then it clears the point selection. Pressing Esc with neither active leaves the curve alone

Every one of these is undoable.

The panel shows two read-only lines so you can tell what state you are in:

- **Curve Point Selection** - "No points selected", the point being edited ("Anchor 3"), or a count when several are picked
- **Insert Point Mode** - "Off", or "Click a curve segment" while insert mode is armed

## Handles

Each anchor point has two handles, and how they behave when you drag one is the point's handle mode. Select a point and use the **Handles** row in the Properties panel. It is the same set of four buttons the 2D path editor uses, each drawn as a picture of what the handles do:

- **Sharp** - A corner, with no handles at all, so both segments meeting at the point come in straight
- **Matched** - Moving one handle mirrors the other through the point, matching both direction and length. This is the smooth, symmetrical case
- **Aligned** - Moving one handle swings the other opposite it, but each keeps its own length. Smooth through the point, with a different amount of curve on each side
- **Free** - The two handles move independently

There is also an **Auto Handles** button, which computes the handles from where the neighbouring anchors are. Auto has no button of its own in the row, so none of the four is checked while a point is on Auto -- clicking one of them converts the point to that mode.

The buttons are greyed and unchecked when there is nothing single and definite to describe: no selection, or several points picked at once.

## Tips

- A 3D Curve on its own does nothing. Pair it with a [Sweep](sweep.md), or select it together with a path and choose **Loft** -- a curve in the selection turns that into a Sweep with the curve as the rail
- Sharp points give a swept tube a hard kink; Matched or Auto keep it flowing
- Work from a couple of well-placed anchors outward. It is easier to insert a point where the curve needs more shape than to fight a curve with too many
- Rotate the view before dragging. A point moves on the plane facing the camera, so the view you drag from decides which way it can go
- Deleting the rail out of a Sweep leaves the sweep with nothing to follow and no geometry, so add one back rather than leaving it empty

## Related

- [Sweep](sweep.md) - Carry a 2D profile along a 3D Curve
- [Loft](loft.md) - Selecting a curve alongside your sections turns a Loft into a Sweep
- [Custom Path](../../2d-paths/custom-path.md) - The flat equivalent, drawn in 2D
- [Keyboard Shortcuts](../../workspace/keyboard-shortcuts.md) - The rest of the keys the 3D view answers
