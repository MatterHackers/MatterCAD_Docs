---
title: Variable Sheet
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 3
---
# Variable Sheet

The Variable Sheet stores shared values for a design. Use it when several objects should reference the same dimensions, counts, labels, or formulas. Changing a value in the sheet recalculates the dependent objects, so parametric designs stay consistent without editing every object one at a time.

<!--  Screenshot of the Variable Sheet editor showing named cells, formulas, and the Documentation button -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## How to Add a Variable Sheet

1. Open the library and add **Variable Sheet** to the scene.
2. Select the Variable Sheet object to show the sheet editor.
3. Select a cell, then enter a **Name** and a value or formula.
4. Use the cell name from other expression-enabled fields in the design.

## Editing Cells

Each cell has two editable parts:

- **Name** - An optional variable name for the cell. Names are case-insensitive, spaces are converted to underscores, and duplicate names are automatically adjusted.
- **Expression** - The cell value. Plain text or numbers are stored directly. Formulas start with `=`.

Cells can also be referenced by address, such as `A1` or `B2`. Named cells are usually clearer for design parameters because they describe intent, such as `wall_thickness`, `outer_diameter`, or `hole_count`.

## Formulas

Start a formula with `=` to evaluate it in the sheet:

- `=20 + 5` returns `25`
- `=pi * 10` returns `31.41592653589793`
- `=A1 * 2` references another cell by address
- `=wall_thickness + 4` references a named cell

The sheet supports arithmetic, parentheses, comparison operators, common `Math` functions such as `sin`, `cos`, `sqrt`, and `round`, and constants including `pi`, `tau`, and `e`.

## Using Sheet Values in Objects

Most numeric fields in MatterCAD support expressions. To use a sheet value in an object parameter, prefix the reference with `=`:

- Set a Cube **Width** to `=case_width`.
- Set an Array **Count** to `=hole_count`.
- Set a Translate **Offset** value to `=wall_thickness * 2`.

When the sheet changes, MatterCAD recalculates the objects that depend on it.

## Text and Helper Functions

Variable Sheet cells can hold text as well as numbers. Text values are useful for generated labels, part numbers, imported data, and custom design apps.

Useful helper functions include:

- `concat()` or `strcat()` - Join text or values together.
- `substring()` - Extract part of a text value.
- `split()` - Split text and return one item.
- `count()` - Count delimited items in text.
- `substitute()` - Replace text.
- `rand(seed)` - Generate a deterministic random value when a seed is supplied.
- `importdata()` - Read a value from a URL or local file path.

## Tips

- Prefer descriptive names over cell addresses for values used by other objects.
- Keep core dimensions near the top-left of the sheet so they are easy to find.
- Use formulas for derived values, such as `inner_diameter = outer_diameter - wall_thickness * 2`.
- Avoid using reserved words such as `pi`, `e`, `true`, `false`, or function names as cell names.
- If a formula cannot be parsed, MatterCAD keeps the original input as text.

## Related

- [Expressions](expressions.md) - Use expressions in object parameters
- [Components](components.md) - Create reusable parameterized designs
- [Array](../operations/array/array.md) - Create repeated patterns driven by sheet values
