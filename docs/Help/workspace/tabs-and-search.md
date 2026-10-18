---
title: Tabs, Search and the Status Bar
parent: "Workspace"
nav_order: 21
---
# Tabs, Search and the Status Bar

The tabs along the top of the window hold the **Store**, the **Library**, **Help** and every design you have open. At the right end of the tab bar are the help search button and your account. The status bar along the bottom of the window shows hints, running tasks and your connection.

On a Mac, press ⌘ (Command) wherever this page says Ctrl.

<!-- IMAGE_NEEDED: The full width of the tab bar: the ☰ MatterCAD menu, the Store, Library and Help tabs, two design tabs (one with its cube icon tinted and underlined for unsaved changes), the + button, and at the right the search button and (sign in) -->

## The Tabs

From the left, after the **☰ MatterCAD** menu:

- **Store** - Featured products and articles from MatterHackers.
- **Library** - Your designs, the built-in shapes and sample parts, and your [Cloud Library](../library/cloud-library.md). See [Library](../library/index.md).
- **Help** - These help pages. It opens when you press F1, choose **Help** in the **☰ MatterCAD** menu, or open help from anywhere else in the app. Close it with its **X** when you are done.
- **Design tabs** - One for each design you have open, with a small cube icon and the design's name. Hover over a design tab to see where its file is.
- **+** (**Create New Design**) - Opens a new design on an empty bed, in a tab named **New Design**.

The **Store** and **Library** tabs are always there. When there are more tabs than fit, the design tabs (and the Store and Library tabs) get narrower and their names are shortened, so every tab stays in reach.

### Unsaved changes

While a design has changes you have not saved, the cube icon on its tab is tinted and underlined in the highlight color. The **Save** button in its toolbar reads **Save •** at the same time.

### Opening, closing and reordering

- **Open a new design** - Click **+**, or press Ctrl+T while a design is showing.
- **Close a design** - Click the **X** on its tab. If it has unsaved changes, MatterCAD asks "Would you like to save changes before closing?" Click **Save Changes**, **Discard Changes**, or **Cancel** to keep it open.
- **Reopen the design you closed last** - Press Ctrl+Shift+T. This works for designs that were saved to a file.
- **Reorder** - Drag a design tab left or right. Design tabs stay to the right of the Store, Library and Help tabs.
- **Open files** - Drag files from your computer onto the tab bar. While you hover there, the status bar says "You can drag and drop .mcx files here to open them". An MCX design opens in its own tab, and any other model or picture opens on the bed of a new design, the same as **Open System File**.

When you quit MatterCAD with unsaved designs, it asks once for all of them, for example "You have 2 unsaved designs. Would you like to save changes before closing?"

The next time you start MatterCAD, the tabs you had open come back, with the tab you were looking at in front. See [Updates and Recovery](updates-and-recovery.md#your-tabs-come-back).

### The design tab's menu

Right-click a design tab for:

| Item | What it does |
|------|--------------|
| **Rename** | Opens **Rename Item**. Type the new name and click **Rename**. For a saved design, the file is renamed too, in the same folder |
| **Reload** | Throws away your changes and opens the design again as you last saved it, after asking. See [Menus and Toolbar](menus-and-toolbar.md#bed) |
| **Show in Explorer** (Windows), **Show in Finder** (Mac), **Show in Files** (Linux) | Opens the folder the design's file is in, with the file selected. Only for designs saved as files on your computer |

## Search

The **Search** button (the magnifying glass) at the right end of the tab bar searches these help pages.

1. Click **Search**. A search box opens under it, ready for you to type.
2. Type what you are looking for and press Enter. MatterCAD shows **Searching...**, then the help pages that match, or **No results found**.
3. Click a result to open that page in the **Help** tab, with your search words highlighted.

Click **Search** again, or click somewhere else, to close the box. The **Clear** button in the box empties it. The first time you search after starting MatterCAD, the button may show **Preparing help...** for a moment while it gets the help pages ready.

Search finds help pages, not parts. To find a part in the library, use the search box in the **Library**.

## Your Account

**(sign in)**, at the far right of the tab bar, signs you in to your account. Once you are signed in, it shows your name and opens a menu. See [Signing In](account.md).

## The Status Bar

The bar along the bottom of the window shows, from left to right:

- **Running tasks** - Anything MatterCAD is working on, such as saving a design, with a small progress bar under its name.
- **Hints** - What the button or control under the mouse does, or the keys that do the same thing. For example, hover over **Reset View** to see "W Key".
- **The theme button** - Opens the **Theme** settings in a small panel, so you can change the colors without opening Settings. See [Settings](settings.md#theme).
- **The AI item** - Shows **AI Ready**, **AI Connected** or **AI Editing** while AI assistant access is on, and is hidden while it is off. Click it to open **AI Assistant Access**. See [Using AI Assistants](../getting-started/ai-assistants.md).
- **The globe** - Your connection to MatterCAD's online services. It reads **Connected** while you are signed in and online, **Disconnected** while you are signed out or offline, and **Retry Login** when your sign-in has run out and you need to [sign in](account.md) again. Hover over it to see, for example, "Services: Connected". Click it and choose **AI Assistant Access...** to open the AI assistant panel, whether or not you are signed in.

## Related

- [Menus and Toolbar](menus-and-toolbar.md) - The ☰ MatterCAD menu and the toolbar
- [Signing In](account.md) - Your account, sign in and sign out
- [Saving and Exporting](../getting-started/saving-and-exporting.md) - Save your work
- [Keyboard Shortcuts](keyboard-shortcuts.md) - Every shortcut
