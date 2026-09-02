---
title: Components
articleKey: ComponentObject3D
parent: "Workspace"
nav_order: 1
---
# Components

A component is a group of objects that shows only a chosen handful of controls. Everything inside it is still there in the design tree, but the Properties panel presents just the settings that matter -- the height of one extrude, the diameter of one hole -- so the component reads as a single part with a few parameters rather than as the stack of operations it is built from. The [Image Converter](../operations/image/image-converter.md) is a component MatterCAD builds for you, and the [Design Apps](../designing/design-apps/index.md) are components too.

<!--  Screenshot showing a component in the design tree with exposed parameters -->
![20260318 193745 paste 20260318 193745](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193745-paste-20260318-193745.jpg)


## How to Use

### Creating a Component

1. Select one or more objects at the top level of the scene
2. Choose **Make Component** from the object's right-click **Modify** menu, or click it in the Constraints group of the toolbar
3. The selection is replaced by a component named "New Component", which starts in editing mode so you can choose what it surfaces

**Make Component** is only enabled for a selection sitting at the top of the scene, not for something already nested inside another object.

The Constraints group the toolbar button lives in is hidden by default. Click **Tools** at the right end of the toolbar and set **Constraints** to Expand or Collapse to bring it back. The right-click Modify menu offers Make Component either way.

### Editing and Finalizing

A component has two modes, switched by the **Finalized** setting:

- **Editing** (Finalized off) - Everything inside is on show, including any [Variable Sheet](variable-sheet.md) it holds, so you can build and wire it up
- **Distribution** (Finalized on) - Only the surfaced controls are shown, and the embedded sheet is hidden. This is how someone using your component sees it

**Edit Component** puts a finalized component back into editing mode. It is offered in the Modify menu for a finalized component sitting at the top level of the scene.

### Using a Component

1. Select the component
2. The surfaced parameters appear in the Properties panel
3. Change them to change the part

Behind the scenes those parameters usually write into a Variable Sheet inside the component, and the objects in the component read their dimensions back out of it -- which is what makes one control move several things at once.

## Tips

- Components are useful for creating reusable building blocks in complex designs
- Parameter changes are non-destructive and can be adjusted at any time
- Surface as few controls as you can. A component with four meaningful settings is far easier to use than one with forty
- Copy a component and the copy is independent. Editing one does not change the other -- for parts that must stay identical, drive them from one [Variable Sheet](variable-sheet.md) instead
- **Apply** on a component flattens it down to plain meshes and cannot be undone by re-editing, so keep an unapplied copy if you may want to change it later

## Related

- [Grouping](grouping.md) - Simple grouping without parameterization
- [Expressions](expressions.md) - Use expressions to link component parameters
- [Variable Sheet](variable-sheet.md) - Store the shared values a component's parameters read
- [Object References](object-references.md) - Link a parameter to another object's setting
- [Design Apps](../designing/design-apps/index.md) - Pre-built components you can customize
