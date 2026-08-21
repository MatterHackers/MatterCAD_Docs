---
title: Bildekonverterer
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c1a05f9688ebe115babfad5d63fc49445af7c449
source_lang: en
---
# Bildekonverterer

Bildekonverterer gjør et rasterbilde om til en 3D-relieff der pikselens lysstyrke bestemmer høyden. Lyse områder blir hevet og mørke områder blir lave (eller omvendt).

![20260323 210414 paste 20260323 210414](https://matterhackers.github.io/MatterCAD_Docs/assets/20260323-210414-paste-20260323-210414.jpg)


## Slik bruker du den

1. Legg til en Bildekonverterer fra Primitiver-panelet, eller dra en bildefil inn i arbeidsområdet
2. Bildet konverteres til et 3D-høydekart
3. Juster høyden og andre parametere

## Tips

- Bilder med høy kontrast og tydelige former gir de beste resultatene
- For å spore bildekonturer som flate baner i stedet for høydekart, bruk [Bilde til bane](image-to-path.md)
- For å lage bakbelyste bildevisninger, bruk [Litofan](lithophane.md)
- Du kan dra bilder direkte fra skrivebordet inn i arbeidsområdet
- Legg til en base ved å kombinere bildereliefen med en [Kube](../../primitives/cube.md)

## Relatert

- [Bilde til bane](image-to-path.md) – Spor konturer i stedet for å lage et høydekart
- [Litofan](lithophane.md) – Lag bakbelyste bildevisninger
- [Bilde-objekt](../../primitives/image-object.md) – Primitiv-versjonen av bildeimport
