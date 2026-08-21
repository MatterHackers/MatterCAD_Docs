---
title: Neue Objekte erstellen
parent: "Getting Started"
nav_order: 2
source_hash: 3eccb5aac5bb6f4d88f1ca3583eedd2f70384eeb
source_lang: en
---
# Neue Objekte erstellen

MatterCAD bietet eine umfangreiche Auswahl an Werkzeugen zum Erstellen von 3D-Objekten. Sie können mit Grundkörpern beginnen, spezialisierte Werkzeuge wie Text und QR-Codes verwenden oder komplexe Formen mithilfe von booleschen Operationen und Arrays aufbauen.

![20260324 081122 paste 20260324 081122](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081122-paste-20260324-081122.jpg)

## Grundkörper hinzufügen

Am schnellsten beginnen Sie einen Entwurf, indem Sie Grundkörper hinzufügen. Öffnen Sie das Bedienfeld „Primitives“ in der Bibliothek und klicken Sie auf eine beliebige Form, um sie Ihrem Arbeitsbereich hinzuzufügen. Folgende Grundkörper stehen zur Verfügung:

- **Grundformen** – Würfel, Zylinder, Kugel, Kegel, Torus, Ring, Pyramide, Keil sowie deren Halbvarianten
- **Text und Spezialformen** – Text, Braille, QR-Code, Bildobjekt, SVG-Objekt

Jeder Grundkörper besitzt Parameter, die Sie nach dem Auswählen im Bedienfeld „Properties“ anpassen können. Ein Würfel verfügt beispielsweise über die Einstellungen Breite, Tiefe und Höhe. Details zu den einzelnen Formen finden Sie unter [Grundkörper](../primitives/index.md).

## Die Werkzeugleiste für Operationen

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

Die Werkzeugleiste am oberen Rand des Ansichtsfensters bietet Ihnen schnellen Zugriff auf häufig verwendete Operationen:

- **Undo / Redo** – Änderungen rückgängig machen oder wiederherstellen. Sie können auch **Strg+Z** zum Rückgängigmachen und **Strg+Y** zum Wiederherstellen verwenden
- **Group / Ungroup** – Ausgewählte Objekte zu einer Gruppe zusammenfassen, die sich als eine Einheit bewegen und bearbeiten lässt, oder eine Gruppe wieder auflösen
- **Copy / Delete** – Ausgewählte Objekte duplizieren oder entfernen. Die Standardkürzel **Strg+C**, **Strg+X** und **Strg+V** funktionieren ebenfalls
- **Align** – Mehrere Objekte relativ zueinander ausrichten
- **Boolesche Operationen** – [Combine](../operations/boolean/combine.md), [Subtract](../operations/boolean/subtract.md), [Intersect](../operations/boolean/intersect.md) und [Subtract & Replace](../operations/boolean/subtract-and-replace.md)
- **Arrays** – [Lineare, radiale, Kurven- und Transformationsmuster](../operations/array/array.md) aus duplizierten Objekten erstellen
- **Transformationen** – [Rotate](../operations/transform/rotate.md), [Scale](../operations/transform/scale.md), [Mirror](../operations/transform/mirror.md) und weitere Änderungen anwenden

## Komplexe Formen aufbauen

Die meisten Entwürfe in MatterCAD entstehen durch das Kombinieren einfacher Formen:

1. **Mit Grundkörpern beginnen** – Fügen Sie die benötigten Grundformen hinzu
2. **Positionieren** – Verschieben und drehen Sie die Objekte so, dass sie sich an den gewünschten Stellen überschneiden
3. **Boolesche Operationen anwenden** – Verwenden Sie [Combine](../operations/boolean/combine.md), um Formen zu verschmelzen, oder [Subtract](../operations/boolean/subtract.md), um eine Form aus einer anderen auszuschneiden
4. **Verfeinern** – Nutzen Sie [Reshape](../operations/reshape/index.md)-Operationen wie Bevel, Curve oder Twist, um Details hinzuzufügen

## Verwandte Themen

- [Grundkörper](../primitives/index.md) – Vollständige Referenz zu allen Grundkörpern
- [Vorhandene Objekte hinzufügen](adding-existing-objects.md) – Dateien importieren, statt von Grund auf neu zu erstellen
- [Boolesche Operationen](../operations/boolean/index.md) – Formen zu komplexen Gebilden kombinieren
- [Objekte bearbeiten](editing-objects.md) – Objekte nach dem Erstellen verschieben, drehen und skalieren
