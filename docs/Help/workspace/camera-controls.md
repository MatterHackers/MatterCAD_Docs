---
title: Camera Controls
parent: "Workspace"
nav_order: 20
---
# Camera Controls

The camera controls sit in the top-right corner of the 3D view: a cube that shows which way you are looking, round buttons around it, and a few more buttons under it. They change how you see the design, never the design itself, except the units button, which asks first.

To move the view with the mouse, the keyboard or a touch screen, see [Viewport Navigation](../getting-started/viewport-navigation.md).

On a Mac, press ⌘ (Command) wherever this page says Ctrl.

<!-- IMAGE_NEEDED: Close-up of the top-right corner of the 3D view: the cube with the round buttons around it (the four mode buttons above, Reset View and Zoom to Selection lower left, Turntable Mode and Perspective Mode lower right), and under it the Show Bed and view style buttons with the snap and units buttons below them, each labelled -->

Hover over any button to see its name. While you hover, the status bar at the bottom of the window shows a hint, such as the key that does the same thing.

## The Cube

The cube turns with the view, so its labelled faces show which side of the design you are looking at.

- **Click a face, edge or corner** to turn the view to look straight at it. The part of the cube under the mouse lights up first, so you can see what you will get.
- **Drag the cube** to turn the view.

## The Buttons Around the Cube

| Button | What it does |
|--------|--------------|
| **Select Parts** | A left-drag moves a part, or draws a selection rectangle when you start on empty space. This is the usual mode |
| **Rotate View** | A left-drag turns the view |
| **Move View** | A left-drag moves the view sideways |
| **Zoom View** | A left-drag zooms in and out |
| **Reset View** (the house) | Goes Home: the standard three-quarter view with everything you can see in frame, as **W** does |
| **Zoom to Selection** | Fits the selected parts in the view, as **Z** does. It is greyed out while nothing is selected |
| **Turntable Mode** | When on, turning the view spins it around the bed's upright axis, so up stays up. When off, the view turns freely in any direction |
| **Perspective Mode** | When on, near things look bigger. When off, the view is orthographic: sizes don't change with distance, which makes it easier to line things up |

### Select, Rotate, Move and Zoom

The four mode buttons choose what a left-drag in the 3D view does. Only one is on at a time. The other mouse buttons keep working in every mode: a right-drag still turns the view, and the wheel still zooms.

While you hold Ctrl, or drag with another mouse button, the mode changes for that one drag, and the buttons show it. When you let go, the mode you chose comes back.

Hover over a mode button to see every way to do the same thing in the status bar, for example "Rotate: Right Mouse Button, Ctrl + Left Mouse Button, Arrow Keys".

### Turntable Mode and Perspective Mode

- **Turntable Mode** starts on. It is one setting for the whole app: turning it on or off changes every open design. Turning it on also stands the view upright again, without changing the direction you look from.
- **Perspective Mode** belongs to the design tab you click it in. A design remembers its setting when you save it, and a new design starts with the setting you chose last.

## The Buttons Under the Cube

### Show Bed

**Show Bed** shows or hides the bed, its grid and the shadow under the parts. With the bed hidden, the parts float on the background. It starts on, and the choice applies to every open design.

### The View Style Button

The button beside **Show Bed** shows a picture of the style in use. Click it to choose how parts are drawn:

| Style | What you see |
|-------|--------------|
| **Shaded** | Solid parts with no lines |
| **Outlines (default)** | Solid parts with a line along each sharp edge. This is the starting style |
| **Non-Manifold** | Solid parts with no lines, except a highlighted line along any edge that leaves a gap in the surface, so you can find holes in a mesh |
| **Polygons** | Solid parts with every triangle of the mesh outlined |
| **Overhang** | Faces colored by the way they point: blue for faces that point up or sideways, turning to red as a face turns to point straight down |

Under the styles, **Show part colors** turns the parts' own colors on and off. When it is off, every part is drawn in one neutral gray. This setting applies to every open design.

Each design tab keeps its own style. A new design starts with the style you chose last.

### The Snap Button

The snap button shows how far a dragged part moves at a time, in the design's units. It reads **-** when snapping is off. Hover over it to see the full distance, for example "Snap Grid = 1 mm".

Click it to choose a distance, or **Off** to stop snapping. The choices depend on the units:

| Units | Choices | Starts at |
|-------|---------|-----------|
| **mm** | 0.1, 0.25, 0.5, 1, 2 and 5 mm | 1 mm |
| **in** | 1/64, 1/32, 1/16, 1/8, 1/4, 1/2 and 1 in | 1/16 in |
| **ft** | 1, 3 and 6 in, and 1, 2 and 5 ft | 1 in |
| **m** | 0.01, 0.05, 0.1, 0.5 and 1 m | 0.01 m |

The button flashes each time a drag snaps to the grid. The arrow keys nudge a selected part by the same distance. MatterCAD remembers a separate snap distance for each unit, for all your designs.

### The Units Button

The units button, beside the snap button, shows the units the design in front of you is shown and edited in: **mm**, **in**, **ft** or **m**. Hover over it to see "Units for this design".

Click it and choose **Millimeters (mm)**, **Inches (in)**, **Feet (ft)** or **Meters (m)**.

- For an empty design, the units change at once.
- For a design with parts in it, MatterCAD opens **Change Units** and asks how the design should follow. It names one of your parts and its size, for example "Your Cube is 20 mm wide. After the change it should be:", and offers two buttons, each with a line on what it means:
  - The first button keeps your numbers, for example "20 in wide", beside "I typed my sizes in inches." Every number stays the same and is read in the new unit, so every part changes size: "Everything gets 25.4x bigger." One Undo takes it back.
  - The second button keeps the real sizes, for example "0.7874 in wide", beside "It is the right size already." and "Nothing changes size." The parts stay the same size and their numbers are shown in the new unit.
  - Click **Cancel** to leave the units as they were.
- A design that takes its sizes from a [Variable Sheet](variable-sheet.md) is offered only the second button, because its numbers come from the sheet. To change them, change the numbers in the sheet.

Each design remembers its units when you save it, so a design made in feet opens in feet. A new design starts in the units you used last.

## In a Narrow Window

When the window is very narrow, the cube is left out and the buttons stand in a column at the right edge of the 3D view.

## Related

- [Viewport Navigation](../getting-started/viewport-navigation.md) - Turn, move and zoom the view with the mouse, keys or touch
- [Mouse Controls](mouse-controls.md) - Every mouse control
- [Keyboard Shortcuts](keyboard-shortcuts.md) - Every shortcut
- [Menus and Toolbar](menus-and-toolbar.md) - The application menu and the toolbar above the 3D view
