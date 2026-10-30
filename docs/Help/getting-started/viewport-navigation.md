---
title: Viewport Navigation
parent: "Getting Started"
nav_order: 5
description: Turn, move and zoom the 3D view with the mouse, keyboard, camera cube or touch screen.
keywords: orbit, pan, zoom, rotate view, spin view, look around, home view, trackpad
---
# Viewport Navigation

The 3D view is where you look at and work on your design. You can turn the view around your design, move it sideways and zoom in and out with the mouse, the keyboard, the camera controls or a touch screen. None of these change your design.

On a Mac, press ⌘ (Command) wherever this page says Ctrl.

<!-- AUTO_IMAGE: type=shot id=gs-viewport-cube -->
![The cube in the top-right corner of the 3D view with its ring of round buttons](https://matterhackers.github.io/MatterCAD_Docs/assets/gs-viewport-cube.png)

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

The round buttons around the cube reset the view (**Reset View**, as W does), zoom to the selected parts (**Zoom to Selection**, as Z does), switch **Turntable Mode** and **Perspective Mode**, and choose what a left-drag does (**Select Parts**, **Rotate View**, **Move View** or **Zoom View**). Under the cube are **Show Bed**, the view style button, the snap button and the units button.

See [Camera Controls](../workspace/camera-controls.md) for what every button does.

## Touch Screen

- **One finger** - Tap to select. Drag to do what the selected mode button says: move a part in **Select Parts**, or turn, move or zoom the view in the other modes.
- **Two fingers** - Spread or pinch to zoom, and move both fingers together to move the view, in any mode.
- **Hold one finger still** - On a part, opens the part's menu, the one a right click opens. On empty space, opens the bed menu. A ring fills around your finger while you hold, and the menu opens after about half a second, with rows big enough for a finger.

## Tips

- If you lose sight of your design, press **W** (or click **Reset View**) to bring everything back into frame.
- Select a part and press **Z** to look closely at it.
- Moving the view does not count as a change to your design, so it never asks you to save just because you looked around.

## Related

- [Camera Controls](../workspace/camera-controls.md) - Every button around the cube
- [Editing Objects](editing-objects.md) - Move, turn and resize parts in the 3D view
- [Selection](../workspace/selection.md) - How to select parts
- [Mouse Controls](../workspace/mouse-controls.md) - Every mouse control
- [Keyboard Shortcuts](../workspace/keyboard-shortcuts.md) - Every shortcut
