---
title: Variable Sheet
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 12
---
# Variable Sheet

The Variable Sheet stores shared values for a design. Use it when several objects should reference the same dimensions, counts, labels, or formulas. Changing a value in the sheet recalculates the dependent objects, so parametric designs stay consistent without editing every object one at a time.

<!-- IMAGE_NEEDED: Replacement hero shot of the current Variable Sheet editor - menu bar, Name and formula boxes, and a grid of named cells with formulas. The image below predates the menu bar. -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## How to Add a Variable Sheet

1. Open the library and add **Variable Sheet** to the scene.
2. Select the Variable Sheet object to show the sheet editor.
3. Select a cell, then enter a **Name** and a value or formula.
4. Use the cell name from other expression-enabled fields in the design.

Objects use the nearest sheet above them in the scene tree, so a sheet dropped inside a group serves that group only. A sheet at the top level serves the whole design.

## The Sheet Editor

The editor appears in the properties panel when the sheet is selected, and it has three parts.

<!-- IMAGE_NEEDED: The sheet editor with the menu bar, the Name box and formula box, and a selected cell in the grid all visible -->

- **The menu bar** - File, Edit and Help. See [Menu Bar](#menu-bar) below.
- **The edit row** - the **Name** box on the left and the formula box beside it, both acting on whichever cell is selected. At the far right is a button that pops the editor out into a window of its own, which is worth doing for anything bigger than a handful of rows.
- **The grid** - column letters across the top, row numbers down the side, and `+` buttons at the right and bottom edges for adding a column or a row. Drag the edge of a column heading to make the column wider.

Click a cell to select it, then type into the formula box to change what it holds. Type into the Name box to give the cell a name.

## Editing Cells

Each cell has two editable parts:

- **Name** - An optional variable name for the cell. Names are case-insensitive, spaces are converted to underscores, and duplicate names are automatically adjusted.
- **Expression** - The cell value. Plain text or numbers are stored directly. Formulas start with `=`.

Cells can also be referenced by address, such as `A1` or `B2`. Named cells are usually clearer for design parameters because they describe intent, such as `wall_thickness`, `outer_diameter`, or `hole_count`.

## Menu Bar

### File

<!-- IMAGE_NEEDED: The sheet editor's File menu open, showing Import CSV... and Download CSV... -->

- **Import CSV...** - Replaces the entire contents of the sheet with a CSV file, as a single undoable step. Fields arrive exactly as they are written in the file, so a field starting with `=` becomes a formula - which means a sheet exported as expressions, or a spreadsheet saved out of Excel, imports as live formulas rather than as text. A ragged file is padded out with empty cells; cell **names** are not part of a CSV and are not restored by an import.
- **Download CSV...** - Writes the sheet out **exactly as it was typed**: a formula is written as its own text (`=A1*3`), not as the number it currently shows, and text cells are written as they stand. Importing that file again restores the sheet, formulas and all, still live - the round trip is the point. Cell **names** and column **widths** are not part of a CSV and are not carried by it.

### Edit

- **Undo** / **Redo** - Step back and forward through sheet edits, including a whole CSV import.
- **Copy Cell** - Puts the selected cell's formula, not its result, on the clipboard.
- **Paste Cell** - Writes the clipboard text into the selected cell.
- **Clear Cell** - Empties the selected cell.
- **Add Row** / **Add Column** - Grow the sheet. The `+` buttons at the edges of the grid do the same thing.

The cell commands need a selected cell; they are greyed out until you click one.

### Help

- **Variable Sheet Help** - Opens this article.

## Formulas

Start a formula with `=` to evaluate it in the sheet:

- `=20 + 5` returns `25`
- `=pi * 10` returns `31.415926535897931`
- `=A1 * 2` references another cell by address
- `=wall_thickness + 4` references a named cell

The sheet supports arithmetic, parentheses, comparisons, the constants `pi`, `tau` and `e`, the bracketed unit constants `[cm]`, `[m]`, `[inch]` and `[ft]`, and the whole function library. See [Expressions](expressions.md) for the syntax and [Expression Functions](expression-functions.md) for the functions.

A cell whose formula references something that does not exist - a misspelled name, a cell past the end of the sheet, or a loop of cells depending on each other - shows `0` rather than a made-up value.

## Using Sheet Values in Objects

Most numeric fields in MatterCAD support expressions. To use a sheet value in an object parameter, prefix the reference with `=`:

- Set a Cube **Width** to `=case_width`.
- Set an Array **Count** to `=hole_count`.
- Set a Translate **Offset** value to `=wall_thickness * 2`.

When the sheet changes, MatterCAD recalculates the objects that depend on it - and only those objects, so a big design stays responsive.

## Text and Data

Variable Sheet cells can hold text as well as numbers. Text values are useful for generated labels, part numbers, imported data, and custom design apps.

Functions worth knowing about here:

- `strcat()` or `concat()` - Join text or values together.
- `substring()` - Extract part of a text value.
- `split()` - Split text and return one item.
- `count()` - Count delimited items in text.
- `substitute()` - Replace text.
- `rand(seed)` - Generate a deterministic random value when a seed is supplied.
- `importdata()` - Read a URL or a local file.
- `index()` - Read a cell whose row is calculated, which is how an arrayed copy reads its own row.
- `xlookup()` - Find the row that holds a value and return another column from it.

Each is described with an example in [Expression Functions](expression-functions.md).

### Driving an Array from a Table

Put a table in the sheet - part numbers down column A, say, with a header in row 1 - and give an object inside an [Array](../operations/array/index.md) an expression that reads a row per copy:

```
=index("A", [index]+2)
```

`[index]` is the copy's position counting from 0, so the first copy reads `A2`, the second `A3`, and so on down the table past the header. Set the Array's **Count** to `=count(...)` or to a cell holding the number of rows and the run resizes with the data.

## Tips

- Prefer descriptive names over cell addresses for values used by other objects.
- Keep core dimensions near the top-left of the sheet so they are easy to find.
- Use formulas for derived values, such as `inner_diameter = outer_diameter - wall_thickness * 2`.
- Avoid using reserved words such as `pi`, `e`, `true`, `false`, or function names as cell names.
- If a formula cannot be parsed, MatterCAD keeps the original input as text.
- Pop the editor out into its own window before working on a large sheet.

## Related

- [Expressions](expressions.md) - Expression syntax, cell references and bracket tokens
- [Expression Functions](expression-functions.md) - Every function, with examples
- [Object References](object-references.md) - Read a value off another object instead of a cell
- [Components](components.md) - Create reusable parameterized designs
- [Array](../operations/array/array.md) - Create repeated patterns driven by sheet values
