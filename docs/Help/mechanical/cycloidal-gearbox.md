---
title: Cycloidal Gearbox
articleKey: CycloidalGearboxObject3D
parent: "Mechanical Parts"
nav_order: 6
description: Make a complete, printable cycloidal gearbox that bolts onto a stepper motor, with its parts list and print layout.
keywords: cycloidal gearbox, speed reducer, gear reducer, stepper motor, NEMA 17, robot joint, bearings, parts list, print parts
---
# Cycloidal Gearbox

Cycloidal Gearbox makes a whole gearbox in one go: every printed part, sized to fit the stepper motor and the bearings you choose, plus the list of bearings and screws to buy. It bolts onto the face of the motor and slows the motor down by the **Ratio** -- at the default 20:1 the output turns once for every 20 turns of the motor, with about 20 times the force.

<!-- AUTO_IMAGE: type=shot id=mechanical-cycloidal-gearbox -->
![A Cycloidal Gearbox assembled on the bed, its bearings and screws in grey, selected beside its Properties panel: the View buttons and the Gearbox section's Ratio, Ring Diameter and Eccentricity](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical-cycloidal-gearbox.png)

## How It Works

The motor turns an **Eccentric**, an off-center cam that pushes the **Cycloid Disc** around in a small circle. The disc has lobes that roll against a ring of bearings (the **Ring Rollers**). Because the ring has one more roller than the disc has lobes, every turn of the motor moves the disc back by one lobe, so the disc turns slowly the other way. Bearings on pins in the **Output** ride in the disc's holes and take that slow turn out through the top of the gearbox.

The output turns the opposite way to the motor. **Reduction Ratio** under Gear Data says so.

## How to Use

1. Open **Included > Mechanical** in the Library (or under **Add to Bed**) and add **Cycloidal Gearbox** to the bed
2. Under **Motor**, pick your stepper motor (NEMA 14 or NEMA 17), or **Custom** to type in its sizes
3. Under **Bearings**, pick the bearings you have or will buy
4. Set the **Ratio** and the **Ring Diameter**
5. Read **Problems** under Gear Data and change what it asks for, until there are none
6. Check **Motor Shaft Needed** against your motor's shaft
7. Switch **View** to **Print Parts** and export, to print the parts
8. Buy what the **Parts List** says

A gearbox with problems is still drawn, so you can see what is wrong while you fix it.

## Parameters

### View

- **Assembled** - The whole gearbox put together, with its bearings and screws shown in grey so you can see how everything fits
- **Print Parts** - Only the parts to print, each one as many times as the gearbox needs, laid out flat on the bed. This is the view to export to your slicer

### Gearbox

- **Ratio** - How many turns of the motor turn the output once (default 20; the slider runs 3 to 60). The disc gets this many lobes and the ring one roller more. Higher ratios turn slower with more force
- **Ring Diameter** - The diameter of the circle the ring rollers stand on, in mm (default 80). This is the working size of the whole gearbox: everything else is sized inside it. Make it larger when Problems asks for room
- **Eccentricity** - How far the disc's center is offset from the motor shaft, in mm (default 1). Larger values make deeper lobes that carry more load. Too large and the lobes would come to points, so it is lowered and Problems says so
- **Input Angle** - Turns the motor to this angle, in degrees, so you can watch the disc roll and the output turn. It only moves the parts; nothing is rebuilt. Shown only in the Assembled view

### Motor

- **Motor** - NEMA 14, NEMA 17 or Custom. Custom shows the sizes to measure on your own motor: **Shaft Diameter**, **Shaft Flat Depth** (0 for a round shaft), **Flat Length** (how far the flat runs down from the shaft's tip; the NEMA presets assume a typical 15 mm, so check your motor's drawing, because the set screw that holds the gearbox on has to tighten on the flat), **Shaft Length** (how far the shaft stands out of the motor's face), **Bolt Spacing** (the side of the square the mounting holes stand on), **Bolt Size**, **Thread Depth**, and **Boss Diameter** and **Boss Height** (the raised ring around the shaft; 0 if there is none)

### Bearings

- **Ring Rollers** - The bearings standing in the ring, which the disc's lobes roll against. The gearbox needs one more of these than the Ratio
- **Output Rollers** - The bearings on the output pins, which run in the disc's holes
- **Input Bearing** - The bearing between the eccentric and the disc
- **Output Bearing** - The bearing the output turns in, held in the top plate

Each one lists common metric bearing sizes. **Custom** shows that bearing's **Bore**, **Outside Diameter** and **Width** for any other bearing. Measure a bearing you already have rather than trusting the label.

### Advanced

- **Running Clearance** - The gap left between parts that move against each other, such as the disc and the rollers, in mm (default 0.1). Raise it if the gearbox binds; lower it if it has play
- **Print Clearance** - Extra room printed holes and seats get so the bearings and screws fit, in mm (default 0.15). Raise it if bearings are too tight to press in; lower it if they are loose

### Gear Data (read only)

- **Reduction Ratio** - The reduction, and which way the output turns
- **Motor Shaft Needed** - How far the motor shaft has to stand out of the motor's face to drive the disc. A shorter shaft can't reach; a much longer one has to be cut, and Problems says to what length
- **Outer Diameter** - The diameter of the housing
- **Overall Height** - The height from the motor's face to the top of the output
- **Problems** - Shown only when something is wrong. Each line says what happened and what to change, often "make the Ring Diameter at least" a size it has worked out for you
- **Parts List** - Everything to buy and print: each bearing and screw with its size and how many, the motor, and the printed parts

## What to Buy

The **Parts List** is the shopping list. For the default gearbox on a NEMA 17 motor it is:

- 21 MR63 bearings for the ring and 12 more for the output pins
- One 6800 bearing (input) and one 6805 bearing (output)
- Socket head screws: M3 for the ring, the output pins and the motor, and M5 to mount what you drive onto the output
- One M3 x 5 set screw (cup point) that holds the eccentric on the motor shaft
- The stepper motor

The screw lengths are standard sizes worked out for your gearbox. When no standard length fits, the list says what to cut a longer screw down to.

## Putting It Together

Build it from the motor up:

1. **Eccentric on the shaft.** Do this first: once the housing is on, the set screw can't be reached. Screw the set screw into the hole in the side of the eccentric's round collar until its tip just shows inside. Slide the eccentric onto the motor shaft, collar first, with its flat lined up with the flat on the shaft and the set screw facing the shaft's flat. Set its bottom about 0.5 mm above the motor's boss (a sheet of paper folded twice makes a good feeler), then tighten the set screw on the flat with a hex key. It ends below the collar's surface, so nothing rubs as it turns
2. **Housing on the motor.** Lower the housing over the eccentric onto the motor's face and screw it down with the motor screws, from inside the housing
3. **Ring rollers.** Drop a ring roller onto each post in the housing
4. **Disc.** Press the input bearing into the disc from the top, then lower the disc over the eccentric so its lobes sit between the ring rollers
5. **Output.** Turn the output upside down. On each pin hole stack an upper pin spacer, an output roller and a lower pin spacer, then screw an output pin screw through them into the output. Turn it back over and lower it so the output rollers drop into the disc's holes
6. **Top plate.** Press the output bearing into the top plate from below, then lower the plate over the output so its posts rest on the ring rollers
7. **Ring screws.** Screw the ring screws down through the top plate and the ring rollers into the housing

Turn the motor by hand (or set Input Angle in MatterCAD) to check that it runs smoothly before you power it.

## Printing

- Switch **View** to **Print Parts** and export that. Every part is already turned the way it prints best and none of them needs supports. The top plate prints upside down
- The parts are sized for a 0.4 mm nozzle and 0.2 mm layers: the thinnest walls are five lines and the thinnest spacers five layers
- PLA or PETG both work. Print the disc and the eccentric with enough walls to be solid
- If the bearings won't press in, or fall out, change **Print Clearance** and reprint only the parts that hold them

## Tips

- Start with the motor and bearings you have, then set the Ratio, and only then grow the Ring Diameter until Problems is empty
- A larger Ring Diameter makes a stronger gearbox that is wider; a higher Ratio needs more ring rollers, so it needs a larger ring too
- When a finished gearbox binds, raise **Running Clearance** a little and reprint the disc

## Related

- [Cycloidal Gear](cycloidal-gear.md) - Just the disc and pin ring, to build your own cycloidal drive
- [Involute Gear](gears.md) - Involute gears, for ordinary meshing gear trains
- [Screw](screw.md) - Screws and the holes for them
