---
title: Gruppieren
parent: "Workspace"
nav_order: 3
source_hash: 82b506a886e270535b5bd58c3913f49328abc4d5
source_lang: en
---
# Gruppieren

Beim Gruppieren werden mehrere Objekte zu einer einzigen Einheit zusammengefasst, die als ein Objekt bewegt, kopiert und bearbeitet werden kann. Anders als beim [Kombinieren](../operations/boolean/combine.md) wird die Geometrie dabei nicht verschmolzen -- jedes Objekt bleibt innerhalb der Gruppe eigenständig.

<!-- Screenshot showing objects before and after grouping, with the design tree showing the group hierarchy -->
![20260318 193104 paste 20260318 193104](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193104-paste-20260318-193104.jpg)

![20260318 193235 paste 20260318 193235](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193235-paste-20260318-193235.jpg)

![20260318 193138 paste 20260318 193138](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193138-paste-20260318-193138.jpg)


## Anwendung

### Objekte gruppieren

1. Wählen Sie zwei oder mehr Objekte aus (Mehrfachauswahl mit Shift-Klick oder Strg-Klick)
2. Klicken Sie in der Symbolleiste auf die Schaltfläche **Gruppieren**
3. Die Objekte sind nun gruppiert -- sie bewegen sich gemeinsam als eine Einheit

### Gruppierung von Objekten aufheben

1. Wählen Sie eine Gruppe aus
2. Klicken Sie in der Symbolleiste auf die Schaltfläche **Gruppierung aufheben**
3. ![20260318 193354 paste 20260318 193354](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193354-paste-20260318-193354.jpg)
4. Die einzelnen Objekte werden als separate Elemente wiederhergestellt

Beim Aufheben der Gruppierung wird außerdem versucht, mehrere Körper innerhalb einer einzelnen importierten STL-Datei voneinander zu trennen, sofern vorhanden.

## Gruppieren vs. Kombinieren

| Merkmal | Gruppieren | Kombinieren |
|---------|-------|---------|
| Objekte bleiben eigenständig | Ja | Nein |
| Später wieder auflösbar | Ja | Nein (destruktiv) |
| Überlappende Geometrie wird verschmolzen | Nein | Ja |
| Objekte können unterschiedliche Farben haben | Ja | Farben bleiben pro Fläche erhalten |
| Anwendungsfall | Organisation und Bewegung | Erstellen einzelner Volumenkörper |

## Tipps

- Gruppen lassen sich verschachteln -- Sie können Objekte gruppieren, die bereits in Gruppen enthalten sind
- Wählen Sie eine Gruppe aus und sehen Sie im Konstruktionsbaum nach, um einzelne Objekte darin anzuzeigen und auszuwählen
- Gruppieren ist nicht destruktiv und kann jederzeit mit „Gruppierung aufheben“ rückgängig gemacht werden

## Verwandte Themen

- [Kombinieren](../operations/boolean/combine.md) - Objekte zu einem einzelnen Volumenkörper verschmelzen, statt sie zu gruppieren
- [Auswahl](selection.md) - So wählen Sie mehrere Objekte zum Gruppieren aus
- [Komponenten](components.md) - Wiederverwendbare parametrisierte Gruppen erstellen
