---
title: Trekk fra og erstatt
articleKey: SubtractAndReplaceObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c1698bab75faca8046b23cc148803c8063ba0678
source_lang: en
---
# Trekk fra og erstatt

Trekk fra og erstatt trekker delene du velger ut av delene du ikke valgte, men beholder biten som ble skåret bort som en egen del i stedet for å forkaste den. Bruk **Del(er) som skal trekkes fra** til å velge kutteformene; alt annet er grunnlaget som blir kuttet.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->
![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)

[Kombiner](combine.md), [Trekk fra](subtract.md), [Skjæring](intersect.md) og Trekk fra og erstatt utføres alle av ett boolsk objekt -- verktøylinjeknappen oppretter det med Trekk fra og erstatt allerede valgt, og du kan når som helst bytte til en av de tre andre fra ikonraden **Operasjon** øverst i Egenskaper-panelet.

Trekk fra og erstatt tilbys ikke for 2D-baner -- et område har ikke noe fjernet volum å gi tilbake.

## Slik bruker du den

1. Velg to eller flere objekter
2. Klikk **Trekk fra og erstatt** i verktøylinjen
3. Bruk **Del(er) som skal trekkes fra** til å velge hvilke underobjekter som er kutteformene
4. Ombestem deg når som helst ved å klikke et annet ikon i raden **Operasjon** øverst i Egenskaper-panelet -- formen bygges opp på nytt med den nye operasjonen

## Parametere

- **Operasjon** - Hvilken boolsk operasjon som skal utføres. Vises som en ikonrad øverst i panelet
- **Del(er) som skal trekkes fra** - Hvilke underobjekter som er kutteformene
- **Behold geometri med invertert innside** - Behandle et skall som vender innsiden ut som massivt materiale i stedet for å la det oppheve volumet rundt seg. Slå dette på når en modell som skal være massiv kommer tilbake med manglende deler. Det tvinger frem den tregere, eksakte boolske motoren
- **Reparer viklingsrekkefølge** - Snu viklingsrekkefølgen på hver dels inverterte skall før den boolske operasjonen kjøres. Dette retter opp geometrien én gang i stedet for å endre hva alle senere operasjoner regner som massivt, og er som regel den beste av de to løsningene på en modell med invertert innside

## Tips

- De to delene passer nøyaktig sammen, fordi de kom ut av samme operasjon
- Bruk den til flerfargede design, sammenlåsende sammenstillinger og innlegg
- Hvis et resultat ser feil ut, kontroller at kildeobjektene er vanntette. **Reparer viklingsrekkefølge** retter opp skall med invertert innside; [Reparer](../mesh/repair.md) retter opp større skader i importerte modeller

## Relatert

- [Kombiner](combine.md) - Slå sammen flere objekter til én massiv form
- [Trekk fra](subtract.md) - Skjær én form ut av en annen
- [Skjæring](intersect.md) - Behold bare volumet der objektene overlapper
- [Plankutt](../reshape/plane-cut.md) - Kutt med et flatt plan i stedet for en annen form
- [Reparer](../mesh/repair.md) - Reparer skadede importerte masker før en boolsk operasjon

Denne siden dekker også de eldre Trekk fra og erstatt-objektene som fortsatt finnes i design lagret før operasjonene ble slått sammen. De fungerer nøyaktig som før; nye design bruker det felles boolske objektet med operasjonen Trekk fra og erstatt valgt.
