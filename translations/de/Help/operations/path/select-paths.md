---
title: Pfade auswählen
articleKey: SelectPathsObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: f7df7bb24841030643e4634febedcfce6e92ada9
source_lang: en
---
# Pfade auswählen

Pfade auswählen filtert, welche Unterpfade eines komplexen Pfadobjekts beibehalten werden. Besonders nützlich ist die Funktion bei dekorativen oder mehrteiligen Schriftarten, wenn Sie die äußeren Buchstabenformen und die inneren Ausschnitte als getrennte Teile benötigen – zum Beispiel, um sie in zwei verschiedenen Farben zu drucken.

<!--  Screenshot showing Select Paths applied to decorative text with outer paths highlighted -->
![20260506 154655 paste 20260506 154655](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154655-paste-20260506-154655.jpg)

## So funktioniert die Pfadtiefe

Wenn ein Pfadobjekt Formen mit eingeschlossenen Flächen enthält (etwa das Innere des Buchstabens „O“ oder die Aussparung einer dekorativen Schnörkelform), sind diese eingeschlossenen Flächen **Löcher** auf Tiefe 1. Die äußere Kontur jedes Buchstabens oder jeder Form liegt auf **Tiefe 0**.

```
Depth 0 — outer contour of each letter or shape
Depth 1 — first level of enclosed holes (inside an "O", "A", etc.)
Depth 2 — shapes nested inside a hole (rarely used)
```

## Filtervorgaben

### Alle
Übernimmt jeden Pfad unverändert. Dies ist die Standardeinstellung und entspricht dem vollständigen Verzicht auf Pfade auswählen.

### Nur äußere Pfade
Behält nur die äußere Kontur jeder Form (Tiefe == 0). Damit erhalten Sie ausschließlich die Buchstabenumrisse einer dekorativen Schriftart, ohne die inneren Ausschnittflächen.

### Nur Löcher
Behält nur die eingeschlossenen Löcher (Tiefe > 0). Damit erhalten Sie ausschließlich die inneren Ausschnittflächen von Buchstaben und Formen.

### Nach Gruppenindex
Behält nur Pfade, die zu einer einzelnen zusammenhängenden Form gehören. Gruppe 0 ist die erste Form, Gruppe 1 die zweite und so weiter. Damit isolieren Sie ein einzelnes Zeichen aus einem Wort.

### Benutzerdefiniert
Schreiben Sie einen Ausdruck, der für jeden Pfad ausgewertet wird. Der Pfad wird **einbezogen**, wenn der Ausdruck ungleich null ist, und **ausgeschlossen**, wenn er null ist.

Ausdrücke müssen mit `=` beginnen, damit die Variablenersetzung aktiviert wird. Ohne `=` wird der Wert als einfache Zahl behandelt (z. B. schließt `1` immer ein, `0` immer aus).

## Beispiele für benutzerdefinierte Ausdrücke

| Ausdruck | Wirkung |
|------------|--------|
| `=PathDepth==0` | Nur äußere Konturen (wie Nur äußere Pfade) |
| `=PathDepth>0` | Nur Löcher (wie Nur Löcher) |
| `=GroupIndex==0` | Nur die erste zusammenhängende Form |
| `=PathArea>100` | Formen mit einer Fläche größer als 100 mm² |
| `=PathLength>50` | Formen mit einem Umfang größer als 50 mm |

## Variablen für benutzerdefinierte Ausdrücke

| Variable | Bedeutung |
|----------|---------|
| `PathDepth` | 0 = äußere Kontur; 1+ = Loch oder verschachtelte Form |
| `GroupIndex` | Index der zusammenhängenden Form (0, 1, 2 …) |
| `GroupOuterArea` | Fläche des äußeren Pfads dieser Gruppe |
| `GroupOuterLength` | Umfang des äußeren Pfads dieser Gruppe |
| `ChildCount` | Anzahl der Löcher innerhalb des äußeren Pfads dieser Gruppe |
| `PathIndex` | Fortlaufender Index dieses Pfads innerhalb seiner Gruppe |
| `PathArea` | Fläche dieses einzelnen Pfads |
| `PathLength` | Umfang dieses einzelnen Pfads |

## Beispiel: Mehrfarbiger Druck einer Weihnachtsschrift

Ein häufiger Einsatzzweck von Pfade auswählen ist das Drucken dekorativer Texte, deren Buchstaben innere Ausschnittformen besitzen. So drucken Sie die äußeren Buchstaben in einer Farbe und die inneren Ausschnitte in einer zweiten Farbe:

1. Ein **Text**-Objekt hinzufügen und auf **2D-Ausgabe** setzen
2. **Pfade auswählen** anwenden → Vorgabe auf **Nur äußere Pfade** setzen
3. **Linear extrudieren** anwenden, um Höhe zu erzeugen → erste Filamentfarbe zuweisen
4. Zum ursprünglichen Textobjekt zurückkehren
5. Ein zweites **Pfade auswählen** anwenden → Vorgabe auf **Nur Löcher** setzen
6. **Linear extrudieren** mit derselben Höhe anwenden → zweite Filamentfarbe zuweisen
7. Ein extrudiertes Objekt auf dem anderen positionieren – die beiden Farben liegen exakt übereinander

## Verwandte Themen

- [Linear extrudieren](linear-extrude.md) – Den gefilterten Pfaden Höhe geben, um ein 3D-Objekt zu erzeugen
- [Rotieren](revolve.md) – Gefilterte Pfade um eine Achse drehen
- [SVG-Objekt](../../primitives/svg-object.md) – Vektorpfade importieren, die mehrere Unterpfade enthalten können
- [Text](../../primitives/text.md) – Textobjekte im 2D-Modus erzeugen eine Ausgabe mit mehreren Pfaden
