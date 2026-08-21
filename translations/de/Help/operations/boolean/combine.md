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

Vereinen führt alles zu einem einzigen Volumenkörper zusammen. Innenliegende Flächen an den Überlappungen der Formen werden entfernt, sodass ein durchgehendes Netz statt sich überlappender Hüllen entsteht.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->
![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)

Vereinen, [Subtrahieren](subtract.md), [Schnittmenge](intersect.md) und [Subtrahieren und Ersetzen](subtract-and-replace.md) werden alle von ein und demselben Boolean-Objekt ausgeführt -- die Symbolleistenschaltfläche erzeugt es bereits mit ausgewähltem Vereinen, und Sie können jederzeit über die Symbolreihe **Operation** oben im Eigenschaftenbereich zu einer der anderen drei wechseln.

Vereinen funktioniert mit Volumenkörpern und mit 2D-Pfaden. Es prüft, was Sie ihm übergeben, und führt die passende Art von Operation aus: Das Vereinen zweier Pfade ergibt einen Pfad, das Vereinen zweier Netze ergibt einen Volumenkörper.

## Vorgehensweise

1. Wählen Sie zwei oder mehr Objekte aus
2. Klicken Sie in der Symbolleiste auf **Vereinen**
3. Ändern Sie Ihre Auswahl jederzeit, indem Sie in der Reihe **Operation** oben im Eigenschaftenbereich auf ein anderes Symbol klicken -- die Form wird mit der neuen Operation neu aufgebaut

## Parameter

- **Operation** - Welche boolesche Operation ausgeführt wird. Wird als Symbolreihe oben im Bereich angezeigt
- **Umgestülpte Geometrie beibehalten** - Behandelt eine umgestülpte Hülle als massives Material, anstatt zuzulassen, dass sie das umgebende Volumen aufhebt. Aktivieren Sie dies, wenn bei einem Modell, das massiv sein sollte, Teile fehlen. Dadurch wird die langsamere, exakte Boolean-Engine erzwungen
- **Umlaufrichtung reparieren** - Dreht die umgestülpten Hüllen jedes Teils um, bevor die boolesche Operation ausgeführt wird. Das repariert die Geometrie ein einziges Mal, anstatt zu ändern, was jede spätere Operation als massiv betrachtet, und ist bei einem umgestülpten Modell meist die bessere der beiden Lösungen

## Tipps

- Vereinen fügt auch nicht überlappende Objekte zu einem Netz zusammen, sie bleiben jedoch optisch getrennt
- Vereinen berücksichtigt Loch-Objekte automatisch: Alles, was als Loch markiert ist, wird vom Ergebnis abgezogen statt hinzugefügt
- Vereinen übernimmt die flächenbezogenen Farben der Ursprungsobjekte
- Wenn ein Ergebnis falsch aussieht, prüfen Sie, ob die Ausgangsobjekte wasserdicht sind. **Umlaufrichtung reparieren** behebt umgestülpte Hüllen; [Reparieren](../mesh/repair.md) behebt größere Schäden in importierten Modellen

## Verwandte Themen

- [Subtrahieren](subtract.md) - Eine Form aus einer anderen ausschneiden
- [Schnittmenge](intersect.md) - Nur das Volumen behalten, in dem sich Objekte überlappen
- [Subtrahieren und Ersetzen](subtract-and-replace.md) - Eine Form subtrahieren und das herausgeschnittene Teil behalten
- [Ebenenschnitt](../reshape/plane-cut.md) - Mit einer ebenen Fläche statt mit einer anderen Form schneiden
- [Loch](../../primitives/hole.md) - Ein Würfel, der bereits zum Subtrahieren konfiguriert ist
- [Reparieren](../mesh/repair.md) - Beschädigte importierte Netze vor einer booleschen Operation reparieren

Diese Seite behandelt auch die älteren Combine-Objekte, die noch in Designs zu finden sind, die vor der Zusammenführung der Operationen gespeichert wurden. Sie funktionieren weiterhin genau wie zuvor; neue Designs verwenden das gemeinsame Boolean-Objekt mit der ausgewählten Operation Vereinen.
