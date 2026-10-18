---
title: Viewport Navigation
parent: "Getting Started"
nav_order: 5
---
# Viewport Navigation

The 3D view is where you look at and work on your design. You can turn the view around your design, move it sideways and zoom in and out with the mouse, the keyboard, the camera controls or a touch screen. None of these change your design.

On a Mac, press ⌘ (Command) wherever this page says Ctrl.

![20260324 080636 paste 20260324 080636](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080636-paste-20260324-080636.jpg)

## Mouse

| To | Do this |
|----|---------|
| **Turn the view** | Right-drag, or Ctrl + left-drag |
| **Move the view** | Middle-drag, Ctrl + Shift + left-drag, or Shift + right-drag |
| **Zoom** | Scroll the wheel, Ctrl + Alt + left-drag, or Alt + right-drag |

- The wheel zooms toward the point under the mouse, so point at what you want a closer look at.
- Let go of a turning drag while the mouse is still moving and the view keeps turning for a moment. Hold Shift as you let go to stop it at once.
- On a Mac trackpad, a two-finger click and drag turns the view, and a two-finger scroll zooms. On a Mac, Ctrl + Alt + left-drag is ⌘ + ⌥ (Option) + drag.

## Keyboard

| Key | What it does |
|-----|--------------|
| **W** | Go Home: the standard three-quarter view, with everything you can see in frame. Hidden parts are left out, and an empty design shows the bed |
| **Z** | Zoom to the selected parts |
| **Ctrl + Plus (+)** | Zoom in |
| **Ctrl + Minus (-)** | Zoom out |
| **Arrow keys** | With nothing selected: turn the view |
| **Shift + arrow keys** | With nothing selected: move the view |

With a part selected, the arrow keys move the part instead. See [Editing Objects](editing-objects.md#moving-parts).

## Camera Controls

The cube in the top-right corner of the 3D view shows which way you are looking. Click a face, edge or corner of the cube to turn the view to face it, or drag the cube to turn the view.

Around the cube are round buttons. Hover over one to see its name.

- **Reset View** - Go Home, as W does.
- **Zoom to Selection** - Fit the selected parts in the view, as Z does. It is greyed out while nothing is selected.
- **Turntable Mode** - When on (the starting setting), turning the view spins it around the bed's upright axis, so up stays up. When off, the view turns freely in any direction.
- **Perspective Mode** - When on, the view shows perspective (near things look bigger). When off, it shows an orthographic view, with no perspective. Each design remembers its own setting, and a new design starts with the one you chose last.
- **Select Parts**, **Rotate View**, **Move View** and **Zoom View** - Choose what a left-drag does. **Select Parts** is the usual mode, where a left-drag moves a part or draws a selection rectangle. In the other three, a left-drag turns, moves or zooms the view. While you hold Ctrl (or press another mouse button) the mode changes for that drag, and the buttons show it.

Under the cube are more buttons:

- **Show Bed** - Show or hide the bed and its grid.
- **The view style button** - How parts are drawn: **Shaded**, **Outlines** (the starting style), **Non-Manifold**, **Polygons** or **Overhang**. **Show part colors** turns part colors on and off.

### Snap Grid

The snap button shows how far a drag moves at a time, in the design's units ("-" when snapping is off). Click it to choose another distance, or **Off** to stop snapping. The button flashes when a drag snaps. The arrow keys nudge a part by the same distance.

### Units

The units button beside the snap button shows the units the design is shown and edited in: **mm**, **in**, **ft** or **m**. When you pick another unit, MatterCAD asks whether to keep the parts' real sizes (the numbers change) or keep your numbers (the parts change size).

## Touch Screen

- **One finger** - Tap to select. Drag to do what the selected mode button says: move a part in **Select Parts**, or turn, move or zoom the view in the other modes.
- **Two fingers** - Spread or pinch to zoom, and move both fingers together to move the view, in any mode.

## Tips

- If you lose sight of your design, press **W** (or click **Reset View**) to bring everything back into frame.
- Select a part and press **Z** to look closely at it.
- Moving the view does not count as a change to your design, so it never asks you to save just because you looked around.

## Related

- [Editing Objects](editing-objects.md) - Move, turn and resize parts in the 3D view
- [Selection](../workspace/selection.md) - How to select parts
- [Mouse Controls](../workspace/mouse-controls.md) - Every mouse control
- [Keyboard Shortcuts](../workspace/keyboard-shortcuts.md) - Every shortcut
