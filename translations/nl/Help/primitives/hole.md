---
title: Gat
articleKey: CubeHoleObject3D
parent: "Primitives"
nav_order: 9
source_hash: c6c802f54eaaccbd4caad827b9f967aa46b059a6
source_lang: en
---
# Gat

Een kubusvormig object dat vooraf is ingesteld om te fungeren als booleaans aftrekgereedschap. Wanneer je [Combineren](../operations/boolean/combine.md) gebruikt, worden Gat-objecten automatisch van andere vormen afgetrokken in plaats van eraan toegevoegd.

<!--  Screenshot showing a Hole object being used to cut a rectangular slot in another shape -->
![20260318 183619 paste 20260318 183619](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183619-paste-20260318-183619.jpg)


## Hoe het werkt

De primitief Gat werkt als een [Kubus](cube.md), maar het uitvoertype is ingesteld op "Gat". Wanneer je objecten combineert waar een Gat bij zit, wordt het volume van het Gat uit het resultaat verwijderd.

## Parameters

Hetzelfde als bij [Kubus](cube.md):

- **Breedte** - Grootte langs de X-as
- **Diepte** - Grootte langs de Y-as
- **Hoogte** - Grootte langs de Z-as

## Tips

- Plaats het Gat zo dat het overlapt met het object dat je wilt uitsnijden
- Laat het Gat volledig door het doelobject heen steken als je een doorlopend gat wilt
- Je kunt gewone vormen met [Aftrekken](../operations/boolean/subtract.md) gebruiken voor hetzelfde effect, maar Gaten zijn handig omdat ze automatisch werken met [Combineren](../operations/boolean/combine.md)
- Gebruik voor ronde gaten in plaats daarvan een [Cilinder](cylinder.md) met Aftrekken

## Gerelateerd

- [Kubus](cube.md) - Dezelfde vorm zonder het gatgedrag
- [Combineren](../operations/boolean/combine.md) - Voegt vormen samen en trekt Gaten automatisch af
- [Aftrekken](../operations/boolean/subtract.md) - Trek handmatig een willekeurige vorm van een andere af
