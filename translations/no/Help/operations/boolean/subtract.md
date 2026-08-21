---
title: Trekk fra
articleKey: SubtractObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 59685bd0a635b70d7f938780f71e90be595dd993
source_lang: en
---
# Trekk fra

Trekk fra skjærer delene du velger ut av delene du ikke velger. Bruk **Del(er) som skal trekkes fra** til å velge skjæreformene; alt annet er grunnlaget som blir skåret i.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->
![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)

[Kombiner](combine.md), Trekk fra, [Skjæring](intersect.md) og [Trekk fra og erstatt](subtract-and-replace.md) utføres alle av ett boolsk objekt – verktøylinjeknappen oppretter det med Trekk fra allerede valgt, og du kan når som helst bytte til en av de tre andre fra ikonraden **Operasjon** øverst i Egenskaper-panelet.

Trekk fra fungerer på solider og på 2D-baner. Den ser på hva du gir den og utfører riktig type operasjon, slik at det å trekke én bane fra en annen gir en bane, og det å trekke ett nett fra et annet gir en solid.

## Slik bruker du den

1. Velg to eller flere objekter
2. Klikk **Trekk fra** i verktøylinjen – en standarddel som skal skjæres bort velges for deg, slik at operasjonen gjør noe med en gang
3. Bruk **Del(er) som skal trekkes fra** til å velge hvilke underobjekter som er skjæreformene
4. Ombestem deg når som helst ved å klikke et annet ikon i raden **Operasjon** øverst i Egenskaper-panelet – formen bygges opp på nytt med den nye operasjonen

## Parametere

- **Operasjon** – Hvilken boolsk operasjon som skal utføres. Vises som en ikonrad øverst i panelet
- **Del(er) som skal trekkes fra** – Hvilke underobjekter som er skjæreformene
- **Behold fratrukne deler** – La delene som ble skåret bort bli værende i scenen i stedet for å forkaste dem
- **Behold geometri med invertert innside** – Behandle et invertert skall som massivt materiale i stedet for å la det oppheve volumet rundt seg. Slå på dette når en modell som skal være massiv kommer tilbake med manglende deler. Det tvinger frem den tregere, eksakte boolske motoren
- **Reparer viklingsrekkefølge** – Snu viklingsrekkefølgen på hver dels inverterte skall før den boolske operasjonen kjøres. Dette retter opp geometrien én gang i stedet for å endre hva hver senere operasjon regner som massivt, og er som regel det beste av de to svarene på en invertert modell

## Tips

- Objektene må overlappe for at Trekk fra skal ha noen effekt
- For å skjære et gjennomgående hull må du sørge for at skjæreobjektet går helt gjennom grunnlaget
- For et enkelt hull er primitivet [Hull](../../primitives/hole.md) allerede satt opp til å trekkes fra
- Skjæreobjektene blir værende i designtreet, så du kan flytte eller endre størrelse på dem, og skjæringen oppdateres
- Hvis et resultat ser feil ut, kontroller at kildeobjektene er vanntette. **Reparer viklingsrekkefølge** retter opp inverterte skall; [Reparer](../mesh/repair.md) retter opp mer omfattende skader i importerte modeller

## Relatert

- [Kombiner](combine.md) – Slå sammen flere objekter til én massiv form
- [Skjæring](intersect.md) – Behold bare volumet der objektene overlapper
- [Trekk fra og erstatt](subtract-and-replace.md) – Trekk fra én form og behold delen som ble skåret bort
- [Plankutt](../reshape/plane-cut.md) – Skjær med et flatt plan i stedet for med en annen form
- [Hull](../../primitives/hole.md) – En kube som er forhåndskonfigurert til å trekkes fra
- [Reparer](../mesh/repair.md) – Reparer skadde importerte nett før en boolsk operasjon

Denne siden dekker også de eldre Trekk fra-objektene som fortsatt finnes i design lagret før operasjonene ble slått sammen. De fungerer nøyaktig som før; nye design bruker det felles boolske objektet med operasjonen Trekk fra valgt.
