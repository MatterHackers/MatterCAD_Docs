---
title: Plankutt
articleKey: PlaneCutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 5
source_hash: 64a9901bf54b71cd2ecc12c8db189b6e2fcde25e
source_lang: en
---
# Plankutt

Plankutt deler et objekt i en angitt høyde med et horisontalt plan, og beholder bare delen under kuttet. Kuttflaten lukkes med en flat overflate.

<!--  Before and after showing an object being sliced at a specific height -->
![20260506 155526 paste 20260506 155526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155526-paste-20260506-155526.jpg)

## Slik bruker du den

1. Velg et objekt
2. Bruk operasjonen **Plankutt** fra Endre form-menyen
3. Angi kuttehøyden

## Parametere

- **Kuttehøyde** – Z-høyden objektet skal deles ved (standard: 10 mm, område: 1–200 mm)

## Tips

- Bruk Plankutt til å flate ut toppen av en modell i en bestemt høyde
- Nyttig for å beskjære importerte modeller eller lage flate underlag
- For å kutte med en form som ikke er plan, bruk [Trekk fra](../boolean/subtract.md) med et annet objekt i stedet
- For å kutte med et skråstilt plan roterer du objektet først, bruker Plankutt og roterer tilbake

## Relatert

- [Skjæring](../boolean/intersect.md) – Behold bare der objektene overlapper
- [Trekk fra](../boolean/subtract.md) – Kutt med hvilken som helst form, ikke bare et plan
- [Hul ut](hollow-out.md) – Lag et hult skall
