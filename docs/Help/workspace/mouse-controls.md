---
title: Mouse Controls
parent: "Workspace"
nav_order: 8
description: "Everything the mouse does in the 3D view: turning the view, selecting and moving parts and the handles."
keywords: mouse buttons, click, scroll wheel, right click, middle click
---
# Mouse Controls

Everything the mouse does in the 3D view. On a Mac, press ⌘ (Command) wherever this page says Ctrl, and ⌥ (Option) for Alt.

## Moving Around the View

| To | Do this |
|----|---------|
| **Turn the view** | Right drag, or Ctrl + left drag |
| **Move the view** | Middle drag, Ctrl + Shift + left drag, or Shift + right drag |
| **Zoom** | Scroll the wheel, Ctrl + Alt + left drag, or Alt + right drag |

- The wheel zooms toward the point under the mouse.
- Let go of a turning drag while the mouse is still moving and the view keeps turning for a moment. Hold Shift as you let go to stop it at once.
- On a Mac trackpad, a two-finger click and drag turns the view, and a two-finger scroll zooms.
- Ctrl + left drag is useful when you have no right or middle button.

## What a Left Drag Does

The round buttons around the cube in the top-right corner of the 3D view choose what a left drag does:

- **Select Parts** (the usual mode) - A left drag on a part moves it; on empty space it draws a selection rectangle.
- **Rotate View**, **Move View**, **Zoom View** - A left drag turns, moves or zooms the view.

Holding Ctrl, or pressing the right or middle button, changes the mode just for that drag. The buttons show the mode while you drag.

## Selecting and Moving Parts

These work in **Select Parts** mode.

| Action | Mouse |
|--------|-------|
| **Select a part** | Click it |
| **Add a part to the selection** | Shift + click it |
| **Add or remove a part** | Ctrl + click it (without dragging) |
| **Clear the selection** | Click empty space |
| **Select parts in an area** | Drag a rectangle on empty space |
| **Move parts** | Drag a part |
| **Move along one direction** | Shift + drag a part |
| **Edit the parts inside a group or operation** | Double-click it |
| **Open a part's menu** | Right click it |
| **Open the bed menu** | Right click empty space |

See [Selection](selection.md) for the details.

## Handles on the Selected Part

| Action | Handle |
|--------|--------|
| **Lift or lower** | Drag the arrow above the part. Double-click it to drop the part onto what is under it |
| **Turn** | Drag a curved-arrow handle at a corner. Hold Shift to snap to 45 degrees |
| **Resize** | Drag a small cube handle at a bottom corner. Hold Shift to keep the proportions |

Press Escape during a drag to put the part back. See [Editing Objects](../getting-started/editing-objects.md).

## Touch Screen

- **One finger** - Tap to select. Drag to do what the selected mode says: move a part in **Select Parts**, or turn, move or zoom the view in the other modes.
- **Two fingers** - Spread or pinch to zoom, and move both fingers together to move the view, in any mode.
- **Hold one finger still** - On a part, opens the part's menu, the one a right click opens. On empty space, opens the bed menu. A ring fills around your finger while you hold, and the menu opens after about half a second, with rows big enough for a finger.

## Related

- [Keyboard Shortcuts](keyboard-shortcuts.md) - Every shortcut
- [Viewport Navigation](../getting-started/viewport-navigation.md) - The camera controls and view settings
- [Selection](selection.md) - How selecting works
