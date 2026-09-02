---
title: Description
articleKey: DescriptionObject3D
parent: "Workspace"
nav_order: 13
---
# Description

Description puts a note in the scene. It is a label anchored to a point in your design, showing text you write in Markdown -- a build note, an assembly instruction, a reminder about which way a part goes on the bed.

<!-- IMAGE_NEEDED: Screenshot of a Description in the 3D view, showing the note panel connected to its anchor point on a part, with the Properties panel showing the Markdown text field -->

Like the [Measure Tool](measure-tool.md), it is a design aid rather than a part. A Description does not print and is left out of exports.

## How to Use

1. Open the Tools group in the library and drag **Description** onto the bed
2. Type your note in the **Description - Markdown Text** field in the Properties panel. The note updates as you type
3. Click in the 3D view to place the note's anchor point where you want it
4. Choose a **Placement** and a **Width** so the note sits clear of the part

## Parameters

- **Description - Markdown Text** - The note itself. It is [Markdown](https://guides.github.com/features/mastering-markdown/), so you can use headings, lists, bold, links and images. It is a multi-line field that updates on every keystroke
- **Placement** - Which corner the note is drawn in relative to its anchor: Left Top, Left Bottom, Right Top or Right Bottom
- **Width** - Narrow, Normal or Wide. How much room the note gets before its text wraps

The note's position is set by dragging its anchor in the 3D view rather than by typing coordinates. A **Reset** button in the Properties panel puts the anchor back to its starting position and hides the note until you place it again.

## Tips

- Use Descriptions to document a design you are sharing. Someone opening your file sees the note in the scene, not buried in a filename
- Markdown means you can link out -- to a datasheet, to a printing profile, to the page you got a dimension from
- Place the anchor on the feature the note is about. A note about a hole should point at the hole
- Set **Width** to Wide for a paragraph and Narrow for a one-line label
- Descriptions do not print, so you can leave them in the design. There is no need to strip them before exporting

## Related

- [Measure Tool](measure-tool.md) - The other in-scene design aid, for checking dimensions
- [Variable Sheet](variable-sheet.md) - Store the numbers a design is built from, with their own names
- [Expressions](expressions.md) - Drive dimensions from those numbers
