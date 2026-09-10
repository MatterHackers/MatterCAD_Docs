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

This page covers what a sheet is for and how its values are written and read. For the mechanics of the editor itself - adding and removing rows and columns, column widths, cell formatting and CSV - see [Editing a Variable Sheet](sheet-editing.md).

## How to Add a Variable Sheet

1. Open the library and add **Variable Sheet** to the scene.
2. Select the Variable Sheet object to show the sheet editor.
3. Select a cell, then enter a **Name** and a value or formula.
4. Use the cell name from other expression-enabled fields in the design.

Objects use the nearest sheet above them in the scene tree, so a sheet dropped inside a group serves that group only. A sheet at the top level serves the whole design.

## The Sheet Editor

The editor appears in the properties panel when the sheet is selected.

<!-- IMAGE_NEEDED: The sheet editor with the menu bar, the Name box and formula box, the units line, and a selected cell in the grid all visible -->

- **The menu bar** - File, Edit, Insert, Format and Help. See [Editing a Variable Sheet](sheet-editing.md) for what each one does.
- **The edit row** - the **Name** box on the left and the formula box beside it, both acting on whichever cell is selected. At the far right is a button that pops the editor out into a window of its own, which is worth doing for anything bigger than a handful of rows.
- **The units line** - a reminder that the sheet's numbers are millimetres: *Values are in millimeters. Write a unit for inches, e.g. =2in*.
- **The grid** - column letters across the top, row numbers down the side, and `+` buttons at the right and bottom edges for adding a column or a row. Right-click a column letter or a row number for the menu of commands that act on that column or row.

Click a cell to select it, then type into the formula box to change what it holds. You can also type straight into the selected cell in the grid, and move between cells with the arrow keys.

## Entering Values

Each cell holds one **expression**, which is whatever you typed into it:

- **A number** - `12`, `0.5`, `-3`. Sheet numbers are millimetres.
- **A number with a unit** - `2.5mm`, `5in`, `1ft`. The unit is converted for you, so `5in` is worth `127`. See [Expressions](expressions.md#units) for the full list.
- **Text** - anything that is not a number and does not start with `=`. It is shown exactly as you typed it, quote characters and all.
- **A formula** - anything starting with `=`. It is evaluated, and the cell shows the result.

A formula that produces text shows that text **without** the quotes the expression language carries it in, so `=strcat("MC-", A2)` shows `MC-MMQFQZ5S` rather than `"MC-MMQFQZ5S"`. A cell you typed `"hello"` into is not a formula, so it shows `"hello"` - the quotes are part of what you typed.

## Naming Cells

A cell can be given a name in the **Name** box, and that name is how the rest of the design should refer to it. `=wall_thickness` says what it means where `=B2` does not, and a name keeps working when rows and columns are inserted above or beside the cell.

<!-- IMAGE_NEEDED: The edit row with a cell selected, the Name box holding wall_thickness and the formula box holding 2.4 -->

To name a cell, select it, type the name into the **Name** box and press Enter. To take a name off a cell, clear the box.

Names look after themselves in two ways:

- **A name travels with its cell.** Insert a row above a named cell and the name moves down with it - it belongs to the cell, not to the address.
- **Renaming rewrites every reference.** Change a cell's name and every `=oldname` in the sheet and everywhere in the design is rewritten to the new name, as a single Undo step.

Clearing a name is the one case that does not rewrite: the name no longer exists, so every formula that read it becomes `#REF!`. That is deliberate - a reference to a name that has gone breaks visibly instead of quietly evaluating to zero.

### What a Name Can Be

Names are not case sensitive, and a name is refused - with a message saying why - rather than being quietly changed into something else:

- **Letters, digits and underscores**, starting with a letter or an underscore. Spaces are turned into underscores for you, so `wall thickness` becomes `wall_thickness`.
- **Not a cell address.** `b2` names a cell on any sheet that has a column B and a row 2, so it cannot also be a name.
- **Not a built-in constant or unit.** `pi`, `tau`, `e`, `mm`, `cm`, `m`, `in`, `inch`, `ft`, `true` and `false` already mean something in a formula.
- **Not a name another cell already has.** Two cells sharing a name would leave every formula reading whichever one happened to be resolved first.

## Formulas

Start a formula with `=` to evaluate it in the sheet:

- `=20 + 5` returns `25`
- `=pi * 10` returns `31.415926535897931`
- `=A1 * 2` references another cell by address
- `=wall_thickness + 4` references a named cell
- `=2.5in` returns `63.5` - the unit is converted to millimetres

The sheet supports arithmetic, parentheses, comparisons, the constants `pi`, `tau` and `e`, the bracketed unit constants `[cm]`, `[m]`, `[inch]` and `[ft]`, and the whole function library. See [Expressions](expressions.md) for the syntax and [Expression Functions](expression-functions.md) for the functions.

A cell whose formula references something that does not exist - a misspelled name, a cell past the end of the sheet, or a loop of cells depending on each other - shows `0` rather than a made-up value. A reference the sheet knows is broken, because the cell it named was removed or its name was cleared, is rewritten to `#REF!` so the damage is visible in the formula itself.

## Using Sheet Values in Objects

Most numeric fields in MatterCAD support expressions. To use a sheet value in an object parameter, prefix the reference with `=`:

- Set a Cube **Width** to `=case_width`.
- Set an Array **Count** to `=hole_count`.
- Set a Translate **Offset** value to `=wall_thickness * 2`.

When the sheet changes, MatterCAD recalculates the objects that depend on it - and only those objects, so a big design stays responsive.

An expression can also read a value straight off another object rather than out of a sheet - `=Handle.Sides`, or `=self.Depth` for the object's own settings. See [Object References](object-references.md).

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
- If a formula cannot be parsed, MatterCAD keeps the original input as text.
- Pop the editor out into its own window before working on a large sheet.

## Related

- [Editing a Variable Sheet](sheet-editing.md) - Rows and columns, column widths, cell formats and CSV
- [Expressions](expressions.md) - Expression syntax, cell references and bracket tokens
- [Expression Functions](expression-functions.md) - Every function, with examples
- [Object References](object-references.md) - Read a value off another object instead of a cell
- [Components](components.md) - Create reusable parameterized designs
- [Array](../operations/array/array.md) - Create repeated patterns driven by sheet values
