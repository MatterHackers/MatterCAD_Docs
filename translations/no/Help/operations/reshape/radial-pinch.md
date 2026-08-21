---
title: Radiell klemming
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: 95ef5847767e5cfcdbae9df9aaa1cb1727da2f5e
source_lang: en
---
# Radiell klemming

Radiell klemming komprimerer et objekt innover fra et senterpunkt med en tilpassbar profilkurve. Lik ikke vanlig [Klem](pinch.md), som virker fra bak til front, komprimerer Radiell klemming symmetrisk rundt en senterakse.

<!--  Before and after showing an object with radial pinch applied, creating a waisted shape -->
![20260506 155741 paste 20260506 155741](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155741-paste-20260506-155741.jpg)

## Slik bruker du den

1. Velg et objekt
2. Bruk operasjonen **Radiell klemming** fra Endre form-menyen
3. Rediger baneprofilen for å definere hvor mye klemming som brukes ved hver høyde
4. Juster antall snitt for jevnhet

## Parametere

- **Bane** – En profilkurveredigerer som definerer klemmemengden ved hvert høydenivå. Rediger kurven for å lage egne klemmeprofiler
- **Snitt** – Antall horisontale kutt for jevn klemming, jevnt fordelt oppover delen. Flere snitt = jevnere resultat

### Avanserte parametere

- **Klemmetype** – Retning på komprimeringen:
  - **Radiell** – Komprimer likt fra alle sider mot senter
  - **X-akse** – Komprimer bare langs X-aksen
  - **Y-akse** – Komprimer bare langs Y-aksen
- **Rotasjonsforskyvning** – Forskyv senteret for klemmeeffekten

## Tips

- Bruk baneredigereren til å lage timeglass-, flaske- eller vaselignende former
- Radiell klemming er ideell for å lage organiske, avrundede former fra sylindriske objekter
- Øk Snitt for jevnere kurver, spesielt ved trange klemmeprofiler

## Relatert

- [Klem](pinch.md) – Enkel komprimering fra bak til front
- [Vri](twist.md) – Spiralrotasjon langs høyden
- [Kurve](curve.md) – Bøy til en bue
