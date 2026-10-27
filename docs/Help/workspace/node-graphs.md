---
title: Node Graphs
articleKey: GeometryNodesObject3D, PositionObject3D, CompareObject3D, InsideBoxObject3D, SeparateXyzObject3D, CombineXyzObject3D, MathObject3D, VectorMathObject3D, SwitchObject3D, TransparencyMaskObject3D, IntensityMaskObject3D, ColorMaskObject3D, AnalyzePictureObject3D, TraceMaskObject3D, LineCopiesObject3D, CircleCopiesObject3D, StepCopiesObject3D, AdjustCopiesObject3D, PlaceOnCopiesObject3D
parent: "Workspace"
nav_order: 18
description: Build a part by wiring nodes together in a graph instead of stacking operations in the tree.
keywords: nodes, graph, visual programming, node editor, wires, procedural, arithmetic, conditional, variants, copies
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
- **Sockets** are the dots on a card's edges: inputs on the left, outputs on the right. Their colour says what they carry - green for solids, blue for paths, grey for numbers, lilac for yes/no values, indigo for positions and sizes (an X, Y and Z together), orange for 3D curves, plum for images, lime for copies, pink for Variables. A single number or yes/no is drawn as a short bar instead of a dot. Hover a socket to see its name.
- **Diamond sockets** are selections: they carry an answer for each edge or corner, not one value. See **Choose Edges with Selection Nodes** below.
- **Noodles** are the wires. Drag from an output socket and drop on an input socket of the same colour to connect them. To move a noodle, pick it up by the end at its input and drop it somewhere else; drop it on empty space to remove it. A noodle that would make a loop is refused, and so is one between sockets that don't match - the editor tells you why, for example *Types don't match: geometry into image*. A noodle into a diamond socket is dashed.

Scroll the mouse wheel to zoom, and drag with the right or middle mouse button to pan.

## Add and Delete Nodes

- Press **Shift+A**, or right-click on empty space, to open the **Add Node** menu at the pointer. It lists **Shapes**, **2D Shapes**, **Image** (Image, Transparency Mask, Intensity Mask and Trace Mask), **Operations**, **Math** (Separate XYZ, Combine XYZ, Math and Vector Math), **Copies** (Line Copies, Circle Copies, Step Copies, Adjust Copies and Place on Copies), **Sheet**, **Selection** (Position, Compare and Inside Box), **Flow** (Switch) and **My Tools**; type to search. The node you pick lands at the pointer, unwired and selected. If a node is selected and the new one can take its result, the new node goes in after it instead - to its right, wired to it and to whatever it fed - so picking Linear Extrude with a Circle selected gives *Circle -> Linear Extrude -> Output*.
- Drag a noodle from a socket and let go on empty space to open the Add Node menu there. It lists only the nodes that can take that noodle, and the one you pick lands wired to it.
- With a graph shown, the toolbar's operation buttons add a node to the graph you are looking at.
- Drag an object from the scene tree onto the editor to move it into the graph, or drag an item from the Library to add a copy.
- To delete a node, select it and press **Delete** or **Backspace**, or right-click its card and choose **Delete Node**. Its noodles go with it. Input and Output can't be deleted.

Every one of these is a single undo step.

## Operations as Nodes

Most toolbar operations are also nodes. Wire a shape or an outline into an operation's **Source** and wire its **Result** on to the next node or the Output. A few operations have their own inputs:

- **Translate**, **Rotate**, **Scale** and **Fit to Bounds** take whatever you wire in, solid or outline, and give back the same kind of thing, so *Circle -> Translate -> Linear Extrude* works. Rotate turns the parts about their own centre, Scale grows them from their bottom centre, and Fit to Bounds fits them in a box centred on them - so the node keeps working when what is wired in changes size or moves. Wire a parameter into a Scale's Width, Depth or Height to size the part to that number.
- **Subtract** has a **Keep** input (the parts that stay) and a **Remove** input (the parts cut out of them). **Subtract & Replace** has **Keep** and **Replace**: the Replace parts are cut from the Keep parts and left in the hole. Switching a node between the two keeps its noodles.
- **Loft** has one **Sections** input that takes as many outlines as you like. They are stacked by height, lowest first, so the order you wire them in doesn't matter. To raise a section, wire it through a Translate first.
- **Sweep** has a **Profile** (the outline to carry) and a **Rail** (the path to carry it along). Only a 3D Curve's result - the orange socket - fits the Rail. With nothing wired into the Rail, the sweep follows the S-shaped rail it was made with.
- **Image to Path** takes a picture through its plum **Source** socket. Drag an image from the Library or the scene tree into the graph and wire its result there; Image to Path traces the outline, which you can then wire into Linear Extrude like any other outline. Only an image fits this socket. (The Image Converter is not a node; it stays a shape you drop in from the Library.)
- **Bounds** takes parts in and gives back a box that fits them, plus the box's **Min**, **Max**, **Size** and **Center** as values (see **Values Between Nodes** below).
- **Fillet** and **Chamfer** as nodes round (or cut) **every sharp edge** of what is wired in, since a card has no 3D view to click edges in. Fed an outline, they round every corner. To round only some, wire a selection into their **Selection** diamond (see **Choose Edges with Selection Nodes** below). Unchecking Selection, with nothing wired in, rounds none. The toolbar's Fillet and Chamfer still round only the edges you click.

