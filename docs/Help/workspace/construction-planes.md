---
title: Construction Planes
parent: "Workspace"
nav_order: 16
---
# Construction Planes

A construction plane is a flat frame you can put anywhere in space and then work on. It is three values — an **Origin**, a **Normal** and an **X Direction** — and together they answer "where is flat, which way is up, and which way is sideways".

Construction planes are what let a 2D shape be drawn somewhere other than the bed, what let an operation say which way it turns or repeats, and what say where a solid is cut. You will meet one in six places:

- **Plane** on a 2D shape, which is the surface that shape is drawn on
- **Projection Plane** on any operation that consumes paths, which is the surface it flattens its inputs onto
- **Rotate About** on [Rotate](../operations/transform/rotate.md), where the normal is the axis it turns around
- **Central Axis** on a radial [Array](../operations/array/array.md), where the normal is the axis copies circle
- **Plane** on [Plane Cut](../operations/reshape/plane-cut.md), which is where the solid is cut and which side is kept
- **Plane** on [Slice to Path](../operations/reshape/slice-to-path.md), which is where the cross section is taken and the plane its path is drawn on

<!-- IMAGE_NEEDED: The Properties panel for a Circle Path with the Plane control expanded, showing the preset tabs, the Flip switch, the Pick Face button, and the Origin, Normal and X Direction rows -->

## The Three Values

**Origin** — where the plane sits, in the object's own coordinates. For a 2D shape this is where the shape's own zero lands. For Rotate it is the pivot point, and for a radial Array it is the centre of the circle.

**Normal** — the direction the plane faces. The plane itself is everything perpendicular to this. You do not have to give a unit-length vector; any length works and MatterCAD normalizes it.

**X Direction** — which way is "right" on the plane, in other words how the flat work is spun within the plane. Leave it at `0, 0, 0` and MatterCAD chooses a direction for you. Anything you give that points along the normal is ignored: only the part lying in the plane is used.

Rotate and Array use only the Origin and the Normal — spinning the plane with X Direction makes no difference to an axis.

## Presets

The row of tabs above offers three ready-made facings, and the **Flip** switch under them turns any of them over:

| Tab | Faces | Flipped | Use it for |
| --- | --- | --- | --- |
| **XY** | up, `+Z` | down, `-Z` | flat on the bed, the default |
| **XZ** | forward, `-Y` | back, `+Y` | standing up, facing you |
| **YZ** | right, `+X` | left, `-X` | standing up, facing sideways |

Flipping is the same flat surface seen from the other side; only the facing reverses. That matters where a direction is a direction and not just a surface: which way an extrude grows, and which way around a Rotate or a radial Array turns.

The tabs say which way the plane **faces**, and nothing else. A Plane Cut lying flat ten high is still an XY plane, so XY stays lit and the `10` shows in the Origin row below — where the plane sits is yours, not the preset's. Choosing a tab re-aims the Normal and clears the X Direction (which only means anything relative to a normal), but leaves the Origin exactly where you put it, all in a single undo step. Flip does the same: it turns the normal over and leaves the plane where it is.

The fourth tab, **Custom**, lights up on its own whenever the plane faces none of those six ways — picked off a slanted face, typed by hand, or driven by an expression. You can also click it yourself at any time: it changes nothing, it only shows the **Plane Values** section. That section appears on its own whenever there is something in the values the tabs cannot say — an Origin that is not `0, 0, 0`, an X Direction of your own, an expression, or a normal that is none of the six.

## Expressions

Each of the three values takes an [expression](expressions.md) per component, so a plane can be driven by the rest of the design rather than typed in. Write `=` and then the formula, exactly as anywhere else:

- `=sheetHeight` in the Origin's Z, to lift a sketch plane to a height a [Variable Sheet](variable-sheet.md) owns
- `=Lid.Height` in the Origin's Z, to sit a plane on another object using an [object reference](object-references.md)
- `=360/Count` driving the parts of a Normal, to swing a plane as a count changes

A plane whose values are expressions is re-evaluated whenever anything it depends on changes, so the shapes on it move with the design.

## Pick Face

Rather than typing a normal, you can take one off a model.

