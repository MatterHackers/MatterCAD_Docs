---
title: Tekst
articleKey: TextObject3D_2
parent: "Primitives"
nav_order: 16
source_hash: 526f3190c7b2150243499b5874ac455d74810bb2
source_lang: en
---
# Tekst

Opret 3D-ekstruderet tekst med tilpasseligt indhold, skrifttype, størrelse og højde. Tekstobjekter er velegnede til etiketter, skilte, navneskilte og dekorative bogstaver.

<!--  Screenshot of a 3D Text object on the workspace showing extruded letters -->
![20260318 184207 paste 20260318 184207](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184207-paste-20260318-184207.jpg)


## Sådan bruges den

1. Tilføj en **Tekst**-primitiv fra Primitiver-panelet
2. Skriv din tekst i feltet **Navn** i Egenskaber-panelet
3. Justér skrifttype, størrelse og ekstruderingshøjde efter behov

## Parametre

- **Navn** - Det tekstindhold, der skal vises
- **Punktstørrelse** - Skriftstørrelsen. Den er nøjagtig i forhold til standardstørrelser i tryk -- en 12-punkts størrelse i MatterCAD svarer til 12-punkts skrift på en 2D-printer
- **Højde** - Ekstruderingshøjden (hvor langt teksten rager op fra overfladen)
- **Skrifttype** - Vælg blandt tilgængelige systemskrifttyper

## Tips

- Brug [Træk fra](../operations/boolean/subtract.md) til at gravere tekst ned i en overflade i stedet for at hæve den
- Ved meget lille tekst kan du øge Punktstørrelse og derefter [Skalér](../operations/transform/scale.md) hele objektet ned for at få bedre detaljer
- Hvert bogstav i teksten er en separat kontur, der ekstruderes sammen med de øvrige

## Relateret

- [Braille](braille.md) - Generer 3D-printbar punktskrift
- [QR-kode](qr-code.md) - Generer en QR-kode som et 3D-objekt
- [Billedobjekt](image-object.md) - Konvertér billeder til 3D
