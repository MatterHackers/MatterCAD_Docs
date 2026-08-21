---
title: Braille
articleKey: BrailleObject3D
parent: "Primitives"
nav_order: 2
source_hash: d1d9d4aeb9b87efbe32045f2a96cfea49048f95f
source_lang: en
---
# Braille

Generer 3D-printbar brailletekst ud fra almindelig engelsk tekst. Braille-værktøjet understøtter både Grade 1 (bogstav for bogstav) og Grade 2 (forkortet) braillekodning.

<!-- Screenshot of a Braille object showing raised dots on the workspace -->
![20260318 182800 paste 20260318 182800](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-182800-paste-20260318-182800.jpg)


## Sådan bruges den

1. Tilføj en **Braille**-primitiv fra panelet Primitiver
2. Skriv din tekst i feltet **Tekst, der skal kodes**
3. Værktøjet konverterer den automatisk til det korrekte braillepunktmønster

## Parametre

- **Tekst, der skal kodes** - Den engelske tekst, der skal konverteres til braille
- **Skalér** - Justér den samlede størrelse af brailleteksten
- **Højde** - Højden på de hævede braillepunkter

## Tips

- Grade 2-braille bruger sammentrækninger og forkortelser for almindelige ord og bogstavkombinationer, hvilket gør den mere kompakt
- Der anvendes standardmål for brailleceller, så resultatet kan læses
- Kombinér med en flad [Terning](cube.md) som bund for at lave en komplet brailleetiket eller et skilt
- For braillekort med indbygget bund, se [Braillekort](braille-card.md)

## Relateret

- [Braillekort](braille-card.md) - Braille med en indbygget kortbund
- [Tekst](text.md) - Almindelig 3D-tekst
