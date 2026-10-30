---
title: Boolean Operations
articleKey: BooleanObject3D
parent: "Operations"
has_children: true
nav_order: 2
description: Combine, subtract and intersect parts to make new shapes from simple ones.
keywords: csg, constructive solid geometry, shape math, merge group
---
# Boolean Operations
<!-- AUTO_IMAGE: type=toolbar_icons group=Merge -->
![Merge toolbar icons](https://matterhackers.github.io/MatterCAD_Docs/assets/toolbar-icons-Merge.png)

Boolean operations let you create complex shapes by combining simpler ones. They are the **Merge** group of the toolbar. Select two or more objects and apply a boolean operation to merge, cut, or find the overlap between them.

All four operations are performed by one Boolean object. The toolbar buttons below just pre-select which operation it starts with, and you can change it afterwards from the row of operation icon tabs at the top of the Properties panel.

|Combine|Subtract|Intersect|Subtract & Replace|
| :--- | :--- | :--- | :--- |
|<!-- AUTO_IMAGE: type=shot id=boolean-index-combine -->![The result of Combine: the overlapping parts merged into one](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean-index-combine.png)|<!-- AUTO_IMAGE: type=shot id=boolean-index-subtract -->![The result of Subtract: a block with the cutter's shape taken out of it](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean-index-subtract.png)|<!-- AUTO_IMAGE: type=shot id=boolean-index-intersect -->![The result of Intersect: only the volume the parts share](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean-index-intersect.png)|<!-- AUTO_IMAGE: type=shot id=boolean-index-subtract-replace -->![The result of Subtract and Replace: the block with the cutter's shape taken out of it, and the cut-away piece kept as its own part](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean-index-subtract-replace.png)|

## Operations

- [Combine](combine.md) - Merge multiple objects into a single solid shape
- [Subtract](subtract.md) - Cut one shape out of another
- [Intersect](intersect.md) - Keep only the volume where objects overlap
- [Subtract and Replace](subtract-and-replace.md) - Subtract one shape from another and replace the cut area
