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


Klicken Sie in der Symbolleiste auf die Schaltfläche **Öffnen**, um Dateien von Ihrem Computer zu durchsuchen und hinzuzufügen. MatterCAD unterstützt die folgenden Importformate:

- **STL** (.stl) – Industriestandard für 3D-Modelle, weit verbreitet im 3D-Druck
- **AMF** (.amf) – Fortgeschrittenes Format mit Unterstützung für Farben und Objekte aus mehreren Materialien
- **OBJ** (.obj) – Wavefront-3D-Grafikformat (nur Netzgeometrie)
- **3MF** (.3mf) – 3D Manufacturing Format mit umfangreicher Metadaten-Unterstützung
- **MCX** (.mcx) – Das native Format von MatterCAD, das alle Konstruktionsdaten und Parameter erhält
- **SVG** (.svg) – Scalable Vector Graphics, wird als 2D-Pfade importiert
- **TTF / OTF** (.ttf, .otf) – Schriftartdateien zur Verwendung mit dem Text-Werkzeug

## Drag & Drop

Sie können Dateien auch per Drag & Drop direkt von Ihrem Desktop oder aus dem Datei-Explorer in den MatterCAD-Arbeitsbereich ziehen. Unterstützte Dateitypen werden automatisch importiert.

![20260324 081416 paste 20260324 081416](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081416-paste-20260324-081416.jpg)

## Aus der Bibliothek

### Die Bibliotheks-Seitenleiste

Klicken Sie in der Symbolleiste auf die Schaltfläche **Inhalt hinzufügen**, um den Bibliotheksbrowser zu öffnen. Von hier aus können Sie:

- Ihre gespeicherten Konstruktionen durchsuchen
- Zur Bibliothek Primitive navigieren, um integrierte Formen zu verwenden
- Auf Ihre Cloud-Bibliothek zugreifen, sofern Sie angemeldet sind
- Jedes Element aus der Bibliothek per Drag & Drop direkt in Ihren Arbeitsbereich ziehen

![20260324 081446 paste 20260324 081446](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081446-paste-20260324-081446.jpg)

### Die Registerkarte Bibliothek

Sie können auch die Registerkarte Bibliothek verwenden, um Ihre Sammlungen zu durchsuchen. Klicken Sie mit der rechten Maustaste auf ein beliebiges Objekt in der Bibliothek und wählen Sie **Zur Szene hinzufügen**, um es in Ihren aktuellen Konstruktionsarbeitsbereich zu importieren.

![20260324 081536 paste 20260324 081536](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081536-paste-20260324-081536.jpg)

## Tipps

- MCX ist das beste Format, um Konstruktionen später erneut zu bearbeiten, da es alle Parameter und den Konstruktionsbaum erhält
- STL-Dateien enthalten nur Netzgeometrie. Wenn Sie eine STL-Datei importieren, können Sie zwar weiterhin Operationen darauf anwenden, die ursprünglichen Parameter jedoch nicht bearbeiten
- Beim Import mehrerer Dateien wird jede davon zu einem eigenen Objekt in Ihrer Szene. Verwenden Sie [Gruppieren](../workspace/grouping.md), um sie zu organisieren

## Verwandte Themen

- [Neue Objekte erstellen](creating-new-objects.md) – Eine Konstruktion von Grund auf mit Primitiven beginnen
- [Speichern und Exportieren](saving-and-exporting.md) – Ihre fertigen Konstruktionen speichern und exportieren
- [Bibliothek](../library/index.md) – Mehr über das Organisieren Ihrer Konstruktionsbibliothek erfahren
