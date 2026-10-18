---
title: Keyboard Shortcuts
parent: "Workspace"
nav_order: 5
---
# Keyboard Shortcuts

The **Keys** and **Mouse** tables below are the same lists as the **Keys** and **Mouse** pages in MatterCAD's own Help (press F1 and find them in the list of help pages). In the app, those pages show Mac keys on a Mac.

On a Mac, Ctrl is ⌘ (Command) and Shift is ⇧.

## Keys

| Windows and Linux | Mac | Action |
|-------------------|-----|--------|
| F1 | F1 | Show Help |
| ctrl + + | ⌘+ | Zoom in |
| ctrl + - | ⌘- | Zoom out |
| ← → ↑ ↓ | ← → ↑ ↓ | Rotate |
| shift + ← → ↑ ↓ | ⇧ + ← → ↑ ↓ | Pan |
| w | w | Zoom to window |
| z | z | Zoom to selection |
| ctrl + a | ⌘A | Select all |
| space bar | space bar | Clear selection |
| esc | esc | Cancel command |
| ctrl + s | ⌘S | Save |
| ctrl + z | ⌘Z | Undo |
| ctrl + y | ⌘Y | Redo |
| delete | delete | Delete selection |

The arrow keys turn (Rotate) and move (Pan) the view only while nothing is selected. With a part selected, they move the part instead (see [More keys](#more-keys)). **w** goes to the Home view: the standard three-quarter view with everything you can see in frame.

## Mouse

| Windows and Linux | Mac | Action |
|-------------------|-----|--------|
| left click | left click | Make Selection |
| left click + shift | left click + ⇧ | Add to Selection |
| left click + ctrl | left click + ⌘ | Toggle Selection |
| left drag | left drag | Rubber Band Selection |
| left drag | left drag | Move Part |
| left drag + shift | left drag + ⇧ | Move Part Constrained |
| left drag + shift + ctrl | left drag + ⇧ + ⌘ | Pan View |
| left drag + ctrl | left drag + ⌘ | Rotate View |
| middle drag | middle drag | Pan View |
| right drag | right drag | Rotate View |
| wheel | wheel | Zoom |

A left drag that starts on empty space draws a selection rectangle (Rubber Band Selection); one that starts on a part moves it (Move Part). Move Part Constrained keeps the move along one direction.

## More Keys

These work too, but are not in the in-app lists.

| Windows and Linux | Mac | Action |
|-------------------|-----|--------|
| Arrow keys, with a part selected | Arrow keys, with a part selected | Move the part one snap step across the bed |
| Shift + arrow keys, with a part selected | ⇧ + arrow keys, with a part selected | Move the part five snap steps |
| Ctrl + arrow keys, with a part selected | ⌘ + arrow keys, with a part selected | Move the part a fifth of a snap step |
| Ctrl + Shift + Z | ⇧⌘Z | Redo |
| Ctrl + = | ⌘= | Zoom in |
| Backspace | Backspace | Delete selection |
| Ctrl + C | ⌘C | Copy |
| Ctrl + X | ⌘X | Cut |
| Ctrl + V | ⌘V | Paste |
| G | G | Group the selected parts |
| Shift + G | ⇧G | Ungroup |
| F2 | F2 | Rename the selected part |
| Ctrl + O | ⌘O | Open System File |
| Ctrl + Shift + S | ⇧⌘S | Save As |
| Ctrl + T | ⌘T | New design (while a design is showing) |
| Ctrl + Shift + T | ⇧⌘T | Reopen the design tab you closed last |
| Esc, during a drag | Esc, during a drag | Put the part back where it was |

A snap step is the distance the snap button shows (at least 0.1 mm, also when snapping is off).

### In the Design tree

Click a row first, then:

| Key | Action |
|-----|--------|
| ↑ ↓ | Select the row above or below |
| → | Open the selected row |
| ← | Close an open row; on a closed row, open it if it has parts inside, or else go to the row it is in |

## More Mouse Controls

| Windows and Linux | Mac | Action |
|-------------------|-----|--------|
| Shift + right drag | ⇧ + right drag | Pan View |
| Alt + right drag | ⌥ + right drag | Zoom |
| Ctrl + Alt + left drag | ⌘ + ⌥ + left drag | Zoom |
| Double-click a group or operation | Double-click a group or operation | Edit the parts inside it |
| Right click on a part | Right click on a part | The part's menu |
| Right click on empty space | Right click on empty space | The bed menu |

On a Mac trackpad, a two-finger click and drag rotates the view, and a two-finger scroll zooms.

## Related

- [Mouse Controls](mouse-controls.md) - Every mouse control, with the view modes and touch
- [Viewport Navigation](../getting-started/viewport-navigation.md) - How to move around the 3D view
- [Selection](selection.md) - How selecting works
