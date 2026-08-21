---
title: Subtrahieren
articleKey: SubtractObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 59685bd0a635b70d7f938780f71e90be595dd993
source_lang: en
---
# Subtrahieren

Subtrahieren schneidet die Teile, die Sie auswählen, aus den Teilen heraus, die Sie nicht ausgewählt haben. Über **Zu subtrahierende Teile** wählen Sie die Schneidkörper aus; alles Übrige bildet die Basis, aus der geschnitten wird.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->
![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)

[Kombinieren](combine.md), Subtrahieren, [Überschneiden](intersect.md) und [Subtrahieren und Ersetzen](subtract-and-replace.md) werden alle von einem einzigen Boolean-Objekt ausgeführt – die Schaltfläche in der Symbolleiste erzeugt es mit bereits ausgewähltem Subtrahieren, und Sie können jederzeit über die Symbolreihe **Operation** oben im Eigenschaften-Panel zu einer der drei anderen Operationen wechseln.

Subtrahieren funktioniert mit Volumenkörpern und mit 2D-Pfaden. Es betrachtet, was Sie ihm übergeben, und führt die passende Art von Operation aus: Das Subtrahieren eines Pfads von einem anderen ergibt einen Pfad, das Subtrahieren eines Netzes von einem anderen ergibt einen Volumenkörper.

## Verwendung

1. Wählen Sie zwei oder mehr Objekte aus
2. Klicken Sie in der Symbolleiste auf **Subtrahieren** – ein Standardteil zum Wegschneiden wird automatisch ausgewählt, sodass sofort etwas passiert
3. Legen Sie über **Zu subtrahierende Teile** fest, welche untergeordneten Objekte die Schneidkörper sind
4. Ändern Sie Ihre Wahl jederzeit, indem Sie in der Reihe **Operation** oben im Eigenschaften-Panel ein anderes Symbol anklicken – die Form wird mit der neuen Operation neu aufgebaut

## Parameter

- **Operation** – Welche Boolean-Operation ausgeführt wird. Wird als Symbolreihe oben im Panel angezeigt
- **Zu subtrahierende Teile** – Welche untergeordneten Objekte die Schneidkörper sind
- **Subtrahierte Teile behalten** – Belässt die weggeschnittenen Teile in der Szene, anstatt sie zu verwerfen
- **Umgestülpte Geometrie behalten** – Behandelt eine umgestülpte Hülle als massives Material, statt sie das umgebende Volumen aufheben zu lassen. Aktivieren Sie diese Option, wenn ein Modell, das massiv sein sollte, mit fehlenden Bereichen zurückkommt. Dadurch wird die langsamere, exakte Boolean-Engine erzwungen
- **Umlaufrichtung reparieren** – Dreht die umgestülpten Hüllen jedes Teils vor der Boolean-Operation um. Damit wird die Geometrie einmalig korrigiert, statt zu ändern, was jede spätere Operation als massiv betrachtet – meist die bessere der beiden Antworten auf ein umgestülptes Modell

## Tipps

- Objekte müssen sich überlappen, damit Subtrahieren eine Wirkung hat
- Damit ein Durchgangsloch entsteht, muss der Schneidkörper vollständig durch die Basis hindurchreichen
- Für ein einfaches Loch ist das Primitiv [Loch](../../primitives/hole.md) bereits auf Subtrahieren eingestellt
- Die Schneidkörper bleiben im Konstruktionsbaum erhalten, sodass Sie sie verschieben oder in der Größe ändern können und der Schnitt aktualisiert wird
- Wenn ein Ergebnis falsch aussieht, prüfen Sie, ob die Ausgangsobjekte wasserdicht sind. **Umlaufrichtung reparieren** korrigiert umgestülpte Hüllen; [Reparieren](../mesh/repair.md) behebt umfassendere Schäden in importierten Modellen

## Verwandte Themen

- [Kombinieren](combine.md) – Mehrere Objekte zu einem einzigen Volumenkörper verschmelzen
- [Überschneiden](intersect.md) – Nur das Volumen behalten, in dem sich Objekte überlappen
- [Subtrahieren und Ersetzen](subtract-and-replace.md) – Eine Form subtrahieren und das weggeschnittene Stück behalten
- [Ebenenschnitt](../reshape/plane-cut.md) – Mit einer ebenen Fläche statt mit einer anderen Form schneiden
- [Loch](../../primitives/hole.md) – Ein Würfel, der bereits zum Subtrahieren vorkonfiguriert ist
- [Reparieren](../mesh/repair.md) – Beschädigte importierte Netze vor einer Boolean-Operation reparieren

Diese Seite behandelt auch die älteren Subtrahieren-Objekte, die noch in Designs zu finden sind, die vor der Zusammenführung der Operationen gespeichert wurden. Sie funktionieren weiterhin genau wie bisher; neue Designs verwenden das gemeinsame Boolean-Objekt mit ausgewählter Operation „Subtrahieren“.
