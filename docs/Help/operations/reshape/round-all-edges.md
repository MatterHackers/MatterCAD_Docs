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

It is the answer to "which edges?" being "all of them". Where [Fillet](fillet.md) asks you to click the edges you want, this one takes the whole part and needs no clicks at all. Both round at a single radius.

It rounds the edges that stick out, and only those. Its mirror image, [Round Inside Edges](round-inside-edges.md), fills the ones that go in. Neither touches the other's edges, so running both is how you round everything.

This operation is [Erode](erode.md) followed by [Dilate](dilate.md) at the same radius. Use those operations separately when you want just the shrink or grow step.

## How to Use

1. Select a solid part
2. Click **Round All Edges** in the Reshape group of the toolbar
3. Set the **Radius**
4. Wait -- on most parts this takes real time, and shows a progress bar while it works

## Parameters

- **Radius** - How far every outside edge is rounded. It is the radius of the largest ball that would roll over the whole part. The part has to be thicker than twice this everywhere (default: 1 mm)
- **Segments** - How finely the rounding ball is drawn (default: 12). This is the single biggest lever on how long the operation takes, because the ball's detail is paid for on every triangle of the part. 12 is smooth enough for a rounding of any normal size; raise it only if you can see the facets

## How Long It Takes, and How to Stop It

How long this takes depends on one thing about your part, and the two answers are very far apart.

**A part with no dents in it is fast.** If the shape bulges outward everywhere -- a box, a cylinder, a cone, a wedge, a sphere, anything with no pocket, step or notch cut into it -- there is a shortcut, and Round All Edges takes it without being asked. These finish in a blink; the progress bar is barely there.

**A part with an inside corner anywhere on it is slow.** Cut one notch in that box and the shortcut is gone: the work is now done over every triangle of the part rather than over a handful of edges. Seconds on a simple part, considerably longer on a detailed or imported one. This is the case most real parts are in.

You do not have to work out which one you are in -- the operation does that itself, every time, and takes the fast route whenever it is available.

While it runs there is a progress bar in the task area with a **Cancel** button beside it. Cancelling leaves the part as it was, unrounded, and costs nothing but the time already spent.

Two things keep the bill down on the slow case:

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
- you need only SOME of the inside corners rounded. Round All Edges never touches an inside corner; [Round Inside Edges](round-inside-edges.md) rounds all of them at once, and a Fillet is what picks a few
- the part is large or detailed and you do not want to pay for whole-part work
- you want the selection to be a parametric part of the design that survives changes to the shape underneath

## Tips

- The radius is measured in the source part's own units, so a part with a non-uniform scale on it rounds into an oval rather than a circle. Scale before rounding, not after
- It rounds outside edges only. To soften the inside of a pocket as well, add [Round Inside Edges](round-inside-edges.md) after it, or a [Fillet](fillet.md) on just the corners that matter
- The result is a new solid, so booleans, transforms and everything else work on it normally
- If you only want a soft break on the edges rather than a visible round, a small [Chamfer](chamfer.md) on the edges that matter is much faster

## Related

- [Round Inside Edges](round-inside-edges.md) - The mirror image: fills every inside corner instead
- [Fillet](fillet.md) - Round the edges you pick, at a radius you set
- [Chamfer](chamfer.md) - Cut chosen edges flat
- [Hollow Out](hollow-out.md) - Another whole-part operation with a similar cost profile
- [Decimate](../mesh/decimate.md) - Reduce a heavy mesh before rounding it
