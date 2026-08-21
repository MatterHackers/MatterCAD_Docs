---
title: Kurve
articleKey: CurveObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 6adde5da3bb469384f59eb5e9dfe5cb642b3eec5
source_lang: en
---
# Kurve

Kurve bøyer et rett objekt til en bue eller sirkulær form. Du kan styre bøyen ved å angi enten en vinkel eller en diameter som objektet skal legges rundt.

<!--  Before and after showing a straight bar being curved into an arc -->
![20260506 155243 paste 20260506 155243](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155243-paste-20260506-155243.jpg)

## Slik bruker du den

1. Velg et objekt
2. Bruk operasjonen **Kurve** fra menyen Endre form
3. Velg mellom bøytypen Vinkel eller Diameter
4. Juster parameterne for å oppnå ønsket krumning

## Parametere

- **Bøytype** – Velg mellom:
  - **Vinkel** – Angi bøyevinkelen direkte (1–360 grader)
  - **Diameter** – Angi diameteren på sirkelen delen legges rundt
- **Bøyeretning** – Bøy opp eller Bøy ned
- **Startprosent** – Hvor langs objektet bøyen skal starte (0–100 %)
- **Del opp mesh** – Del opp mesh for jevne kurver (standard: på)
- **Min sider per rotasjon** – Minste antall mesh-segmenter per hele omdreining. Høyere verdier = jevnere kurver

### Avanserte parametere

- **Startbøy i prosent** – Prosentandel fra venstre der bøyen starter
- **Sluttbøy i prosent** – Prosentandel fra venstre der bøyen slutter

## Tips

- Bruk Kurve til å lage buer, ringer og bøyde braketter fra rette utgangsformer
- Setter du vinkelen til 360, legges objektet sammen til en komplett ring
- Øk Min sider per rotasjon for jevnere resultat ved krappe bøyer
- Objektet bøyes langs lengden (X-aksen)

## Relatert

- [Vri](twist.md) – Roter langs høyden i stedet for å bøye
- [Torus](../../primitives/torus.md) – En ferdig ringform
