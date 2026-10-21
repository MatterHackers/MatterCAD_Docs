---
title: Screw
articleKey: ScrewObject3D
parent: "Mechanical Parts"
nav_order: 4
description: Make a standard metric screw or bolt, or the threaded, clearance or pilot hole for one, by picking its size.
keywords: bolt, fastener, socket head, countersink, cap screw, machine screw
---
# Screw

Screw generates a complete fastener -- head, shank, thread and tip -- from a standard size you pick off a list. Choose M6 and you get an M6 screw with the right pitch, the right head proportions and the right hex socket, without looking anything up. Turn on **Use As Hole** and the same settings make the hole that screw fits instead: threaded, clearance or pilot, with a pocket for the head.

<!-- IMAGE_NEEDED: Screenshot of a Screw in the 3D view with the Properties panel open, showing the Measurement buttons, the Size dropdown and the Head Type icon row -->

Where [Threads](threads.md) gives you a bare threaded rod (or the threaded hole it fits), Screw gives you the whole fastener, or the whole hole for one, head pocket included.

## How to Use

1. Open **Included > Mechanical** in the Library (or under **Add to Bed**) and add **Screw** to the bed
2. Choose **Metric** or **Inch**
3. Pick the **Size** you want
4. Set the **Length**, then the head and drive to suit

Everything else takes standard values for the size you chose. The model is always built in mm, whichever measurement system you specify it in.

## Making the Hole for a Screw

1. Add a Screw and set it up like the screw you will use: size, length and head type
2. Turn on **Use As Hole**. The screw becomes a hole (its Output is set to Hole in the same undo step), and the rows for the drive and the tip disappear, since a hole has neither
3. Choose the **Hole Type**:
   - **Tapped** (default) - The hole carries the thread, for screwing straight in
   - **Clearance** - A plain hole the screw passes through freely
   - **Pilot** - A plain hole sized for the screw to cut its own thread into the plastic
4. Move the hole into your part, sink it until the head's pocket reaches the surface (raise **Head Clearance** if it doesn't), then select both and [Combine](../operations/boolean/combine.md) them. A hole cuts away whatever it overlaps

The hole always includes room for the head: a round counterbore for Socket, Button and Pan heads, a cone topped by a counterbore for a Flat head, and a six-sided pocket for a Hex head. Turn **Use As Hole** off again and the screw is solid once more.

## Parameters

### Usage

- **Use As Hole** - Off by default. Turn it on to build the hole this screw fits instead of the screw
- **Hole Type** - **Tapped** (default), **Clearance** or **Pilot** (see above). Shown only with Use As Hole on
- **Tolerance** - Extra room for the fit, in mm (default 0.2; the slider runs 0 to 0.5). A bigger value makes a looser fit. Type a bigger value, or let go of the slider at its end, and the slider grows to fit, up to 10 mm, which is also the most Tolerance takes. Shown only with Use As Hole on
- **Countersink Ends** - On by default. Adds a cone at both ends of the thread so the screw starts easily and the edge of the hole stays clean. Shown only for a Tapped hole
- **Head Clearance** - How far the pocket for the head reaches above the top of the head, in mm (the slider runs 0 to 50 and grows for a bigger value, up to 1000 mm, which is also the most it takes). It follows the head's height (6 for the default M6 socket head) until you type a value of your own. Shown only with Use As Hole on

### Thread

- **Measurement** - **Metric** (default) or **Inch**. This only chooses which table of standard sizes you pick from; the model is built in mm either way
- **Size** (metric) - M2, M2.5, M3, M4, M5, M6 (default), M8, M10, M12, or **Custom**
- **Size** (inch) - #2-56, #4-40, #6-32, #8-32, #10-24, #10-32, 1/4-20 (default), 1/4-28, 5/16-18, 3/8-16, or **Custom**. The number after the dash is the threads per inch
- **Thread Spacing** - Coarse or Fine. Coarse is the usual choice; fine threads hold better in thin material and resist loosening. Only shown for metric sizes that have a fine pitch defined -- the inch sizes name their own pitch, so there is nothing for the switch to do there. Also hidden for a Clearance hole, whose size does not depend on the pitch

