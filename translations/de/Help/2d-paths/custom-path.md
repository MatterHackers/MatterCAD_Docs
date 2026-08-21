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
3. Wenden Sie [Linear extrudieren](../operations/path/linear-extrude.md) oder andere Pfadoperationen an, um ein 3D-Objekt zu erstellen

## Offene und geschlossene Pfade

Das Kontrollkästchen **Geschlossen** legt fest, ob der Pfad seinen letzten Punkt wieder mit seinem ersten verbindet.

- **Geschlossen** (die Standardeinstellung) lässt den Pfad einen Bereich umranden. Dieser Bereich ist es, den [Linear extrudieren](../operations/path/linear-extrude.md) und [Rotieren](../operations/path/revolve.md) füllen.
- **Öffnen** macht den Pfad zu einer Linie. Eine Linie umschließt nichts, daher erscheint sie in der Szene als schmales Band entlang ihrer Länge und nicht als gefüllte Form. Verwenden Sie [Pfad aufblasen](../operations/path/inflate-path.md), um ihr eine Breite zu geben und sie wieder in etwas Massives zu verwandeln.

Zwei Dinge sollten Sie wissen, bevor Sie **Geschlossen** deaktivieren:

- **Erneutes Schließen ist kein Rückgängigmachen.** Beim Öffnen eines Pfades wird sein Schlusssegment verworfen. War dieses Segment gekrümmt, bringt ein erneutes Aktivieren von **Geschlossen** eine gerade Linie zurück, nicht die Kurve. Verwenden Sie stattdessen Strg+Z – das Rückgängigmachen stellt den ursprünglichen Pfad exakt wieder her.
- **Manche Konturen lassen sich nicht öffnen.** Eine Kontur, die dabei mit weniger als zwei Punkten zurückbliebe – etwa eine Tropfenform aus einem einzigen Punkt und einer zu ihm zurücklaufenden Kurve – bleibt geschlossen, statt zu etwas zusammenzufallen, das Sie weder sehen noch anklicken könnten. Dasselbe gilt für eine Kontur mit einer quadratischen Kurve, wie sie in einer importierten SVG-Datei vorkommen kann: Ein Öffnen würde die Kurve zu einer Ecke abflachen. Die Verweigerung gilt pro Kontur, der Rest des Pfades öffnet sich also weiterhin.

Wenn ein Pfad mehrere Konturen besitzt und diese nicht übereinstimmen, zeigt das Kontrollkästchen den Zustand „offen“ an. Durch Aktivieren werden alle Konturen angeglichen.

Operationen, die einen Bereich benötigen, schließen einen offenen Pfad für Sie, anstatt ihn abzulehnen. Linear extrudieren, Rotieren, Subtrahieren und die übrigen booleschen Operationen tun dies alle, sodass ein offener Pfad zu demselben Volumenkörper extrudiert wird wie seine geschlossene Fassung.

## Tipps

- Verwenden Sie den Benutzerdefinierten Pfad, wenn keine der eingebauten Pfadformen zu Ihren Anforderungen passt
- Zum Importieren von Formen aus externen Vektoreditoren siehe [SVG-Objekt](../primitives/svg-object.md)
- Um eine Linie zu zeichnen und sie in ein Bauteil zu verwandeln, deaktivieren Sie **Geschlossen**, wenden Sie [Pfad aufblasen](../operations/path/inflate-path.md) an, um ihr eine Dicke zu geben, und anschließend [Linear extrudieren](../operations/path/linear-extrude.md), um ihr Höhe zu geben

## Verwandte Themen

- [Kreis-Pfad](circle-path.md) – Ein fertiger Kreis
- [Box-Pfad](box-path.md) – Ein fertiges Rechteck
- [SVG-Objekt](../primitives/svg-object.md) – Vektorpfade aus SVG-Dateien importieren
- [Linear extrudieren](../operations/path/linear-extrude.md) – Pfaden Höhe geben
