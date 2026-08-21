---
title: Text
articleKey: TextObject3D_2
parent: "Primitives"
nav_order: 16
source_hash: 526f3190c7b2150243499b5874ac455d74810bb2
source_lang: en
---
# Text

Erstellen Sie extrudierten 3D-Text mit anpassbarem Inhalt, Schriftart, Größe und Höhe. Textobjekte eignen sich hervorragend für Beschriftungen, Schilder, Namensschilder und dekorative Schriftzüge.

<!--  Screenshot of a 3D Text object on the workspace showing extruded letters -->
![20260318 184207 paste 20260318 184207](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184207-paste-20260318-184207.jpg)


## Verwendung

1. Fügen Sie ein **Text**-Grundobjekt aus dem Bereich „Primitives“ hinzu
2. Geben Sie Ihren Text im Feld **Name** im Eigenschaftenbereich ein
3. Passen Sie Schriftart, Größe und Extrusionshöhe nach Bedarf an

## Parameter

- **Name** – Der anzuzeigende Textinhalt
- **Point Size** – Die Schriftgröße. Diese entspricht der Standard-Druckgröße – eine Größe von 12 Punkt in MatterCAD entspricht 12-Punkt-Schrift auf einem 2D-Drucker
- **Height** – Die Extrusionshöhe (wie weit der Text von der Oberfläche absteht)
- **Font** – Auswahl aus den verfügbaren Systemschriftarten

## Tipps

- Verwenden Sie [Subtrahieren](../operations/boolean/subtract.md), um Text in eine Oberfläche zu gravieren, statt ihn zu erhöhen
- Erhöhen Sie bei sehr kleinem Text die Punktgröße und [skalieren](../operations/transform/scale.md) Sie anschließend das gesamte Objekt herunter, um mehr Details zu erhalten
- Jeder Buchstabe im Text ist ein eigener Pfad, der gemeinsam extrudiert wird

## Verwandte Themen

- [Braille](braille.md) – 3D-druckbaren Brailletext erzeugen
- [QR-Code](qr-code.md) – Einen QR-Code als 3D-Objekt erzeugen
- [Bildobjekt](image-object.md) – Bilder in 3D umwandeln
