---
title: Speichern und Exportieren
parent: "Getting Started"
nav_order: 4
source_hash: 020d4bf43f07d3ab7dbd7d585e13c99309f0c0b8
source_lang: en
---
# Speichern und Exportieren

MatterCAD unterstützt mehrere Dateiformate zum Speichern und Exportieren Ihrer Konstruktionen. Welches Format Sie wählen, hängt davon ab, wie Sie die Datei verwenden möchten.

## Speicherformate

### MCX (natives Format)

MCX ist das native Dateiformat von MatterCAD und die beste Wahl für Konstruktionen, die Sie später weiterbearbeiten möchten. Es bewahrt:

- Den vollständigen Konstruktionsbaum mit allen Objekten und ihrer Hierarchie
- Alle Parameter und Einstellungen jedes Objekts
- Boolesche Operationen, Anordnungen und andere Operationen in bearbeitbarer Form
- Komponentenbeziehungen

**MCX verwenden, wenn:** Sie Ihre Arbeit sichern und später weiterbearbeiten möchten.

### STL

STL ist das am weitesten verbreitete Format für den 3D-Druck. Es enthält nur die endgültige Dreiecksnetz-Geometrie ohne Konstruktionsverlauf oder Parameter.

**STL verwenden, wenn:** Sie Ihre Konstruktion in 3D drucken oder mit jemandem teilen möchten, der MatterCAD nicht verwendet.

### OBJ

OBJ (Wavefront) ist ein gängiges 3D-Format, das von den meisten 3D-Programmen unterstützt wird. Wie STL enthält es ausschließlich Netzgeometrie.

**OBJ verwenden, wenn:** Sie Ihre Konstruktion in anderer 3D-Software wie Blender oder einer Game-Engine öffnen müssen.

### SVG

Der SVG-Export erzeugt aus der Draufsicht Ihrer Konstruktion eine 2D-Vektordatei. Das ist nützlich für Laserschneiden oder CNC-Fräsen.

**SVG verwenden, wenn:** Sie eine 2D-Kontur Ihrer Konstruktion zum Laserschneiden oder Gravieren benötigen.

## So speichern Sie

![20260324 080726 paste 20260324 080726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080726-paste-20260324-080726.jpg)

1. Öffnen Sie das **Markenmenü** (das MatterCAD-Logo in der oberen linken Ecke)
2. Wählen Sie **Speichern unter**, um Speicherort und Format festzulegen
3. Wählen Sie das Dateiformat aus der Formate-Auswahlliste
4. Legen Sie fest, wo die Datei gespeichert werden soll, und klicken Sie auf **Speichern**

Ihre Konstruktion wird während der Arbeit auch automatisch gespeichert, sodass keine Änderungen verloren gehen, wenn Sie die Anwendung schließen.

## Tipps

- Speichern Sie immer eine MCX-Kopie Ihrer Konstruktion, bevor Sie nach STL oder OBJ exportieren, damit Sie später noch Änderungen vornehmen können
- Beim Export nach STL werden alle Objekte in der Szene zu einem einzigen Netz zusammengeführt
- Wenn Sie eine Konstruktion mit jemandem teilen möchten, der MatterCAD verwendet, senden Sie die MCX-Datei, um die vollständige Bearbeitbarkeit zu erhalten
- Sie können Konstruktionen auch in Ihrer [Cloud-Bibliothek](../library/cloud-library.md) speichern, um von jedem Computer aus darauf zuzugreifen

## Verwandte Themen

- [Vorhandene Objekte hinzufügen](adding-existing-objects.md) – Dateien in MatterCAD importieren
- [Bibliothek](../library/index.md) – Ihre gespeicherten Konstruktionen organisieren
- [Cloud-Bibliothek](../library/cloud-library.md) – Konstruktionen in der Cloud speichern
