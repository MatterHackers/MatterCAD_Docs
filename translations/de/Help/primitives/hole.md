---
title: Loch
articleKey: CubeHoleObject3D
parent: "Primitives"
nav_order: 9
source_hash: c6c802f54eaaccbd4caad827b9f967aa46b059a6
source_lang: en
---
# Loch

Ein würfelförmiges Objekt, das bereits als boolesches Subtraktionswerkzeug voreingestellt ist. Wenn Sie [Vereinen](../operations/boolean/combine.md) verwenden, werden Loch-Objekte automatisch von anderen Formen subtrahiert, anstatt zu ihnen hinzugefügt zu werden.

<!--  Screenshot showing a Hole object being used to cut a rectangular slot in another shape -->
![20260318 183619 paste 20260318 183619](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183619-paste-20260318-183619.jpg)


## Funktionsweise

Das Primitiv Loch funktioniert wie ein [Würfel](cube.md), hat jedoch den Ausgabetyp "Loch". Wenn Sie Objekte vereinen, zu denen ein Loch gehört, wird das Volumen des Lochs aus dem Ergebnis entfernt.

## Parameter

Identisch mit [Würfel](cube.md):

- **Breite** - Größe entlang der X-Achse
- **Tiefe** - Größe entlang der Y-Achse
- **Höhe** - Größe entlang der Z-Achse

## Tipps

- Positionieren Sie das Loch so, dass es sich mit dem Objekt überschneidet, das Sie ausschneiden möchten
- Lassen Sie das Loch vollständig durch das Zielobjekt hindurchreichen, wenn Sie ein Durchgangsloch erzeugen möchten
- Sie können denselben Effekt auch mit normalen Formen und [Subtrahieren](../operations/boolean/subtract.md) erzielen, aber Löcher sind praktisch, weil sie automatisch mit [Vereinen](../operations/boolean/combine.md) zusammenarbeiten
- Verwenden Sie für runde Löcher stattdessen einen [Zylinder](cylinder.md) mit Subtrahieren

## Verwandte Themen

- [Würfel](cube.md) - Dieselbe Form ohne das Loch-Verhalten
- [Vereinen](../operations/boolean/combine.md) - Führt Formen zusammen und subtrahiert Löcher automatisch
- [Subtrahieren](../operations/boolean/subtract.md) - Beliebige Form manuell von einer anderen subtrahieren
