---
title: Editing a Variable Sheet
parent: "Workspace"
nav_order: 13
---
# Editing a Variable Sheet

This page covers the mechanics of the [Variable Sheet](variable-sheet.md) editor: changing the shape of the sheet, sizing its columns, formatting what a cell shows, and moving a sheet in and out as CSV. For what a sheet is and how its values are written and read, start at [Variable Sheet](variable-sheet.md).

Every edit on this page is a single Undo step - the only exception is **Refresh Imported Data**, which changes nothing you authored. The sheet shares the design's undo history, so **Ctrl+Z** in the workspace steps back through sheet edits along with everything else. See [Undo and Redo](undo-redo.md).

## Moving Around the Grid

<!-- IMAGE_NEEDED: The sheet grid with one cell selected and its editor open, showing the highlighted selection border -->

| Key | What it does |
| --- | --- |
| Arrow keys | Move the selection one cell |
| Arrow keys, while editing | Move the caret through the cell's text |
| Tab / Shift+Tab | Move to the next or previous cell |
| Enter or F2 | Start editing the selected cell |
| Enter, while editing | Finish the edit and move down |
| Tab, while editing | Finish the edit and move across |
| Escape, while editing | Abandon the edit and keep what was there |
| Delete or Backspace | Empty the selected cell |
| Any other character | Start editing, replacing what the cell held - as in a spreadsheet |

## Rows and Columns

There are three ways to change the shape of a sheet, and they run the same commands.

### The Headers

**Click a column letter or a row number** to select that whole column or row - the header lights up to show it - and **right-click** one for the menu of commands that act on it. A right-click selects the header as well, so the menu always acts on the line you can see is selected. **Escape** clears a header selection.

<!-- IMAGE_NEEDED: The sheet editor with a right-click menu open on column header B, showing Auto-size Column, Insert Column Left, Insert Column Right, Remove Column and Add Column -->

Right-clicking a **column letter** offers:

- **Auto-size Column** - Fit the column to the widest value in it.
- **Insert Column Left** / **Insert Column Right** - Add a blank column beside this one.
- **Remove Column** - Take this column away, moving the columns right of it left.
- **Add Column** - Append a column at the right-hand end of the sheet.

Right-clicking a **row number** offers:

- **Insert Row Above** / **Insert Row Below** - Add a blank row beside this one.
- **Remove Row** - Take this row away, moving the rows below it up.
- **Add Row** - Append a row at the bottom of the sheet.

A sheet must keep at least one row and one column, so **Remove Row** and **Remove Column** are greyed out once it is down to its last one.

### The Insert Menu

The menu bar's **Insert** menu holds the same commands, and they act on whatever is **selected**: the row and column of a selected cell, or the one line a selected header names. A selected column header names no row, so the row entries are greyed out while it is selected, and the other way about. With nothing selected there is nothing for them to act on, so every entry but **Add Row** and **Add Column** is greyed out.

The two `+` buttons at the right and bottom edges of the grid are **Add Column** and **Add Row** under another name.

### Keyboard

Two chords insert and remove a line, and **what they act on is what is selected**: a selected cell spends them on its row, a selected column header on that column, a selected row header on that row.

| Chord | With a cell or a row header selected | With a column header selected |
| --- | --- | --- |
| Ctrl + Shift + '+', or Ctrl + numpad '+' | Insert Row Above | Insert Column Left |
| Ctrl + '-', or Ctrl + numpad '-' | Remove Row | Remove Column |

On a Mac, use Cmd in place of Ctrl.

The chords work while a cell or header is *selected*, not while a cell is being edited - press Escape or Enter to finish an edit first. An insert from a header leaves the new blank line selected, so pressing the chord again inserts another one. A removal the sheet would refuse - its last row or column - does nothing, the same thing the greyed menu entry says.

### What Happens to Your Formulas

A structural edit moves cells, and every reference to a moved cell is rewritten so it still points at the same value. That covers formulas **in the sheet** and formulas **in every object that reads this sheet** - an object whose Width is `=B2` follows B2 to C2 when a column is inserted to its left.

Three things are worth knowing:

- **A reference to a cell that was removed becomes `#REF!`.** It does not slide onto the neighbour that took the removed cell's place, because that would silently point the formula at a different value. `=A1+1` becomes `=#REF!+1`, and the cell shows `#REF!+1` - the stored formula without its leading `=` - instead of a number. A sheet cell reading the broken one falls back to `0`; an object parameter reading it keeps an error value, `0.1` for a decimal parameter and `1` for a whole-number one, so the shape it drives comes out visibly wrong rather than plausibly wrong. Either way nothing is invented, and the formula says exactly what went wrong.
- **Cell names travel with their cells** and are never rewritten. A cell named `wall_thickness` keeps that name wherever the edit moves it, so `=wall_thickness` never needs touching.
- **The whole thing is one Undo step** - the insertion or removal, the cells that moved, and every formula that was rewritten in the sheet and in the design. One Undo puts all of it back exactly as it was.

