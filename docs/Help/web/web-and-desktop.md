---
title: Web and Desktop Differences
parent: "MatterCAD on the Web"
nav_order: 5
description: What works differently in the website editor than in the desktop app, and which browsers you need.
keywords: browser differences, desktop app, webgpu, chrome, safari, firefox, limitations
---
# Web and Desktop Differences

The editor on the website is MatterCAD itself: the same shapes, operations, Properties panel and 3D view as MatterCAD on your computer. A web page can't reach your computer's files or other programs, though, so a few things work differently.

## Your Designs and Files

- **Save** keeps the design in your online library, not in a file on your computer. **Save As** lists only **My Designs** and its folders: choose the folder and the name for the copy there. It has no **Computer** folder. See [Saving on the Web](saving.md#save-as).
- **Export** and the page's **Download** button are how you get a file on your computer. Your browser downloads it.
- **Add to Bed** has no **Computer** folder. To bring in a file from your computer, open **System File** at the top of the library (your browser asks you to pick the file) or drag the file onto the 3D view. See [Adding Parts on the Web](adding-parts.md).
- Unsaved changes are kept as a copy in your browser, which holds designs up to about 3.5 MB. MatterCAD on your computer offers to recover unsaved work when it starts instead ([Saving and Exporting](../getting-started/saving-and-exporting.md#recover-unsaved-work)).

## The Window and Menus

- Each design has its own page. There are no tabs, and no **Library** or **Help** tab.
- The **☰ Options** button is in the page's title bar, shown while you edit. Its menu holds **New Design**, **Interface Tour**, **Help** and **Settings**. **Open System File**, **Open Recent**, **Open Demo**, **Check For Update**, **Community** and **About MatterCAD** are only in MatterCAD on your computer.
- **Submit Feedback** is the **Feedback** button in the website's header, not a button in the status bar ([Getting More Help](../get-support.md#feedback-on-the-website)).
- There is no **Check For Update**: the website runs the version of MatterCAD it serves. Reload the page to get a newer version once the website has one.
- **Settings** has only **Number format**, **Anti-aliasing** and **Transparency Layers**. The colors follow the theme you chose on the website, in the menu under your name in its header ([The Options Menu](mattercad-menu.md#settings)).
- The **Bed** menu has no **Reload**.
- A selected part has no **Help** button and no **Help Docs** menu row. Open **Help** from the Options menu instead: it opens the help pages on the website in a new browser tab ([Help](mattercad-menu.md#help)).
- There is no **Open With** in a part's right-click menu, and no menu item that shows a file in your computer's file manager.
- **Save as Tool**, for node graphs, is only in MatterCAD on your computer.

## AI

- The **AI** tab goes through the website and never uses AI keys of your own.
- Outside AI tools such as Claude Code, Codex and Claude Desktop connect only to MatterCAD on your computer, not to the website's editor ([Using AI Assistants](../getting-started/ai-assistants.md)).

## Variable Sheets

A sheet's **importdata()** can't read a file or a web address in a browser. Instead of a value, the cell shows: "Error: importdata cannot read files or web addresses in the browser. To import data, open this design in the MatterCAD desktop app." See [importdata](../workspace/expression-functions.md#importdata).

## Keyboard

- Click in MatterCAD's part of the page before you use keys, so they go to MatterCAD and not to the web page.
- While you edit, Ctrl+S and Ctrl+Shift+S (⌘S and ⌘⇧S on a Mac) run MatterCAD's **Save** and **Save As**, not your browser's "save page". While you only preview the design, they are your browser's.

## The Browser You Need

MatterCAD on the website needs a browser with WebGPU, such as a current Chrome, Edge or Safari. Without it, the page shows a message and a **Download file** button instead of the design ([What You Need](index.md#what-you-need)).

## Related

- [MatterCAD on the Web](index.md) - Preview, Edit and View
- [Using MatterCAD on a Phone](phone.md) - The phone layout
