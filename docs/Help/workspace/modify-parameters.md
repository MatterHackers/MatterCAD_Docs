---
title: Modify Parameters
articleKey: ModifyParametersObject3D
parent: "Workspace"
nav_order: 14
---
# Modify Parameters

Modify Parameters wraps whatever you have selected and lets [expressions](expressions.md) decide whether it is visible and what colour it is. It is how you make a part appear only under certain conditions, or shade itself from a value on a [Variable Sheet](variable-sheet.md).

<!-- IMAGE_NEEDED: Screenshot of a Modify Parameters selected in the design tree, with the Properties panel showing the Visible Override field and the Red/Green/Blue expression fields -->

## Turning It On

Modify Parameters lives in the **Constraints** group of the toolbar, which is hidden by default.

1. Click **Tools** at the right end of the toolbar
2. Find **Constraints** in the list
3. Set it to **Expand** (buttons always shown) or **Collapse** (buttons behind the group button)

The Constraints group remembers its own setting, so showing it here is all it takes -- it comes back the next time MatterCAD starts whatever you have done with the **Path** group or any other. The same menu is where you show, hide, expand and collapse every other toolbar group.

You do not have to show the group at all if you would rather not: **Modify Parameters** is also in the right-click **Modify** menu of any selected object, whether the toolbar group is showing or not.

## How to Use

1. Select one or more objects
2. Choose **Modify Parameters** from the right-click **Modify** menu, or click it in the Constraints group of the toolbar
3. The selection becomes a child of the new Modify Parameters
4. Type an expression into **Visible Override**, or into **Red**, **Green** and **Blue**

## Parameters

- **Visible Override** - True or false, or an expression that works out to one. When it is false, every child is hidden. Point it at a named [Variable Sheet](variable-sheet.md) cell and one value in one place decides whether a whole assembly of parts shows: `=show_brackets`
- **Red**, **Green**, **Blue** - Expressions giving the 0-255 colour channels of anything below. Each starts as `=[Red]`, `=[Green]` and `=[Blue]`, which leaves the colour exactly as it was

### The colour variables

Inside the three colour expressions you can use three extra variables that stand for the part's current colour:

- `[Red]` - the part's current red value
- `[Green]` - the part's current green value
- `[Blue]` - the part's current blue value

They must be written in square brackets and they are not case sensitive, so `[red]` and `[Red]` are the same thing. Results outside 0-255 are clamped.

Examples:

- `=[red] - 2` - a shade darker in red than whatever the part already is
- `=255 - [red]` - inverted red
- `=warm * 255` - a channel driven straight from a named sheet cell holding a 0 to 1 value

The Properties panel prints a reminder of these three variables above the colour fields.

## Tips

- One Modify Parameters can wrap a whole branch. Everything under it answers to the same Visible Override
- Use it with a sheet to build variants of a design in one file: a cell that says which options are fitted, and a Modify Parameters over each optional part reading it
- Colour driven from a value is a quick way to see a number you cannot otherwise see -- redder as a clearance gets tighter, for instance
- Hiding through Visible Override is different from [Lock and Hide](lock-hide.md). Lock and Hide is something you do by hand to one object; Visible Override is a rule that recalculates every time the value it reads changes
- Leaving the colour expressions at their defaults means Modify Parameters changes nothing about the colour, so you can use it for visibility alone

## Related

- [Expressions](expressions.md) - The expression language these fields are written in
- [Expression Functions](expression-functions.md) - Every function an expression can call
- [Variable Sheet](variable-sheet.md) - Store the values the expressions read
- [Object References](object-references.md) - Read another object's setting with `Name.Property`
- [Lock and Hide](lock-hide.md) - Hide an object by hand rather than by rule
