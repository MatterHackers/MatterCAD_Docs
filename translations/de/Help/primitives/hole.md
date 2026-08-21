---
title: Loch
articleKey: CubeHoleObject3D
parent: "Primitives"
nav_order: 9
source_hash: c6c802f54eaaccbd4caad827b9f967aa46b059a6
source_lang: en
---
# Loch

Ein würfelförmiges Objekt, das bereits als boolesches Subtraktionswerkzeug voreingestellt ist. Wenn Sie [Kombinieren](../operations/boolean/combine.md) verwenden, werden Loch-Objekte automatisch von anderen Formen abgezogen, statt ihnen hinzugefügt zu werden.

<!--  Screenshot showing a Hole object being used to cut a rectangular slot in another shape -->
![20260318 183619 paste 20260318 183619](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183619-paste-20260318-183619.jpg)


## Funktionsweise

Das Grundobjekt Loch funktioniert wie ein [Würfel](cube.md), sein Ausgabetyp ist jedoch auf „Loch“ gesetzt. Wenn Sie Objekte kombinieren, zu denen ein Loch gehört, wird das Volumen des Lochs aus dem Ergebnis entfernt.

## Parameter

Wie beim [Würfel](cube.md):

- **Breite** – Größe entlang der X-Achse
- **Tiefe** – Größe entlang der Y-Achse
- **Höhe** – Größe entlang der Z-Achse

## Tipps

- Positionieren Sie das Loch so, dass es sich mit dem Objekt überschneidet, das Sie ausschneiden möchten
- Lassen Sie das Loch vollständig durch das Zielobjekt hindurchreichen, wenn Sie eine durchgehende Öffnung wünschen
- Sie können mit [Subtrahieren](../operations/boolean/subtract.md) auch normale Formen für denselben Effekt verwenden, doch Löcher sind praktisch, weil sie automatisch mit [Kombinieren](../operations/boolean/combine.md) zusammenarbeiten
- Verwenden Sie für runde Löcher stattdessen einen [Zylinder](cylinder.md) mit Subtrahieren

## Verwandte Themen

- [Würfel](cube.md) – Dieselbe Form ohne das Loch-Verhalten
- [Kombinieren](../operations/boolean/combine.md) – Führt Formen zusammen und subtrahiert Löcher automatisch
- [Subtrahieren](../operations/boolean/subtract.md) – Beliebige Form manuell von einer anderen abziehen
