---
title: Lock and Hide
parent: "Workspace"
nav_order: 6
---
# Lock and Hide

On a busy design, three switches help you work on one part without disturbing the others:

- **Hide** takes a part out of sight, and out of the shapes your design makes.
- **X-ray** draws a part see-through, so you can see what is behind or inside it.
- **Lock** keeps a part from being picked in the 3D view, so you can't move it by accident.

## Where to Find Them

- **In the Design tree:** each row has an eye (Hide), an x-ray column and a padlock (Lock). Click one to switch it for that part.
- **On a part's right-click menu:** **Hide**, **X-ray** and **Lock** sit at the top. Each is lit while the part is in that state. **Hide Others** hides every part except the selected one.
- **Above the Design tree:** **Show All**, **Clear X-ray** and **Unlock All** turn the state off for every part. Each is available only while some part is in that state. **Show All** and **Unlock All** are also on the right-click menu of the empty bed.

## Hide

A hidden part disappears from the 3D view. It stays in the design and in the Design tree, so you can show it again.

A hidden part is left out of what your design makes:

- **Operations leave hidden parts out.** Hide the cutting shape inside a Subtract and the part is no longer cut; show it again and the cut comes back.
- **Exports leave hidden parts out.** An export to STL, 3MF, OBJ, AMF or STEP has no hidden parts in it. An MCX file keeps them, still hidden.
- **Home (W) leaves hidden parts out** when it fits the design in the view.

You can't select a hidden part, and hiding a selected part clears the selection.

## X-ray

An x-rayed part is drawn see-through, so the parts behind and inside it show. X-ray changes only how the part looks: you can still select it, and it still takes part in operations and exports.

## Lock

A locked part stays visible and still takes part in operations and exports, but you can't pick it in the 3D view, so a click or drag there goes past it. Locking a selected part clears the selection.

## Tips

- Lock a base or reference part while you work on the details around it.
- Hide parts that are in the way, but remember to show them before you export.
- Hiding and showing are not steps you can undo with Ctrl+Z (⌘Z on Mac); use the eye or **Show All** instead.
- Hide and Lock are saved with the design.
- You can hide, x-ray or lock parts inside groups from their rows in the Design tree.

## Related

- [Selection](selection.md) - How to select parts
- [Grouping](grouping.md) - Keep parts together as a group
