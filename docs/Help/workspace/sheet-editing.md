---
title: Editing a Variable Sheet
parent: "Workspace"
nav_order: 13
---
# Editing a Variable Sheet

This page covers the mechanics of the [Variable Sheet](variable-sheet.md) editor: changing the shape of the sheet, sizing its columns and rows, formatting what a cell shows, and moving a sheet in and out as CSV. For what a sheet is and how its values are written and read, start at [Variable Sheet](variable-sheet.md).

Every edit on this page is a single Undo step - the only exception is **Refresh Imported Data**, which changes nothing you authored. The sheet shares the design's undo history, so **Ctrl+Z** in the workspace steps back through sheet edits along with everything else. See [Undo and Redo](undo-redo.md).

## Moving Around the Grid

<!-- IMAGE_NEEDED: The sheet grid with one cell selected and its editor open, showing the highlighted selection border -->

| Key | What it does |
| --- | --- |
| Arrow keys | Move the selection one cell |
| Shift+Arrow | Take the selection out to a rectangle of cells |
| Arrow keys, while editing | Move the caret through the cell's text |
| Tab / Shift+Tab | Move to the next or previous cell |
| Enter or F2 | Start editing the selected cell |
| Enter, while editing | Finish the edit and move down |
| Tab, while editing | Finish the edit and move across |
| Escape, while editing | Abandon the edit and keep what was there |
| Delete or Backspace | Empty every selected cell, as one Undo step |
| Any other character | Start editing, replacing what the cell held - as in a spreadsheet |

**Shift+click a second cell** to select the rectangle between it and the cell you clicked plainly, and every cell in it is shaded to show it: click B2, Shift+click D4, and the nine cells from B2 to D4 are all selected. **Shift+Arrow** does the same thing a cell at a time. The range is always measured from the cell you clicked plainly, so a further Shift+click moves its far end rather than starting from where the range currently begins. A **plain click**, or a plain arrow key, drops back to that one cell.

The formula bar, the name box and the **Format** menu go on acting on the **active** cell - the one you took the selection out to, which carries the accent border. **Copy**, **Paste**, **Clear** and **Delete** act on the whole range.

## Rows and Columns

There are three ways to change the shape of a sheet, and they run the same commands.

### The Headers

**Click a column letter or a row number** to select that whole column or row - the header lights up to show it - and **right-click** one for the menu of commands that act on it. A right-click selects the header as well, so the menu always acts on the line you can see is selected. **Escape** clears a header selection.

**Shift+click a second header of the same kind** to select the range between the two, and every header in it lights up: click column B, Shift+click column E, and B, C, D and E are all selected. The range is always measured from the header you clicked plainly, so a further Shift+click moves its far end rather than starting from where the range currently begins. Shift+clicking the *other* kind of header - a row number while columns are selected - is treated as a plain click and starts again there, as an ordinary click anywhere does. A right-click starts again too, on the header it lands on, which is why a header menu always acts on that one line even when it is opened inside a range. The commands that act on a range as a whole are the **Insert** menu's and the keyboard chords.

<!-- IMAGE_NEEDED: The sheet editor with a right-click menu open on column header B, showing Auto-size Column, Insert Column Left, Insert Column Right, Remove Column and Add Column -->

Right-clicking a **column letter** offers:

- **Auto-size Column** - Fit the column to the widest value in it.
- **Insert Column Left** / **Insert Column Right** - Add a blank column beside this one.
- **Remove Column** - Take this column away, moving the columns right of it left.
- **Add Column** - Append a column at the right-hand end of the sheet.

Right-clicking a **row number** offers:

- **Auto-fit Row** - Fit the row to the tallest value in it.
- **Insert Row Above** / **Insert Row Below** - Add a blank row beside this one.
- **Remove Row** - Take this row away, moving the rows below it up.
- **Add Row** - Append a row at the bottom of the sheet.

A sheet must keep at least one row and one column, so **Remove Row** and **Remove Column** are greyed out once it is down to its last one.

### The Insert Menu

The menu bar's **Insert** menu holds the same commands, and they act on whatever is **selected**: the row and column of a selected cell, or the lines a selected header names. A selected column header names no row, so the row entries are greyed out while it is selected, and the other way about. With nothing selected there is nothing for them to act on, so every entry but **Add Row** and **Add Column** is greyed out.

A range of headers is acted on **as a whole, in one step**. With columns B through D selected, **Insert Column Left** puts three blank columns in and records a single Undo entry named for what it did, *Insert 3 Columns*; **Remove Column** takes all three away as *Remove 3 Columns*, and two selected rows removed are *Remove 2 Rows*. **Insert Column Left** and **Insert Row Above** go in before the **first** line of the range, **Insert Column Right** and **Insert Row Below** after the **last**. A removal that would take every row or every column of the sheet is refused, so **Remove Row** and **Remove Column** are greyed out for a range covering the lot, just as they are for the sheet's last line.

The two `+` buttons at the right and bottom edges of the grid are **Add Column** and **Add Row** under another name.

### Keyboard

Two chords insert and remove a line, and **what they act on is what is selected**: a selected cell spends them on its row, a selected column header on that column, a selected row header on that row.

| Chord | With a cell or a row header selected | With a column header selected |
| --- | --- | --- |
| Ctrl + Shift + '+', or Ctrl + numpad '+' | Insert Row Above | Insert Column Left |
| Ctrl + '-', or Ctrl + numpad '-' | Remove Row | Remove Column |

On a Mac, use Cmd in place of Ctrl.

The chords work while a cell or header is *selected*, not while a cell is being edited - press Escape or Enter to finish an edit first. A removal the sheet would refuse - its last row or column, or a range covering every one of them - does nothing, the same thing the greyed menu entry says.

