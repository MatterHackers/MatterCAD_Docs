---
title: Pfad aufweiten
articleKey: InflatePathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: c0e11d3d24c5f832f797cde4d392e26a4694733d
source_lang: en
---
# Pfad aufweiten

Pfad aufweiten erweitert einen 2D-Pfad nach außen und vergrößert so die Form, wobei ihr Gesamtverlauf erhalten bleibt. Das entspricht einem gleichmäßigen Versatz aller Kanten.

<!--  Before and after showing a path inflated outward -->
![20260506 100652 paste 20260506 100652](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100652-paste-20260506-100652.jpg)


## Verwendung

1. Wählen Sie einen 2D-Pfad aus
2. Wenden Sie **Pfad aufweiten** aus dem Menü der Pfadoperationen an
3. Passen Sie den Aufweitungsbetrag an

## Eine offene Linie aufweiten

Mit dem Aufweiten machen Sie aus einer Linie eine Fläche. Deaktivieren Sie **Geschlossen** bei einem [benutzerdefinierten Pfad](../../2d-paths/custom-path.md), um eine offene Linie zu zeichnen, und weiten Sie diese anschließend auf: Das Ergebnis ist ein gefülltes Band, das beidseitig der Linie so breit ist wie der eingestellte Betrag. Von da an lässt es sich wie jeder andere Pfad extrudieren.

**Stil** legt fest, wie die beiden Enden der Linie abgeschlossen und wie ihre Ecken verbunden werden:

- **Flach** schließt das Band an jedem Endpunkt gerade ab
- **Rund** fügt hinter jedem Endpunkt einen Halbkreis an
- **Spitz** fügt hinter jedem Endpunkt ein Quadrat an

Eine offene Linie hat kein Inneres, in das sie schrumpfen könnte, daher würde ein Betrag von null oder ein negativer Betrag überhaupt nichts übrig lassen. Wenn der Pfad *vollständig* offen ist, begrenzt Pfad aufweiten den Wert auf eine kleine positive Zahl und schreibt diese begrenzte Zahl in das Feld zurück, damit Sie sehen können, was passiert ist.

Ein Pfad, der offene und geschlossene Konturen mischt, wird nicht begrenzt: Die geschlossenen Konturen schrumpfen wie gewohnt, die offenen entfallen einfach. Geschlossene Pfade schrumpfen bei negativen Werten weiterhin genau wie bisher.

## Tipps

- Verwenden Sie negative Werte, um den Pfad nach innen zu schrumpfen statt ihn zu erweitern
- Pfad aufweiten eignet sich gut, um Toleranzversätze um Formen herum zu erzeugen
- Kombinieren Sie es mit [Pfad umranden](outline-path.md), um Ränder mit bestimmten Breiten zu erstellen

## Verwandte Themen

- [Pfad umranden](outline-path.md) – Eine Umrandung aus einem Pfad erstellen
- [Pfad-Rahmen](border-path.md) – Einen Rahmenversatz hinzufügen
- [Pfad glätten](smooth-path.md) – Die Ecken eines Pfads abrunden
