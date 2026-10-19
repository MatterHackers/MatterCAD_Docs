---
title: Object References
parent: "Workspace"
nav_order: 9
---
# Object References

An expression can read a value straight off another object in the scene, without a [Variable Sheet](variable-sheet.md) in between. Write the object's name, a dot, and the name of the setting you want:

```
=Handle.Sides
```

That reads the **Sides** value of the object named `Handle`. When you change Sides on the handle, everything that references it rebuilds on its own.

<!-- IMAGE_NEEDED: Scene tree with an object named "Handle" selected, and a second object's parameter field showing =Handle.Sides -->

Use object references when one object's shape should follow another's - a cut that must always have the same number of sides as the part it cuts, a lid whose diameter tracks its jar. Use a [Variable Sheet](variable-sheet.md) instead when a value belongs to the design as a whole rather than to one object.

## Naming the Object

Rename objects from the scene tree, then reference them by that name. Matching is not case sensitive.

- `=Handle.Sides` - a plain name
- `='Handle Cuts'.Sides` - a name containing spaces, wrapped in single quotes
- `=self.Depth` - this object's own setting, whatever it is called

### self

`self` is a reserved name meaning "the object this expression belongs to". It is the form to reach for when an object reads its own inputs, because it keeps working after the object is renamed:

```
Width  = 40
Depth  = =self.Width / 2
```

Renaming that object leaves the expression correct. An object named `self` in the scene tree cannot be reached by a dotted reference - the reserved word wins.

### Which Object a Name Finds

Names do not have to be unique. When more than one object answers to a name, the nearest one in the scene tree wins, searched in this order:

1. The object holding the expression
2. Its own children, deepest branch first
3. Each ancestor in turn, and then that ancestor's other branches

That ordering is what makes references survive copying. Duplicate a part named `Cube` whose Depth reads `=Cube.Width`, and the copy - also named `Cube` - binds to *itself*, not to the original. An array of copies stays an array of independent parts instead of becoming followers of the first one.

## Which Settings You Can Read

A reference can read an object's **settings** - the values the Properties panel gives you a box, slider or switch for. In practice that means numbers, whole numbers, on/off settings and text:

- `=Arm.Width` - the Width of the object named `Arm`
- `=self.Width` - this object's own Width

For a value made of X, Y and Z, add the letter to read one number:

- `=Mover.Translation.X` - how far the [Translate](../operations/transform/translate.md) named `Mover` moves its part along X
- `=Bounds.Max.Z` - the top of a [Bounds](../operations/placement/bounds.md) box. A Bounds also gives its **Min**, **Size** and **Center**, so `=Bounds.Size.X` is its width

Type the object's name and a dot, and [autocomplete](expressions.md#autocomplete) lists the settings you can read, with their current values.

Some things deliberately cannot be read, and a reference to them is left unresolved rather than guessed at:

- **Where an object sits** - the position, turn and size you give it by dragging, rotating or scaling it in the 3D view (its **Matrix** row in the Properties panel). To have other parts follow a position, move the part with a [Translate](../operations/transform/translate.md) and read the Translate's Translation, like `=Mover.Translation.X`
- **Drop-down choices**, because substituting the hidden number behind a choice would mean something you never wrote
- **A whole X, Y and Z value** such as an offset written as `[10, 20, 30]`, because there is no single number to put in its place - read one part of it instead, like `=Mover.Translation.X`
- **Results rather than settings** - a mesh, or anything the Properties panel does not show as a row
- **Longer chains** such as `=A.B.C.X`, and anything with a call in it

## Sheet Names Win

If a Variable Sheet in scope happens to define a cell whose *name* is `Handle.Sides`, that cell answers the reference. This keeps designs authored before object references existed working exactly as they did. Ordinary cell names never contain a dot, so this rarely comes up.

## When a Reference Cannot Be Resolved

A reference to a name that is not in the scene, to a setting the object does not have, or to a value that has no numeric or text form, is left in place unresolved. It then behaves like a misspelled cell name: the field falls back to a placeholder value rather than silently using something wrong. The Properties panel also warns you:

- An orange **!** appears beside the setting, and beside the object in the design tree. Hover over it to see the formula and why it has no value, such as "Cannot find object 'Handle'." or "Cannot find property 'Sides' on 'Handle'."
- The top of the Properties panel says "Some expressions need attention. Automatic updates may be paused."

Check the spelling of both halves - the object name in the design tree, and the setting's name as autocomplete lists it.

When the [AI](../getting-started/ai-assistants.md) writes a formula into a number, whole-number or X, Y and Z setting, a reference to an object or setting that is not there is refused instead: the AI's change is not made, and it is told the names it can use. See [Expressions](expressions.md#formulas-the-ai-writes).

References that would chase each other in a circle - `A` reading `B` while `B` reads `A` - are detected and reported unresolved instead of hanging.

## Updates and Rebuilding

Editing a referenced value rebuilds every object that follows it, and the operations above those objects, in the right order. Dragging a slider updates followers as you drag.

A design that feeds itself - where rebuilding a follower changes the value it was following - is given a few passes to settle and is then left alone rather than looping forever. If a value looks one edit out of date in a design like that, nudge the source value again.

## Related

- [Expressions](expressions.md) - Expression syntax, constants and cell references
- [Expression Functions](expression-functions.md) - The function library
- [Variable Sheet](variable-sheet.md) - Shared values for a whole design
- [Components](components.md) - Package a design with just the parameters you want exposed
