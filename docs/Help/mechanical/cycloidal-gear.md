---
title: Cycloidal Gear
articleKey: CycloidalGearObject3D
parent: "Mechanical Parts"
nav_order: 5
---
# Cycloidal Gear

Cycloidal Gear generates the flat parts of a cycloidal drive -- the single stage speed reducer built from a lobed disc rolling inside a ring of pins. It is the mechanism inside a lot of robot joints and printed gearboxes, because it gets a large reduction out of one very compact stage.

<!-- IMAGE_NEEDED: Screenshot of a Cycloidal Gear disc and pin ring side by side in the 3D view, with the Properties panel showing the Part tabs -->

## How a Cycloidal Drive Works

An eccentric on the input shaft pushes a lobed disc so that it *wobbles* rather than spins -- the disc's centre walks a small circle around the ring's centre. The lobes press against a ring of pins as it goes, and because there is one fewer lobe than there are pins, each full turn of the input advances the disc by exactly one pin. So the disc turns one lobe's worth for every whole input revolution: a 10-pin ring gives a 9-lobe disc and a 9:1 reduction.

That slow rotation is taken out of the disc through a set of oversized holes near its centre, which ride on output pins standing in a plate. The holes are drawn larger than the pins by twice the eccentricity, which is exactly the room the pins need to stay in contact as the disc walks around.

**A drive is a matched pair.** The Disc and the Pin Ring have to be built with the same Pin Count, Pin Circle Diameter, Pin Diameter and Eccentricity or they will not run together. MatterCAD remembers those numbers per user, so adding a Disc and then a Pin Ring gives you two parts on the same settings.

## How to Use

1. Open the Mechanical group in the library and drag **Cycloidal Gear** onto the bed
2. Leave **Part** on **Disc** and set the sizes you want
3. Add a second Cycloidal Gear and switch its **Part** to **Pin Ring** -- it comes up on the same numbers
4. Add the eccentric bearing bore, the output pins and the housing yourself

Sizes left at 0 take the value you last used, seeded on first run with a sensible default (60mm pin circle, 6mm pins, 1.5mm eccentricity, 5mm high). **Center Bore Diameter** and **Output Hole Count** are the exceptions: 0 is a real answer there, meaning "no bore" and "no output holes", so those two are not seeded.

## Parameters

### Which part, and how

- **Output** - **3D** builds the part as a solid; **2D** builds it as a flat path that [path operations](../operations/path/index.md) can consume. 3D is the default and is what almost every drive part is wanted as
- **Part** - **Disc** (the lobed rotor) or **Pin Ring** (the ring the pins stand in). The tabs switch which set of controls below is relevant
- **Height** - How thick the part is. Only shown for 3D output

### The drive (both parts)

These four have to match between the disc and the ring:

- **Pin Count** - The number of pins in the ring (default 10, range 3-40). The disc gets one lobe fewer than this, and that lobe count is the reduction ratio of the drive
- **Pin Circle Diameter** - The diameter of the circle the pin centres stand on. This is the working size of the drive
- **Pin Diameter** - The diameter of a single pin. Pins that would touch each other are pulled back, since there has to be ring material between them
- **Eccentricity** - How far the disc's centre is offset from the ring's centre, in mm. This is what the eccentric on the input shaft has to be made to. It cannot reach the pin circle radius divided by the pin count -- the lobes come to points there -- so larger values snap back
- **Clearance** - The running clearance between the disc and the pins, in mm. It is taken off the disc profile and added to the ring's bore. The pins themselves are always drawn at their true size, since they are normally dowels or bearings that have to fit the holes that hold them

### Disc only

- **Center Bore Diameter** - The bore in the middle of the disc, which carries the eccentric bearing. 0 for no bore. It is bounded by the valleys between the lobes -- a bore wider than that leaves nothing to extrude
- **Output Hole Count** - How many output pin holes the disc has (default 6, up to 24). These are what the slow output motion is taken out through. 0 for none
- **Output Hole Circle Diameter** - The diameter of the circle the output pin holes are spaced around
- **Output Pin Diameter** - The diameter of the output pins that run in those holes

### Pin Ring only

- **Ring Edge Width** - The width of the material outside the pins. The slider covers the useful range; a typed or calculated value can go up to 1000

### Computed values (read only)

- **Lobe Count** - The number of lobes on the disc, always one fewer than the Pin Count
- **Reduction Ratio** - How many turns of the input shaft it takes to turn the output once, with the pin ring held still and the output taken off the disc's holes. It is the Lobe Count
- **Output Hole Diameter** - The diameter the output pin holes are actually drawn at, which is the Output Pin Diameter plus twice the Eccentricity. This is the number you have to hold when you drill the plate the output pins stand in
- **Outer Diameter** - The diameter to the outside of the part that was built

## Tips

- Raise the **Pin Count** for more reduction. 10 pins gives 9:1; 21 pins gives 20:1 in the same footprint
- Start from the pin circle. It sets the size of the whole gearbox, and everything else is proportioned inside it
- **Clearance** is the number to reach for when a printed drive binds. Add a little and reprint the disc; the pins are unchanged
- Two discs at 180 degrees to each other balance the wobble out, which is why most real drives use a pair. Duplicate the disc and rotate the second one half a turn of the eccentric
- Switch **Output** to 2D when you want to take the profile into path operations -- [Border Path](../operations/path/border-path.md), or your own [Linear Extrude](../operations/path/linear-extrude.md) with a bevel on it

## Related

- [Gears](gears.md) - Involute gears, for ordinary meshing gear trains
- [Gear 2D](gear-2d.md) - A 2D involute gear path
- [Threads](threads.md) - Screw threads
- [Subtract](../operations/boolean/subtract.md) - Cut the bearing bore and output holes to your own sizes
