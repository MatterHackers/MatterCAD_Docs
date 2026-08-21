---
title: Braille
articleKey: BrailleObject3D
parent: "Primitives"
nav_order: 2
source_hash: d1d9d4aeb9b87efbe32045f2a96cfea49048f95f
source_lang: en
---
# Braille

Erzeugen Sie 3D-druckbaren Braille-Text aus normalem englischem Text. Das Braille-Werkzeug unterstützt sowohl die Braille-Kodierung nach Grad 1 (Buchstabe für Buchstabe) als auch nach Grad 2 (Kurzschrift).

<!-- Screenshot of a Braille object showing raised dots on the workspace -->
![20260318 182800 paste 20260318 182800](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-182800-paste-20260318-182800.jpg)


## Verwendung

1. Fügen Sie ein **Braille**-Primitiv aus dem Bereich Primitive hinzu
2. Geben Sie Ihren Text im Feld **Zu kodierender Text** ein
3. Das Werkzeug wandelt ihn automatisch in das korrekte Braille-Punktmuster um

## Parameter

- **Zu kodierender Text** – Der englische Text, der in Braille umgewandelt werden soll
- **Skalieren** – Passt die Gesamtgröße der Braille-Ausgabe an
- **Höhe** – Die Höhe der erhabenen Braille-Punkte

## Tipps

- Braille nach Grad 2 verwendet Kürzungen und Abkürzungen für häufige Wörter und Buchstabenkombinationen und ist dadurch kompakter
- Es werden die standardmäßigen Abmessungen der Braille-Zelle verwendet, damit die Ausgabe lesbar ist
- Vereinen Sie das Ergebnis mit einer flachen [Würfel](cube.md)-Grundplatte, um ein vollständiges Braille-Schild oder -Etikett zu erstellen
- Für Braille-Karten mit integrierter Grundplatte siehe [Braille-Karte](braille-card.md)

## Verwandte Themen

- [Braille-Karte](braille-card.md) – Braille mit integrierter Kartengrundplatte
- [Text](text.md) – Normaler 3D-Text
