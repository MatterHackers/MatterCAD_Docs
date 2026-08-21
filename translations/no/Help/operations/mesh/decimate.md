---
title: Reduser
articleKey: DecimateObject3D
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 58a2573b968808e98203832142fa8bacf7a9cf99
source_lang: en
---
# Reduser (desimer)

Reduser senker polygonantallet i et nett samtidig som den overordnede formen bevares. Dette er nyttig for å forenkle svært detaljerte modeller, redusere filstørrelsen og få operasjoner på kompleks geometri til å gå raskere.

![20260324 080430 paste 20260324 080430](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080430-paste-20260324-080430.jpg)


## Slik bruker du den

1. Velg et objekt
2. Bruk operasjonen **Reduser** fra Nett-menyen
3. Velg målet ditt (antall eller prosentandel) og juster

## Parametere

- **Modus** – Velg hvordan målet skal angis:
  - **Prosent** – Behold en prosentandel av de opprinnelige polygonene (standard: 50 %)
  - **Antall** – Sikt mot et bestemt polygonantall
- **Antall kildepolygoner** – Opprinnelig antall polygoner (skrivebeskyttet)
- **Målprosent** – Prosentandel av polygonene som skal beholdes (synlig i modusen Prosent)
- **Målantall** – Nøyaktig antall polygoner som skal beholdes (synlig i modusen Antall)
- **Antall etter prosentreduksjon** – Endelig polygonantall etter prosentvis reduksjon (skrivebeskyttet)
- **Behold overflate** – Projiser hjørnepunktene tilbake til den opprinnelige overflaten for høyere nøyaktighet (tregere, men mer tro mot den opprinnelige formen)

## Tips

- 50 % reduksjon bevarer vanligvis den visuelle kvaliteten godt
- Aktiver Behold overflate når nøyaktighet er viktigere enn hastighet
- Å redusere polygonantallet gjør boolske operasjoner på komplekse importerte modeller raskere
- Svært lave polygonantall vil forringe formen synlig – kontroller resultatet før du bekrefter

## Relatert

- [Reparer](repair.md) – Løs problemer med nettet
