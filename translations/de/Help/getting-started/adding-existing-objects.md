---
title: Vorhandene Objekte hinzufügen
parent: "Getting Started"
nav_order: 1
source_hash: e384a5c024336c3c58343d262d914fa40e0b0426
source_lang: en
---
# Vorhandene Objekte hinzufügen

Sie können vorhandene 3D-Modelle in MatterCAD einbringen, indem Sie Dateien von Ihrem Computer importieren oder Inhalte aus der integrierten Bibliothek hinzufügen.

## Von Ihrem Computer

![20260324 081143 paste 20260324 081143](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081143-paste-20260324-081143.jpg)

![20260324 081240 paste 20260324 081240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081240-paste-20260324-081240.jpg)


Klicken Sie in der Symbolleiste auf die Schaltfläche **Open**, um Dateien von Ihrem Computer zu durchsuchen und hinzuzufügen. MatterCAD unterstützt die folgenden Importformate:

- **STL** (.stl) – Branchenübliches 3D-Modellformat, weit verbreitet für den 3D-Druck
- **AMF** (.amf) – Erweitertes Format mit Unterstützung für Farben und Multi-Material-Objekte
- **OBJ** (.obj) – Wavefront-3D-Grafikformat (nur Netzgeometrie)
- **3MF** (.3mf) – 3D Manufacturing Format mit umfangreicher Metadatenunterstützung
- **MCX** (.mcx) – MatterCADs natives Format, das alle Konstruktionsdaten und Parameter erhält
- **SVG** (.svg) – Scalable Vector Graphics, wird als 2D-Pfade importiert
- **TTF / OTF** (.ttf, .otf) – Schriftdateien zur Verwendung mit dem Text-Werkzeug

## Drag and Drop

Sie können Dateien auch direkt von Ihrem Desktop oder aus dem Datei-Explorer per Drag and Drop in den MatterCAD-Arbeitsbereich ziehen. Unterstützte Dateitypen werden automatisch importiert.

![20260324 081416 paste 20260324 081416](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081416-paste-20260324-081416.jpg)

## Aus der Bibliothek

### Die Bibliotheks-Seitenleiste

Klicken Sie in der Symbolleiste auf die Schaltfläche **Add Content**, um das Bibliotheks-Browserfenster zu öffnen. Von hier aus können Sie:

- Ihre gespeicherten Designs durchsuchen
- Zur Primitives-Bibliothek mit den integrierten Formen navigieren
- Auf Ihre Cloud Library zugreifen, sofern Sie angemeldet sind
- Jedes Element aus der Bibliothek per Drag and Drop direkt in Ihren Arbeitsbereich ziehen

![20260324 081446 paste 20260324 081446](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081446-paste-20260324-081446.jpg)

### Der Bibliotheks-Tab

Sie können auch den Library-Tab verwenden, um Ihre Sammlungen zu durchsuchen. Klicken Sie mit der rechten Maustaste auf ein beliebiges Objekt in der Bibliothek und wählen Sie **Add to Scene**, um es in Ihren aktuellen Konstruktionsarbeitsbereich zu importieren.

![20260324 081536 paste 20260324 081536](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081536-paste-20260324-081536.jpg)

## Tipps

- MCX ist das beste Format, um Designs später erneut zu bearbeiten, da es alle Parameter und den Konstruktionsbaum erhält
- STL-Dateien enthalten ausschließlich Netzgeometrie. Wenn Sie eine STL-Datei importieren, können Sie weiterhin Operationen darauf anwenden, die ursprünglichen Parameter jedoch nicht bearbeiten
- Beim Importieren mehrerer Dateien wird jede einzelne zu einem eigenständigen Objekt in Ihrer Szene. Verwenden Sie [Gruppieren](../workspace/grouping.md), um sie zu organisieren

## Verwandte Themen

- [Neue Objekte erstellen](creating-new-objects.md) – Ein Design von Grund auf mit Grundkörpern beginnen
- [Speichern und Exportieren](saving-and-exporting.md) – Ihre fertigen Designs speichern und exportieren
- [Bibliothek](../library/index.md) – Mehr über das Organisieren Ihrer Designbibliothek erfahren
