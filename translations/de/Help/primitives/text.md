---
title: Text
articleKey: TextObject3D_2
parent: "Primitives"
nav_order: 16
source_hash: 526f3190c7b2150243499b5874ac455d74810bb2
source_lang: en
---
# Text

Erstellen Sie 3D-extrudierten Text mit anpassbarem Inhalt, anpassbarer Schriftart, Größe und Höhe. Textobjekte eignen sich hervorragend für Beschriftungen, Schilder, Namensschilder und dekorative Lettern.

<!--  Screenshot of a 3D Text object on the workspace showing extruded letters -->
![20260318 184207 paste 20260318 184207](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184207-paste-20260318-184207.jpg)


## Verwendung

1. Fügen Sie ein **Text**-Primitiv aus dem Panel **Primitive** hinzu
2. Geben Sie Ihren Text im Feld **Name** im Panel **Eigenschaften** ein
3. Passen Sie Schriftart, Größe und Extrusionshöhe nach Bedarf an

## Parameter

- **Name** - Der anzuzeigende Textinhalt
- **Punktgröße** - Die Schriftgröße. Sie ist im Verhältnis zu den üblichen Druckgrößen exakt -- eine Punktgröße von 12 in MatterCAD entspricht einer 12-Punkt-Schrift auf einem 2D-Drucker
- **Höhe** - Die Extrusionshöhe (wie weit der Text aus der Oberfläche herausragt)
- **Schriftart** - Auswahl aus den verfügbaren Systemschriften

## Tipps

- Verwenden Sie [Subtrahieren](../operations/boolean/subtract.md), um Text in eine Oberfläche zu gravieren, anstatt ihn hervorstehen zu lassen
- Erhöhen Sie bei sehr kleinem Text die Punktgröße und verkleinern Sie anschließend das gesamte Objekt mit [Skalieren](../operations/transform/scale.md), um mehr Details zu erhalten
- Jeder Buchstabe des Textes ist ein eigener Pfad, der gemeinsam extrudiert wird

## Verwandte Themen

- [Braille](braille.md) - Erzeugt 3D-druckbaren Braille-Text
- [QR-Code](qr-code.md) - Erzeugt einen QR-Code als 3D-Objekt
- [Bild-Objekt](image-object.md) - Wandelt Bilder in 3D um
