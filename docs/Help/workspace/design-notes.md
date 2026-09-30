---
title: Design Notes
parent: "Workspace"
nav_order: 17
---
# Design Notes

Design Notes are a short written brief that travels with your design: what it is for, the sizes that matter, the decisions you made and what is still open. Whoever opens the design next reads them first, whether that's you in a month, a colleague, or an [AI assistant](../getting-started/ai-assistants.md).

<!-- IMAGE_NEEDED: Screenshot of the Design Notes window on the Preview tab, showing a short brief with Goal, Key sizes, Decisions still in force and Open / next headings, and the highlighted Notes button at the top of the scene tree, beside Show All and Unlock All -->

Notes belong to the whole design, not to one object. To put a note next to a feature in the 3D view, use a [Description](description.md) instead.

## How to Use

1. Click the **Notes** button at the top of the scene tree, beside **Show All** and **Unlock All**. The button is highlighted when the design has notes, so you can see there is something to read.
2. The window opens on **Preview**, showing the notes as formatted text. A design with no notes shows a hint about what to write.
3. Click **Edit** to change the notes. They are [Markdown](https://guides.github.com/features/mastering-markdown/), so you can use headings, lists, bold and links. The **Help** tab is a Markdown reference.
4. Click **Save** to keep your changes, or close the window to throw them away.

While you edit, a count below the text shows how long the notes are, for example "1,240 characters; AI assistants keep their part under 2,000". It's for your information only. Your own notes can be as long as you like.

The notes are the same wherever you are in the design. If you are inside an object with **Edit Children**, the button still opens the notes of the whole design.

## Saving and Undo

- Notes are saved in the design's `.mcx` file, and open with it.
- Saving changed notes is one change, named "Edit Notes" in the undo history. **Undo** takes it back, like any other change.
- Changing the notes marks the design as unsaved, so remember to save the design as well.

## Notes and AI Assistants

An AI assistant connected to MatterCAD reads the notes before anything else, and keeps them up to date as it works. It keeps a short brief under four headings:

- **Goal** - what the design is for
- **Key sizes** - the measurements that matter
- **Decisions still in force** - choices that should guide the next change
- **Open / next** - what is unfinished or still to decide

The AI rewrites the notes as a current brief, not a history. It prunes what no longer helps, such as things the design already shows or decisions that no longer apply, and keeps its notes under 2,000 characters.

The AI keeps what you wrote. It only changes or removes your text when you ask it to. Every change it makes to the notes is part of an "AI: ..." step in the undo history, so one **Undo** takes it back.

## Tips

- Write the notes for someone who has never seen the design. A sentence on what it's for saves them guessing.
- Put the sizes that come from outside the design in **Key sizes**: the jar the lid fits, the board the case holds.
- When you change your mind about a decision, update the notes, so the AI doesn't keep following the old one.

## Related

- [Using AI Assistants](../getting-started/ai-assistants.md) - Let an AI tool work on your designs
- [Description](description.md) - Put a note next to a feature in the 3D view
- [Undo and Redo](undo-redo.md) - Take back changes, including changes to the notes