## Values Between Nodes

Some nodes give values as well as, or instead of, a part: a **Bounds** gives its **Min** (low corner), **Max** (high corner), **Size** and **Center**, and a [Measure Tool](measure-tool.md) gives its **Distance**. Wire one of these outputs into a setting on another card and the setting follows it every time the graph rebuilds. The card shows the value the last rebuild worked out, in your units.

Min, Max, Size and Center are each an X, Y and Z together (the indigo socket). To use just one number:

- **Separate XYZ** (Add Node > Math) splits a position or size into its **X**, **Y** and **Z**. For example, wire the Bounds' **Size** into Separate XYZ's **Vector** and its **Z** into a Cube's **Height** to make the cube exactly as tall as the parts in the Bounds.
- **Combine XYZ** does the reverse: three numbers in, one position or size out.
- In a formula, add the letter: `=Bounds.Max.Z` is the top of the Bounds box, and `=Bounds.Size.X` its width. Inside a graph, wire the Bounds card's Variables socket to the card whose formula reads it, as for any formula (see **Formulas Inside a Graph** below).

## Math and Vector Math

**Math** (Add Node > Math) works out a number from two numbers, **A** and **B**. Pick what it does on its card: Add, Subtract, Multiply, Divide, Power, Minimum, Maximum, Modulo, Absolute, Round, Floor, Ceiling, Square Root, Sine, Cosine, Tangent or Clamp. Sine, Cosine and Tangent take A as an angle in degrees, and Clamp keeps A between B and **Max**. Type A and B on the card, or wire values into them, and wire its **Result** into any setting on another card - a Cube's Width, say, or a Compare's B.

**Vector Math** does the same for positions and sizes (an X, Y and Z together). Its operations are Add, Subtract, Multiply, Scale (A times the number **Scale**), Length, Distance, Dot, Cross, Normalize, Minimum and Maximum. Operations that give a position or size come out of **Vector**; Length, Distance and Dot give a single number, which comes out of **Value**.

Both work in plain numbers, so a factor of 2 stays 2 whatever units you use. When an operation has no answer - dividing by zero, the square root of a negative number, the tangent of 90 degrees - the result is 0 and the card shows a warning saying what to change.

For example, to make a hole half the width of a part: wire a Bounds' **Size** through **Separate XYZ**, wire its **X** into a Math set to **Divide** with B at 2, and wire the Result into a Cylinder's Diameter.

## Switch Between Branches

A **Switch** (Add Node > Flow) passes on one of its inputs and ignores the rest, so one graph can make several versions of a part.

- Wire a choice parameter (a setting with a drop-down of options) into its **Choose** input and the Switch gets one input per option, named after it. Wire a different part into each, and the option picked in the Properties panel decides which part comes out of its **Result**.
- Wire a yes/no value into Choose and the inputs are **False** and **True**.
- With anything else, or nothing, wired into Choose, the inputs are numbered; set how many with **Options**, and type the number or name of the one to pass on into **Choose**.

Only the chosen branch is built, so a graph with many options stays quick. If Choose names no input, or nothing is wired into the chosen one, the Switch passes nothing on and its card says why.

## Trace a Picture with Masks

The Image nodes split **Image to Path** into steps you can see and change:

1. Add an **Image** (Add Node > Image) and pick its picture on its card, or drag a picture in from the Library.
2. Wire it into a mask. **Transparency Mask** keeps the picture's solid (not see-through) pixels. **Intensity Mask** keeps the pixels whose brightness is inside its **Select Range**, set on the histogram on its card. **Color Mask** splits the picture into its most distinct colors and keeps the pixels nearest the colors you tick on its card, as Image to Path's Colors tab does; its **Colors** output lists those colors. The card shows the mask it makes.
3. Wire the mask into **Trace Mask**. It traces the mask's outline into a path, leaving out pieces smaller than **Min Surface Area**.
4. Wire Trace Mask's result into **Linear Extrude**, or any other node that takes an outline.

The same picture at the same size traces to the same outline Image to Path gives. A picture wired straight into Trace Mask traces its solid pixels.

To let the picture choose, wire it into **Analyze Picture** too. It gives the analysis Image to Path would pick for that picture - Transparency, Colors or Intensity - so wired into a **Switch**'s Choose, with each mask wired into the option of the same name, it passes on the mask that suits the picture.

## Copies

The Copies nodes make many copies of a part, as the [Array](../operations/array/array.md) does, with each step a node you can see and wire:

