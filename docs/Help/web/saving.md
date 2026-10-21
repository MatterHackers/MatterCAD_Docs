---
title: Saving on the Web
parent: "MatterCAD on the Web"
nav_order: 2
description: Save your design to your online library from the website, download it, or get back unsaved changes.
keywords: save online, download, web save, browser save, save in browser
---
# Saving on the Web

On the website, **Save** keeps your design in your online library, the same library you see on the website's **Library** page and in MatterCAD's Cloud Library on your computer. To get a file on your computer, use **Export** or the page's **Download** button.

## Save

Click **Save** in the toolbar, or press Ctrl+S (⌘S on a Mac). The button reads **Save •** while the design has changes that are not saved.

- **A design you can change** is saved over its own copy in your library.
- **A design you can't save over** (one that isn't yours, or one that isn't an MCX design, such as an STL) is never written over. Save opens **Save As** instead, to save your own copy as a new MCX design.
- **A new design** asks where to save it the first time you save it.

When Save can't save in place, the [Save As](#save-as) box opens with the design's name filled in. Choose a folder and a name there. From then on **Save** saves that new design.

If the website refuses to save over a design, the **Save As** box opens with the reason above the list: "You can't save over this design. Choose a folder and a name to save your own copy." When your sign-in may have expired, the line starts "Your sign-in has expired, or you can't save over this design."

## Save As

Click the arrow beside **Save** and choose **Save As**, or press Ctrl+Shift+S (⌘⇧S on a Mac). The **Save As** box, headed "Choose where to save your design", shows your online library, so you choose the folder the copy goes in:

1. Pick a folder. The box opens in the folder named in the page's address: the folder you opened the design from on the **Library** page. When you opened the design from a direct link that names no folder, the box opens in **My Designs**. For a new design, it opens in the folder you clicked **New Design** in on the **Library** page, or, after **New Design** in the MatterCAD menu, in the folder of the design you had open. When the design isn't in your own library (it came from **Shared with Me** or **Purchased**), the box opens in **My Designs**.
2. Type a name under **Design Name**. Clicking a design or a part in the list puts its name there, without the extension (for example "Bracket"). The design always saves as an MCX design.
3. Click **Save**.

In the box:

- **The path along the top** shows where you are. Click a folder in it to go back to that folder. Double-click a folder in the list to open it. Double-clicking a design is the same as clicking it and then **Save**.
- **Create Folder** makes a new folder in the folder you are in. Type its name under **Folder Name** and click **Create**.
- **Only My Designs is listed.** Designs can't be saved in **Shared with Me** or **Purchased**, so they aren't there. While no folder that can take a design is open, the box says "Choose a folder you can save in." and **Save** can't be clicked.
- **There is no Computer folder.** A web page can't save to your computer: to get a file there, use [Export or Download](#export-and-download).

### Saving over a design

When the folder already has a design with that name, MatterCAD asks first, in a box titled **Confirm Save As**, for example:

> "Bracket" already exists. Do you want to replace it?

- **Replace** - Saves your design over that one.
- **Cancel** - Goes back to the **Save As** box to choose another name or folder.

You can replace only your own designs. If the design there isn't yours, or is locked, the **Save As** box opens again and says so above the list, for example:

> You can't replace "Bracket". Choose another name or folder.

### After Save As

The page now shows the design you saved: its address, title and **Download** button change to it, and the address names the folder it is in. **Save** saves that design from then on.

## Export and Download

- **Export** (in the **Save** arrow's menu, and in the **Bed** menu) writes the design in another format, such as STL or 3MF. Your browser downloads each file it writes. See [Saving and Exporting](../getting-started/saving-and-exporting.md#export-to-another-format) for the formats and options.
- **Download**, in the page's title bar, downloads the design's file as it was last saved.

## Unsaved Changes Found

While you edit, MatterCAD keeps a copy of your unsaved changes in this browser every few seconds. If the tab closes, the browser crashes or your phone drops the page before you save, your changes are not lost.

The next time you open the same design's page in this browser, MatterCAD asks, in a box titled **Unsaved Changes Found**: "MatterCAD found changes to this design that weren't saved. Restore them?"

- **Restore** - Puts your changes back and opens the editor. They are still not saved: click **Save** to keep them. **Discard Changes** (when you press **Done**) still takes you back to the saved version.
- **Discard** - Throws the copy away.

If you close the box without choosing, the copy is kept and offered again next time.

For a new design you never saved, the copy belongs to its folder: on the website's **Library** page, open the same folder and click **New Design** to be offered it.

Good to know:

- The copy is kept only in the browser you were using, on that computer or phone.
- If the design has been saved since the copy was made (here, in another browser or in MatterCAD on your computer), the copy is older than the saved design, so it is thrown away without asking.
- A browser keeps only a few megabytes for a website. A design larger than about 3.5 MB is too big to keep a copy of, so save it often.
- Saving the design, choosing **Discard Changes**, or undoing back to the saved version removes the copy.

## Related

- [MatterCAD on the Web](index.md) - Preview, Edit and Done
- [The MatterCAD Menu](mattercad-menu.md) - Start a new design
- [Cloud Library](../library/cloud-library.md) - Your designs online
