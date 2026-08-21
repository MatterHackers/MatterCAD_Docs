---
title: Gruppieren
parent: "Workspace"
nav_order: 3
source_hash: 82b506a886e270535b5bd58c3913f49328abc4d5
source_lang: en
---
# Gruppieren

Beim Gruppieren werden mehrere Objekte zu einer einzigen Einheit zusammengefasst, die als ein Objekt verschoben, kopiert und bearbeitet werden kann. Im Gegensatz zu [Vereinen](../operations/boolean/combine.md) wird die Geometrie beim Gruppieren nicht zusammengeführt -- jedes Objekt bleibt innerhalb der Gruppe eigenständig.

<!-- Screenshot showing objects before and after grouping, with the design tree showing the group hierarchy -->
![20260318 193104 paste 20260318 193104](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193104-paste-20260318-193104.jpg)

![20260318 193235 paste 20260318 193235](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193235-paste-20260318-193235.jpg)

![20260318 193138 paste 20260318 193138](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193138-paste-20260318-193138.jpg)


## Anwendung

### Objekte gruppieren

1. Wählen Sie zwei oder mehr Objekte aus (Umschalt-Klick oder Strg-Klick für die Mehrfachauswahl)
2. Klicken Sie in der Symbolleiste auf die Schaltfläche **Gruppieren**
3. Die Objekte sind nun gruppiert -- sie bewegen sich gemeinsam als eine Einheit

### Gruppierung von Objekten aufheben

1. Wählen Sie eine Gruppe aus
2. Klicken Sie in der Symbolleiste auf die Schaltfläche **Gruppierung aufheben**
3. ![20260318 193354 paste 20260318 193354](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193354-paste-20260318-193354.jpg)
4. Die einzelnen Objekte werden als separate Elemente wiederhergestellt

Beim Aufheben der Gruppierung wird außerdem versucht, mehrere Körper innerhalb einer einzelnen importierten STL-Datei zu trennen, sofern vorhanden.

## Gruppieren vs. Vereinen

| Merkmal | Gruppieren | Vereinen |
|---------|-------|---------|
| Objekte bleiben eigenständig | Ja | Nein |
| Gruppierung später aufhebbar | Ja | Nein (destruktiv) |
| Überlappende Geometrie wird zusammengeführt | Nein | Ja |
| Objekte können unterschiedliche Farben haben | Ja | Farben werden pro Fläche beibehalten |
| Anwendungsfall | Organisation und Bewegung | Erstellen einzelner Volumenkörper |

## Tipps

- Gruppen können verschachtelt werden -- Sie können Objekte gruppieren, die sich bereits in Gruppen befinden
- Wählen Sie eine Gruppe aus und sehen Sie im Konstruktionsbaum nach, um einzelne Objekte darin anzuzeigen und auszuwählen
- Das Gruppieren ist nicht destruktiv und kann jederzeit mit Gruppierung aufheben rückgängig gemacht werden

## Verwandte Themen

- [Vereinen](../operations/boolean/combine.md) - Objekte zu einem einzigen Volumenkörper zusammenführen, statt sie zu gruppieren
- [Auswahl](selection.md) - So wählen Sie mehrere Objekte zum Gruppieren aus
- [Komponenten](components.md) - Wiederverwendbare parametrisierte Gruppen erstellen
