---
title: Hollow Out
articleKey: HollowOutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 3
---
# Hollow Out

Hollow Out turns a solid part into a shell with walls of exactly the thickness you set. It works like [Erode](erode.md): it shrinks a copy of the part inward by the wall thickness and removes that copy from the inside, leaving a closed, hidden cavity.

<!--  Cross-section view showing a solid object hollowed out with visible wall thickness -->
![20260506 155412 paste 20260506 155412](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155412-paste-20260506-155412.jpg)

## How to Use

1. Select a solid part
2. Click **Hollow Out** in the Round & Offset group of the toolbar
3. Set **Wall Thickness** to how thick the walls should be
4. Wait for the operation to finish; the progress bar shows the time left, and **Cancel** in the task area keeps the previous result
5. To open the cavity, [Subtract](../boolean/subtract.md) a [Hole](../../primitives/hole.md) or other shape that reaches through a wall

## Parameters

- **Wall Thickness** - How thick the walls are (default: 2 mm). Every wall comes out exactly this thick
- **Segments** - How finely the offset ball is drawn (default: 12). More segments make the inside surface smoother and take longer, especially on parts with pockets or notches

## Tips

- The cavity is fully enclosed, so it is invisible from outside. Use a cut or a Subtract to open it or to see inside
- A part thinner than twice the wall thickness stays solid there, since it is all wall. If nothing hollows out, lower **Wall Thickness**
- Hollow Out is useful for creating enclosures, containers, vases, and lightweight parts
- A wall thickness of 1-2 mm is typical for most 3D-printed parts
- Increase **Segments** if the inside surface looks faceted

## Related

- [Erode](erode.md) - Shrink a solid inward
- [Plane Cut](plane-cut.md) - Cut an object at a specific height
- [Subtract](../boolean/subtract.md) - Manually cut material away
