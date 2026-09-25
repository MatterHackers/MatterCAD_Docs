---
title: Using AI Assistants
parent: "Getting Started"
nav_order: 6
---
# Using AI Assistants with MatterCAD

AI chat tools such as Claude Code, Codex and Claude Desktop can work on your designs in MatterCAD. Ask one to "add four 3 mm holes in the corners" or "make the lid 2 mm thicker", and it reads the design in the tab you're looking at, makes the change, and checks the result.

You watch every change happen live in the 3D view. Each AI change is a single undo step with a name that starts with "AI:", for example "AI: add mounting holes", so one Undo takes it back.

<!-- IMAGE_NEEDED: Screenshot of MatterCAD with an AI change just applied, the Undo history showing an "AI: add mounting holes" step -->

## Turn It On

AI assistant access is off until you turn it on.

1. Open the **AI Assistant Access** panel in one of two ways:
   - Click the **AI** item in the status bar at the bottom of the window. This always works, even when you're not signed in.
   - Open the account menu and choose **AI Assistant Access...**. This menu is only there while you're signed in.
2. Turn on **Allow AI assistants to edit designs**.

<!-- IMAGE_NEEDED: Screenshot of the AI Assistant Access panel showing the Allow AI assistants to edit designs switch, the Address and Port rows, the AI can save and export to folder, and the Copy buttons for Claude Code, Codex and Claude Desktop -->

Access stays on when you close and reopen MatterCAD, until you turn it off again.

While access is on, the status bar item shows what is happening:

- **AI Ready** - access is on, and no AI tool has talked to MatterCAD in the last minute.
- **AI Connected** - an AI tool has talked to MatterCAD in the last minute.
- **AI Editing** - an AI tool is changing your design right now. You can keep working while it does.

