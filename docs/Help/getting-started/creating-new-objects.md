---
title: Creating New Objects
parent: "Getting Started"
nav_order: 2
---
# Creating New Objects

Most designs start from simple shapes. You add them, size them, place them, and then combine or reshape them with operations.

![20260324 081122 paste 20260324 081122](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081122-paste-20260324-081122.jpg)

## Start a New Design

Click the **+** button in the row of tabs (**Create New Design**), or press Ctrl+T (⌘T on Mac) while a design is showing. The new design opens in its own tab with an empty bed.

## Add Shapes

Click a shape in the favorites bar down the left side of the design, or drag it onto the bed where you want it.

For more shapes, click **Add to Bed** in the toolbar and open **Included**:

- **3D Primitives** - Cube, Hole, Pyramid, Wedge, Half Wedge, Text, Cylinder, Cone, Half Cylinder, Torus, Tube, Sphere, Half Sphere and Image Converter
- **2D Primitives** - Flat shapes (paths) you can extrude or revolve into solids
- **Mechanical** - Involute Gear, Cycloidal Gear, Threads and Screw
- **Tools** - QR Code, Measure Tool, Description and Variable Sheet
- **Sample Parts** - Finished designs to start from

Drag a shape onto the bed, or right-click it and choose **Add to Bed**.

Each shape has settings you change in the Properties panel once it is selected. A Cube, for example, has **Width**, **Depth** and **Height**. See [Primitives](../primitives/index.md) for every shape.

## The Toolbar

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

After **Add to Bed**, **Save** and **Bed**, the toolbar holds:

- **Undo / Redo** - Take back a change or put it back: Ctrl+Z (⌘Z on Mac) and Ctrl+Y (⌘Y on Mac)
- **Group / Ungroup** - Join the selected parts into a group that moves as one, or split a group apart
- **Duplicate / Remove** - Make a copy of the selected parts, or delete them. Ctrl+C, Ctrl+X and Ctrl+V (⌘C, ⌘X and ⌘V on Mac) copy, cut and paste
- **Arrange All Parts** - Arrange all the parts around the middle of the bed
- **Lay Flat** - Turn the selected part so its lowest face lies flat on the bed
- **Merge group** - [Combine](../operations/boolean/combine.md), [Subtract](../operations/boolean/subtract.md), [Intersect](../operations/boolean/intersect.md) and [Subtract & Replace](../operations/boolean/subtract-and-replace.md)
- **Duplication group** - Clone, [Array](../operations/array/array.md) (rows, rings and other patterns of copies) and Select Child
- **Transform group** - [Translate](../operations/transform/translate.md), [Rotate](../operations/transform/rotate.md), [Scale](../operations/transform/scale.md) and [Mirror](../operations/transform/mirror.md)
- **Placement group** - [Align](../operations/placement/align.md) and other ways to place parts against each other
- **Round & Offset** and **Deform** groups - [Reshape](../operations/reshape/index.md) operations such as Fillet, Curve and Twist
- **Tools** - At the end of the toolbar: collapse or hide groups you don't use

Hover over a button to see its name. A button that is greyed out tells you, when you hover over it, what to select first.

## Building a Shape from Simple Parts

1. **Add the shapes you need.**
2. **Place them** so they overlap where you want them joined or cut.
3. **Select the parts** (click one, then Shift-click the others).
4. **Apply a Merge operation:** [Combine](../operations/boolean/combine.md) joins them; [Subtract](../operations/boolean/subtract.md) cuts every part you selected after the first out of the first one.
5. **Refine** with the **Round & Offset** and **Deform** groups ([Reshape](../operations/reshape/index.md)) to round edges, bend or twist.

An operation keeps the parts it was made from, so you can go back and change them later.

## Related

- [Primitives](../primitives/index.md) - Every shape and its settings
- [Adding Existing Objects](adding-existing-objects.md) - Bring in files instead of starting from scratch
- [Boolean Operations](../operations/boolean/index.md) - Combine shapes into more complex ones
- [Editing Objects](editing-objects.md) - Move, turn and resize parts
