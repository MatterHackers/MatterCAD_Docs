---
title: Sylinder
articleKey: CylinderObject3D
parent: "Primitives"
nav_order: 5
source_hash: ab8394a14de799f83dc9c39eb86b8eaf2aab37b7
source_lang: en
---
# Sylinder

En rund søyleform med konfigurerbar diameter, høyde og antall sider. Sylinder er avgjørende for å lage pinner, staver, hull og runde detaljer.

<!--  Screenshot of a Cylinder primitive on the workspace -->
![20260318 183248 paste 20260318 183248](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183248-paste-20260318-183248.jpg)


## Parametere

- **Diameter** - Bredden tvers over sylinderen (standard: 20mm)
- **Høyde** - Hvor høy sylinderen er (standard: 20mm)
- **Sider** - Antall segmenter rundt omkretsen (standard: 40). Lavere verdier gir polygonale former (f.eks. 6 for en sekskant)

### Avanserte parametere

Aktiver **Avansert**-modus for å få tilgang til flere kontroller:

- **Diameter topp** - Angi en annen diameter for toppen av sylinderen for å lage koniske eller avkuttede kjegleformer (standard: samme som Diameter)
- **Startvinkel** - Vinkelen der sylinderen begynner (standard: 0). Brukes sammen med Sluttvinkel for å lage delvise sylindere
- **Sluttvinkel** - Vinkelen der sylinderen slutter (standard: 360). Sett lavere enn 360 for kakestykkeformer

## Tips

- Sett Sider til et lavt tall for å lage regulære polygoner -- 6 for sekskanter, 8 for åttekanter osv.
- Bruk ulike verdier for Diameter og Diameter topp for å lage avkuttede kjegler og koniske former
- Angi Startvinkel og Sluttvinkel for å lage kakestykke- eller bueformer
- Sylindere er utmerkede kutteverktøy for å lage runde hull med [Trekk fra](../operations/boolean/subtract.md)

## Relatert

- [Kjegle](cone.md) - En sylinder som smalner av til et punkt
- [Halvsylinder](half-cylinder.md) - En sylinder delt i to på langs
- [Ring](ring.md) - En hul sylinder (rør)