With a standard size chosen, **Diameter** and **Pitch** are shown as read-only values so you can see what you are getting. Choose **Custom** and they become editable:

- **Diameter** - The outside diameter of the thread, measured crest to crest
- **Pitch** - The distance from one thread crest to the next
- **Thread Direction** - **Right Hand** (default) threads tighten clockwise. **Left Hand** threads tighten counterclockwise, and are used where normal rotation would loosen a fastener. Not shown for a Clearance or Pilot hole

A Clearance hole has no Pitch row, because its size does not depend on the pitch.

### Length

- **Length** - Distance from under the head to the tip of the screw, in mm (default 20; the slider runs 2 to 100 and grows for a longer screw, up to 1000 mm, which is also the most it takes)
- **Threading** - **Fully Threaded** (default) carries thread the whole way. **Partially Threaded** leaves a smooth shank under the head, which centres the parts being joined. Not shown for a Clearance or Pilot hole
- **Thread Length** - How much of the length carries thread, measured up from the tip, in mm (default 12; the slider runs 2 to 100 and grows for a bigger value, up to 1000 mm). It can't be more than **Length**. Only shown for a partially threaded screw

### Head

- **Head Type** - **Socket** (a straight cylindrical head with a recessed drive, the most common cap screw head), **Button** (low and domed, for where a socket head would stand too proud), **Flat** (a cone, 90 degrees for metric sizes and 82 degrees for inch sizes, that sits flush in a countersunk hole), **Pan** (wide with a rounded top edge, for general purpose machine screws), or **Hex** (six sided, turned with a wrench)
- **Custom Head Size** - Off by default, in which case **Head Diameter** and **Head Height** are shown read-only at the standard proportions for the head type. Turn it on to type your own
- **Head Diameter** - The width of the head. For a hex head this is measured across the flats
- **Head Height** - How far the head stands above the part

Socket is the default head.

### Drive

The drive rows are not shown when Use As Hole is on.

- **Drive Style** - The recess cut into the head for the tool that turns the screw: **Hex** (turned with a hex key), **Torx** (six lobed, carries more torque than a hex of the same size), **Square**, **Slotted** (a single straight slot), **Phillips** (a crossed recess), or **None** (no recess at all -- for hex heads only ever turned by a wrench). Hex is the default
- **Custom Drive Size** - Off by default, in which case **Drive Size** is shown read-only at the size that goes with the thread. Turn it on to type your own. Hidden when the drive style is None
- **Drive Size** - Across the flats for hex and square, the outside diameter for Torx, and the blade width for slotted and Phillips

### Tip and Geometry

These are the panel's **Tip** and **Geometry** sections.


- **Tip Type** - **Flat** (the threads are cut off square at the end), **Chamfered** (the last turn of thread tapers in so the screw starts easily in a hole -- the default), or **Dog Point** (an unthreaded pilot on the end that lines the screw up before the threads engage). Not shown when Use As Hole is on
- **Sides** - The number of segments around the screw (default 40; the slider runs 8 to 120). Raise it for a smoother model, lower it for a faster one

## Tips

- Mating threads need room. If you are making both the screw and the part it goes into, make the hole from a second Screw of the same size with **Use As Hole** on; raise **Tolerance** if the fit is too tight
- Keep **Sides** low while you experiment with head types and drives -- the thread is the expensive part of the model -- and raise it before you export
- A Chamfered tip is worth keeping: a flat-ended thread is much harder to start
- To make room for a bought fastener, build the Screw at the bought size, turn on **Use As Hole** and pick **Clearance** (the screw passes through) or **Tapped** (it screws in)
- A countersunk (Flat) head gets a matching cone in the hole automatically

## Related

- [Threads](threads.md) - Bare threads, for threaded holes and for adding thread to your own shape
- [Involute Gear](gears.md) - Involute gears
- [Combine](../operations/boolean/combine.md) - Combine a part with a screw hole to cut the hole into it
- [Cylinder](../primitives/cylinder.md) - A plain round column, with no threads
