---
title: Kombiner
articleKey: CombineObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: a3066faa634b5a88a2fe1650a4e2ac278ac50e24
source_lang: en
---
# Kombiner

Kombiner slår alt sammen til ett enkelt solid. Interne flater der formene overlappet fjernes, slik at resultatet blir ett sammenhengende mesh i stedet for overlappende skall.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->
![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)

Kombiner, [Trekk fra](subtract.md), [Skjæring](intersect.md) og [Trekk fra og erstatt](subtract-and-replace.md) utføres alle av ett boolsk objekt – verktøylinjeknappen oppretter det med Kombiner allerede valgt, og du kan når som helst bytte til en av de tre andre fra ikonraden **Operasjon** øverst i Egenskaper-panelet.

Kombiner fungerer på solider og på 2D-baner. Den ser på hva du har gitt den og utfører riktig type operasjon, slik at kombinering av to baner gir én bane og kombinering av to mesh gir ett solid.

## Slik bruker du den

1. Velg to eller flere objekter
2. Klikk **Kombiner** i verktøylinjen
3. Ombestem deg når som helst ved å klikke et annet ikon i raden **Operasjon** øverst i Egenskaper-panelet – formen bygges opp på nytt med den nye operasjonen

## Parametere

- **Operasjon** – Hvilken boolsk operasjon som skal utføres. Vises som en ikonrad øverst i panelet
- **Behold geometri med invertert innside** – Behandle et skall med invertert innside som fast materiale i stedet for å la det oppheve volumet rundt seg. Slå på dette når en modell som skal være solid kommer tilbake med manglende deler. Det tvinger frem den tregere, eksakte boolske motoren
- **Reparer viklingsrekkefølge** – Snu viklingsrekkefølgen på hver dels skall med invertert innside før den boolske operasjonen kjøres. Dette retter geometrien én gang i stedet for å endre hva hver senere operasjon regner som solid, og er som regel den beste av de to løsningene på en modell med invertert innside

## Tips

- Kombiner vil fortsatt slå sammen objekter som ikke overlapper til ett mesh, men de forblir visuelt adskilte
- Kombiner håndterer Hull-objekter for deg: alt som er merket som et hull trekkes fra resultatet i stedet for å legges til
- Kombiner viderefører farger per flate fra de opprinnelige objektene
- Hvis et resultat ser feil ut, kontroller at kildeobjektene er vanntette. **Reparer viklingsrekkefølge** retter skall med invertert innside; [Reparer](../mesh/repair.md) retter mer omfattende skader i importerte modeller

## Relatert

- [Trekk fra](subtract.md) – Skjær én form ut av en annen
- [Skjæring](intersect.md) – Behold bare volumet der objektene overlapper
- [Trekk fra og erstatt](subtract-and-replace.md) – Trekk fra én form og behold delen som ble skåret bort
- [Plankutt](../reshape/plane-cut.md) – Kutt med et flatt plan i stedet for en annen form
- [Hull](../../primitives/hole.md) – En kube forhåndskonfigurert til å trekkes fra
- [Reparer](../mesh/repair.md) – Reparer skadede importerte mesh før en boolsk operasjon

Denne siden dekker også de eldre Kombiner-objektene som fortsatt finnes i design lagret før operasjonene ble slått sammen. De fungerer nøyaktig som før; nye design bruker det felles boolske objektet med operasjonen Kombiner valgt.
