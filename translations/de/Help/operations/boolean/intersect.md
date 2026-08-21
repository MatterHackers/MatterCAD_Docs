---
title: Verschneiden
articleKey: IntersectionObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b997cfc4f6d2f02559346365311f217388a6a2da
source_lang: en
---
# Verschneiden

Verschneiden behält nur das Volumen, das alle Objekte gemeinsam haben, und verwirft den Rest.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->
![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)

[Vereinen](combine.md), [Subtrahieren](subtract.md), Verschneiden und [Subtrahieren und Ersetzen](subtract-and-replace.md) werden alle von einem einzigen booleschen Objekt ausgeführt -- die Schaltfläche in der Symbolleiste erzeugt es mit bereits ausgewähltem Verschneiden, und Sie können jederzeit über die Symbolreihe **Operation** oben im Eigenschaften-Panel zu einer der anderen drei wechseln.

Verschneiden funktioniert mit Volumenkörpern und mit 2D-Pfaden. Es betrachtet, was Sie ihm übergeben, und führt die passende Art von Operation aus: Das Verschneiden zweier Pfade ergibt einen Pfad, das Verschneiden zweier Netze ergibt einen Volumenkörper.

## Verwendung

1. Wählen Sie zwei oder mehr Objekte aus
2. Klicken Sie in der Symbolleiste auf **Verschneiden**
3. Ändern Sie Ihre Wahl jederzeit, indem Sie in der Reihe **Operation** oben im Eigenschaften-Panel auf ein anderes Symbol klicken -- die Form wird mit der neuen Operation neu aufgebaut

## Parameter

- **Operation** - Welche boolesche Operation ausgeführt wird. Wird als Symbolreihe oben im Panel angezeigt
- **Innen-nach-außen-Geometrie beibehalten** - Behandelt eine nach innen gestülpte Hülle als massives Material, statt sie das umgebende Volumen aufheben zu lassen. Aktivieren Sie dies, wenn ein Modell, das massiv sein sollte, mit fehlenden Teilen zurückkommt. Es erzwingt die langsamere, exakte boolesche Engine
- **Windungsreihenfolge reparieren** - Dreht die nach innen gestülpten Hüllen jedes Teils vor der booleschen Operation um. Damit wird die Geometrie einmalig korrigiert, statt zu ändern, was jede spätere Operation als massiv wertet -- meist die bessere der beiden Antworten auf ein nach innen gestülptes Modell

## Tipps

- Die Objekte müssen sich überlappen. Wenn sie sich nicht tatsächlich überlappen, ist das Ergebnis leer
- Bei mehr als zwei Objekten arbeitet die Operation die Liste ab: Die ersten beiden werden verschnitten, dann wird dieses Ergebnis mit dem dritten verschnitten und so weiter
- Wenn ein Ergebnis falsch aussieht, prüfen Sie, ob die Ausgangsobjekte wasserdicht sind. **Windungsreihenfolge reparieren** korrigiert nach innen gestülpte Hüllen; [Reparieren](../mesh/repair.md) behebt größere Schäden in importierten Modellen

## Verwandte Themen

- [Vereinen](combine.md) - Mehrere Objekte zu einer einzigen massiven Form zusammenführen
- [Subtrahieren](subtract.md) - Eine Form aus einer anderen ausschneiden
- [Subtrahieren und Ersetzen](subtract-and-replace.md) - Eine Form subtrahieren und das herausgeschnittene Stück behalten
- [Ebenenschnitt](../reshape/plane-cut.md) - Mit einer ebenen Fläche statt mit einer anderen Form schneiden
- [Reparieren](../mesh/repair.md) - Beschädigte importierte Netze vor einer booleschen Operation korrigieren

Diese Seite behandelt auch die älteren Schnittmenge-Objekte, die noch in Entwürfen zu finden sind, die vor der Zusammenführung der Operationen gespeichert wurden. Sie funktionieren weiterhin genau wie zuvor; neue Entwürfe verwenden das gemeinsame boolesche Objekt mit der ausgewählten Operation Verschneiden.
