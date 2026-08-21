---
title: Speichern und Exportieren
parent: "Getting Started"
nav_order: 4
source_hash: 020d4bf43f07d3ab7dbd7d585e13c99309f0c0b8
source_lang: en
---
# Speichern und Exportieren

MatterCAD unterstützt mehrere Dateiformate zum Speichern und Exportieren Ihrer Entwürfe. Welches Format Sie wählen, hängt davon ab, wie Sie die Datei verwenden möchten.

## Speicherformate

### MCX (natives Format)

MCX ist das native Dateiformat von MatterCAD und die beste Wahl für Entwürfe, die Sie später weiterbearbeiten möchten. Es bewahrt:

- Den vollständigen Entwurfsbaum mit allen Objekten und ihrer Hierarchie
- Alle Parameter und Einstellungen jedes Objekts
- Boolesche Operationen, Arrays und andere Operationen in bearbeitbarer Form
- Komponentenbeziehungen

**MCX verwenden, wenn:** Sie Ihre Arbeit speichern und später weiterbearbeiten möchten.

### STL

STL ist das am weitesten verbreitete Format für den 3D-Druck. Es enthält ausschließlich die endgültige Dreiecksnetz-Geometrie ohne Entwurfsverlauf oder Parameter.

**STL verwenden, wenn:** Sie Ihren Entwurf im 3D-Druck fertigen oder mit jemandem teilen möchten, der MatterCAD nicht verwendet.

### OBJ

OBJ (Wavefront) ist ein gängiges 3D-Format, das von den meisten 3D-Programmen unterstützt wird. Wie STL enthält es nur die Netzgeometrie.

**OBJ verwenden, wenn:** Sie Ihren Entwurf in anderer 3D-Software wie Blender oder in einer Game-Engine öffnen müssen.

### SVG

Der SVG-Export erzeugt eine 2D-Vektordatei aus der Draufsicht Ihres Entwurfs. Das ist nützlich für das Laserschneiden oder CNC-Fräsen.

**SVG verwenden, wenn:** Sie eine 2D-Kontur Ihres Entwurfs zum Laserschneiden oder Gravieren benötigen.

## So speichern Sie

![20260324 080726 paste 20260324 080726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080726-paste-20260324-080726.jpg)

1. Öffnen Sie das **Markenmenü** (das MatterCAD-Logo in der oberen linken Ecke)
2. Wählen Sie **Speichern unter**, um Speicherort und Format festzulegen
3. Wählen Sie das Dateiformat aus der Formatliste aus
4. Wählen Sie aus, wo die Datei gespeichert werden soll, und klicken Sie auf **Speichern**

Ihr Entwurf wird während der Arbeit außerdem automatisch gespeichert, sodass beim Schließen der Anwendung keine Änderungen verloren gehen.

## Tipps

- Speichern Sie stets eine MCX-Kopie Ihres Entwurfs, bevor Sie nach STL oder OBJ exportieren, damit Sie später noch Änderungen vornehmen können
- Beim STL-Export werden alle Objekte der Szene zu einem einzigen Netz zusammengeführt
- Wenn Sie einen Entwurf mit jemandem teilen möchten, der MatterCAD verwendet, senden Sie die MCX-Datei, um die vollständige Bearbeitbarkeit zu erhalten
- Sie können Entwürfe auch in Ihrer [Cloud-Bibliothek](../library/cloud-library.md) speichern, um von jedem Computer aus darauf zuzugreifen

## Verwandte Themen

- [Vorhandene Objekte hinzufügen](adding-existing-objects.md) – Dateien in MatterCAD importieren
- [Bibliothek](../library/index.md) – Ihre gespeicherten Entwürfe organisieren
- [Cloud-Bibliothek](../library/cloud-library.md) – Entwürfe in der Cloud speichern
