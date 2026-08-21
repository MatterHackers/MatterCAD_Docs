---
title: Juster
articleKey: AlignObject3D_3
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 1fadae72ba00cb06e36a21f0b96962dcff3f60ad
source_lang: en
---
# Juster

Juster plasserer flere objekter nøyaktig i forhold til et ankerobjekt. Bruk den til å stille opp kanter, sentrere deler på hverandre, plassere ett objekt oppå et annet eller lage jevnt fordelte stabler.

<!--  Screenshot showing two objects being aligned with alignment options visible -->
![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)


## Slik bruker du den

1. Velg to eller flere objekter.
2. Bruk operasjonen **Juster** fra menyen **Plassering**.
3. Velg **Anker**-objektet. Ankeret blir stående, og de andre objektene flyttes.
4. Angi justering for X-, Y- og Z-aksen uavhengig av hverandre.
5. Bruk **Bruk** når du vil brenne de justerte posisjonene inn i objekttreet.

## Parametere

### Anker

Listen **Anker** velger barneobjektet som brukes som referanse. Ankeret flyttes ikke. Alle andre barn i Juster-operasjonen blir omplassert i forhold til ankeret, med mindre en akse bruker **Stablet**-modus.

### Aksekontroller

Hver akse har sine egne kontroller. Du kan justere på én akse, to akser eller alle tre. Minimums- og maksimumskantene er navngitt etter aksen:

- **X-akse** – Min er venstre, Maks er høyre.
- **Y-akse** – Min er foran, Maks er bak.
- **Z-akse** – Min er bunn, Maks er topp.

For hver akse:

- **Juster** – Velger ankerets referansepunkt for den aksen. Bruk **Ingen** for å la posisjonene være uendret på den aksen.
- **Modus** – Styrer hvordan den valgte justeringen brukes:
  - **Enkel** – Match hvert bevegelige objekts tilsvarende kant, senter eller origo med ankeret. Ingen forskyvning brukes.
  - **Forskyvning** – Velg hvilken del av det bevegelige objektet som skal lande på ankerreferansen, og legg deretter til avstand med **Forskyvning**.
  - **Stablet** – Plasser objektene etter hverandre langs den aksen, med **Forskyvning** som mellomrom mellom dem.
- **Underjuster** – Tilgjengelig i **Forskyvning**-modus. Velger hvilken del av det bevegelige objektet som skal plasseres på ankerreferansen. Hvis **Underjuster** er **Ingen**, bruker Juster den samme kanten, senteret eller origoen som er valgt i **Juster**.
- **Forskyvning** – Tilgjengelig i modusene **Forskyvning** og **Stablet**. Legger til avstand langs den aksen og støtter [uttrykk](../../workspace/expressions.md).

## Justeringsmoduser

### Enkel

Bruk **Enkel** når du matcher like posisjoner med hverandre. For eksempel flytter **X-justering: Senter** alle objekter som ikke er anker, slik at X-senteret deres samsvarer med ankerets X-senter. **Z-justering: Min** flytter alle objekter som ikke er anker, slik at bunnen deres ligger på ankerets bunnhøyde.

### Forskyvning

Bruk **Forskyvning** når delen av det bevegelige objektet skal være en annen enn ankerreferansen. For eksempel, for å plassere et objekt oppå ankeret:

1. Sett **Z-justering** til **Maks** (topp).
2. Sett **Z-modus** til **Forskyvning**.
3. Sett **Z-underjuster** til **Bunn**.
4. Sett **Z-forskyvning** til ønsket mellomrom, eller la den stå på `0` for direkte kontakt.

Dette plasserer bunnen av det bevegelige objektet på ankerets topp, med valgfri avstand.

### Stablet

Bruk **Stablet** for å kjede sammen flere objekter langs en akse. Objektene behandles etter navn, deretter etter intern ID, så tydelig navngiving av objektene gir forutsigbar stablingsrekkefølge.

I **Stablet**-modus plasseres hvert bevegelige objekt inntil den forrige referansen på den aksen:

- **Min**-justering stabler i positiv retning, for eksempel venstre-til-høyre på X eller bunn-til-topp på Z.
- **Maks**-justering stabler i negativ retning, for eksempel høyre-til-venstre på X eller topp-til-bunn på Z.
- **Senter**- og **Origo**-justering bruker forskyvningen mellom hvert objekts senter eller origo.

Bruk **Forskyvning** i **Stablet**-modus for å angi mellomrommet mellom objektene.

## Eksempler

- **Sentrere objekter på byggeplatens flate** – Velg objektet som skal stå fast som **Anker**, og sett deretter **X-justering** og **Y-justering** til **Senter**.
- **Plassere ett objekt oppå et annet** – Sett **Z-justering** til **Maks** (topp), **Z-modus** til **Forskyvning** og **Z-underjuster** til **Bunn**.
- **Legge til et nøyaktig mellomrom fra en kant** – Bruk **Forskyvning**-modus, velg kanten på det bevegelige objektet med **Underjuster**, og sett deretter **Forskyvning** til avstanden du trenger.
- **Stille opp flere objekter ende mot ende** – Sett **X-justering** til **Min** (venstre), **X-modus** til **Stablet**, og bruk **X-forskyvning** for mellomrommet.
- **Bygge en vertikal stabel** – Sett **Z-justering** til **Min** (bunn), **Z-modus** til **Stablet**, og bruk **Z-forskyvning** for avstanden mellom objektene.

## Tips

- Ankerobjektet blir stående; de andre objektene flyttes for å justeres etter det.
- Du kan bruke forskjellige moduser på forskjellige akser, for eksempel **Stablet** på X samtidig som du bruker **Senter** og **Enkel** på Y.
- Bruk objektnavn til å styre **Stablet**-rekkefølgen når flere objekter justeres samtidig.
- Juster er ikke-destruktiv til den er brukt. Du kan endre innstillingene når som helst for å justere barna på nytt.
- Bruk **Origo** når du trenger å stille opp modelleringsorigoer i stedet for kanter på avgrensningsboksen.

## Relatert

- [Tilpass til grenser](fit-to-bounds.md) – Skaler et objekt slik at det passer til bestemte mål
- [Flytt](../transform/translate.md) – Flytt en bestemt avstand
- [Gruppering](../../workspace/grouping.md) – Grupper justerte objekter for å holde dem samlet
