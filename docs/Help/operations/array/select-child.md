---
title: Select Child
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 4
---
# Select Child

Select Child picks one child from a group of objects based on either an index number or a name. This is especially useful in scripted and parametric designs where you want to dynamically choose which object to display.

<!-- IMAGE_NEEDED: Screenshot showing Select Child operation with multiple children and one selected by index -->

## How to Use

1. Select two or more objects
2. Apply the **Select Child** operation from the Duplication menu
3. Choose **By Index** or **By Name** to control how the child is selected
4. Set the index number or name to match

## Parameters

- **Selection Method** - Choose between **By Index** (select by position) or **By Name** (select by object name). Displayed as buttons.
- **Child Index** - The zero-based index of the child to select (shown when using By Index). Supports [expressions](../../workspace/expressions.md).
- **Child Name** - The name of the child to select (shown when using By Name). Supports [expressions](../../workspace/expressions.md).

If the index is out of range or the name doesn't match any child, the first child is returned as a fallback. If there are no children, nothing is returned.

## Use in Scripting

Select Child is designed to work with expressions and the `rand()` function to create dynamic, data-driven designs. For example, you can build a scene with several variant objects as children and use an expression like `rand(42)` as the index seed to randomly pick one.

**Example: Random book props for a stage show**

1. Import 5 different book meshes as children of a Select Child operation
2. Set the Selection Method to **By Index**
3. Use an expression for Child Index, such as `floor(rand(seed) * 5)` where `seed` is a sheet variable
4. Duplicate the Select Child operation multiple times, each with a different seed value
5. Each instance randomly picks a different book from the set

This pattern works for any scenario where you need to pick from a set of variants: furniture, decorations, architectural elements, or any collection of interchangeable parts.

## Tips

- Combine with [Array](array.md) to create varied patterns where each copy selects a different child
- Use sheet variables for the index or name to drive selection from a spreadsheet
- The fallback-to-first-child behavior means your design never breaks even if the index or name is wrong

## Related

- [Array](array.md) - Duplicate objects in linear, radial, curve, and transform patterns
