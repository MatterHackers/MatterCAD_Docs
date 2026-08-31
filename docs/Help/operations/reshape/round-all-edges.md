---
title: Round All Edges
articleKey: RoundAllEdgesObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 10
---
# Round All Edges

Round All Edges rolls every outside edge and corner of a solid off at one radius. There is nothing to pick and nothing to select -- you give it a radius and it rounds the whole part.

<!-- AUTO_IMAGE: type=from_mcx file=reshape_round_all_edges -->
![reshape_round_all_edges](https://matterhackers.github.io/MatterCAD_Docs/assets/reshape_round_all_edges.png)

It is the answer to "which edges?" being "all of them". Where [Fillet](fillet.md) asks you to click the edges you want and can give each one its own radius, this one takes the whole part at a single radius and needs no clicks at all.

## How to Use

1. Select a solid part
2. Click **Round All Edges** in the Reshape group of the toolbar
3. Set the **Radius**
4. Wait -- this one takes real time, and shows a progress bar while it works

## Parameters

- **Radius** - How far every outside edge is rounded. It is the radius of the largest ball that would roll over the whole part. The part has to be thicker than twice this everywhere (default: 1 mm)
- **Segments** - How finely the rounding ball is drawn (default: 12). This is the single biggest lever on how long the operation takes, because the ball's detail is paid for on every triangle of the part. 12 is smooth enough for a rounding of any normal size; raise it only if you can see the facets

## It Takes Time, and You Can Stop It

Round All Edges is much slower than a Fillet on a few edges, and honestly so -- it does real work over every triangle of the part rather than over a handful of edges. Seconds on a simple part, considerably longer on a detailed or imported one.

While it runs there is a progress bar in the task area with a **Cancel** button beside it. Cancelling leaves the part as it was, unrounded, and costs nothing but the time already spent.

Two things keep the bill down:

- **Keep Segments low.** It multiplies into every step of the work
- **Round last.** Do it once, at the end, on the finished shape

Dragging the Radius slider does not queue one run per pixel: the operation coalesces the changes, so a drag of any length costs about two runs -- the one it started with and the one for where the slider ended up.

## When It Refuses

Round All Edges can only round a part that is thicker than the rounding everywhere, so a radius that is too big is refused rather than applied. It says so before starting where it can, so you are not made to wait for a result that was never possible:

> A radius of 6 would round Cube away to nothing. Half its smallest side is 5, so the radius has to be under that - and a thin feature inside it may need less still.

That is the bounding-box check -- fast, and honest about its limits. A part that is 40 mm across can still have a 1 mm web in the middle of it, so the second message appears when the work has actually been done and found nowhere the ball fits:

> A radius of 3 rounds Bracket away to nothing - somewhere it is thinner than 6, which is twice the radius. Half its smallest side, 20, is the most it could ever take.

Read both as "the radius has to be smaller than this". The first number is the radius you asked for; the last is the ceiling.

Two other refusals are simpler:

- *"Round All Edges rounds the edges of a solid. Use Fillet to round the corners of a 2D path."* -- there is nothing for a ball to roll along on a flat path. Use [Fillet](fillet.md) instead
- *"Round All Edges needs a radius greater than zero."*

## When to Prefer It Over Per-Edge Fillets

Use **Round All Edges** when:

- you want every outside edge softened and do not care which is which -- a handle, a case, a toy, anything meant to be pleasant to hold
- the part is imported or organic, with far too many edges to pick sensibly
- one radius everywhere is the design intent, not a compromise

Use [Fillet](fillet.md) when:

- only some edges should be rounded, or different edges want different radii
- you need the inside corners rounded too. Round All Edges only touches outside (convex) edges; it leaves inside corners exactly as they are
- the part is large or detailed and you do not want to pay for whole-part work
- you want the selection to be a parametric part of the design that survives changes to the shape underneath

## Tips

- The radius is measured in the source part's own units, so a part with a non-uniform scale on it rounds into an oval rather than a circle. Scale before rounding, not after
- It rounds outside edges only. If you need the inside of a pocket softened as well, add a [Fillet](fillet.md) on those edges
- The result is a new solid, so booleans, transforms and everything else work on it normally
- If you only want a soft break on the edges rather than a visible round, a small [Chamfer](chamfer.md) on the edges that matter is much faster

## Related

- [Fillet](fillet.md) - Round chosen edges, each at its own radius
- [Chamfer](chamfer.md) - Cut chosen edges flat
- [Hollow Out](hollow-out.md) - Another whole-part operation with a similar cost profile
- [Decimate](../mesh/decimate.md) - Reduce a heavy mesh before rounding it
