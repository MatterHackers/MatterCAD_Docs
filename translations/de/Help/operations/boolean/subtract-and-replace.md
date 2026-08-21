---
title: Subtrahieren und Ersetzen
articleKey: SubtractAndReplaceObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c1698bab75faca8046b23cc148803c8063ba0678
source_lang: en
---
# Subtrahieren und Ersetzen

Subtrahieren und Ersetzen subtrahiert die von Ihnen ausgewählten Teile aus den nicht ausgewählten Teilen, behält das herausgeschnittene Stück aber als eigenes Teil bei, statt es zu verwerfen. Verwenden Sie **Zu subtrahierende Teile**, um die Schnittkörper festzulegen; alles Übrige bildet die Basis, aus der geschnitten wird.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->
![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)

[Vereinigen](combine.md), [Subtrahieren](subtract.md), [Verschneiden](intersect.md) und Subtrahieren und Ersetzen werden alle von einem einzigen Boolean-Objekt ausgeführt -- die Schaltfläche in der Symbolleiste erzeugt es mit bereits ausgewählter Operation Subtrahieren & Ersetzen, und Sie können jederzeit über die Symbolreihe **Operation** oben im Eigenschaften-Bereich zu einer der drei anderen wechseln.

Für 2D-Pfade steht Subtrahieren & Ersetzen nicht zur Verfügung -- eine Fläche besitzt kein entferntes Volumen, das zurückgegeben werden könnte.

## Verwendung

1. Wählen Sie zwei oder mehr Objekte aus
2. Klicken Sie in der Symbolleiste auf **Subtrahieren & Ersetzen**
3. Legen Sie über **Zu subtrahierende Teile** fest, welche untergeordneten Objekte die Schnittkörper sind
4. Sie können sich jederzeit umentscheiden, indem Sie in der Reihe **Operation** oben im Eigenschaften-Bereich auf ein anderes Symbol klicken -- die Form wird mit der neuen Operation neu aufgebaut

## Parameter

- **Operation** - Welche boolesche Operation ausgeführt wird. Wird als Symbolreihe oben im Bereich angezeigt
- **Zu subtrahierende Teile** - Welche untergeordneten Objekte die Schnittkörper sind
- **Umgestülpte Geometrie beibehalten** - Behandelt eine umgestülpte Hülle als massives Material, anstatt sie das umgebende Volumen aufheben zu lassen. Aktivieren Sie diese Option, wenn ein Modell, das massiv sein sollte, mit fehlenden Bereichen zurückkommt. Dies erzwingt die langsamere, exakte Boolean-Engine
- **Umlaufrichtung reparieren** - Dreht die umgestülpten Hüllen jedes Teils um, bevor die boolesche Operation ausgeführt wird. Damit wird die Geometrie einmalig korrigiert, statt zu ändern, was jede spätere Operation als massiv wertet, und ist meist die bessere der beiden Antworten auf ein umgestülptes Modell

## Tipps

- Die beiden Teile passen exakt zusammen, da sie aus derselben Operation stammen
- Verwenden Sie die Funktion für mehrfarbige Entwürfe, ineinandergreifende Baugruppen und Einlegearbeiten
- Wenn ein Ergebnis falsch aussieht, prüfen Sie, ob die Ausgangsobjekte wasserdicht sind. **Umlaufrichtung reparieren** behebt umgestülpte Hüllen; [Reparieren](../mesh/repair.md) behebt umfassendere Schäden in importierten Modellen

## Verwandte Themen

- [Vereinigen](combine.md) - Mehrere Objekte zu einer einzigen massiven Form zusammenführen
- [Subtrahieren](subtract.md) - Eine Form aus einer anderen herausschneiden
- [Verschneiden](intersect.md) - Nur das Volumen behalten, in dem sich Objekte überschneiden
- [Ebenenschnitt](../reshape/plane-cut.md) - Mit einer ebenen Fläche statt mit einer anderen Form schneiden
- [Reparieren](../mesh/repair.md) - Beschädigte importierte Meshes vor einer booleschen Operation reparieren

Diese Seite behandelt auch die älteren Objekte Subtrahieren und Ersetzen, die noch in Entwürfen vorkommen, die vor der Zusammenführung der Operationen gespeichert wurden. Sie funktionieren weiterhin genau wie zuvor; neue Entwürfe verwenden das gemeinsame Boolean-Objekt mit der ausgewählten Operation Subtrahieren & Ersetzen.
