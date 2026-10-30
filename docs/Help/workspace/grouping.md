---
title: Grouping
articleKey: GroupObject3D, GroupHolesAppliedObject3D
parent: "Workspace"
nav_order: 4
description: Group parts so they move and copy as one, without merging them, and ungroup them again.
keywords: ungroup, together, assembly, keep together, move together
---
# Grouping

Grouping combines multiple objects into a single unit that can be moved, copied, and operated on as one object. Unlike [Combine](../operations/boolean/combine.md), grouping does not merge the geometry -- each object remains separate inside the group.

<!-- Screenshot showing objects before and after grouping, with the design tree showing the group hierarchy -->
<!-- AUTO_IMAGE: type=shot id=workspace-grouping-before -->
![A cube and a cylinder side by side on the bed, each its own row in the design tree, before they are grouped](https://matterhackers.github.io/MatterCAD_Docs/assets/workspace-grouping-before.png)

<!-- AUTO_IMAGE: type=shot id=workspace-grouping-group-button -->
![The toolbar's Group button with the pointer resting on it and its tool tip showing, the Ungroup button beside it](https://matterhackers.github.io/MatterCAD_Docs/assets/workspace-grouping-group-button.png)

<!-- AUTO_IMAGE: type=shot id=workspace-grouping-after -->
![The cube and cylinder grouped: one Group selected on the bed, its design tree row opened to show Cube and Cylinder inside it](https://matterhackers.github.io/MatterCAD_Docs/assets/workspace-grouping-after.png)


## How to Use

### Grouping Objects

1. Select two or more objects (click one, then Shift-click the others)
2. Click the **Group** button in the toolbar, or press **G**
3. The objects are now grouped -- they move together as one unit

### Ungrouping Objects

1. Select a group
2. Click the **Ungroup** button in the toolbar, or press **Shift + G**
3. <!-- AUTO_IMAGE: type=shot id=workspace-grouping-ungroup-button -->
   ![The toolbar's Ungroup button with the pointer resting on it and its tool tip showing, a Group selected](https://matterhackers.github.io/MatterCAD_Docs/assets/workspace-grouping-ungroup-button.png)
4. The individual objects are restored as separate items

Ungrouping also attempts to separate multiple bodies within a single imported STL file, if present.

## Group vs. Combine

| Feature | Group | Combine |
|---------|-------|---------|
| Objects remain separate | Yes | Kept inside the Combine, but shown as one joined shape |
| Can change the parts later | Yes | Yes: double-click the Combine (Edit Children) and change a part, and the Combine updates |
| Ungroup | Puts the parts back as separate objects | Bakes the Combine into one plain shape; the original parts are gone (Ctrl+Z / ⌘Z takes it back) |
| Merges overlapping geometry | No | Yes |
| Objects can have different colors | Yes | Colors preserved per-face |
| Use case | Organization and movement | Creating single solid shapes |

## Tips

- Groups can be nested -- you can group objects that are already in groups
- Select a group and look at the Design Tree to see and select individual objects within it
- Grouping is non-destructive and can always be reversed with Ungroup

## Related

- [Combine](../operations/boolean/combine.md) - Merge objects into a single solid instead of grouping
- [Selection](selection.md) - How to select multiple objects for grouping
- [Components](components.md) - Create reusable parameterized groups
