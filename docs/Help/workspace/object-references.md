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

A reference can read the object's **inputs** - the values the properties panel gives you an editor for. In practice that means numbers, whole numbers, on/off settings and text.

Some things deliberately cannot be read, and a reference to them is left unresolved rather than guessed at:

- **Drop-down choices**, because substituting the hidden number behind a choice would mean something you never wrote
- **Grouped values** such as an offset or an axis written as `[10, 20, 30]`, because there is no single number to put in their place
- **Results rather than inputs** - a mesh, a computed bounding size, or anything the properties panel does not offer as a field
- **Chained references** such as `=Mover.Translation.X`, and anything with a call in it

## Sheet Names Win

If a Variable Sheet in scope happens to define a cell whose *name* is `Handle.Sides`, that cell answers the reference. This keeps designs authored before object references existed working exactly as they did. Ordinary cell names never contain a dot, so this rarely comes up.

## When a Reference Cannot Be Resolved

A reference to a name that is not in the scene, to a setting the object does not have, or to a value that has no numeric or text form, is left in place unresolved. It then behaves like a misspelled cell name: the field falls back to a placeholder value rather than silently using something wrong. Check the spelling of both halves - the object name in the scene tree, and the property name as the properties panel spells it.

References that would chase each other in a circle - `A` reading `B` while `B` reads `A` - are detected and reported unresolved instead of hanging.

## Updates and Rebuilding

Editing a referenced value rebuilds every object that follows it, and the operations above those objects, in the right order. Dragging a slider updates followers as you drag.

A design that feeds itself - where rebuilding a follower changes the value it was following - is given a few passes to settle and is then left alone rather than looping forever. If a value looks one edit out of date in a design like that, nudge the source value again.

## Related

- [Expressions](expressions.md) - Expression syntax, constants and cell references
- [Expression Functions](expression-functions.md) - The function library
- [Variable Sheet](variable-sheet.md) - Shared values for a whole design
- [Components](components.md) - Package a design with just the parameters you want exposed