A range of headers takes the chords as a whole, in one Undo step, exactly as the **Insert** menu does: three row headers selected and the insert chord adds three blank rows as *Insert 3 Rows*, and the remove chord takes all three away as *Remove 3 Rows*. After an insert the new blank lines are the ones left selected, so pressing the chord again inserts another set the same size; after a removal the line that took their place is selected on its own.

### What Happens to Your Formulas

A structural edit moves cells, and every reference to a moved cell is rewritten so it still points at the same value. That covers formulas **in the sheet** and formulas **in every object that reads this sheet** - an object whose Width is `=B2` follows B2 to C2 when a column is inserted to its left.

Three things are worth knowing:

- **A reference to a cell that was removed becomes `#REF!`.** It does not slide onto the neighbour that took the removed cell's place, because that would silently point the formula at a different value. `=A1+1` becomes `=#REF!+1`, and the cell shows `#REF!+1` - the stored formula without its leading `=` - instead of a number. A sheet cell reading the broken one falls back to `0`; an object parameter reading it keeps an error value, `0.1` for a decimal parameter and `1` for a whole-number one, so the shape it drives comes out visibly wrong rather than plausibly wrong. Either way nothing is invented, and the formula says exactly what went wrong.
- **Cell names travel with their cells** and are never rewritten. A cell named `wall_thickness` keeps that name wherever the edit moves it, so `=wall_thickness` never needs touching.
- **The whole thing is one Undo step** - the insertion or removal, the cells that moved, and every formula that was rewritten in the sheet and in the design. One Undo puts all of it back exactly as it was. A range is one step too, however many lines it covers: *Remove 3 Columns* is a single entry, and one Undo brings all three columns and every formula they touched back together.

## Column Widths and Row Heights

<!-- IMAGE_NEEDED: Close-up of the separator between two column headers with the horizontal resize cursor showing -->

- **Drag the separator** between two column letters to set a column's width by hand.
- **Double-click the separator** to size the column to the widest value it is currently showing - the same thing **Auto-size Column** does from the column's header menu.

<!-- IMAGE_NEEDED: Close-up of the bottom edge of a row number with the vertical resize cursor showing, beside a row holding a wrapped multi-line value -->

Rows work the same way, on the bottom edge of the row number:

- **Drag the bottom edge of a row number** to set that row's height by hand, as one *Resize Row* Undo step.
- **Double-click that edge**, or pick **Auto-fit Row** from the row's header menu, to fit the row to the tallest value it is showing, as one *Auto-fit Row* step. A row whose values are all single lines fits back to the standard height - dragging is the only thing that takes a row below that.

Each of these is undoable, and a drag counts as one step no matter how far you moved the pointer.

Auto-size and auto-fit measure what the column or row **displays**, so a cell showing a formula's result is measured by the result. Column widths and row heights belong to the sheet and are saved with the design, but they are not part of a CSV. A height belongs to the row itself rather than to the row number, so it travels with that row through inserts, removals and their undo; and because a CSV import replaces the values rather than the shape of the grid, it keeps the heights of the rows it covers - a row the file adds arrives at the standard height, the way a new column arrives at the default width.

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
- **Copy** - Puts the selected cells on the clipboard **as they were typed**, formulas rather than results. One cell copies as its bare formula; a range copies as tab separated text, which pastes into Excel, Google Sheets or anything else that speaks a spreadsheet's clipboard.
- **Paste** - Writes the clipboard in starting at the **top left of the selection**, however many cells are selected - a spreadsheet pastes what was copied, not what will fit. A block running past the right or bottom edge **grows the sheet** to hold it, and the whole paste, growth included, is one Undo step named *Paste Cells*. A single value with no tabs or line breaks in it pastes as an ordinary cell edit into the top left cell.
- **Clear** - Empties every selected cell, as one Undo step.

The cell commands need a selected cell; they are greyed out until you click one.

Anything pasted in becomes a cell's text exactly as it reads, so a field starting with `=` arrives as a **live formula** - the same caveat as [Import CSV...](#import-csv), and the same reason to be careful with a block copied from a source you do not trust.

### Pasting Formulas

When you paste cells you copied from a MatterCAD sheet, their **cell references move with the block**, the way a spreadsheet's relative references do. Copy `=A1*2` out of B1, paste it at B3, and it reads `=A3*2` - it went down two rows, so the cell it reads went down two rows with it, and the formula still means "twice the cell two above me".

Three things never move:

- **Cell names.** `=wall_thickness` means the same cell wherever the formula lands, which is the whole point of naming a cell - the same rule the structural edits follow, in [What Happens to Your Formulas](#what-happens-to-your-formulas).
- **Quoted text**, including the quoted column names `index()` and `xlookup()` take.
- **Object references** such as `=Bracket.Width`, which name a part of your design rather than a cell of the sheet.

A reference that the move would carry **above the first row or left of column A** has no cell left to name, and becomes `#REF!`. Copy `=A1*2` from B2 and paste it at B1 and you get `=#REF!*2`: a visibly broken formula, rather than one quietly reading somewhere you did not mean. Running off the **right or bottom** is not an error, because a sheet grows in those directions.

Text copied out of **another program**, or typed by hand, pastes **exactly as written** - MatterCAD did not write it, so it has no idea where the formulas in it came from and adjusts nothing.

## The Help Menu

- **Variable Sheet Help** - Opens the [Variable Sheet](variable-sheet.md) article.

## Related

- [Variable Sheet](variable-sheet.md) - What a sheet is for, and naming its cells
- [Expressions](expressions.md) - Expression syntax, cell references and units
- [Expression Functions](expression-functions.md) - Every function, with examples
- [Undo and Redo](undo-redo.md) - How the design's undo history works
- [Keyboard Shortcuts](keyboard-shortcuts.md) - Shortcuts across the rest of the app
