---
title: Menus and Toolbar
parent: "Workspace"
nav_order: 19
description: What the MatterCAD menu, the Mac menu bar and the toolbar buttons do, from adding and deleting parts to saving.
keywords: delete, erase, buttons, file menu, main menu, duplicate
---
# Menus and Toolbar

The **☰ MatterCAD** menu at the left end of the tabs holds what belongs to the whole app: adding and opening files, help, updates and settings. The toolbar across the top of a design holds what belongs to that design: adding parts, saving, the bed, undo and the operations.

On a Mac, press ⌘ (Command) wherever this page says Ctrl.

<!-- AUTO_IMAGE: type=shot id=workspace-menus-open -->
![The top of the MatterCAD window with the MatterCAD menu open over a design tab, every item showing, and the toolbar beside it](https://matterhackers.github.io/MatterCAD_Docs/assets/workspace-menus-open.png)

## The ☰ MatterCAD Menu

Click **☰ MatterCAD** at the left end of the tabs. A row with a key shows it at its right, as **Open System File** shows Ctrl+O. The items, from top to bottom:

| Item | What it does |
|------|--------------|
| **Add System File to Bed** | Adds a file from your computer to the design you have open. Its parts land on the bed, in one undo step. It is greyed out while the **Library** or **Help** tab is in front. See [Adding Existing Objects](../getting-started/adding-existing-objects.md) |
| **Open System File** | Opens a file from your computer (Ctrl+O). An MCX design opens in its own tab. Any other file (an STL, a picture, a drawing) opens on the bed of a new design. See [Adding Existing Objects](../getting-started/adding-existing-objects.md) |
| **Open Recent** | Lists the last 10 designs you opened, newest first, each with a small picture. Hover over one to see where it is. Click one to open it again. A design that is already open shows its tab instead of opening twice. When there are none, the list says **No recent files** |
| **Help** | Opens the **Help** tab, the same as pressing F1 |
| **Interface Tour** | Opens the welcome window. Click **Next** there for a short guided tour of the window. See [Updates and Recovery](updates-and-recovery.md#the-welcome-page-and-the-interface-tour) |
| **Check For Update** | Looks for a newer version of MatterCAD. See [Updates and Recovery](updates-and-recovery.md#check-for-update). It isn't in the menu in the browser, where reloading the page gets the newest version, or in a copy of MatterCAD set up not to use the network |
| **Settings** | Opens **MatterCAD Settings**. See [Settings](settings.md) |
| **Community** › **Guides and Articles** | Opens MatterHackers' MatterCAD guides and articles in your web browser |
| **About MatterCAD** | Shows the version you have. See [Updates and Recovery](updates-and-recovery.md#about-mattercad) |

### When a recent design is gone

If you pick a design in **Open Recent** that has been moved or deleted, MatterCAD tells you it no longer exists where it was and asks whether to take it off the list. Click **Remove from Recent** to remove it, or **Cancel** to keep it.

A design from your [Cloud Library](../library/cloud-library.md) that has been deleted or moved shows **Cloud Item Not Found** with the same choice. If MatterCAD can't reach the cloud at that moment, it says so and keeps the design on the list.

## The Mac Menu Bar

On a Mac, the same items are also in the menu bar at the top of the screen, and **File** adds **Save**, **Save As** and **Share...**, which the ☰ MatterCAD menu leaves to the toolbar. An item with a key shows it:

- **MatterCAD** - **About MatterCAD**, **Settings** (⌘,), **Check For Update** and **Quit** (⌘Q).
- **File** - **Add System File to Bed**, **Open System File** (⌘O), **Open Recent**, **Save** (⌘S), **Save As** (⇧⌘S) and **Share...**. **Save** and **Save As** work on the design in front, as the toolbar's do. **Share...** opens the Share dialog for the design in front; it is greyed out unless that design is saved in your Cloud Library. See [Sharing](../library/sharing.md).
- **Help** - **Help** (F1), **Interface Tour** and **Community**.

The first time MatterCAD starts, these items stay greyed out until you accept the license agreement. **Quit** always works.

## The Toolbar

The toolbar runs across the top of each design tab. When the window is too narrow for every button, the toolbar wraps onto more rows. From the left:

- **Add to Bed**, **Save** and **Bed** (below). Between **Save** and **Bed**, a **Share** button opens the Share dialog for the design; it is only there while the design is saved in your Cloud Library. See [Sharing](../library/sharing.md).
- **Undo** and **Redo**. Hover over one to see the step it takes back or does again, for example "Undo - Move". See [Undo and Redo](undo-redo.md).
- Buttons that work on the selected parts: **Arrange All Parts**, **Lay Flat**, **Rebuild**, **Group**, **Ungroup**, **Convert to Nodes**, **Duplicate** and **Remove**.
- The operation groups: **Transform**, **Placement**, **Round & Offset**, **Deform**, **Image**, **Path**, **Merge**, **Duplication**, **Mesh** and **Constraints**.
- **My Tools**, the operation tools you saved yourself, when you have any.
- **Tools**, at the end (below).

Hover over any button to see its name, with its key when it has one, for example "Group (G)". A greyed-out button can't be used on what is selected; hover over it to see what it needs. While you hover, the status bar at the bottom of the window shows a hint for the button, such as its shortcut.

### Add to Bed

Click **Add to Bed** to open the library over the left side of the design. Drag a part or a file from it onto the bed. Click **Add to Bed** again, or click outside the library, to close it. See [Adding Existing Objects](../getting-started/adding-existing-objects.md#add-to-bed).

To pick a file on your computer instead, choose **Add System File to Bed** in the **☰ MatterCAD** menu (above).

### Save

- Click **Save** to save the design (Ctrl+S). The button reads **Save •** while the design has changes you have not saved.
- Click the arrow beside it for **Save As** (Ctrl+Shift+S) and **Export**, and **Share...** when the design is saved in your Cloud Library. A design saved only on your computer has no **Share...** row. See [Sharing](../library/sharing.md).

See [Saving and Exporting](../getting-started/saving-and-exporting.md) for what each one does.

### Bed

Click **Bed** for a menu of things you do to the whole design:

| Item | What it does |
|------|--------------|
| **Export** | Writes the design in another format, such as STL or 3MF. See [Saving and Exporting](../getting-started/saving-and-exporting.md#export-to-another-format) |
| **Cut** (Ctrl+X), **Copy** (Ctrl+C), **Paste** (Ctrl+V) | Work on the selected parts |
| **Reload** | Throws away your changes and opens the design again as you last saved it. If you have unsaved changes, MatterCAD asks first: click **Yes** to reload or **No** to keep working. It is greyed out while the design has no file to go back to, such as a new design you have not saved yet |
| **Clear Bed** | Deletes the parts on the bed. Undo brings them back |

### Tools and the Operation Groups

Each operation group shows its operations as a row of buttons, with a small **Collapse** button at its end. Click it to fold the group into one button that runs the group's last-used operation. Its arrow lists every operation in the group, and **Expand** to open the group out again.

Click **Tools** at the end of the toolbar (or right-click anywhere on the toolbar) to open **Design Tools**, where you choose how each group is shown:

- Each group has a row with **Collapse**, **Expand** and **Hide**. The highlighted one is how the group is shown now. **Hide** takes the group off the toolbar.
- **Collapse All**, **Expand All** and **Hide All**, at the top, set every group at once.

The panel stays open while you work in it, so you can set several groups in one visit. Click outside it to close it. MatterCAD remembers your choices for every design and the next time you start it. To get a hidden group back, open **Tools** and click **Expand** or **Collapse** on its row.

## Related

- [Camera Controls](camera-controls.md) - The cube and buttons in the corner of the 3D view
- [Tabs, Search and the Status Bar](tabs-and-search.md) - The tab strip, help search and the bar at the bottom of the window
- [Keyboard Shortcuts](keyboard-shortcuts.md) - Every shortcut
