---
title: MatterCAD on the Web
has_children: true
nav_order: 3.5
---
# MatterCAD on the Web

On the MatterCAD website, each design in your library has a page of its own. The page shows the design in 3D, and the same page lets you edit it with MatterCAD, right in your browser. There is nothing to install.

A design page works in three steps:

1. **Preview** - The design opens as a 3D preview. You can turn it, move it and zoom, but nothing changes the design.
2. **Edit** - Press **Edit** and the MatterCAD editor slides in around the same view.
3. **Done** - Press **Done** to go back to the preview.

<!-- IMAGE_NEEDED: A design page on the MatterCAD website in a desktop browser: the title bar (Library back button, Edit, the design's name, Full screen, Download) above the 3D preview of a design, with Reset View and the Rotate View / Move View / Zoom View buttons at the preview's top-left -->

## What You Need

MatterCAD on the website needs a browser with **WebGPU**, such as a current Chrome, Edge or Safari.

In a browser without WebGPU, the page shows this message where the 3D view would be: "This browser can't show the 3D preview because it doesn't support WebGPU. Use a current Chrome, Edge or Safari, or download the file." On a design's page, the **Download file** button under it gets the design's file, so you can open it in MatterCAD on your computer.

## Open a Design

1. On the website's **Library** page, open the folder the design is in.
2. Click the design.

Its page opens. While it gets ready you see "Loading MatterCAD…", then "Downloading model…" with how far along it is, then "Preparing model…". Then the design appears, framed so you can see all of it.

The title bar above the design holds:

- **Library** (with the back arrow) - Back to the library folder you came from.
- **Edit** - Opens the editor. It reads **Done** while you edit. It can't be pressed until MatterCAD has started, or while the editor is sliding in or out.
- The design's name.
- **Full screen** - Fills the screen with the title bar and the design. Press it again (**Exit full screen**), or press Esc, to go back. It is there only when your browser can fill the screen.
- **Download** - Downloads the design's file as it was last saved.

If the design can't be shown, the page says why, starting with "This design couldn't be shown", and tells you to use **Download** to get the file.

## Look Around the Preview

- **Drag** in the 3D view to turn it. Scroll the mouse wheel to zoom.
- **The buttons at the top-left** - **Reset View** brings back the starting view. **Rotate View**, **Move View** and **Zoom View** choose whether a drag turns, moves or zooms the view.
- **On a touch screen**, one finger does what the selected button says, and two fingers pinch to zoom and move the view. See [Touch Screen](../getting-started/viewport-navigation.md#touch-screen).
- **Keys** - Click in the 3D view first, so your keys go to MatterCAD and not to the web page. Then the arrow keys turn the view, Shift + arrow keys move it, Ctrl + Plus and Ctrl + Minus zoom (⌘ on a Mac), and **W** goes back to the starting view.

In the preview a click never selects or moves a part. Press **Edit** to change the design.

## Edit the Design

Press **Edit** in the title bar. The editor slides in around the design:

- The **toolbar** across the top, starting with **Add to Bed** and the **MatterCAD** menu ([The MatterCAD Menu](mattercad-menu.md)).
- The **favorites bar** of shapes down the left side.
- The **side panel** on the right, with its **Design** and **AI** tabs and the **Notes** button.
- The **camera controls**: the cube in the top-right corner of the view and the round buttons around it.

From here, editing works as it does in MatterCAD on your computer. [Getting Started](../getting-started/index.md) shows you how to add shapes, change them and combine them.

While you edit, the page's address says so: reloading the page, or opening that address later, opens the design straight in the editor.

## Stop Editing

Press **Done** in the title bar. If every change is saved, the editor slides away and you are back in the preview.

If you have changes that are not saved, MatterCAD asks first, in a box titled **Save Changes?**: "Save your changes before you stop editing?"

- **Save Changes** - Saves the design, then goes back to the preview once the save has finished. If the design can't be saved over, MatterCAD asks for a name and saves your own copy first ([Saving on the Web](saving.md)).
- **Discard Changes** - Throws your changes away, puts back the last saved version, and goes back to the preview.
- **Cancel** - Stays in the editor with your changes.

## Leaving the Page

While you have changes that are not saved, your browser asks before you leave the page or close the tab. As you work, MatterCAD keeps a copy of your unsaved changes in this browser, so if the page closes anyway it can offer them back the next time you open the design ([Unsaved Changes Found](saving.md#unsaved-changes-found)).

## Topics

- [The MatterCAD Menu](mattercad-menu.md) - New Design, the Interface Tour, Help and Settings on the website
- [Saving on the Web](saving.md) - Save, Save As, Export, and getting back unsaved changes
- [Adding Parts on the Web](adding-parts.md) - Shapes, sample parts and the designs in your own library
- [Using MatterCAD on a Phone](phone.md) - The phone layout, the bottom sheet and touch gestures
- [Web and Desktop Differences](web-and-desktop.md) - What works differently in a browser
