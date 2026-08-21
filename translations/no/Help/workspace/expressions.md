---
title: Uttrykk
parent: "Workspace"
nav_order: 2
source_hash: 79a2f2c42d81f7fca56a87ad89f69e4303ed0ae5
source_lang: en
---
# Uttrykk

Mange parametere i MatterCAD godtar matematiske uttrykk i stedet for vanlige tall. Dette muliggjør parametrisk design der endring av én verdi automatisk oppdaterer relaterte mål.

<!--  Screenshot showing an expression being entered in a parameter field -->
![20260318 193631 paste 20260318 193631](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193631-paste-20260318-193631.jpg)


## Slik bruker du det

I stedet for å skrive inn et vanlig tall i et parameterfelt, kan du skrive et matematisk uttrykk. For eksempel:

- `20 + 5` gir 25
- `pi * 10` gir 31,416
- `width * 2` refererer til en annen parameter med navnet «width»

## Tilgjengelige konstanter

- **pi** – 3,14159 … (forholdet mellom omkrets og diameter)
- **tau** – 6,28318 … (2 * pi, en hel omdreining i radianer)

## Støttede operasjoner

- Addisjon: `+`
- Subtraksjon: `-`
- Multiplikasjon: `*`
- Divisjon: `/`
- Parenteser: `(` og `)` for gruppering

## Tips

- Uttrykk støttes i alle felt som viser `DoubleOrExpression`, `IntOrExpression` eller `StringOrExpression` i koden – i praksis godtar de fleste numeriske felt i designverktøyene dem
- Bruk uttrykk til å opprette sammenhenger mellom parametere – sett for eksempel diameteren til et hull til `outer_diameter - 4` slik at det alltid har 2 mm vegger
- Uttrykk oppdateres automatisk når de refererte verdiene endres
- Bruk et [Variabelark](variable-sheet.md) når flere objekter skal dele de samme navngitte verdiene eller formlene
- Du kan bruke uttrykk i [Matrise](../operations/array/index.md)-operasjoner for å lage parametriske mønstre

## Relatert

- [Komponenter](components.md) – Opprett gjenbrukbare parametriserte design
- [Variabelark](variable-sheet.md) – Lagre delte verdier og formler for et design
- [Rediger objekter](../getting-started/editing-objects.md) – Arbeide med objektparametere
