---
title: Kube
articleKey: CubeObject3D
parent: "Primitives"
nav_order: 4
source_hash: a376a9c78d88d995f3c6ce21dd5098672d6c1dfb
source_lang: en
---
# Kube

En rektangulær boksform med justerbar bredde, dybde, høyde og valgfrie avrundede kanter. Kuben er en av de mest brukte primitivene for å bygge design.

<!--  Screenshot of a Cube primitive on the workspace -->
![20260318 183230 paste 20260318 183230](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183230-paste-20260318-183230.jpg)


## Parametere

- **Bredde** - Størrelse langs X-aksen (standard: 20mm)
- **Dybde** - Størrelse langs Y-aksen (standard: 20mm)
- **Høyde** - Størrelse langs Z-aksen (standard: 20mm)
- **Rund** - Aktiver avrundede kanter
- **Radius** - Størrelsen på avrundingen (synlig når Rund er aktivert)
- **Runde segmenter** - Hvor glatt avrundingen er, flere segmenter = glattere kurver (synlig når Rund er aktivert)

## Tips

- Bruk en Kube som utgangspunkt for bokser, plater, braketter og kabinetter
- Aktiver Rund for glatte kanter med profesjonelt utseende
- Radiusen kan ikke overstige halvparten av den minste dimensjonen
- Kombiner en Kube med [Trekk fra](../operations/boolean/subtract.md) for å lage rektangulære utskjæringer og spor

## Relatert

- [Sylinder](cylinder.md) - Rund søyleform
- [Pyramide](pyramid.md) - Avsmalnende firesidig form
- [Hull](hole.md) - En kube forhåndskonfigurert for boolsk subtraksjon
