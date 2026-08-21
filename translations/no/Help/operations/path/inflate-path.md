---
title: Utvid bane
articleKey: InflatePathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: c0e11d3d24c5f832f797cde4d392e26a4694733d
source_lang: en
---
# Utvid bane

Utvid bane utvider en 2D-bane utover, slik at formen blir større samtidig som den overordnede formen beholdes. Dette tilsvarer å bruke en jevn forskyvning på alle kanter.

<!--  Before and after showing a path inflated outward -->
![20260506 100652 paste 20260506 100652](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100652-paste-20260506-100652.jpg)


## Slik bruker du den

1. Velg en 2D-bane
2. Bruk **Utvid bane** fra Bane-operasjonsmenyen
3. Juster utvidelsesmengden

## Utvide en åpen linje

Utvid er måten du gjør en linje om til en form på. Fjern avkrysningen for **Lukket** på en [Egendefinert bane](../../2d-paths/custom-path.md) for å tegne en åpen linje, og utvid den deretter: resultatet er et fylt bånd som er like bredt på hver side av linjen som mengden du angir. Derfra ekstruderes den som enhver annen bane.

**Stil** angir hvordan de to endene av linjen avsluttes, og hvordan hjørnene skjøtes:

- **Flat** avslutter båndet rett av ved hvert endepunkt
- **Rund** legger til en halvsirkel forbi hvert endepunkt
- **Skarp** legger til et kvadrat forbi hvert endepunkt

En åpen linje har ingen innside å krympe inn i, så en verdi på null eller en negativ verdi ville ikke etterlatt noe som helst. Når banen er *helt* åpen, begrenser Utvid verdien opp til et lite positivt tall og skriver det begrensede tallet tilbake i feltet, slik at du kan se hva som skjedde.

En bane som blander åpne og lukkede konturer, begrenses ikke: de lukkede konturene krymper som normalt, og de åpne faller rett og slett bort. Lukkede baner krymper fortsatt ved negative verdier, akkurat som de alltid har gjort.

## Tips

- Bruk negative verdier for å krympe banen innover i stedet for å utvide den
- Utvid er nyttig for å lage toleranseforskyvninger rundt former
- Kombiner med [Konturbane](outline-path.md) for å lage kantlinjer med bestemte bredder

## Relatert

- [Konturbane](outline-path.md) – Opprett et omriss fra en bane
- [Kantbane](border-path.md) – Legg til en kantforskyvning
- [Glatt bane](smooth-path.md) – Avrund hjørnene på en bane
