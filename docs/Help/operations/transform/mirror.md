---
title: Mirror
articleKey: MirrorObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 1
description: Flip a part across X, Y or Z to make its mirror image, such as a left and right pair.
keywords: flip, reverse, left and right, symmetric, opposite hand
---
# Mirror

Mirror flips an object across one of the three main axes. The mirrored shape replaces the original in the design: the original is kept, hidden, inside the Mirror, so you can change the axis at any time.

<!-- AUTO_IMAGE: type=shot id=mirror -->
![Mirror: a text reading normally at the left, and at the right the same text flipped left to right, beside the Mirror On setting](https://matterhackers.github.io/MatterCAD_Docs/assets/mirror.png)


## How to Use

1. Select an object
2. Click **Mirror** in the Transform group of the toolbar
3. Choose which axis to mirror across

## Parameters

- **Mirror On** - The axis to mirror across:
  - **X Axis** (default) - Flips the object left to right
  - **Y Axis** - Flips the object front to back
  - **Z Axis** - Flips the object top to bottom

## Tips

- Mirror is centered on the object's bounding box, so the mirrored result occupies the same space as the original
- Face normals are automatically corrected after mirroring to maintain proper rendering
- Use Mirror to create symmetrical designs -- model one half, **Duplicate** it (toolbar), mirror the copy, line the two up and [Combine](../boolean/combine.md) them
- Mirror is non-destructive: you can change the mirror axis at any time

## Related

- [Rotate](rotate.md) - Rotate an object instead of mirroring
- [Scale](scale.md) - Resize an object
- [Combine](../boolean/combine.md) - Merge an original and a mirrored copy into one object
