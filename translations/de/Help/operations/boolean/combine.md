---
title: Vereinen
articleKey: CombineObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: a3066faa634b5a88a2fe1650a4e2ac278ac50e24
source_lang: en
---
# Vereinen

Vereinen verschmilzt alles zu einem einzigen Volumenkörper. Interne Flächen, an denen sich die Formen überlappt haben, werden entfernt, sodass das Ergebnis ein durchgehendes Netz statt überlappender Hüllen ist.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->
![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)

Vereinen, [Subtrahieren](subtract.md), [Verschneiden](intersect.md) und [Subtrahieren und Ersetzen](subtract-and-replace.md) werden alle von einem einzigen booleschen Objekt ausgeführt -- die Schaltfläche in der Symbolleiste erzeugt es mit bereits ausgewählter Operation Vereinen, und Sie können jederzeit über die Symbolreihe **Operation** oben im Eigenschaften-Panel zu einer der drei anderen wechseln.

Vereinen funktioniert mit Volumenkörpern und mit 2D-Pfaden. Es prüft, was Sie ihm übergeben, und führt die passende Art von Operation aus: Das Vereinen zweier Pfade ergibt einen Pfad, das Vereinen zweier Netze einen Volumenkörper.

## Verwendung

1. Wählen Sie zwei oder mehr Objekte aus
2. Klicken Sie in der Symbolleiste auf **Vereinen**
3. Ändern Sie Ihre Entscheidung jederzeit, indem Sie in der Reihe **Operation** oben im Eigenschaften-Panel auf ein anderes Symbol klicken -- die Form wird mit der neuen Operation neu aufgebaut

## Parameter

- **Operation** - Welche boolesche Operation ausgeführt wird. Wird als Symbolreihe oben im Panel angezeigt
- **Innen-nach-außen-Geometrie beibehalten** - Behandelt eine nach innen gestülpte Hülle als massives Material, anstatt sie das umgebende Volumen aufheben zu lassen. Aktivieren Sie dies, wenn bei einem Modell, das massiv sein sollte, Teile fehlen. Dadurch wird die langsamere, exakte boolesche Engine erzwungen
- **Windungsreihenfolge reparieren** - Kehrt die nach innen gestülpten Hüllen jedes Teils vor der booleschen Operation um. Damit wird die Geometrie einmalig korrigiert, statt zu ändern, was jede spätere Operation als massiv wertet, und ist meist die bessere der beiden Antworten auf ein nach innen gestülptes Modell

## Tipps

- Vereinen fügt auch nicht überlappende Objekte zu einem Netz zusammen, sie bleiben jedoch optisch getrennt
- Vereinen berücksichtigt Loch-Objekte automatisch: Alles, was als Loch markiert ist, wird vom Ergebnis subtrahiert statt hinzugefügt
- Vereinen überträgt die Farben einzelner Flächen von den Ausgangsobjekten
- Wenn ein Ergebnis falsch aussieht, prüfen Sie, ob die Ausgangsobjekte wasserdicht sind. **Windungsreihenfolge reparieren** korrigiert nach innen gestülpte Hüllen; [Reparieren](../mesh/repair.md) behebt umfassendere Schäden in importierten Modellen

## Verwandte Themen

- [Subtrahieren](subtract.md) - Eine Form aus einer anderen ausschneiden
- [Verschneiden](intersect.md) - Nur das Volumen behalten, in dem sich Objekte überlappen
- [Subtrahieren und Ersetzen](subtract-and-replace.md) - Eine Form subtrahieren und das ausgeschnittene Teil behalten
- [Ebenenschnitt](../reshape/plane-cut.md) - Mit einer ebenen Fläche statt mit einer anderen Form schneiden
- [Loch](../../primitives/hole.md) - Ein Würfel, der zum Subtrahieren vorkonfiguriert ist
- [Reparieren](../mesh/repair.md) - Beschädigte importierte Netze vor einer booleschen Operation reparieren

Diese Seite behandelt auch die älteren Vereinen-Objekte, die noch in Konstruktionen vorkommen, die vor dem Zusammenführen der Operationen gespeichert wurden. Sie funktionieren weiterhin genau wie bisher; neue Konstruktionen verwenden das gemeinsame boolesche Objekt mit ausgewählter Operation Vereinen.
