---
title: Expressions
parent: "Workspace"
nav_order: 3
---
# Expressions

Most parameters in MatterCAD accept an expression instead of a plain number. An expression is a small formula that MatterCAD evaluates every time something it depends on changes, which is what makes a design parametric: change one value and every dimension derived from it follows.

<!--  Screenshot showing an expression being entered in a parameter field -->
![20260318 193631 paste 20260318 193631](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193631-paste-20260318-193631.jpg)

This page describes the expression language itself. See [Expression Functions](expression-functions.md) for the function library, [Object References](object-references.md) for reading another object's settings, [Variable Sheet](variable-sheet.md) for storing shared values a whole design can use, and [Modify Parameters](modify-parameters.md) for driving an object's visibility and colour from an expression.

## Starting an Expression

Type `=` as the first character of the field. Everything after the `=` is treated as a formula:

- `=20 + 5` evaluates to `25`
- `=pi * 10` evaluates to `31.415926535897931`
- `=wall_thickness * 2` reads a value from the [Variable Sheet](variable-sheet.md)

Without the leading `=`, the field keeps what you typed - `20 + 5` in a numeric field is just an unparsed entry, and in a text field it is the literal text.

The same rule applies inside Variable Sheet cells: a cell whose contents start with `=` is a formula, and anything else is stored as a plain number or as text.

## Operators

| Operator | Meaning |
| --- | --- |
| `+` | Addition. If either side is text, the two sides are joined instead |
| `-` | Subtraction, and negation as in `=-A1` |
| `*` | Multiplication |
| `/` | Division. Dividing by zero produces `NaN` |
| `( )` | Grouping |
| `<` `<=` `>` `>=` | Comparison. The result is `1` for true and `0` for false |
| `==` `!=` | Equal and not equal. Numbers compare as numbers, text compares as text |

Comparisons are what drive checkbox-style parameters and switch one value in for another:

- `=hole_count > 4` gives `1` or `0`
- `=(diameter > 20) * 3 + 2` gives `5` when the diameter is over 20 and `2` otherwise

Subtracting text is not meaningful, so `="a" - 1` produces `NaN` rather than a value.

## Constants

Three math constants can be used by name anywhere in a formula:

- `pi` - 3.14159..., the ratio of a circle's circumference to its diameter
- `tau` - 6.28318..., a full revolution in radians
- `e` - 2.71828..., the base of the natural logarithm

Unit constants convert a measurement into MatterCAD's internal millimetres. These must be written in square brackets, because they are substituted into the formula before it is evaluated:

| Constant | Value in mm |
| --- | --- |
| `[cm]` | 10 |
| `[m]` | 1000 |
| `[inch]` | 25.4 |
| `[ft]` | 304.8 |

- `=2 * [inch]` gives `50.8`
- `=1.5 * [cm] + 2` gives `17`

`[pi]`, `[tau]` and `[e]` work in brackets too, so you can write either style.

## Referencing Sheet Values

When a [Variable Sheet](variable-sheet.md) is in the design, its cells become names your expressions can use. Every cell can be referenced two ways:

- **By address** - `=A1`, `=B12`. Addresses are the familiar spreadsheet A1 style: column letters then a one-based row number, and they are not case sensitive (`=a1` and `=A1` are the same cell).
- **By name** - `=wall_thickness`, if you gave the cell that name in the sheet's Name box.

Names are usually the better choice because they say what the value means and they survive rows and columns being added. Addresses are useful when a formula has to walk a table - see `index()` and `xlookup()` in [Expression Functions](expression-functions.md).

Objects find the nearest Variable Sheet above them in the scene tree, so a sheet inside a group only serves that group.

## Bracket Tokens

A few values are not part of the formula's arithmetic - they are substituted into the text of the formula before it is evaluated, which is why they are written in square brackets.

| Token | Meaning |
| --- | --- |
| `[index]` | The position of this copy inside the enclosing [Array](../operations/array/index.md), counting from 0 |
| `[index0]` | The same as `[index]` |
| `[index1]` | The position inside the next Array out, for arrays nested inside arrays |
| `[index2]` | The position inside the Array one further out again |
| `[rand]` | A new random number between 0 and 1 each time the expression is evaluated |

Because the substitution happens first, an arrayed copy sees its own position as a literal number - the fifth copy evaluates `=[index] * 12` as `=4 * 12`. That is what lets an array of copies each read a different row out of a sheet:

```
=index("A", [index]+2)
```

<!-- IMAGE_NEEDED: An Array of Text objects on the bed, each showing a different part number, next to the sheet column those values come from -->

The `+2` skips the header row and converts the 0-based copy position into the 1-based row number `index()` expects, so the first copy reads `A2`, the second reads `A3`, and so on. Give a Text object that expression as its text and an array of it becomes a run of parts, each labelled from its own row.

`[index]` only means something for an object inside an Array. In a sheet cell there is no array copy to ask about, so use it in the object's own parameter fields.

## Text Values

Text in a formula goes in double quotes, and the usual escape sequences work inside those quotes: `\n` for a newline, `\t` for a tab, `\\` for a backslash and `\"` for a quote character.

- `=strcat("Part ", A1)` joins a label to a cell value
- `="Serial " + B2` does the same thing with `+`, since one side is text

A cell holding text is text everywhere it is used, so a text cell fed into a numeric field will not produce a number.

## Object Property References

An expression can read a setting off another object in the scene by name:

- `=Handle.Sides` - the Sides value of the nearest object named Handle
- `=self.Depth` - this object's own Depth
- `='Handle Cuts'.Sides` - a name with spaces, in single quotes

Editing the referenced value rebuilds everything that follows it, the same way a sheet edit does. See [Object References](object-references.md) for how names are resolved and which properties can be read.

## When an Expression Cannot Be Resolved

MatterCAD never guesses at a value it could not work out:

- A misspelled cell name or address, or a reference to a cell that does not exist, resolves as unknown. In the sheet the cell shows `0`; in an object parameter the field falls back to a placeholder value (`0.1` for a decimal field, `1` for a whole-number field), which is a strong hint that the reference is wrong.
- Cells that depend on each other in a loop also resolve to `0` rather than looping forever.
- A formula that cannot be parsed at all is kept as the text you typed, so nothing is lost and you can correct it in place.

## Tips

- Expressions work in any parameter the properties panel shows a value box for - dimensions, counts, angles, offsets and text.
- Build relationships instead of repeating numbers: set a hole's diameter to `=outer_diameter - 4` so it always leaves 2 mm walls.
- Use a [Variable Sheet](variable-sheet.md) when more than one object needs the same value.
- Expressions re-evaluate on their own when anything they reference changes - there is nothing to refresh by hand.

## Related

- [Expression Functions](expression-functions.md) - Every function you can call, with examples
- [Object References](object-references.md) - Read another object's settings with `Name.Property` and `self.Property`
- [Variable Sheet](variable-sheet.md) - Store shared values and formulas for a design
- [Components](components.md) - Create reusable parameterized designs
- [Array](../operations/array/index.md) - Repeat an object and drive each copy from `[index]`
- [Editing Objects](../getting-started/editing-objects.md) - Working with object parameters
