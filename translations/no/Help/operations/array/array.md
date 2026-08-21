---
title: Matrise
articleKey: ArrayObject3D_2
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c547fa24e5f47e0d60f0cec0eac979700d946daf
source_lang: en
---
# Matrise

Matrise lager flere kopier av et objekt ordnet i et mønster. Velg en modus fra knappene øverst — **Lineær**, **Radiell** eller **Transformer** — for å bytte mellom mønstertyper.

<!--  Screenshot of the Array operation panel showing the mode buttons at the top (Linear | Radial | Transform) -->
![20260506 080647 paste 20260506 080647](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080647-paste-20260506-080647.jpg)


## Slik bruker du den

1. Velg et objekt
2. Bruk operasjonen **Matrise** fra Duplisering-menyen
3. Velg en modus (Lineær, Radiell eller Transformer)
4. Juster parameterne for den valgte modusen

## Modus: Lineær

Lineær modus plasserer kopier langs en retning med valgfri rotasjons- og skaleringsprogresjon.

**Antall** — Antall kopier (heltall eller uttrykk). Kildeobjektet er den første kopien; ytterligere kopier forskyves fra det.

**Forskyvningsmetode** — Hvordan avstanden beregnes:
- **Relativ** — Forskyvningen multipliseres med størrelsen på objektets avgrensningsboks. En Relativ forskyvning på (1, 0, 0) plasserer kopiene nøyaktig én objektbredde fra hverandre langs X.
- **Forskyvning** — Fast avstand i verdensrommet i mm per kopi.
- **Endepunkt** — Angi posisjonen til den siste kopien; avstanden fordeles jevnt mellom kopiene.

**Relativ forskyvning** / **Forskyvning** / **Endepunkt** — Avstandsvektoren, avhengig av valgt Forskyvningsmetode.

**Rotasjonsmodus** — Hvordan rotasjonen akkumuleres over kopiene:
- **Lokal** — Hver kopi roterer på stedet om sitt eget senter; forskyvningsretningen forblir i verdensaksene.
- **Sammensetting** — Rotasjonen akkumuleres og styrer forskyvningen, noe som gir spiraler, vifter og helikser.

**Rotasjon** — Rotasjon per kopi i grader på hver akse.

**Skaler** — Kumulativ skalering per kopi på hver akse. Verdier under 1 krymper kopiene; verdier over 1 forstørrer dem.

**Skalering påvirker forskyvning** — Når dette er på, skaleres også avstanden mellom kopiene for hvert trinn. Bruk dette til spiraler som strammes inn og til geometriske progresjoner (nautilusskjell, stablede spikerskjell-kurver).

## Modus: Radiell

Radiell modus fordeler kopiene jevnt rundt en sentralakse med en fast radius.

<!--  Screenshot of Array in Radial mode showing 6 copies arranged in a circle, with Radius and Central Axis parameters visible -->
![20260506 092618 paste 20260506 092618](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-092618-paste-20260506-092618.jpg)


**Telle­metode** — Hvordan antallet kopier bestemmes:
- **Antall** — Eksplisitt antall kopier.
- **Avstand** — Vinkelavstand mellom kopiene i grader; antallet beregnes slik at sveipet fylles.

**Antall** / **Vinkelavstand** — Antall kopier (modusen Antall) eller vinkelavstand i grader (modusen Avstand). Støtter uttrykk.

**Sentralakse** — Aksen det roteres rundt (standard: Z).

**Sirkelsegment** — Om kopiene dekker en hel sirkel på 360° (**Hel**) eller en delvis bue (**Bue**).

**Radius** — Avstand fra sentralaksen til hver kopi.

**Sveipvinkel** — Antall grader av buen som skal fylles (vises når Sirkelsegment er Bue). Støtter uttrykk.

**Juster rotasjon** — Roter hver kopi slik at forkasen peker utover fra senteret.

**Forakse** — Hvilken akse på kopien som behandles som «forover» ved justering (vises når Juster rotasjon er på).

## Modus: Transformer

Transformer-modus flytter kopiene trinnvis ved hjelp av en manuell transformasjon eller ved å følge transformasjonen til et annet objekt.

**Antall** — Antall kopier (heltall eller uttrykk).

**Transformasjonsreferanse** — Hvor transformasjonen per trinn hentes fra:
- **Inndata** — Du angir forskyvning, rotasjon og skalering direkte.
- **Objekt** — Transformasjonen leses fra et navngitt søskenobjekt.

**Forskyvning** — Forskyvning per trinn i verdensrommet i mm (vises når Referanse er Inndata).

**Rotasjon** — Rotasjon per trinn i grader per akse (vises når Referanse er Inndata).

**Skaler** / **Skaler akser** — Uniform og aksevis skalering som brukes ved hvert trinn (vises når Referanse er Inndata).

**Transformasjonsnavn** — Navnet på søskenobjektet hvis transformasjon brukes som trinnvis økning (vises når Referanse er Objekt).

**Relativt rom** — Når dette er på, settes hver kopis transformasjon sammen i det lokale koordinatsystemet til den forrige kopien; når det er av, brukes hvert trinn i verdensrommet (vises når Referanse er Objekt).

## Tilfeldiggjør

Aktiver **Tilfeldiggjør** for å legge til variasjon i alle kopiene.

- **Tilfeldig forskyvning** — Maksimal tilfeldig posisjonsforskyvning per akse i mm.
- **Tilfeldig rotasjon** — Maksimal tilfeldig rotasjon per akse i grader.
- **Tilfeldige skaleringsakser** — Maksimal tilfeldig skaleringsvariasjon per akse.
- **Utelat første** — Behold den første kopien på nøyaktig sin beregnede posisjon (standard: på).
- **Utelat siste** — Behold den siste kopien på nøyaktig sin beregnede posisjon.
- **Tilfeldig frø** — Endre denne for å få en annen tilfeldig plassering. Støtter uttrykk.

## Slå sammen

- **Lag én enkelt mesh** — Kombiner alle kopiene til ett sammenslått mesh-objekt.
- **Slå sammen punkter** — Sveis sammen punkter innenfor terskelen for sammenslåingsavstand (vises når Lag én enkelt mesh er på).
- **Avstand** — Terskel for sammenslåing i mm (vises når Slå sammen punkter er på).

## Tips

- Bruk uttrykk for Antall, Rotasjon eller Endepunkt for å lage parametriske mønstre
- For sirkulære mønstre bruker du Radiell modus — angi Radius for å styre sirkelens størrelse, og aktiver Juster rotasjon hvis kopiene skal vende utover
- Sammensetting av rotasjon i Lineær modus lager spiraler og vifter uten at du må beregne vinkelforskyvninger manuelt
- Skalering påvirker forskyvning gir naturlige oppsett med nautilusskjell og geometriske progresjoner
- Kombiner Matrise med [Velg underobjekt](select-child.md) for å lage mønstre der hver kopi viser en ulik variant

## Relatert

- [Juster](../placement/align.md) - Plasser objekter i forhold til hverandre
- [Velg underobjekt](select-child.md) - Velg en bestemt kopi fra en matrise etter indeks eller navn
