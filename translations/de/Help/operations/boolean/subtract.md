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

Subtrahieren schneidet die von Ihnen ausgewählten Bauteile aus den nicht ausgewählten Bauteilen heraus. Verwenden Sie **Zu subtrahierende Bauteile**, um die Schnittformen festzulegen; alles Übrige bildet die Basis, aus der geschnitten wird.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->
![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)

[Vereinen](combine.md), Subtrahieren, [Verschneiden](intersect.md) und [Subtrahieren und Ersetzen](subtract-and-replace.md) werden alle von einem einzigen Boolean-Objekt ausgeführt -- die Symbolleisten-Schaltfläche erzeugt es mit bereits ausgewähltem Subtrahieren, und Sie können jederzeit über die Symbolreihe **Operation** oben im Eigenschaften-Panel zu einer der anderen drei wechseln.

Subtrahieren funktioniert mit Volumenkörpern und mit 2D-Pfaden. Es prüft, was Sie ihm übergeben, und führt die passende Art von Operation aus: Das Subtrahieren eines Pfades von einem anderen ergibt einen Pfad, das Subtrahieren eines Netzes von einem anderen ergibt einen Volumenkörper.

## Verwendung

1. Wählen Sie zwei oder mehr Objekte aus
2. Klicken Sie in der Symbolleiste auf **Subtrahieren** -- ein Standard-Bauteil zum Wegschneiden wird für Sie ausgewählt, sodass sofort ein Ergebnis entsteht
3. Verwenden Sie **Zu subtrahierende Bauteile**, um festzulegen, welche untergeordneten Objekte die Schnittformen sind
4. Ändern Sie Ihre Wahl jederzeit, indem Sie in der Reihe **Operation** oben im Eigenschaften-Panel auf ein anderes Symbol klicken -- die Form wird mit der neuen Operation neu aufgebaut

## Parameter

- **Operation** - Welche boolesche Operation ausgeführt wird. Wird als Symbolreihe oben im Panel angezeigt
- **Zu subtrahierende Bauteile** - Welche untergeordneten Objekte die Schnittformen sind
- **Abgezogene Teile beibehalten** - Die weggeschnittenen Bauteile in der Szene belassen, statt sie zu verwerfen
- **Innen-nach-außen-Geometrie beibehalten** - Eine nach innen gestülpte Hülle als massives Material behandeln, statt sie das umgebende Volumen aufheben zu lassen. Aktivieren Sie dies, wenn ein Modell, das massiv sein sollte, mit fehlenden Teilen zurückkommt. Dadurch wird die langsamere, exakte Boolean-Engine erzwungen
- **Windungsreihenfolge reparieren** - Die nach innen gestülpten Hüllen jedes Bauteils vor der booleschen Operation umkehren. Dies korrigiert die Geometrie einmalig, statt zu ändern, was jede spätere Operation als massiv wertet, und ist meist die bessere der beiden Antworten auf ein nach innen gestülptes Modell

## Tipps

- Objekte müssen sich überlappen, damit Subtrahieren etwas bewirkt
- Für ein Durchgangsloch muss das schneidende Objekt vollständig durch die Basis hindurchreichen
- Für ein einfaches Loch ist das Primitiv [Loch](../../primitives/hole.md) bereits zum Subtrahieren eingerichtet
- Die schneidenden Objekte bleiben im Konstruktionsbaum erhalten, sodass Sie sie verschieben oder in der Größe ändern können und der Schnitt aktualisiert wird
- Wenn ein Ergebnis falsch aussieht, prüfen Sie, ob die Ausgangsobjekte wasserdicht sind. **Windungsreihenfolge reparieren** korrigiert nach innen gestülpte Hüllen; [Reparieren](../mesh/repair.md) behebt umfassendere Schäden in importierten Modellen

## Verwandte Themen

- [Vereinen](combine.md) - Mehrere Objekte zu einer einzigen massiven Form zusammenführen
- [Verschneiden](intersect.md) - Nur das Volumen behalten, in dem sich Objekte überlappen
- [Subtrahieren und Ersetzen](subtract-and-replace.md) - Eine Form subtrahieren und das weggeschnittene Stück behalten
- [Ebenenschnitt](../reshape/plane-cut.md) - Mit einer ebenen Fläche statt mit einer anderen Form schneiden
- [Loch](../../primitives/hole.md) - Ein Würfel, der zum Subtrahieren vorkonfiguriert ist
- [Reparieren](../mesh/repair.md) - Beschädigte importierte Netze vor einer booleschen Operation korrigieren

Diese Seite behandelt auch die älteren Subtrahieren-Objekte, die noch in Designs vorkommen, die vor der Zusammenführung der Operationen gespeichert wurden. Sie funktionieren weiterhin genau wie zuvor; neue Designs verwenden das gemeinsame Boolean-Objekt mit der ausgewählten Operation Subtrahieren.
