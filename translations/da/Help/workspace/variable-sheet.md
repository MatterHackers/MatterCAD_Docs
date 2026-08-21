---
title: Variabelark
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 3
source_hash: 3137a4da2b9d2086d4dcace156435caca288dd79
source_lang: en
---
# Variabelark

Variabelarket gemmer fælles værdier for et design. Brug det, når flere objekter skal referere til de samme mål, antal, etiketter eller formler. Når du ændrer en værdi i arket, genberegnes de afhængige objekter, så parametriske designs forbliver konsistente, uden at du skal redigere hvert objekt for sig.

<!--  Screenshot of the Variable Sheet editor showing named cells, formulas, and the Documentation button -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## Sådan tilføjer du et Variabelark

1. Åbn biblioteket, og tilføj **Variabelark** til scenen.
2. Vælg Variabelark-objektet for at vise arkeditoren.
3. Vælg en celle, og indtast derefter et **Navn** og en værdi eller formel.
4. Brug cellenavnet fra andre felter i designet, der understøtter udtryk.

## Redigering af celler

Hver celle har to redigerbare dele:

- **Navn** - Et valgfrit variabelnavn for cellen. Der skelnes ikke mellem store og små bogstaver, mellemrum konverteres til understregninger, og dublerede navne justeres automatisk.
- **Udtryk** - Cellens værdi. Almindelig tekst eller tal gemmes direkte. Formler begynder med `=`.

Celler kan også refereres ved adresse, f.eks. `A1` eller `B2`. Navngivne celler er som regel tydeligere for designparametre, fordi de beskriver hensigten, f.eks. `wall_thickness`, `outer_diameter` eller `hole_count`.

## Formler

Begynd en formel med `=` for at få den beregnet i arket:

- `=20 + 5` returnerer `25`
- `=pi * 10` returnerer `31.41592653589793`
- `=A1 * 2` refererer til en anden celle ved adresse
- `=wall_thickness + 4` refererer til en navngivet celle

Arket understøtter aritmetik, parenteser, sammenligningsoperatorer, almindelige `Math`-funktioner såsom `sin`, `cos`, `sqrt` og `round` samt konstanter, herunder `pi`, `tau` og `e`.

## Brug af arkværdier i objekter

De fleste numeriske felter i MatterCAD understøtter udtryk. Hvis du vil bruge en arkværdi i en objektparameter, skal du sætte `=` foran referencen:

- Sæt en Ternings **Bredde** til `=case_width`.
- Sæt et Arrays **Antal** til `=hole_count`.
- Sæt en Flyt-**Forskydning** til `=wall_thickness * 2`.

Når arket ændres, genberegner MatterCAD de objekter, der afhænger af det.

## Tekst- og hjælpefunktioner

Celler i Variabelarket kan indeholde både tekst og tal. Tekstværdier er nyttige til genererede etiketter, varenumre, importerede data og brugerdefinerede designapps.

Nyttige hjælpefunktioner omfatter:

- `concat()` eller `strcat()` - Sammenføj tekst eller værdier.
- `substring()` - Udtræk en del af en tekstværdi.
- `split()` - Opdel tekst, og returner ét element.
- `count()` - Tæl afgrænsede elementer i tekst.
- `substitute()` - Erstat tekst.
- `rand(seed)` - Generer en deterministisk tilfældig værdi, når der angives et startpunkt (seed).
- `importdata()` - Læs en værdi fra en URL eller en lokal filsti.

## Tips

- Foretræk beskrivende navne frem for celleadresser til værdier, der bruges af andre objekter.
- Placer de vigtigste mål øverst til venstre i arket, så de er nemme at finde.
- Brug formler til afledte værdier, f.eks. `inner_diameter = outer_diameter - wall_thickness * 2`.
- Undgå at bruge reserverede ord som `pi`, `e`, `true`, `false` eller funktionsnavne som cellenavne.
- Hvis en formel ikke kan fortolkes, bevarer MatterCAD det oprindelige input som tekst.

## Relateret

- [Udtryk](expressions.md) - Brug udtryk i objektparametre
- [Komponenter](components.md) - Opret genbrugelige parametriske designs
- [Array](../operations/array/array.md) - Opret gentagne mønstre styret af arkværdier
