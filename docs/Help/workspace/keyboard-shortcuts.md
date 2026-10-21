---
title: Keyboard Shortcuts
parent: "Workspace"
nav_order: 5
description: Every key and mouse shortcut in MatterCAD, from the view and selection to editing and files.
keywords: hotkeys, keys, shortcut keys, key bindings, keyboard commands
---
# Keyboard Shortcuts

The **Keys** and **Mouse** tables below are the same list as **Help › Keys** and **Help › Mouse** in MatterCAD itself (press F1 and find them in the list of help pages). In the app, those pages show Mac keys on a Mac.

You don't have to learn the keys from this page. A menu row with a key shows it at its right, for example **Save As** in a part's right-click menu. A button with a key names it in its tooltip after the button's name, for example "Undo - Move (Ctrl+Z)", "Group (G)" or "Reset View (W)".

Keys that belong to one tool are on that tool's page: the [sheet editor](sheet-editing.md), the [path editor](../2d-paths/custom-path.md), [3D Curve](../operations/path/curve-3d.md) points and text fields.

On a Mac, Ctrl is ⌘ (Command) and Shift is ⇧.

## Keys

### View

| Windows and Linux | Mac | Action |
|-------------------|-----|--------|
| ← → ↑ ↓ | ← → ↑ ↓ | Rotate View (when nothing is selected) |
| shift + ← → ↑ ↓ | ⇧ + ← → ↑ ↓ | Move View (when nothing is selected) |
| ctrl + + | ⌘+ | Zoom in |
| ctrl + - | ⌘- | Zoom out |
| w | w | Reset View (the Home button) |
| z | z | Zoom to Selection |
| x | x | Section View (turn on and off) |

### Selection

| Windows and Linux | Mac | Action |
|-------------------|-----|--------|
| ctrl + a | ⌘A | Select all |
| space bar | space bar | Clear the selection |
| esc | esc | Cancel the drag in progress (a dragged part goes back where it was) |
| esc | esc | Turn off Section View |
| ↑ ↓ | ↑ ↓ | In the Design tree: select the row above or below |
| → | → | In the Design tree: open the selected row |
| ← | ← | In the Design tree: close the row, or go to the row it is in |

### Editing

| Windows and Linux | Mac | Action |
|-------------------|-----|--------|
| ← → ↑ ↓ | ← → ↑ ↓ | Move the selected part one snap step (at least 0.1 mm) |
| shift + ← → ↑ ↓ | ⇧ + ← → ↑ ↓ | Move the selected part five snap steps |
| ctrl + ← → ↑ ↓ | ⌘ + ← → ↑ ↓ | Move the selected part a fifth of a snap step |
| delete / backspace | delete / backspace | Delete the selection |
| ctrl + z | ⌘Z | Undo |
| ctrl + y | ⌘Y | Redo |
| ctrl + shift + z | ⇧⌘Z | Redo |
| ctrl + c | ⌘C | Copy |
| ctrl + x | ⌘X | Cut |
| ctrl + v | ⌘V | Paste |
| g | g | Group the selected parts |
| shift + g | ⇧G | Ungroup the selected group |
| F2 | F2 | Rename the selected part |

### Files

| Windows and Linux | Mac | Action |
|-------------------|-----|--------|
| ctrl + o | ⌘O | Open a file |
| ctrl + s | ⌘S | Save |
| ctrl + shift + s | ⇧⌘S | Save As |

### Tabs

| Windows and Linux | Mac | Action |
|-------------------|-----|--------|
| ctrl + t | ⌘T | Open a new design tab (while a design is showing) |
| ctrl + shift + t | ⇧⌘T | Reopen the design tab you closed last |
| F1 | F1 | Show Help |
| - | ⌘Q | Quit MatterCAD |

## Mouse

### Selection

| Windows and Linux | Mac | Action |
|-------------------|-----|--------|
| left click | left click | Select a part |
| left click + shift | left click + ⇧ | Add a part to the selection |
| left click + ctrl | left click + ⌘ | Add or remove a part from the selection |
| left drag | left drag | Select the parts in a rectangle (start on empty space) |
| double-click | double-click | Edit the parts inside a group or operation |

### Parts

| Windows and Linux | Mac | Action |
|-------------------|-----|--------|
| left drag | left drag | Move a part (start on the part) |
| left drag + shift | left drag + ⇧ | Move a part along one direction only |
| right click | right click | Open the part's menu, or the bed menu on empty space |

### View

| Windows and Linux | Mac | Action |
|-------------------|-----|--------|
| right drag | right drag | Rotate View |
| left drag + ctrl | left drag + ⌘ | Rotate View |
| middle drag | middle drag | Move View |
| right drag + shift | right drag + ⇧ | Move View |
| left drag + shift + ctrl | left drag + ⇧ + ⌘ | Move View |
| wheel | wheel | Zoom View |
| right drag + alt | right drag + ⌥ | Zoom View |
| left drag + ctrl + alt | left drag + ⌘ + ⌥ | Zoom View |

## Related

- [Mouse Controls](mouse-controls.md) - Every mouse control, with the view modes and touch
- [Viewport Navigation](../getting-started/viewport-navigation.md) - How to move around the 3D view
- [Selection](selection.md) - How selecting works
- [Section View](section-view.md) - What X and Escape do while the view is cut open
