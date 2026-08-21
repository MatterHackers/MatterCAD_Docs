---
title: Objekte bearbeiten
parent: "Getting Started"
nav_order: 3
source_hash: 5190f3e59be7ea02497903b15c1956ed68b4d270
source_lang: en
---
# Objekte bearbeiten

MatterCAD bietet intuitive Steuerelemente direkt in der 3D-Ansicht, mit denen Sie Ihre Objekte verschieben, drehen und skalieren können. Objektparameter lassen sich außerdem im Eigenschaften-Panel bearbeiten.

## Teile verschieben


- **Auf dem Druckbett ziehen** – Klicken Sie ein beliebiges Objekt an und ziehen Sie es, um es auf der Arbeitsfläche zu verschieben
- **Nach oben und unten bewegen** – Verwenden Sie das vertikale Pfeil-Steuerelement oberhalb eines ausgewählten Objekts, um dessen Höhe (Z-Position) anzupassen
- Für eine präzise Positionierung verwenden Sie die Operation [Verschieben](../operations/transform/translate.md) oder geben Sie exakte Werte im Eigenschaften-Panel ein

## Teile drehen

![20260324 080843 paste 20260324 080843](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080843-paste-20260324-080843.jpg)

Klicken Sie auf eines der **Dreh-Steuerelemente an den Ecken**, die beim Auswählen eines Objekts erscheinen. Damit drehen Sie das Objekt in der Ebene des jeweiligen Steuerelements.

- Bewegen Sie den Mauszeiger über eine der Winkelanzeigen, um die Drehung in **45-Grad-Schritten** einrasten zu lassen
- Für eine präzise Drehung verwenden Sie die Operation [Drehen](../operations/transform/rotate.md) und geben Sie einen exakten Winkel ein

## Teile skalieren

![20260324 080819 paste 20260324 080819](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080819-paste-20260324-080819.jpg)


Klicken Sie auf eines der **Skalier-Steuerelemente an den Ecken**, um die Größe Ihres Teils auf der Arbeitsfläche zu ändern.

- Ziehen Sie an einer Ecke, um proportional zu skalieren
- Für exakte Größen oder ungleichmäßiges Skalieren verwenden Sie die Operation [Skalieren](../operations/transform/scale.md), in der Sie genaue Maße festlegen oder jede Achse unabhängig skalieren können

## Parameter bearbeiten

Wenn Sie ein Objekt auswählen, erscheinen dessen Parameter im Eigenschaften-Panel auf der rechten Seite des Bildschirms. Zum Beispiel:

- Ein **Würfel** zeigt Breite, Tiefe, Höhe und optionale Steuerelemente für die Abrundung
- Ein **Zylinder** zeigt Durchmesser, Höhe und Seiten
- Ein **Text**-Objekt zeigt den Textinhalt, die Schriftart, die Größe und die Höhe

Sie können Werte direkt eingeben, Schieberegler verwenden oder [Ausdrücke](../workspace/expressions.md) für parametrische Beziehungen eingeben.

## Kontextmenü

Klicken Sie mit der rechten Maustaste auf ein beliebiges Objekt, um auf weitere Optionen zuzugreifen, darunter:

- Kopieren, Ausschneiden, Löschen
- Gruppieren / Gruppierung aufheben
- Verfügbare Operationen für das ausgewählte Objekt
- Hilfe zum jeweiligen Objekttyp (sofern verfügbar)

## Tipps

- Halten Sie beim Klicken **Shift** gedrückt, um mehrere Objekte auszuwählen und sie gemeinsam zu verschieben oder zu bearbeiten
- Drücken Sie **Strg+Z**, um eine Änderung rückgängig zu machen
- Verwenden Sie [Ausrichten](../operations/placement/align.md), um mehrere Objekte präzise zueinander zu positionieren
- Drücken Sie die **Leertaste**, um die Auswahl aufzuheben

## Verwandte Themen

- [Navigation im Ansichtsfenster](viewport-navigation.md) – Ansicht drehen, verschieben und zoomen
- [Auswahl](../workspace/selection.md) – Detailliertes Auswahlverhalten
- [Transformationsoperationen](../operations/transform/index.md) – Präzise Transformationssteuerung
- [Tastenkürzel](../workspace/keyboard-shortcuts.md) – Alle verfügbaren Tastenkürzel
