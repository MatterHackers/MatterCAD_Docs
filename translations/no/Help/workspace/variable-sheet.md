---
title: Variabelark
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 3
source_hash: 3137a4da2b9d2086d4dcace156435caca288dd79
source_lang: en
---
# Variabelark

Variabelarket lagrer felles verdier for en design. Bruk det når flere objekter skal referere til de samme målene, antallene, etikettene eller formlene. Når du endrer en verdi i arket, beregnes de avhengige objektene på nytt, slik at parametriske design forblir konsistente uten at du må redigere hvert objekt ett om gangen.

<!--  Screenshot of the Variable Sheet editor showing named cells, formulas, and the Documentation button -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## Slik legger du til et Variabelark

1. Åpne biblioteket og legg **Variabelark** til i scenen.
2. Velg Variabelark-objektet for å vise arkredigereren.
3. Velg en celle, og skriv inn et **Navn** og en verdi eller formel.
4. Bruk cellenavnet fra andre felter i designet som støtter uttrykk.

## Redigere celler

Hver celle har to redigerbare deler:

- **Navn** – Et valgfritt variabelnavn for cellen. Navn skiller ikke mellom store og små bokstaver, mellomrom konverteres til understreker, og duplikate navn justeres automatisk.
- **Uttrykk** – Celleverdien. Ren tekst eller tall lagres direkte. Formler starter med `=`.

Celler kan også refereres til med adresse, for eksempel `A1` eller `B2`. Navngitte celler er vanligvis tydeligere for designparametere fordi de beskriver hensikten, for eksempel `wall_thickness`, `outer_diameter` eller `hole_count`.

## Formler

Start en formel med `=` for å beregne den i arket:

- `=20 + 5` returnerer `25`
- `=pi * 10` returnerer `31.41592653589793`
- `=A1 * 2` refererer til en annen celle med adresse
- `=wall_thickness + 4` refererer til en navngitt celle

Arket støtter aritmetikk, parenteser, sammenligningsoperatorer, vanlige `Math`-funksjoner som `sin`, `cos`, `sqrt` og `round`, samt konstanter som `pi`, `tau` og `e`.

## Bruke arkverdier i objekter

De fleste numeriske felter i MatterCAD støtter uttrykk. For å bruke en arkverdi i en objektparameter setter du `=` foran referansen:

- Sett **Bredde** for en Kube til `=case_width`.
- Sett **Antall** for en Matrise til `=hole_count`.
- Sett en **Forskyvning**-verdi for Flytt til `=wall_thickness * 2`.

Når arket endres, beregner MatterCAD objektene som er avhengige av det, på nytt.

## Tekst- og hjelpefunksjoner

Celler i Variabelark kan inneholde både tekst og tall. Tekstverdier er nyttige for genererte etiketter, delenumre, importerte data og egendefinerte designapper.

Nyttige hjelpefunksjoner omfatter:

- `concat()` eller `strcat()` – Slår sammen tekst eller verdier.
- `substring()` – Henter ut en del av en tekstverdi.
- `split()` – Deler opp tekst og returnerer ett element.
- `count()` – Teller elementer atskilt med skilletegn i tekst.
- `substitute()` – Erstatter tekst.
- `rand(seed)` – Genererer en deterministisk tilfeldig verdi når et frø oppgis.
- `importdata()` – Leser en verdi fra en URL eller en lokal filbane.

## Tips

- Foretrekk beskrivende navn fremfor celleadresser for verdier som brukes av andre objekter.
- Hold kjernemålene øverst til venstre i arket, slik at de er enkle å finne.
- Bruk formler for avledede verdier, for eksempel `inner_diameter = outer_diameter - wall_thickness * 2`.
- Unngå å bruke reserverte ord som `pi`, `e`, `true`, `false` eller funksjonsnavn som cellenavn.
- Hvis en formel ikke kan tolkes, beholder MatterCAD den opprinnelige inndataen som tekst.

## Relatert

- [Uttrykk](expressions.md) – Bruk uttrykk i objektparametere
- [Komponenter](components.md) – Opprett gjenbrukbare parametriske design
- [Matrise](../operations/array/array.md) – Opprett gjentatte mønstre styrt av arkverdier
