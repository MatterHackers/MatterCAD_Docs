---
title: Objekte bearbeiten
parent: "Getting Started"
nav_order: 3
source_hash: 5190f3e59be7ea02497903b15c1956ed68b4d270
source_lang: en
---
# Objekte bearbeiten

MatterCAD bietet intuitive Steuerelemente direkt in der 3D-Ansicht, mit denen Sie Ihre Objekte verschieben, drehen und skalieren können. Sie können auch die Objektparameter im Bereich **Eigenschaften** bearbeiten.

## Bauteile verschieben


- **Auf dem Druckbett ziehen** – Klicken und ziehen Sie ein beliebiges Objekt, um es auf der Arbeitsfläche zu verschieben
- **Nach oben und unten verschieben** – Verwenden Sie das senkrechte Pfeil-Steuerelement über einem ausgewählten Objekt, um dessen Höhe (Z-Position) anzupassen
- Für eine präzise Positionierung verwenden Sie die Operation [Verschieben](../operations/transform/translate.md) oder geben exakte Werte im Bereich **Eigenschaften** ein

## Bauteile drehen

![20260324 080843 paste 20260324 080843](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080843-paste-20260324-080843.jpg)

Klicken Sie auf eines der **Dreh-Steuerelemente an den Ecken**, die erscheinen, wenn Sie ein Objekt auswählen. Damit drehen Sie das Objekt in der Ebene des jeweiligen Steuerelements.

- Bewegen Sie den Mauszeiger über eine der Winkelanzeigen, um die Drehung in **45-Grad-Schritten** einrasten zu lassen
- Für eine präzise Drehung verwenden Sie die Operation [Drehen](../operations/transform/rotate.md) und geben einen exakten Winkel ein

## Bauteile skalieren

![20260324 080819 paste 20260324 080819](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080819-paste-20260324-080819.jpg)


Klicken Sie auf eines der **Skalier-Steuerelemente an den Ecken**, um die Größe Ihres Bauteils auf der Arbeitsfläche zu ändern.

- Ziehen Sie an einer Ecke, um proportional zu skalieren
- Für exakte Größen oder ungleichmäßiges Skalieren verwenden Sie die Operation [Skalieren](../operations/transform/scale.md), in der Sie exakte Maße festlegen oder jede Achse unabhängig skalieren können

## Parameter bearbeiten

Wenn Sie ein Objekt auswählen, erscheinen dessen Parameter im Bereich **Eigenschaften** auf der rechten Seite des Bildschirms. Zum Beispiel:

- Ein **Würfel** zeigt Breite, Tiefe, Höhe und optionale Steuerelemente zur Abrundung
- Ein **Zylinder** zeigt Durchmesser, Höhe und Seiten
- Ein **Text**-Objekt zeigt den Textinhalt, die Schriftart, die Größe und die Höhe

Sie können Werte direkt eingeben, Schieberegler verwenden oder [Ausdrücke](../workspace/expressions.md) für parametrische Beziehungen eingeben.

## Kontextmenü

Klicken Sie mit der rechten Maustaste auf ein beliebiges Objekt, um weitere Optionen aufzurufen, darunter:

- Kopieren, Ausschneiden, Löschen
- Gruppieren / Gruppierung aufheben
- Verfügbare Operationen für das ausgewählte Objekt
- Hilfe zum jeweiligen Objekttyp (sofern verfügbar)

## Tipps

- Halten Sie beim Klicken die **Umschalttaste** gedrückt, um mehrere Objekte auszuwählen, und verschieben oder bearbeiten Sie diese anschließend gemeinsam
- Drücken Sie **Strg+Z**, um eine beliebige Änderung rückgängig zu machen
- Verwenden Sie [Ausrichten](../operations/placement/align.md), um mehrere Objekte präzise zueinander zu positionieren
- Drücken Sie die **Leertaste**, um die Auswahl aufzuheben

## Verwandte Themen

- [Navigation im Ansichtsfenster](viewport-navigation.md) – So drehen, verschieben und zoomen Sie die Ansicht
- [Auswahl](../workspace/selection.md) – Ausführliches Auswahlverhalten
- [Transformieren-Operationen](../operations/transform/index.md) – Präzise Steuerelemente zum Transformieren
- [Tastenkürzel](../workspace/keyboard-shortcuts.md) – Alle verfügbaren Tastenkürzel
