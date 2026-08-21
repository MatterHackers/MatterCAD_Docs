---
title: Billedkonvertering
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c1a05f9688ebe115babfad5d63fc49445af7c449
source_lang: en
---
# Billedkonvertering

Billedkonvertering omdanner et rasterbillede til et 3D-relief, hvor pixlernes lysstyrke bestemmer højden. Lyse områder bliver hævede, og mørke områder bliver lave (eller omvendt).

![20260323 210414 paste 20260323 210414](https://matterhackers.github.io/MatterCAD_Docs/assets/20260323-210414-paste-20260323-210414.jpg)


## Sådan bruges det

1. Tilføj en Billedkonvertering fra panelet Primitiver, eller træk en billedfil ind i arbejdsområdet
2. Billedet konverteres til et 3D-højdekort
3. Juster højden og de øvrige parametre

## Tips

- Kontrastrige billeder med tydelige former giver de bedste resultater
- Hvis du vil optegne billedets omrids som flade baner i stedet for højdekort, skal du bruge [Billede til bane](image-to-path.md)
- Hvis du vil lave gennemlyste billedvisninger, skal du bruge [Litofan](lithophane.md)
- Du kan trække billeder direkte fra skrivebordet ind i arbejdsområdet
- Tilføj en base ved at kombinere billedreliefet med en [Terning](../../primitives/cube.md)

## Relateret

- [Billede til bane](image-to-path.md) - Optegn omrids i stedet for at oprette et højdekort
- [Litofan](lithophane.md) - Opret gennemlyste billedvisninger
- [Billedobjekt](../../primitives/image-object.md) - Primitivversionen af billedimport
