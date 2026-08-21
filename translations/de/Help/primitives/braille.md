---
title: Braille
articleKey: BrailleObject3D
parent: "Primitives"
nav_order: 2
source_hash: d1d9d4aeb9b87efbe32045f2a96cfea49048f95f
source_lang: en
---
# Braille

Erzeugen Sie 3D-druckbaren Brailletext aus normalem englischem Text. Das Braille-Werkzeug unterstützt sowohl Braille der Stufe 1 (Buchstabe für Buchstabe) als auch der Stufe 2 (Kurzschrift).

<!-- Screenshot of a Braille object showing raised dots on the workspace -->
![20260318 182800 paste 20260318 182800](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-182800-paste-20260318-182800.jpg)


## Verwendung

1. Fügen Sie ein **Braille**-Grundkörper aus dem Bedienfeld „Primitives“ hinzu
2. Geben Sie Ihren Text im Feld **Text to Encode** ein
3. Das Werkzeug wandelt ihn automatisch in das korrekte Braille-Punktmuster um

## Parameter

- **Text to Encode** – Der englische Text, der in Braille umgewandelt werden soll
- **Scale** – Passt die Gesamtgröße der Braille-Ausgabe an
- **Height** – Die Höhe der erhabenen Braille-Punkte

## Tipps

- Braille der Stufe 2 verwendet Kürzungen und Abkürzungen für häufige Wörter und Buchstabenkombinationen und ist dadurch kompakter
- Es werden standardisierte Braille-Zellenmaße verwendet, damit die Ausgabe lesbar ist
- Kombinieren Sie das Ergebnis mit einer flachen [Cube](cube.md)-Grundplatte, um ein vollständiges Braille-Schild oder -Etikett zu erstellen
- Für Braille-Karten mit integrierter Grundplatte siehe [Braille Card](braille-card.md)

## Verwandte Themen

- [Braille Card](braille-card.md) – Braille mit integrierter Kartenbasis
- [Text](text.md) – Standardmäßiger 3D-Text
