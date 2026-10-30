---
title: Creating New Objects
parent: "Getting Started"
nav_order: 2
description: Start a new design, add shapes to the bed and build a part from simple shapes.
keywords: blank design, add shape, start designing, first design, make something
---
# Creating New Objects

Most designs start from simple shapes. You add them, size them, place them, and then combine or reshape them with operations.

<!-- AUTO_IMAGE: type=shot id=gs-add-to-bed-popup -->
![The Add to Bed button and the library it opens over the bed, at its top level: Computer, Included, My Tools, History, Cloud Library, Shared with Me and Purchased](https://matterhackers.github.io/MatterCAD_Docs/assets/gs-add-to-bed-popup.png)

## Start a New Design

Click the **+** button in the row of tabs (**Create New Design**), or press Ctrl+T (⌘T on Mac) while a design is showing. The new design opens in its own tab with an empty bed.

## Add Shapes

Double-click a shape in the favorites bar down the left side of the design, or drag it onto the bed where you want it. (A single click only highlights it.) The bar starts with every 3D primitive except 3D Curve; in the library, the heart on an item adds it to the bar or takes it off.

For more shapes, click **Add to Bed** in the toolbar and open **Included**:

- **3D Primitives** - Cube, Hole, Pyramid, Wedge, Half Wedge, Text, Cylinder, Cone, Half Cylinder, Torus, Tube, Sphere, Half Sphere, Image Converter and 3D Curve
- **2D Primitives** - Flat shapes (paths) you can turn into solids with the **Path** group's Linear Extrude or Revolve
- **Mechanical** - Involute Gear, Cycloidal Gear, Threads and Screw
- **Tools** - QR Code, Measure Tool, Description and Variable Sheet
- **Sample Parts** - Finished designs to start from

Drag a shape onto the bed, or right-click it and choose **Add to Bed**.

Each shape has settings you change in the Properties panel once it is selected. A Cube, for example, has **Width**, **Depth** and **Height**. See [Primitives](../primitives/index.md) for every shape.

## The Toolbar

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

After **Add to Bed**, **Save** and **Bed**, the toolbar holds, in this order:

- **Undo / Redo** - Take back a change or put it back: Ctrl+Z (⌘Z on Mac) and Ctrl+Y (⌘Y on Mac)
- **Arrange All Parts** - Arrange all the parts around the middle of the bed
- **Lay Flat** - Turn the selected part so its lowest face lies flat on the bed
- **Rebuild**
- **Group / Ungroup** - Join the selected parts into a group that moves as one, or split a group apart
- **Convert to Nodes** - Turn the selection into a [node graph](../workspace/node-graphs.md)
- **Duplicate / Remove** - Make a copy of the selected parts, or delete them. Ctrl+C, Ctrl+X and Ctrl+V (⌘C, ⌘X and ⌘V on Mac) copy, cut and paste

Then the operation groups:

- **Transform** - [Translate](../operations/transform/translate.md), [Rotate](../operations/transform/rotate.md), [Scale](../operations/transform/scale.md) and [Mirror](../operations/transform/mirror.md)
- **Placement** - [Align](../operations/placement/align.md), Align in Place, Fit to Bounds and Bounds ([Placement](../operations/placement/index.md))
- **Round & Offset** - Fillet, Chamfer, Round All Edges, Round Inside Edges, Dilate, Erode and Hollow Out ([Reshape](../operations/reshape/index.md))
- **Deform** - Curve, Pinch, Radial Pinch, Twist, Plane Cut and Slice to Path ([Reshape](../operations/reshape/index.md))
- **Image** - [Image Converter](../operations/image/image-converter.md), [Image to Path](../operations/image/image-to-path.md) and [Lithophane](../operations/image/lithophane.md)
- **Path** - [Linear Extrude](../operations/path/linear-extrude.md) and [Revolve](../operations/path/revolve.md) turn a flat 2D shape into a solid; also Sweep, Loft, Smooth Path, Inflate Path, Outline Path, Border Path and Select Paths ([Path](../operations/path/index.md))
- **Merge** - [Combine](../operations/boolean/combine.md), [Subtract](../operations/boolean/subtract.md), [Intersect](../operations/boolean/intersect.md) and [Subtract & Replace](../operations/boolean/subtract-and-replace.md)
- **Duplication** - Clone, [Array](../operations/array/array.md) (rows, rings and other patterns of copies) and Select Child
- **Mesh** - [Repair](../operations/mesh/repair.md) and [Reduce](../operations/mesh/decimate.md)
- **Constraints** - [Modify Parameters](../workspace/modify-parameters.md), Make Component and Edit Component ([Components](../workspace/components.md))
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