1. Click **Pick Face**. The button becomes **Cancel Pick** and the cursor becomes a crosshair
2. Move the pointer over any object in the scene — the whole flat face under it highlights, not just the one triangle
3. Click the highlighted face

The face's plane is written into Origin, Normal and X Direction as exact numbers, and the picking session ends. It is one undo step, so a wrong pick is a single [undo](undo-redo.md) away.

<!-- IMAGE_NEEDED: The 3D view during a Pick Face session, with a slanted face of a model highlighted under the crosshair cursor and the Cancel Pick button visible in the Properties panel -->

A pick is cancelled by pressing **Esc**, by clicking **Cancel Pick**, by choosing a viewport tool such as Rotate or Translate, or by selecting a different object. Nothing is changed when a pick is cancelled.

Because a pick writes plain numbers, the plane does not follow the face afterwards. Move or re-shape the model you picked from and the plane stays where it was — pick again to catch up, or use expressions if you need the plane to track something.

## Planes on 2D Shapes

Every 2D shape carries a **Plane**: [Circle](../2d-paths/circle-path.md), [Box](../2d-paths/box-path.md), [Ring](../2d-paths/ring-path.md), [Star](../2d-paths/star-path.md) and [Custom](../2d-paths/custom-path.md) paths, and the shape-producing objects such as [Text](../primitives/text.md), [Gears](../mechanical/gears.md) and Image to Path.

The shape is still drawn the same way, with the same width and height and radius; the Plane only decides where that flat drawing lives. Set a Box Path's Plane to XZ and it stands up; give it an Origin of `0, 0, 20` and it stands up twenty millimetres above the bed.

A shape left on the default XY plane behaves exactly as it always did, which is what files made before construction planes get when they are opened.

## How Path Operations Choose a Plane

Operations that consume paths — [Linear Extrude](../operations/path/linear-extrude.md), [Revolve](../operations/path/revolve.md), [Loft](../operations/path/loft.md), [Sweep](../operations/path/sweep.md), the path [booleans](../operations/boolean/index.md), [Inflate](../operations/path/inflate-path.md), [Outline](../operations/path/outline-path.md), [Smooth](../operations/path/smooth-path.md) and [Border](../operations/path/border-path.md) paths, [Select Paths](../operations/path/select-paths.md), and [Fillet](../operations/reshape/fillet.md) and [Chamfer](../operations/reshape/chamfer.md) when they act on a path — all have a **Projection Plane** section. Since their inputs may be drawn on different planes, the operation needs one plane to flatten them onto before it can work.

**Source** chooses where that plane comes from:

- **Auto** (the default) — the plane of the first input path, wherever it was drawn and however it has been moved. When that path is on plain XY the result is XY, which is what a file saved before construction planes gets. Inputs that are not on that plane are still flattened onto it.
- **Child** — the plane of one input you name. A **Projection Plane Child** dropdown appears; choose exactly one of the operation's own paths.
- **Custom** — a plane you author on the operation itself, with the same Origin, Normal, X Direction, presets and Pick Face as everywhere else. The three rows appear when you choose Custom.

### Warnings

The section ends in a message row that is blank when all is well. Two things can appear there:

**"The input paths are not coplanar. Auto projects them onto the automatically selected projection plane."**

Your inputs are not all on one plane, and Auto has picked the first one's. Everything else is being squashed onto it, which is rarely what you drew. Either put the inputs on a common plane, or set Source to Child (or Custom) and name the plane you actually want. A Loft is the exception that proves the rule: stacking its sections at different heights is the whole point, so a Loft only warns when its sections face different directions.

**"The projection plane child is missing or is not a single path. Using Auto."**

Source is set to Child, but the named child has been deleted, or the selection is not exactly one path. The operation has fallen back to Auto so it still builds. Re-open the Projection Plane Child dropdown and choose one path.

## Related

- [2D Paths](../2d-paths/index.md) — the flat shapes that a Plane places
- [Expressions](expressions.md) — drive a plane's Origin, Normal or X Direction from the rest of the design
- [Rotate](../operations/transform/rotate.md) — turns about a construction plane's normal
- [Array](../operations/array/array.md) — a radial array circles a construction plane's normal
