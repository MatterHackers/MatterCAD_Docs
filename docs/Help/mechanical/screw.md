---
title: Screw
articleKey: ScrewObject3D
parent: "Mechanical Parts"
nav_order: 4
---
# Screw

Screw generates a complete fastener -- head, shank, thread and tip -- from a standard size you pick off a list. Choose M6 and you get an M6 screw with the right pitch, the right head proportions and the right hex socket, without looking anything up.

<!-- IMAGE_NEEDED: Screenshot of a Screw in the 3D view with the Properties panel open, showing the Measurement tabs, the Size dropdown and the Head Type icon row -->

Where [Threads](threads.md) gives you a bare threaded cylinder to build with, Screw gives you the whole fastener. Use Threads when you want to cut a threaded hole or add thread to a shape of your own; use Screw when you want the fastener itself, or a body to subtract to leave a clearance pocket.

## How to Use

1. Open the Mechanical group in the library and drag **Screw** onto the bed
2. Choose **Metric** or **Inch**
3. Pick the **Size** you want
4. Set the **Length**, then the head and drive to suit

Everything else takes standard values for the size you chose. The model is always built in mm, whichever measurement system you specify it in.

## Parameters

### Size

- **Measurement** - Metric or Inch. This only chooses which table of standard sizes you pick from; the model is built in mm either way
- **Size** (metric) - M2, M2.5, M3, M4, M5, M6, M8, M10, M12, or **Custom**
- **Size** (inch) - #2-56, #4-40, #6-32, #8-32, #10-24, #10-32, 1/4-20, 1/4-28, 5/16-18, 3/8-16, or **Custom**. The number after the dash is the threads per inch
- **Thread Spacing** - Coarse or Fine. Coarse is the usual choice; fine threads hold better in thin material and resist loosening. Only shown for metric sizes that have a fine pitch defined -- the inch sizes name their own pitch, so there is nothing for the switch to do there

With a standard size chosen, **Diameter** and **Pitch** are shown as read-only values so you can see what you are getting. Choose **Custom** and they become editable:

- **Diameter** - The outside diameter of the thread, measured crest to crest
- **Pitch** - The distance from one thread crest to the next

### Thread

- **Thread Direction** - Right hand threads tighten clockwise. Left hand threads tighten counterclockwise, and are used where normal rotation would loosen a fastener
- **Length** - Distance from under the head to the tip of the screw (default 20mm)
- **Threading** - **Fully Threaded** carries thread the whole way. **Partially Threaded** leaves a smooth shank under the head, which centres the parts being joined
- **Thread Length** - How much of the length carries thread, measured up from the tip. Only shown for a partially threaded screw

### Head

- **Head Type** - **Socket** (a straight cylindrical head with a recessed drive, the most common cap screw head), **Button** (low and domed, for where a socket head would stand too proud), **Flat** (a 90 degree cone that sits flush in a countersunk hole), **Pan** (wide with a rounded top edge, for general purpose machine screws), or **Hex** (six sided, turned with a wrench)
- **Custom Head Size** - Off by default, in which case **Head Diameter** and **Head Height** are shown read-only at the standard proportions for the head type. Turn it on to type your own
- **Head Diameter** - The width of the head. For a hex head this is measured across the flats
- **Head Height** - How far the head stands above the part

### Drive

- **Drive Style** - The recess cut into the head for the tool that turns the screw: **Hex** (turned with a hex key), **Torx** (six lobed, carries more torque than a hex of the same size), **Square**, **Slotted** (a single straight slot), **Phillips** (a crossed recess), or **None** (no recess at all -- for hex heads only ever turned by a wrench)
- **Custom Drive Size** - Off by default, in which case **Drive Size** is shown read-only at the size that goes with the thread. Turn it on to type your own. Hidden when the drive style is None
- **Drive Size** - Across the flats for hex and square, the outside diameter for Torx, and the blade width for slotted and Phillips

### Tip and Geometry

- **Tip Type** - **Flat** (the threads are cut off square at the end), **Chamfered** (the last turn of thread tapers in so the screw starts easily in a hole -- the default), or **Dog Point** (an unthreaded pilot on the end that lines the screw up before the threads engage)
- **Sides** - The number of segments around the screw (default 40). Raise it for a smoother model, lower it for a faster one

## Tips

- Printed threads need clearance. If you are printing both the screw and the part it goes into, make the hole from a Screw with a slightly larger custom diameter, or from [Threads](threads.md) with a tolerance set
- Keep **Sides** low while you experiment with head types and drives -- the thread is the expensive part of the model -- and raise it before you export
- A Chamfered tip is worth keeping for a printed screw. A flat-ended thread is much harder to start
- To make a clearance pocket for a bought fastener, build the Screw at the bought size and [Subtract](../operations/boolean/subtract.md) it from your part
- A countersunk (Flat) head needs a matching cone in the part. Subtracting the screw itself gives you that for free

## Related

- [Threads](threads.md) - Bare threads, for threaded holes and for adding thread to your own shape
- [Gears](gears.md) - Involute gears
- [Subtract](../operations/boolean/subtract.md) - Cut a screw body out of a part to leave a pocket for it
- [Cylinder](../primitives/cylinder.md) - A plain round column, with no threads
