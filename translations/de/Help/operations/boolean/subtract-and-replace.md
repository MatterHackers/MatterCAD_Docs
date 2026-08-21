---
title: Subtrahieren & Ersetzen
articleKey: SubtractAndReplaceObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c1698bab75faca8046b23cc148803c8063ba0678
source_lang: en
---
# Subtrahieren & Ersetzen

Subtrahieren & Ersetzen subtrahiert die von Ihnen ausgewählten Bauteile aus den nicht ausgewählten, behält das weggeschnittene Stück aber als eigenes Bauteil, anstatt es zu verwerfen. Wählen Sie über **Zu subtrahierende Bauteile** die Schneidformen aus; alles Übrige ist die Basis, die geschnitten wird.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->
![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)

[Vereinen](combine.md), [Subtrahieren](subtract.md), [Verschneiden](intersect.md) und Subtrahieren & Ersetzen werden alle von einem einzigen Boolean-Objekt ausgeführt -- die Schaltfläche in der Symbolleiste erstellt es mit bereits ausgewähltem Subtrahieren & Ersetzen, und Sie können jederzeit über die Symbolreihe **Operation** oben im Eigenschaften-Panel zu einer der anderen drei wechseln.

Subtrahieren & Ersetzen steht für 2D-Pfade nicht zur Verfügung -- eine Fläche hat kein entferntes Volumen, das zurückgegeben werden könnte.

## Verwendung

1. Wählen Sie zwei oder mehr Objekte aus
2. Klicken Sie in der Symbolleiste auf **Subtrahieren & Ersetzen**
3. Legen Sie über **Zu subtrahierende Bauteile** fest, welche untergeordneten Objekte die Schneidformen sind
4. Ändern Sie Ihre Auswahl jederzeit, indem Sie in der Reihe **Operation** oben im Eigenschaften-Panel auf ein anderes Symbol klicken -- die Form wird mit der neuen Operation neu aufgebaut

## Parameter

- **Operation** - Welche boolesche Operation ausgeführt wird. Wird als Symbolreihe oben im Panel angezeigt
- **Zu subtrahierende Bauteile** - Welche untergeordneten Objekte die Schneidformen sind
- **Innen-nach-außen-Geometrie beibehalten** - Behandelt eine nach außen gestülpte Hülle als massives Material, statt sie das umgebende Volumen aufheben zu lassen. Aktivieren Sie diese Option, wenn ein Modell, das massiv sein sollte, mit fehlenden Teilen zurückkommt. Sie erzwingt die langsamere, exakte Boolean-Engine
- **Windungsreihenfolge reparieren** - Kehrt die nach außen gestülpten Hüllen jedes Bauteils um, bevor die boolesche Operation ausgeführt wird. Damit wird die Geometrie einmalig korrigiert, statt zu ändern, was jede spätere Operation als massiv wertet -- meist die bessere der beiden Lösungen für ein nach außen gestülptes Modell

## Tipps

- Die beiden Bauteile passen exakt zusammen, weil sie aus derselben Operation stammen
- Verwenden Sie die Funktion für mehrfarbige Designs, ineinandergreifende Baugruppen und Intarsien
- Wenn ein Ergebnis falsch aussieht, prüfen Sie, ob die Ausgangsobjekte wasserdicht sind. **Windungsreihenfolge reparieren** korrigiert nach außen gestülpte Hüllen; [Reparieren](../mesh/repair.md) behebt größere Schäden in importierten Modellen

## Verwandte Themen

- [Vereinen](combine.md) - Mehrere Objekte zu einer einzigen massiven Form zusammenführen
- [Subtrahieren](subtract.md) - Eine Form aus einer anderen ausschneiden
- [Verschneiden](intersect.md) - Nur das Volumen behalten, in dem sich Objekte überlappen
- [Ebenenschnitt](../reshape/plane-cut.md) - Mit einer flachen Ebene statt mit einer anderen Form schneiden
- [Reparieren](../mesh/repair.md) - Beschädigte importierte Netze vor einer booleschen Operation reparieren

Diese Seite behandelt auch die älteren Subtrahieren-und-Ersetzen-Objekte, die noch in Designs zu finden sind, die vor dem Zusammenführen der Operationen gespeichert wurden. Sie funktionieren weiterhin genau wie zuvor; neue Designs verwenden das gemeinsame Boolean-Objekt mit der ausgewählten Operation Subtrahieren & Ersetzen.
