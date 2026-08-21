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

Mit „Pfade auswählen“ filtern Sie, welche Unterpfade eines komplexen Pfadobjekts erhalten bleiben. Besonders nützlich ist das bei dekorativen oder mehrteiligen Schriften, wenn Sie die äußeren Buchstabenformen und die inneren Ausschnittformen als getrennte Teile benötigen – zum Beispiel, um sie in zwei verschiedenen Farben im 3D-Druck zu fertigen.

<!--  Screenshot showing Select Paths applied to decorative text with outer paths highlighted -->
![20260506 154655 paste 20260506 154655](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154655-paste-20260506-154655.jpg)

## So funktioniert die Pfadtiefe

Wenn ein Pfadobjekt Formen mit umschlossenen Flächen enthält (etwa das Innere des Buchstabens „O“ oder die Aussparung einer dekorativen Schnörkelform), sind diese umschlossenen Flächen **Löcher** in Tiefe 1. Die äußere Kontur jedes Buchstabens bzw. jeder Form liegt in **Tiefe 0**.

```
Depth 0 — outer contour of each letter or shape
Depth 1 — first level of enclosed holes (inside an "O", "A", etc.)
Depth 2 — shapes nested inside a hole (rarely used)
```

## Filter-Voreinstellungen

### Alle
Schließt jeden Pfad unverändert ein. Dies ist die Standardeinstellung und entspricht dem völligen Verzicht auf „Pfade auswählen“.

### Nur äußere Pfade
Behält nur die äußere Kontur jeder Form (depth == 0). Damit erhalten Sie ausschließlich die Buchstabenumrisse einer dekorativen Schrift, ohne die inneren Ausschnittflächen.

### Nur Löcher
Behält nur die umschlossenen Löcher (depth > 0). Damit erhalten Sie ausschließlich die inneren Ausschnittflächen von Buchstaben und Formen.

### Nach Gruppenindex
Behält nur Pfade, die zu einer zusammenhängenden Einzelform gehören. Gruppe 0 ist die erste Form, Gruppe 1 die zweite und so weiter. Damit isolieren Sie ein einzelnes Zeichen aus einem Wort.

### Benutzerdefiniert
Schreiben Sie einen Ausdruck, der für jeden Pfad ausgewertet wird. Der Pfad wird **eingeschlossen**, wenn der Ausdruck ungleich null ist, und **ausgeschlossen**, wenn er null ist.

Ausdrücke müssen mit `=` beginnen, damit die Variablenersetzung aktiv wird. Ohne `=` wird der Wert als einfache Zahl behandelt (z. B. schließt `1` immer ein, `0` schließt immer aus).

## Beispiele für benutzerdefinierte Ausdrücke

| Ausdruck | Wirkung |
|------------|--------|
| `=PathDepth==0` | Nur äußere Konturen (wie „Nur äußere Pfade“) |
| `=PathDepth>0` | Nur Löcher (wie „Nur Löcher“) |
| `=GroupIndex==0` | Nur die erste zusammenhängende Form |
| `=PathArea>100` | Formen mit einer Fläche größer als 100 mm² |
| `=PathLength>50` | Formen mit einem Umfang länger als 50 mm |

## Variablen für benutzerdefinierte Ausdrücke

| Variable | Bedeutung |
|----------|---------|
| `PathDepth` | 0 = äußere Kontur; 1+ = Loch oder verschachtelte Form |
| `GroupIndex` | Index der zusammenhängenden Form (0, 1, 2…) |
| `GroupOuterArea` | Fläche des äußeren Pfads dieser Gruppe |
| `GroupOuterLength` | Umfang des äußeren Pfads dieser Gruppe |
| `ChildCount` | Anzahl der Löcher innerhalb des äußeren Pfads dieser Gruppe |
| `PathIndex` | Fortlaufender Index dieses Pfads innerhalb seiner Gruppe |
| `PathArea` | Fläche dieses einzelnen Pfads |
| `PathLength` | Umfang dieses einzelnen Pfads |

## Beispiel: Mehrfarbiger Druck einer Weihnachtsschrift

Ein häufiger Einsatzzweck von „Pfade auswählen“ ist der Druck dekorativer Texte, deren Buchstaben innere Ausschnittformen besitzen. So drucken Sie die äußeren Buchstaben in einer Farbe und die inneren Ausschnitte in einer zweiten Farbe:

1. Fügen Sie ein **Text**-Objekt hinzu und stellen Sie es auf **2D-Ausgabe**
2. Wenden Sie **Pfade auswählen** an → setzen Sie die Voreinstellung auf **Nur äußere Pfade**
3. Wenden Sie **Lineare Extrusion** an, um Höhe zu erzeugen → weisen Sie Ihre erste Filamentfarbe zu
4. Kehren Sie zum ursprünglichen Textobjekt zurück
5. Wenden Sie ein zweites Mal **Pfade auswählen** an → setzen Sie die Voreinstellung auf **Nur Löcher**
6. Wenden Sie **Lineare Extrusion** mit derselben Höhe an → weisen Sie Ihre zweite Filamentfarbe zu
7. Positionieren Sie das eine extrudierte Objekt über dem anderen – die beiden Farben decken sich exakt

## Verwandte Themen

- [Lineare Extrusion](linear-extrude.md) – Gibt den gefilterten Pfaden Höhe, um ein 3D-Objekt zu erzeugen
- [Rotieren](revolve.md) – Dreht gefilterte Pfade um eine Achse
- [SVG-Objekt](../../primitives/svg-object.md) – Importiert Vektorpfade, die mehrere Unterpfade enthalten können
- [Text](../../primitives/text.md) – Textobjekte im 2D-Modus erzeugen eine Ausgabe mit mehreren Pfaden