## Column Widths

<!-- IMAGE_NEEDED: Close-up of the separator between two column headers with the horizontal resize cursor showing -->

- **Drag the separator** between two column letters to set a column's width by hand.
- **Double-click the separator** to size the column to the widest value it is currently showing - the same thing **Auto-size Column** does from the column's header menu.

Both are undoable, and a drag counts as one step no matter how far you moved the pointer.

Auto-size measures what the column **displays**, so a cell showing a formula's result is measured by the result. Column widths belong to the sheet and are saved with the design, but they are not part of a CSV.

## Formatting Cells

The **Format** menu changes how the **selected** cell is shown. It never changes what the cell is worth, so nothing downstream of it recalculates.

<!-- IMAGE_NEEDED: The Format menu open with the Decimal Places submenu showing Auto, 0, 1, 2, 3, 4 and a bullet beside the current choice -->

- **Decimal Places** - **Auto**, or `0` to `4`. Auto is what every cell starts on and means "however many the value has".
- **Alignment** - **Left**, **Center** or **Right**.
- **Bold** - Show the cell's value in bold.

The choice the cell is already on is marked with a bullet in front of it. Each pick is one Undo step. The **Format** menu itself still opens with nothing selected; its entries are greyed out until you click a cell.

Decimal places only apply to a value that reads as a **number**. Text, and an error marker such as `#REF!`, are shown as they are - there is nothing in them to round. And because the setting is about display only, `=A1/3` set to two places still feeds its full value to whatever reads that cell.

## The File Menu

<!-- IMAGE_NEEDED: The sheet editor's File menu open, showing Import CSV..., Download CSV... and Refresh Imported Data -->

### Import CSV...

Replaces what every cell in the sheet holds with the fields of a CSV file, resizing the sheet to fit, as a single undoable step.

Fields arrive **exactly as they are written in the file**, so a field starting with `=` becomes a formula - which means a sheet exported as expressions, or a spreadsheet saved out of Excel, imports as live formulas rather than as text. Quoting is honoured, so a quoted field carrying commas or newlines arrives as the one field it was written as, and a ragged file is padded out with empty cells.

A CSV carries no cell **names**, no cell **formats** and no column **widths**, so an import keeps the ones the sheet already has - **by position**. The cell in column B, row 3 keeps its name, its decimal places and its alignment, and only what it holds is written over. Column widths are kept the same way, and a column the file adds arrives at the default width.

Rows and columns past the end of the file are **dropped**, and the names on those cells go with them. Nothing is rewritten to `#REF!` for them - an import replaces the sheet wholesale, and one Undo puts every dropped cell back - so a formula that read a dropped name falls back to `0` until the sheet gives the name back or you rewrite the formula.

Because an imported field can be a formula, importing a CSV from a source you do not trust runs whatever that file says to run - including `=importdata("...")`, which reads a file or a URL every time the sheet recalculates.

### Download CSV...

Writes the sheet out **exactly as it was typed**: a formula is written as its own text (`=A1*3`), not as the number it currently shows, and text cells are written as they stand. Importing that file again restores the sheet, formulas and all, still live - the round trip is the point.

The file is named after the sheet object, so a design holding several sheets does not download them all over the top of each other. A sheet with no name of its own downloads as `sheet.csv`.

### Refresh Imported Data

`importdata()` reads a file or a URL once and keeps the answer for the rest of the session, so a design full of imports does not hammer the network every time something rebuilds. **Refresh Imported Data** throws that cache away and recalculates, which is the only way to pick up a source that has changed since MatterCAD started.

Nothing you authored changes, so this is not an undoable step. A sheet importing several slow or unreachable URLs takes as long to refresh as those all take to answer.

## The Edit Menu

- **Undo** / **Redo** - Step back and forward through sheet edits, including a whole CSV import.
- **Copy Cell** - Puts the selected cell's formula, not its result, on the clipboard.
- **Paste Cell** - Writes the clipboard text into the selected cell.
- **Clear Cell** - Empties the selected cell.

The cell commands need a selected cell; they are greyed out until you click one.

## The Help Menu

- **Variable Sheet Help** - Opens the [Variable Sheet](variable-sheet.md) article.

## Related

- [Variable Sheet](variable-sheet.md) - What a sheet is for, and naming its cells
- [Expressions](expressions.md) - Expression syntax, cell references and units
- [Expression Functions](expression-functions.md) - Every function, with examples
- [Undo and Redo](undo-redo.md) - How the design's undo history works
- [Keyboard Shortcuts](keyboard-shortcuts.md) - Shortcuts across the rest of the app
