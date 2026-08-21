---
title: Schnittmenge
articleKey: IntersectionObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b997cfc4f6d2f02559346365311f217388a6a2da
source_lang: en
---
# Schnittmenge

Die Schnittmenge behält nur das Volumen, das alle Objekte gemeinsam haben, und verwirft den Rest.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->
![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)

[Kombinieren](combine.md), [Subtrahieren](subtract.md), Schnittmenge und [Subtrahieren und Ersetzen](subtract-and-replace.md) werden alle von einem einzigen Boolean-Objekt ausgeführt -- die Schaltfläche in der Symbolleiste erzeugt es mit bereits ausgewählter Schnittmenge, und Sie können jederzeit über die Symbolreihe **Operation** oben im Eigenschaften-Panel zu einer der anderen drei wechseln.

Die Schnittmenge funktioniert mit Volumenkörpern und mit 2D-Pfaden. Sie prüft, was Sie ihr übergeben haben, und führt die passende Art von Operation aus: Das Verschneiden zweier Pfade ergibt einen Pfad, das Verschneiden zweier Netze einen Volumenkörper.

## Verwendung

1. Wählen Sie zwei oder mehr Objekte aus
2. Klicken Sie in der Symbolleiste auf **Schnittmenge**
3. Ändern Sie Ihre Entscheidung jederzeit, indem Sie in der Reihe **Operation** oben im Eigenschaften-Panel auf ein anderes Symbol klicken -- die Form wird mit der neuen Operation neu aufgebaut

## Parameter

- **Operation** - Welche boolesche Operation ausgeführt wird. Wird als Symbolreihe oben im Panel angezeigt
- **Umgestülpte Geometrie beibehalten** - Behandelt eine umgestülpte Hülle als massives Material, statt sie das umgebende Volumen auslöschen zu lassen. Aktivieren Sie dies, wenn bei einem Modell, das massiv sein sollte, Teile fehlen. Dies erzwingt die langsamere, exakte Boolean-Engine
- **Umlaufrichtung reparieren** - Dreht die umgestülpten Hüllen jedes Teils um, bevor die boolesche Operation ausgeführt wird. Damit wird die Geometrie einmalig korrigiert, statt zu ändern, was jede spätere Operation als massiv wertet -- meist die bessere der beiden Antworten auf ein umgestülptes Modell

## Tipps

- Die Objekte müssen sich überlappen. Wenn sie sich tatsächlich nicht überlappen, ist das Ergebnis leer
- Bei mehr als zwei Objekten arbeitet die Operation die Liste ab: Die ersten beiden werden verschnitten, dieses Ergebnis wird dann mit dem dritten verschnitten und so weiter
- Sieht ein Ergebnis falsch aus, prüfen Sie, ob die Ausgangsobjekte wasserdicht sind. **Umlaufrichtung reparieren** behebt umgestülpte Hüllen; [Reparieren](../mesh/repair.md) behebt größere Schäden in importierten Modellen

## Verwandte Themen

- [Kombinieren](combine.md) - Mehrere Objekte zu einer einzigen massiven Form zusammenführen
- [Subtrahieren](subtract.md) - Eine Form aus einer anderen ausschneiden
- [Subtrahieren und Ersetzen](subtract-and-replace.md) - Eine Form subtrahieren und das herausgeschnittene Stück behalten
- [Ebenenschnitt](../reshape/plane-cut.md) - Mit einer ebenen Fläche statt mit einer anderen Form schneiden
- [Reparieren](../mesh/repair.md) - Beschädigte importierte Netze vor einer booleschen Operation reparieren

Diese Seite behandelt auch die älteren Intersection-Objekte, die noch in Designs zu finden sind, die vor der Zusammenführung der Operationen gespeichert wurden. Sie funktionieren weiterhin genau wie zuvor; neue Designs verwenden das gemeinsame Boolean-Objekt mit ausgewählter Operation Schnittmenge.
