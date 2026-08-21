---
title: Skjæring
articleKey: IntersectionObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b997cfc4f6d2f02559346365311f217388a6a2da
source_lang: en
---
# Skjæring

Skjæring beholder bare volumet som alle objektene deler, og forkaster resten.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->
![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)

[Kombiner](combine.md), [Trekk fra](subtract.md), Skjæring og [Trekk fra og erstatt](subtract-and-replace.md) utføres alle av ett boolsk objekt -- verktøylinjeknappen oppretter det med Skjæring allerede valgt, og du kan når som helst bytte til en av de tre andre fra ikonraden **Operasjon** øverst i Egenskaper-panelet.

Skjæring fungerer på volumer og på 2D-baner. Den ser på hva du har gitt den, og utfører riktig type operasjon, slik at skjæring mellom to baner gir én bane, og skjæring mellom to masker gir ett volum.

## Slik bruker du den

1. Velg to eller flere objekter
2. Klikk **Skjæring** i verktøylinjen
3. Ombestem deg når som helst ved å klikke et annet ikon i raden **Operasjon** øverst i Egenskaper-panelet -- formen bygges opp på nytt med den nye operasjonen

## Parametere

- **Operasjon** - Hvilken boolsk operasjon som skal utføres. Vises som en ikonrad øverst i panelet
- **Behold geometri med invertert innside** - Behandle et skall med invertert innside som massivt materiale i stedet for å la det oppheve volumet rundt seg. Slå på dette når en modell som skulle vært massiv, kommer tilbake med manglende deler. Det tvinger frem den tregere, eksakte boolske motoren
- **Reparer viklingsrekkefølge** - Snu viklingsrekkefølgen på hver dels skall med invertert innside før den boolske operasjonen kjøres. Dette retter geometrien én gang i stedet for å endre hva hver senere operasjon regner som massivt, og er som regel det beste av de to svarene på en modell med invertert innside

## Tips

- Objektene må overlappe. Hvis de ikke faktisk overlapper, blir resultatet tomt
- Med mer enn to objekter arbeider den nedover listen: de to første skjæres, deretter skjæres resultatet med det tredje, og så videre
- Hvis et resultat ser feil ut, kontroller at kildeobjektene er vanntette. **Reparer viklingsrekkefølge** retter skall med invertert innside; [Reparer](../mesh/repair.md) retter mer omfattende skader i importerte modeller

## Relatert

- [Kombiner](combine.md) - Slå sammen flere objekter til én massiv form
- [Trekk fra](subtract.md) - Skjær én form ut av en annen
- [Trekk fra og erstatt](subtract-and-replace.md) - Trekk fra én form og behold delen som ble skåret bort
- [Plankutt](../reshape/plane-cut.md) - Kutt med et flatt plan i stedet for med en annen form
- [Reparer](../mesh/repair.md) - Reparer skadde importerte masker før en boolsk operasjon

Denne siden dekker også de eldre Snitt-objektene som fortsatt finnes i design lagret før operasjonene ble slått sammen. De fungerer nøyaktig som før; nye design bruker det felles boolske objektet med operasjonen Skjæring valgt.