- **Line Copies** gives a row of placements: **Count** copies, each one **Offset** further on, or spread evenly up to an **Endpoint**, or each a share of the part's size (**Relative Offset**, 1 puts them side by side).
- **Circle Copies** gives a ring: **Count** copies, or as many as fit at **Angle Between**, **Radius** from the **Central Axis**, all the way round or over an arc of **Sweep Angle**. With **Face the Center** on, each copy turns with its place around the circle.
- **Step Copies** gives copies that each move by **Translation**, turn by **Rotation** and scale by **Scale** once more than the one before - spirals, stairs and shrinking rows.
- **Adjust Copies** takes a list of copies and moves, turns and scales every one by **Offset**, **Rotation** and **Scale**. Turn **Randomize** on to add a random amount to each copy, up to **Random Offset**, **Random Rotation** and **Random Scale Axes**. The same **Seed** always gives the same copies; change it for a different mix. **Skip First** and **Skip Last** leave an end copy in place.
- **Place on Copies** puts a copy of the part wired into its **Geometry** at every placement wired into its **Copies**. **Create Single Mesh** joins them into one mesh (with **Merge**, points closer than **Distance** become one). An outline wired in gives outlines out, so *Circle -> Place on Copies -> Linear Extrude* extrudes every copy.

The copies sit exactly where an Array with the same settings puts them. A Copies socket (lime) only connects to another Copies socket.

For example, wire a Cube into Place on Copies' **Geometry** and a Line Copies into its **Copies**, then wire Place on Copies into the Output: the graph shows a row of cubes, as many as Line Copies' Count.

## Choose Edges with Selection Nodes

A Fillet or Chamfer node rounds every sharp edge until you tell it which ones. You tell it with a **selection**: a question the fillet asks about each edge (or, for an outline, each corner), such as "is this edge above 5 mm?". Edges that answer yes are rounded; the rest are left sharp.

Selections travel through **diamond sockets** on **dashed noodles**. A diamond's output only goes into a diamond input - otherwise the editor says *A field only goes into a diamond socket*. A diamond input with a dot in it also takes a plain value, which then answers the same for every edge.

The selection nodes are in the Add Node menu's **Selection** group:

- **Position** gives each edge's own position (for a straight edge, its middle). Wire it through **Separate XYZ** to test just its X, Y or Z.
- **Compare** tests A against B: **Greater Than**, **Less Than**, **Equal To**, **At Least** or **At Most**. Choose **Within Distance** instead to select the edges within a **Distance** of a **Point**. Numbers are in your units.
- **Inside Box** selects the edges inside the box from **Min** to **Max**. An edge lying on the box's surface counts as inside.

<!-- IMAGE_NEEDED: A Cube wired into a Fillet node, with Position -> Separate XYZ -> Z -> Compare (Greater Than 10) wired by a dashed noodle into the Fillet's diamond Selection socket, and only the top edges rounded in the 3D view -->

### Example: Round Only the Top Edges

1. Add a **Cube** and a **Fillet** node, and wire the Cube into the Fillet's Source and the Fillet into the Output. Every edge is rounded.
2. Add **Position**, **Separate XYZ** and **Compare**.
3. Wire Position into Separate XYZ's **Vector**, and Separate XYZ's **Z** into Compare's **A**.
4. Set Compare to **Greater Than** and **B** to the height of the Cube's middle (10 for a 20 mm Cube sitting on the floor).
5. Wire Compare's result into the Fillet's **Selection**.

Only the edges higher than the middle - the four top edges - are rounded. The upright edges stay sharp, because their middles are not higher than B.

### Example: Round the Edges Inside Another Part's Box

1. Wire the part whose edges you want to round into a **Fillet** node.
2. Wire a second part - one that overlaps the corner you want rounded - into a **Bounds** node.
3. Add **Inside Box**. Wire the Bounds' **Min** into its **Min** and the Bounds' **Max** into its **Max**.
4. Wire Inside Box into the Fillet's **Selection**.

Only the edges inside the second part's box are rounded. Move or resize the second part and the rounded edges follow.

### Example: Round the Corners on the Right of an Outline

1. Drag a **Box** from the Library's 2D Shapes into the graph. Wire it into a **Fillet** node, and the Fillet into a **Linear Extrude**. Every corner is rounded.
2. Add **Position**, **Separate XYZ** and **Compare**. Wire Position into Separate XYZ, and its **X** into Compare's **A**.
3. Set Compare to **Greater Than** and **B** to an X between the left and right sides of the outline (0 for an outline centred on the origin).
4. Wire Compare into the Fillet's **Selection**.

Only the corners on the right are rounded. To round the corners near one spot instead, set Compare to **Within Distance** and type the spot into **Point**.

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

- [Fillet](../operations/reshape/fillet.md) - Rounding edges, and picking them in the 3D view
- [Image to Path](../operations/image/image-to-path.md) - Tracing a picture's outline in one step
- [Bounds](../operations/placement/bounds.md) - A box that fits other parts, and its Min, Max, Size and Center
- [Components](components.md) - Another way to show just a few settings for a group of parts
- [Expressions](expressions.md) - Formulas in settings
- [Object References](object-references.md) - Reading another object's settings with `Name.Property`
- [Variable Sheet](variable-sheet.md) - Shared values for a design
