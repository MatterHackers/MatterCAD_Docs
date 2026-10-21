---
title: Saving and Exporting
parent: "Getting Started"
nav_order: 4
description: Save your design as an MCX file, or export STL, 3MF, OBJ, STEP and more for slicers and other programs.
keywords: slicer, 3d printer, 3d printing, file format, file type, save a copy, mcx
---
# Saving and Exporting

**Save** keeps your design as an MCX file, MatterCAD's own format, with every part and setting still editable. **Export** writes a copy in another format (STL, 3MF, OBJ, AMF, STEP, SVG or DXF) for other programs.

On a Mac, press ⌘ (Command) wherever this page says Ctrl.

## Save Your Design

The **Save** button is in the design's toolbar, right after **Add to Bed**. It reads **Save •** while the design has changes you have not saved.

- **Save** (Ctrl+S) writes the design to its MCX file. A design that has never been saved asks for a name and a folder first, as Save As does. So does a design you opened from an STL, a picture or any other file that is not an MCX: Save never writes your design over the file it came from.
- **Save As** (Ctrl+Shift+S, or the arrow beside **Save**) saves the design under a new name or in another folder:
  1. Pick a library folder, on your computer or in your Cloud Library. The box is headed "Choose where to save your design". It opens in the folder you last left it in. While the folder showing can't take a design, it says "Choose a folder you can save in." and **Save** can't be clicked.
  2. Type a **Design Name**. Clicking a design in the list puts its name there, without the extension; the design saves as an MCX file.
  3. Click **Save**. If the folder already has a design with that name, a box titled **Confirm Save As** asks before **Replace** saves over it.

Save and Save As are also on the right-click menu of the empty bed. A part's right-click menu has **Save As** too, which saves just that part.

An MCX file also remembers the view you saved it with - the direction, zoom and perspective or orthographic setting - so it opens looking the way you left it. Moving the view does not count as a change, so it never asks you to save just because you looked around.

## Recover Unsaved Work

While you work, MatterCAD keeps a recovery copy of every open design that has parts on its bed. It does not save your design file for you.

If MatterCAD closes before you save (for example, if it crashes), the next time it starts it asks **Recover Design**: "Unsaved work was found for ... Recover it as an unsaved design?"

- Click **Recover** to open your unsaved work in a tab. It opens as an unsaved design: click **Save** to keep it. Your saved file is not changed until you do.
- Click **Discard recovery** to throw the unsaved work away and open the design as you last saved it.

## Export to Another Format

1. Click the arrow beside **Save** and choose **Export** (it is also in the **Bed** menu). To export one part, right-click it and choose **Export**.
2. Pick the format. A format that can't export your design is greyed out and says why.
3. Set the format's options, if it has any.
4. Click **Export** and choose where the file goes.

The formats are listed most faithful first:

| Format | What it keeps | Use it when |
|--------|---------------|-------------|
| **MCX** | Everything: every part, setting and operation, still editable | You want to keep working on the design, or share it with someone who uses MatterCAD |
| **3MF** | Each part as its own shape, with its position and colors | You want to send a design with several parts or colors to another program |
| **STL** | The shape as triangles, with no colors or settings | A program only needs the shape; almost every 3D program reads STL |
| **OBJ** | The shape as triangles | You want to open the design in another 3D program, such as Blender or a game engine |
| **AMF** | The shape as triangles | A program asks for AMF |
| **STEP** | Each part as a solid with its name and color | You want to open the design in a CAD program |
| **SVG** | The design's 2D paths as a flat drawing | You need an outline for a laser cutter, a cutting machine or a drawing program |
| **DXF** | The design's 2D paths as a flat drawing | A CAD or CNC program asks for DXF |

SVG and DXF are offered only when the design has a 2D path (a flat shape such as those in the library's **2D Primitives**). Otherwise they show **No 2D Path Was Found**.

### Export options

- **STL**, when the design has more than one part: **Perform Union** merges them into a single shape before exporting; **Save by Color** writes one file for each color.
- **STEP**: **Faceted B-rep (for older CAD)** writes a larger file that older CAD programs can read.
- **MCX**: **Include computed meshes** writes every mesh into the file, which makes it much larger.

## Tips

- Save an MCX copy of your design before you export it, so you can change it later.
- Holes are cut for you when you export to STL, 3MF, OBJ, AMF or STEP. Those formats can't say "this shape is a hole", so MatterCAD subtracts each hole from the parts it overlaps and leaves the hole itself out of the file. Your design is not changed - only the exported copy.
- [Hidden](../workspace/lock-hide.md) parts are left out of an export to STL, 3MF, OBJ, AMF or STEP. An MCX file keeps them.
- You can save designs to your [Cloud Library](../library/cloud-library.md) to reach them from any computer.

## Related

- [Adding Existing Objects](adding-existing-objects.md) - Bring files into MatterCAD
- [Library](../library/index.md) - Organize your saved designs
- [Cloud Library](../library/cloud-library.md) - Keep designs in the cloud
