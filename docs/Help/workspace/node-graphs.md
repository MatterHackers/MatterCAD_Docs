---
title: Node Graphs
articleKey: GeometryNodesObject3D
parent: "Workspace"
nav_order: 18
---
# Node Graphs

A node graph lets you build a part by wiring boxes together instead of stacking operations in the scene tree. To the rest of your design it is just an object: it has one row in the scene tree, you move, colour, export and undo it like any other part, and its settings show in the Properties panel. The only difference is the **Show Graph** switch, which opens its graph under the 3D view.

Use a node graph when you want to turn a few parts into one tool with a handful of settings - a bracket with a Width and a Hole Size, say - that you can reuse and share.

<!-- IMAGE_NEEDED: The node editor open under the 3D view, showing the Input node, a Box node wired through an Outline node to the Output node -->

## Start a Graph

1. Select one or more parts.
2. Click **Convert to Nodes** on the toolbar (next to Group and Ungroup).

The selection becomes one object named **Geometry Nodes**, and its graph opens. Each part you selected is a node, wired to the **Output**, so the object looks exactly as the parts did.

## Show and Hide the Graph

Select the object and turn **Show Graph** on or off in the Properties panel. With it off you still use the object's settings, you just don't see the wiring. The choice is saved with the design.

## The Node Editor

- **Input** (on the left) holds everything that comes into the graph: its settings (parameters), the objects it works on, and the **Scene** and **Parameters** sockets used by formulas.
- **Output** (on the right) is what the object shows. Whatever you wire into it is the result.
- **Cards** are the nodes in between. Each card is an object - a shape, an operation, a sheet - and shows the same settings the Properties panel would. Click a card to select it; drag its title bar to move it.
- **Sockets** are the dots on a card's edges: inputs on the left, the result on the right. Their colour says what they carry - green for solids, blue for paths, grey for numbers, pink for Variables. Hover a socket to see its name.
- **Noodles** are the wires. Drag from a result socket and drop on an input socket of the same colour to connect them. To move a noodle, pick it up by the end at its input and drop it somewhere else; drop it on empty space to remove it. A noodle that would make a loop is refused.

Scroll the mouse wheel to zoom, and drag with the right or middle mouse button to pan.

## Add and Delete Nodes

- Press **Shift+A**, or right-click on empty space, to open the **Add Node** menu at the pointer. It lists **Shapes**, **Operations**, **Sheet** and **My Tools**; type to search. The node you pick lands at the pointer, unwired and selected.
- With a graph shown, the toolbar's operation buttons add a node to the graph you are looking at.
- Drag an object from the scene tree onto the editor to move it into the graph, or drag an item from the Library to add a copy.
- To delete a node, select it and press **Delete** or **Backspace**, or right-click its card and choose **Delete Node**. Its noodles go with it. Input and Output can't be deleted.

Every one of these is a single undo step.

## Parameters

Parameters are the settings the object shows in the Properties panel.

1. Show the graph.
2. Drag from the Input node's empty socket (labelled *Drag to a setting or a shape input*) to a setting on any card - a Box's Width, for example.

A new parameter appears on the Input node and as a row in the object's Properties panel. Change it there and everything wired to it follows. Until you add one, the Properties panel says *No parameters yet. Show Graph, then drag from the Input node's empty socket to a setting.*

- **Rename** a parameter by double-clicking its name.
- **Reorder** parameters by dragging the grip at the left end of a row.
- **Remove** a parameter by removing its last noodle; the row goes with it.
- A parameter can hold a formula, like `=A1` from a [Variable Sheet](variable-sheet.md) or `=Handle.Width` from another object.
- Other objects can read it too: `=Bracket.Width` reads the Width parameter of the graph named Bracket. Nodes inside a graph can't be read from outside; if you try, you see *Nodes inside a graph can't be used from outside it; add a graph parameter instead.*

## Object Inputs

A graph can also take objects in, so it works like an operation. Drag from the Input node's empty socket to a card's shape input (the socket an operation reads its source from). This adds an object slot to the Input node. Objects you converted with **Convert to Nodes** are already wired in this way.

## Formulas Inside a Graph

A graph is sealed: a formula inside it sees only what is wired to its card's **Variables** socket. If a formula names something that isn't wired, the setting shows a warning telling you which noodle to add:

- To read another node, like `=Box.Width`, drag from Box's Variables socket to this node's Variables socket. Otherwise: *Box isn't wired to this node. Drag from Box's Variables socket to this node's Variables socket.*
- To read the graph's own parameters, like `=Input.Width`, drag from the Input node's **Parameters** socket to this node's Variables socket. Otherwise: *Input isn't wired to this node. Drag from the Input node's Parameters socket to this node's Variables socket.*
- To read objects in the scene outside the graph, wire the Input node's **Scene** socket to this node's Variables socket. Otherwise: *... isn't wired to this node. Wire the Input node's Scene socket to this node's Variables socket to use names from the scene.*
- A **Sheet** node works the same way: wire its Variables socket to each node whose formulas read its cells. A sheet has no result, so it never goes into the Output.

## Save as Tool and My Tools

Right-click the object and choose **Save as Tool** to keep a copy you can use in any design. Tools are stored in **My Tools** in the Library.

- A tool that **makes** a shape (no object inputs) is also added to the **Favorites** bar. Drag it into your design like a primitive.
- A tool that **works on** objects (it has object inputs) gets a button in the toolbar's **My Tools** group. Select a part and click the button to run the tool on it.

Each use adds an independent copy, so changing one never changes the others. Tools also appear under My Tools in the Add Node menu.

## Graphs Inside Graphs

Add a graph to another graph - from the Add Node menu's My Tools, the Library, or the scene tree - and it becomes one card. Its sockets are the inner graph's parameters and object inputs, plus a **Result**. Leave an object input unwired and the inner graph keeps its own object.

To edit the inner graph, double-click its card or click **Open**. The breadcrumb above the editor (for example *Outer > Inner*) shows where you are; click it or press **Escape** to step back out. Changes inside affect only that copy.

Graphs can be nested up to 8 deep. Deeper than that, the graph shows *Graphs can be nested at most 8 deep. Apply or remove a graph inside this one to build it.*

## Related Topics

- [Components](components.md) - Another way to show just a few settings for a group of parts
- [Expressions](expressions.md) - Formulas in settings
- [Object References](object-references.md) - Reading another object's settings with `Name.Property`
- [Variable Sheet](variable-sheet.md) - Shared values for a design
