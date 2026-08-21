---
title: Bilde til bane
articleKey: ImageToPathObject3D_2
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 0145587f635ede68bfc1df37b4f0d366a03d3a6c
source_lang: en
---
# Bilde til bane

Bilde til bane sporer omrissene i et bilde for å lage 2D-baner. Disse banene kan deretter ekstruderes, roteres eller brukes med alle andre baneoperasjoner. Dette er ideelt for å konvertere logoer, silhuetter og enkel grafikk til 3D-objekter.

![20260324 075521 paste 20260324 075521](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-075521-paste-20260324-075521.jpg)


## Slik bruker du den

1. Velg et bildeobjekt i arbeidsområdet
2. Bruk **Bilde til bane** fra menyen for Bilde-operasjoner
3. Velg analysetype og juster utvalgsområdet

## Parametere

- **Analysetype** - Hvordan bildet analyseres for sporing:
  - **Gjennomsiktighet** - Spor basert på gjennomsiktige kontra ugjennomsiktige områder (best for PNG-filer med gjennomsiktig bakgrunn)
  - **Farger** - Spor basert på fargeområder
  - **Intensitet** - Spor basert på lysstyrkenivåer (best for de fleste bilder)
- **Velg område** - En histogramkontroll for å velge hvilke lysstyrke-/fargeverdier som skal inkluderes i sporingen
- **Min overflateareal** - Minste areal for at en baneløkke skal inkluderes. Øk verdien for å filtrere bort små støyartefakter

## Tips

- Rene bilder med høy kontrast og enkle former fungerer best
- Bruk Gjennomsiktighet-modus for PNG-bilder med gjennomsiktig bakgrunn
- Bruk Intensitet-modus for fotografier og bilder uten gjennomsiktighet
- Etter sporing kan du bruke [Lineær ekstrudering](../path/linear-extrude.md) for å gi banen høyde
- Øk Min overflateareal for å fjerne små uønskede detaljer fra sporingen

## Relatert

- [Bildekonverterer](image-converter.md) - Lag høydekartrelieff i stedet for flate baner
- [Litofan](lithophane.md) - Lag bakbelyste bildevisninger
- [SVG-objekt](../../primitives/svg-object.md) - Importer vektorgrafikk direkte (ingen sporing nødvendig)
- [Lineær ekstrudering](../path/linear-extrude.md) - Gi den sporede banen høyde
