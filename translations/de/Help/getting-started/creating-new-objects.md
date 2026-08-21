---
title: Neue Objekte erstellen
parent: "Getting Started"
nav_order: 2
source_hash: 3eccb5aac5bb6f4d88f1ca3583eedd2f70384eeb
source_lang: en
---
# Neue Objekte erstellen

MatterCAD bietet eine umfangreiche Auswahl an Werkzeugen zum Erstellen von 3D-Objekten. Sie können mit primitiven Formen beginnen, spezialisierte Werkzeuge wie Text und QR-Codes verwenden oder komplexe Formen mit booleschen Operationen und Arrays aufbauen.

![20260324 081122 paste 20260324 081122](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081122-paste-20260324-081122.jpg)

## Primitive hinzufügen

Am schnellsten beginnen Sie einen Entwurf, indem Sie primitive Formen hinzufügen. Öffnen Sie das Panel Primitive in der Bibliothek und klicken Sie auf eine beliebige Form, um sie Ihrem Arbeitsbereich hinzuzufügen. Verfügbare Primitive sind:

- **Grundformen** – Würfel, Zylinder, Kugel, Kegel, Torus, Ring, Pyramide, Keil und deren Halbvarianten
- **Text und Spezielles** – Text, Braille, QR-Code, Bild-Objekt, SVG-Objekt

Jedes Primitiv besitzt Parameter, die Sie nach dem Auswählen im Panel Eigenschaften anpassen können. Ein Würfel verfügt beispielsweise über die Steuerelemente Breite, Tiefe und Höhe. Einzelheiten zu den einzelnen Formen finden Sie unter [Primitive](../primitives/index.md).

## Die Operationsleiste

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

Die Werkzeugleiste am oberen Rand des Ansichtsfensters bietet Ihnen schnellen Zugriff auf gängige Operationen:

- **Rückgängig / Wiederholen** – Änderungen zurücknehmen oder erneut ausführen. Sie können auch **Strg+Z** zum Rückgängigmachen und **Strg+Y** zum Wiederholen verwenden
- **Gruppieren / Gruppierung aufheben** – Ausgewählte Objekte zu einer Gruppe zusammenfassen, die sich als eine Einheit bewegen und bearbeiten lässt, oder eine Gruppe wieder auflösen
- **Kopieren / Löschen** – Ausgewählte Objekte duplizieren oder entfernen. Die üblichen Tastenkürzel **Strg+C**, **Strg+X** und **Strg+V** funktionieren ebenfalls
- **Ausrichten** – Mehrere Objekte relativ zueinander positionieren
- **Boolesche Operationen** – [Vereinen](../operations/boolean/combine.md), [Subtrahieren](../operations/boolean/subtract.md), [Verschneiden](../operations/boolean/intersect.md) und [Subtrahieren & Ersetzen](../operations/boolean/subtract-and-replace.md)
- **Arrays** – [Lineare, radiale, Kurven- und Transformationsmuster](../operations/array/array.md) aus duplizierten Objekten erstellen
- **Transformationen** – [Drehen](../operations/transform/rotate.md), [Skalieren](../operations/transform/scale.md), [Spiegeln](../operations/transform/mirror.md) und weitere Änderungen anwenden

## Komplexe Formen aufbauen

Die meisten Entwürfe in MatterCAD entstehen durch das Kombinieren einfacher Formen:

1. **Mit Primitiven beginnen** – Fügen Sie die benötigten Grundformen hinzu
2. **Positionieren** – Verschieben und drehen Sie die Objekte so, dass sie sich an den gewünschten Stellen überlappen
3. **Boolesche Operationen anwenden** – Verwenden Sie [Vereinen](../operations/boolean/combine.md), um Formen zusammenzuführen, oder [Subtrahieren](../operations/boolean/subtract.md), um eine Form aus einer anderen auszuschneiden
4. **Verfeinern** – Verwenden Sie Operationen zum Umformen wie [Umformen](../operations/reshape/index.md) mit Fase, Kurve oder Verdrehen, um Details hinzuzufügen

## Verwandte Themen

- [Primitive](../primitives/index.md) – Vollständige Referenz zu allen primitiven Formen
- [Vorhandene Objekte hinzufügen](adding-existing-objects.md) – Dateien importieren, statt von Grund auf neu zu erstellen
- [Boolesche Operationen](../operations/boolean/index.md) – Formen zu komplexen Gebilden kombinieren
- [Objekte bearbeiten](editing-objects.md) – Objekte nach dem Erstellen verschieben, drehen und skalieren
