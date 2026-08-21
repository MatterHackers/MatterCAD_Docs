---
title: Tekst
articleKey: TextObject3D_2
parent: "Primitives"
nav_order: 16
source_hash: 526f3190c7b2150243499b5874ac455d74810bb2
source_lang: en
---
# Tekst

Opprett 3D-ekstrudert tekst med tilpassbart innhold, skrift, størrelse og høyde. Tekstobjekter er godt egnet til etiketter, skilt, navneskilt og dekorative bokstaver.

<!--  Screenshot of a 3D Text object on the workspace showing extruded letters -->
![20260318 184207 paste 20260318 184207](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184207-paste-20260318-184207.jpg)


## Slik bruker du den

1. Legg til en **Tekst**-primitiv fra Primitiver-panelet
2. Skriv inn teksten din i feltet **Navn** i Egenskaper-panelet
3. Juster skrift, størrelse og ekstruderingshøyde etter behov

## Parametere

- **Navn** - Tekstinnholdet som skal vises
- **Punktstørrelse** - Skriftstørrelsen. Denne er nøyaktig i forhold til standard trykkstørrelser -- en størrelse på 12 punkt i MatterCAD tilsvarer 12-punkts skrift på en 2D-skriver
- **Høyde** - Ekstruderingshøyden (hvor langt teksten stikker opp fra overflaten)
- **Skrift** - Velg blant tilgjengelige systemskrifter

## Tips

- Bruk [Trekk fra](../operations/boolean/subtract.md) for å gravere teksten inn i en overflate i stedet for å heve den
- For svært liten tekst kan du øke Punktstørrelse og deretter [Skaler](../operations/transform/scale.md) ned hele objektet for å få bedre detaljer
- Hver bokstav i teksten er en egen bane som ekstruderes sammen med de andre

## Relatert

- [Blindeskrift](braille.md) - Generer 3D-utskrivbar blindeskrift
- [QR-kode](qr-code.md) - Generer en QR-kode som et 3D-objekt
- [Bilde-objekt](image-object.md) - Konverter bilder til 3D
