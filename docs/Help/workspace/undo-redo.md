---
title: Undo and Redo
parent: "Workspace"
nav_order: 11
description: Take back a change with Undo, or put it back with Redo.
keywords: mistake, go back, revert, ctrl z, history, take back
---
# Undo and Redo

MatterCAD maintains a full history of your changes so you can undo mistakes and redo actions you reversed.

## How to Use

- **Ctrl + Z** (⌘Z on Mac) - Undo the last change
- **Ctrl + Y** or **Ctrl + Shift + Z** (⌘Y or ⇧⌘Z on Mac) - Redo the last change you undid
- You can also use the **Undo** and **Redo** buttons in the toolbar. Hover over one to see the change it will take back or put back, such as "Undo - Move".

## What Can Be Undone

All design operations are tracked in the undo history, including:

- Adding or deleting objects
- Moving, rotating, and scaling objects
- Applying operations (boolean, transform, reshape, etc.)
- Changing object parameters
- Grouping and ungrouping
- Nudging parts with the arrow keys (each press is one step)
- Changes an [AI assistant](../getting-started/ai-assistants.md) makes (each one is a single step whose name starts with "AI:")

Moving the view, and hiding or showing parts, are not changes to undo.

## Tips

- You can undo several steps by pressing Ctrl + Z (⌘Z on Mac) again and again
- The undo history is maintained for the current session. Closing and reopening a design starts a fresh history.
- If you undo several steps and then make a new change, the redo history beyond that point is cleared

## Related

- [Keyboard Shortcuts](keyboard-shortcuts.md) - All available shortcuts
- [Editing Objects](../getting-started/editing-objects.md) - Working with objects in the viewport
