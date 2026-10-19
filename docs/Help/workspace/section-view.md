---
title: Section View
parent: "Workspace"
nav_order: 25
---
# Section View

Section View cuts the design open in the 3D view so you can see inside it: the walls of a box, a hole through a part, how two parts fit together. It is only a way of looking. It never changes your parts.

## Turning It On and Off

- Click the view style button beside **Show Bed**, at the top right of the 3D view, and choose **Section View**, the last row of the menu. The row is checked while the view is cut open.
- Or press **X** with the 3D view in front.

To turn it off, click **Done** on the bar, press **X** again, choose **Section View** in the menu again, or press Escape. While you are dragging, or while **Align to Face** waits for a click, Escape stops that first; press it again to turn Section View off.

## The First Cut

Turning it on cuts at once. The cut goes through the centre of the selected parts, or through the centre of the whole design when nothing is selected. It lies square to the X, Y or Z direction you are looking along most closely, and the half facing you is taken away, so you look straight at the cut faces.

## The Section View Bar

While the view is cut open, a bar sits at the top of the 3D view:

| Control | What it does |
|---------|--------------|
| **X**, **Y**, **Z** | Turns the cut square to that direction, through the same point. The half facing you is taken away. The direction in use is highlighted |
| **Flip** | Shows the other half: the half that was taken away comes back, and the half you saw is taken away |
| The position box | Where the cut is, for example "Z = 12.5 mm". Type a number and press Enter to move the cut there. A number is read in the design's units, or type the unit with it, such as `1 in`. The Up and Down arrow keys move the cut one step (1 mm, 1 in, 1 ft or 0.1 m, by the design's units); hold Shift for ten steps |
| **Done** | Turns Section View off and shows the parts whole |
| **Align to Face** | Lines the cut up with a face (below) |
| **Make Path** | Adds the outline of the cut as a 2D path (below) |

### Align to Face

1. Click **Align to Face**. It stays highlighted while it waits, and the status bar says "Click a flat face to line the cut up with it. Esc cancels."
2. Click a flat face of a part. The cut moves onto that face, through its centre, and the half facing you is taken away.

A curved face can't be used: MatterCAD says "That face is curved. Click a flat face to line the cut up with it." and waits for another click. Press Escape, or click **Align to Face** again, to stop waiting.

A face that doesn't point along X, Y or Z leaves no axis button highlighted. The position box then reads **Offset**: how far the cut is from the face you clicked, along the face's direction. Typing, the arrow keys and the drag arrow move it from there.

### Make Path

**Make Path** adds a new [Custom Path](../2d-paths/custom-path.md) named "Section Path", in the shape of the cut, ready to extrude, revolve or export:

- With parts selected, it takes the cut through the selected parts only. This lets you take one part's outline out of an assembly.
- With nothing selected, it takes the cut through every part the cut crosses.

Everything it takes becomes one path, so overlapping parts give one outline. The path lies on the cut face, and it is selected when it is added. MatterCAD says which parts it used: "Made a path of the cut through the selected parts." or "Made a path of the cut through every part it crosses." It is one undo step, "Make Path". Section View stays on.

If the cut doesn't cross those parts, nothing is added and MatterCAD says "The cut does not cross the selected parts. Move the cut onto them and try again." or "The cut does not cross any part. Move the cut onto a part and try again."

## Dragging the Cut

An arrow stands on the cut, pointing into the half that is taken away. Drag it to slide the cut along its direction. The cut moves in steps of the snap grid (the snap button under the cube; see [Camera Controls](camera-controls.md#the-snap-button)), and the position box follows. Press Escape during the drag to put the cut back where it was.

## What You See

- **Cut faces are solid and hatched.** Where the cut passes through a part, the cut face is filled in a darker shade of the part's colour, with diagonal lines over it. The lines lean one way on one part and the other way on the next, so parts that touch are easy to tell apart. The lines keep about the same spacing on screen as you zoom.
- **Parts are cut, hidden or whole.** A part the cut passes through is cut. A part wholly in the half taken away is not drawn. A part wholly in the half you see is drawn whole.
- **See-through parts are cut but not filled.**
- **Clicks go to what you can see.** Clicking through the cut selects the part you see there, never a part in the half that is taken away.

## It Is Only a View

- Section View is never saved with the design, and it is not an undo step. Turning it on, moving the cut and turning it off leave nothing to undo.
- Each design tab keeps its own cut while MatterCAD is open. A design opens whole.
- Exports, saved files and design thumbnails always show every part whole.

## Related

- [Camera Controls](camera-controls.md) - The view style button and the other buttons around the cube
- [Keyboard Shortcuts](keyboard-shortcuts.md) - X and every other key
- [Plane Cut](../operations/reshape/plane-cut.md) - Cut a part for real, as part of the design
- [Slice to Path](../operations/reshape/slice-to-path.md) - A path from a slice that updates when the part changes
- [Custom Path](../2d-paths/custom-path.md) - Edit the path Make Path adds
