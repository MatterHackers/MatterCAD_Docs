---
title: Benutzerdefinierter Pfad
articleKey: CustomPathObject3D
parent: "2D Paths"
nav_order: 3
source_hash: 3633c708477de3ac77d3547b730c33f7e4431cf6
source_lang: en
---
# Benutzerdefinierter Pfad

Zeichnen Sie Ihren eigenen 2D-Pfad mit Kontrollpunkten. Das gibt Ihnen völlige Freiheit, jede beliebige 2D-Form zu erstellen, die anschließend zu einem 3D-Objekt extrudiert oder rotiert werden kann.

<!-- Screenshot showing a custom path being edited with control points -->
![20260506 080247 paste 20260506 080247](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080247-paste-20260506-080247.jpg)


## Verwendung

1. Fügen Sie einen **Benutzerdefinierten Pfad** aus der Bibliothek der 2D-Pfade hinzu
2. Bearbeiten Sie die Kontrollpunkte, um Ihre Form festzulegen
3. Wenden Sie [Lineare Extrusion](../operations/path/linear-extrude.md) oder andere Pfadoperationen an, um ein 3D-Objekt zu erzeugen

## Offene und geschlossene Pfade

Das Kontrollkästchen **Geschlossen** legt fest, ob der Pfad seinen letzten Punkt wieder mit seinem ersten verbindet.

- **Geschlossen** (die Voreinstellung) lässt den Pfad einen Bereich umschließen. Genau diesen füllen [Lineare Extrusion](../operations/path/linear-extrude.md) und [Rotation](../operations/path/revolve.md).
- **Offen** macht den Pfad zu einer Linie. Eine Linie umschließt nichts und erscheint in der Szene deshalb als schmales Band entlang ihrer Länge statt als gefüllte Form. Verwenden Sie [Pfad aufweiten](../operations/path/inflate-path.md), um ihr eine Breite zu geben und sie wieder in etwas Solides zu verwandeln.

Zwei Dinge sollten Sie wissen, bevor Sie **Geschlossen** deaktivieren:

- **Erneutes Schließen ist kein Rückgängigmachen.** Beim Öffnen eines Pfades wird sein Schlusssegment verworfen. War dieses Segment gekrümmt, erhalten Sie beim erneuten Aktivieren von **Geschlossen** eine gerade Linie zurück, nicht die Kurve. Verwenden Sie stattdessen Strg+Z – das Rückgängigmachen stellt den ursprünglichen Pfad exakt wieder her.
- **Manche Konturen lassen sich nicht öffnen.** Eine Kontur, bei der weniger als zwei Punkte übrig blieben – etwa ein Tropfen, der aus einem einzelnen Punkt und einer zu ihm zurücklaufenden Kurve besteht –, bleibt geschlossen, statt zu etwas zusammenzufallen, das Sie weder sehen noch anklicken könnten. Dasselbe gilt für eine Kontur mit einer quadratischen Kurve, wie sie eine importierte SVG-Datei enthalten kann: Das Öffnen würde die Kurve zu einer Ecke abflachen. Diese Verweigerung gilt pro Kontur, der Rest des Pfades wird also trotzdem geöffnet.

Wenn ein Pfad mehrere Konturen hat und diese nicht übereinstimmen, wird das Kontrollkästchen als offen angezeigt. Durch Aktivieren werden alle Konturen angeglichen.

Operationen, die einen Bereich benötigen, schließen einen offenen Pfad für Sie, anstatt ihn abzulehnen. Lineare Extrusion, Rotation, Subtrahieren und die übrigen booleschen Operationen tun dies alle, sodass ein offener Pfad zum selben Körper extrudiert wird wie seine geschlossene Fassung.

## Tipps

- Verwenden Sie den Benutzerdefinierten Pfad, wenn keine der eingebauten Pfadformen zu Ihrem Vorhaben passt
- Zum Importieren von Formen aus externen Vektorprogrammen siehe [SVG-Objekt](../primitives/svg-object.md)
- Um eine Linie zu zeichnen und sie in ein Bauteil zu verwandeln, deaktivieren Sie **Geschlossen**, wenden Sie [Pfad aufweiten](../operations/path/inflate-path.md) an, um ihr eine Dicke zu geben, und anschließend [Lineare Extrusion](../operations/path/linear-extrude.md), um ihr Höhe zu geben

## Verwandte Themen

- [Kreispfad](circle-path.md) – Ein fertiger Kreis
- [Rechteckpfad](box-path.md) – Ein fertiges Rechteck
- [SVG-Objekt](../primitives/svg-object.md) – Vektorpfade aus SVG-Dateien importieren
- [Lineare Extrusion](../operations/path/linear-extrude.md) – Pfaden Höhe geben