If the [feedback log](#the-feedback-log) is on, the item adds "(logging)", for example "AI Connected (logging)". When access is off, the item is hidden.

<!-- IMAGE_NEEDED: Close-up of the status bar showing the AI Connected item next to the Connected item -->

## Connect Your AI Tool

Each tool needs a setup line that tells it where MatterCAD is. In the **AI Assistant Access** panel, press the **Copy** button next to your tool's name, then paste the copied text where that tool expects it, as described below.

The copied text contains a private access key. Anyone who has it can edit your designs while MatterCAD is open, so don't share it or paste it into a chat. If you think it has leaked, press **New access token**. This replaces the key and disconnects every tool you set up with the old one. Copy the setup again for each tool you still want to use.

### Claude Code

1. Press **Copy** next to **Claude Code**.
2. Paste the copied command into a terminal and run it. It adds MatterCAD for every folder you use Claude Code in.
3. Start a new Claude Code session, or type `/mcp` in a session that's already running to reconnect.

### Codex

1. Press **Copy** next to **Codex**.
2. Open `~/.codex/config.toml` in a text editor. On Windows, this is `.codex\config.toml` in your user folder. If the file doesn't exist, create it.
3. Paste the copied section at the end of the file and save it.
4. Start a new Codex session.

### Claude Desktop

Claude Desktop connects through a small helper called mcp-remote, which it downloads and runs with Node's `npx`. Install [Node.js](https://nodejs.org) first if you don't have it.

1. Press **Copy** next to **Claude Desktop**.
2. In Claude Desktop, open **Settings**, then **Developer**, then **Edit Config** to find `claude_desktop_config.json`.
3. Paste the copied text into the file and save it:
   - If the file is empty, or has no `mcpServers` section, replace its contents with the copied text.
   - If it already has an `mcpServers` section, copy just the `"mattercad"` entry into it.
4. Quit Claude Desktop completely and open it again.

Don't use Claude Desktop's **Connectors** screen for MatterCAD. It can't reach an app running on your own computer.

## What the AI Can Do

Once connected, the AI can:

- **Read the design** - see the objects in the tab you're looking at, their sizes, and every property you can edit.
- **Measure** - get the size, volume and surface area of objects, check that they are solid, and find the gap between two objects.
- **Take pictures** - look at the design from a named view (front, back, left, right, top, bottom or isometric).
- **Hide and show** - hide objects or show only some of them, the same as the app's own [Hide](../workspace/lock-hide.md). This changes the view only, not the design.
- **Build and change** - create shapes, change their properties (including [expressions](../workspace/expressions.md)), rename, delete, move, rotate and scale them, [combine or subtract](../operations/boolean/index.md) them, make [arrays](../operations/array/index.md), and [group](../workspace/grouping.md) or ungroup them.
- **Edit sheets** - read and write cells in a [Variable Sheet](../workspace/variable-sheet.md), so your design can be driven by named values.
- **Undo and redo** - step back or forward through the design's undo history.
- **Start, open and save designs** - start a new design in a new tab, open a model file in a new tab, and save.
- **Export** - write STL or 3MF files. See [Saving and Exporting](saving-and-exporting.md).
- **Search these help pages** - look up what an operation does before using it.

### What the AI Can't Do

- **Write files outside your chosen folder.** The AI only saves new designs and exports into the folder shown next to **AI can save and export to:** in the panel. It starts as the **MatterCAD AI Exports** folder in your Documents folder; press **Choose...** to pick another.
- **Overwrite a file your design didn't come from.** The AI can save a design back to the file it was opened from, the same as pressing Save. It can't save it over any other file.
- **Run code.** The AI builds designs only from MatterCAD's own shapes and operations.
- **Work while MatterCAD is closed.** MatterCAD must be open, with access turned on.
- **Work in the browser version.** AI assistant access is only in the desktop app.

## Undo and Safety

- **One Undo takes back one AI change.** However many steps the AI took to make a change, they are one "AI: ..." step in your undo history. If any part of a change fails, the AI's whole change is undone and your design is left as it was.
- **The AI works in the tab you're looking at.** If you switch to another tab, the AI is told and has to read the design again before it can change anything. It never edits a tab you've left without knowing. To keep a design safe from the AI, switch to a different tab.
- **Everything stays on your computer.** MatterCAD only accepts connections from your own computer, and only from tools that have your access key. Nothing is sent anywhere.

## The Feedback Log

**Keep a feedback log** is off by default. When it's on, MatterCAD keeps a record on your computer of what the AI tried and where it got stuck. We use these records to find the parts of MatterCAD, and of these help pages, that are hard to understand. Nothing is uploaded.

- **Include pictures** also saves the pictures the AI takes. It can only be turned on while the log is on.
- **Delete log** deletes the records kept so far.
- Turning **Keep a feedback log** off also deletes the log.

## Troubleshooting

### "Port 47813 is in use"

Another program is already using the port MatterCAD listens on. Close that program, or type a different number into **Port** in the panel. When you change the port, copy the setup again for every tool you use, because the old setup still points at the old port.

### My AI tool says it can't connect to MatterCAD

1. Check that MatterCAD is open and that the status bar shows **AI Ready** or **AI Connected**. If there's no AI item, turn on **Allow AI assistants to edit designs**.
2. Reconnect the tool: in Claude Code type `/mcp`, and restart Codex or Claude Desktop.
3. If you pressed **New access token** or changed the port since you set the tool up, copy its setup again and paste it in place of the old one.

### The status bar never leaves AI Ready

MatterCAD hasn't heard from your AI tool yet.

- Make sure you pasted the setup into the right place for your tool, and restarted or reconnected it.
- Ask the tool to do something with MatterCAD, for example "describe the design open in MatterCAD". It only connects when it has something to do.
- For Claude Desktop, check that Node.js is installed.

"AI Connected" changes back to "AI Ready" when the tool has been quiet for a minute. That's normal.

## Related Topics

- [Undo and Redo](../workspace/undo-redo.md)
- [Saving and Exporting](saving-and-exporting.md)
- [Variable Sheet](../workspace/variable-sheet.md)
