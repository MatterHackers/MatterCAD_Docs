---
title: Spiegeln
articleKey: MirrorObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 8a8de28f5e429177d4b0092d0756387eb6b83a70
source_lang: en
---
# Spiegeln

Spiegeln erzeugt eine gespiegelte Kopie eines Objekts an einer der drei Hauptachsen. Das Ergebnis ist eine gespiegelte Version der ursprünglichen Form.

<!--  Before and after showing an object mirrored across the X axis -->
![20260506 160651 paste 20260506 160651](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160651-paste-20260506-160651.jpg)


## Verwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie die Operation **Spiegeln** aus dem Menü Transformieren an
3. Wählen Sie die Achse, an der gespiegelt werden soll

## Parameter

- **Spiegeln ein** – Die Achse, an der gespiegelt wird:
  - **X-Achse** – Spiegelt das Objekt von links nach rechts
  - **Y-Achse** – Spiegelt das Objekt von vorne nach hinten
  - **Z-Achse** – Spiegelt das Objekt von oben nach unten

## Tipps

- Spiegeln wird am Begrenzungsrahmen des Objekts zentriert, sodass das gespiegelte Ergebnis denselben Raum einnimmt wie das Original
- Die Flächennormalen werden nach dem Spiegeln automatisch korrigiert, damit die Darstellung korrekt bleibt
- Verwenden Sie Spiegeln, um symmetrische Konstruktionen zu erstellen – modellieren Sie eine Hälfte, spiegeln Sie sie und [Vereinen](../boolean/combine.md) Sie sie mit dem Original
- Spiegeln ist nicht destruktiv: Sie können die Spiegelachse jederzeit ändern

## Verwandte Themen

- [Drehen](rotate.md) – Ein Objekt drehen, statt es zu spiegeln
- [Skalieren](scale.md) – Die Größe eines Objekts ändern
- [Vereinen](../boolean/combine.md) – Das Original und die gespiegelte Kopie zu einem Objekt zusammenführen
