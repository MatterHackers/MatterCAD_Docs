---
title: Blindeskrift
articleKey: BrailleObject3D
parent: "Primitives"
nav_order: 2
source_hash: d1d9d4aeb9b87efbe32045f2a96cfea49048f95f
source_lang: en
---
# Blindeskrift

Generer 3D-utskrivbar blindeskrifttekst fra vanlig engelsk tekst. Blindeskrift-verktøyet støtter både grad 1 (bokstav for bokstav) og grad 2 (forkortet) blindeskriftkoding.

<!-- Screenshot of a Braille object showing raised dots on the workspace -->
![20260318 182800 paste 20260318 182800](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-182800-paste-20260318-182800.jpg)


## Slik bruker du det

1. Legg til et **Blindeskrift**-primitiv fra Primitiver-panelet
2. Skriv teksten din i feltet **Tekst som skal kodes**
3. Verktøyet konverterer den automatisk til riktig punktmønster i blindeskrift

## Parametere

- **Tekst som skal kodes** - Den engelske teksten som skal konverteres til blindeskrift
- **Skaler** - Juster den totale størrelsen på blindeskriftresultatet
- **Høyde** - Høyden på de opphøyde blindeskriftpunktene

## Tips

- Grad 2-blindeskrift bruker sammentrekninger og forkortelser for vanlige ord og bokstavkombinasjoner, noe som gjør den mer kompakt
- Standard cellemål for blindeskrift brukes for å sikre at resultatet er lesbart
- Kombiner med en flat [Kube](cube.md) som base for å lage en komplett blindeskriftetikett eller et skilt
- For blindeskriftkort med integrert base, se [Blindeskriftkort](braille-card.md)

## Relatert

- [Blindeskriftkort](braille-card.md) - Blindeskrift med integrert kortbase
- [Tekst](text.md) - Vanlig 3D-tekst
