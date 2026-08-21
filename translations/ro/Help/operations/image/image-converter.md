---
title: Convertor de imagini
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c1a05f9688ebe115babfad5d63fc49445af7c449
source_lang: en
---
# Convertor de imagini

Convertorul de imagini transformă o imagine raster într-un relief 3D în care luminozitatea pixelilor determină înălțimea. Zonele luminoase devin ridicate, iar zonele întunecate devin joase (sau invers).

![20260323 210414 paste 20260323 210414](https://matterhackers.github.io/MatterCAD_Docs/assets/20260323-210414-paste-20260323-210414.jpg)


## Mod de utilizare

1. Adaugă un Convertor de imagini din panoul Primitive sau trage un fișier imagine în spațiul de lucru
2. Imaginea este convertită într-o hartă de înălțime 3D
3. Ajustează înălțimea și ceilalți parametri

## Sfaturi

- Imaginile cu contrast ridicat și forme clare produc cele mai bune rezultate
- Pentru a trasa conturul imaginilor ca trasee plane în loc de hărți de înălțime, folosește [Imagine în traseu](image-to-path.md)
- Pentru a crea afișaje de imagini iluminate din spate, folosește [Litofanie](lithophane.md)
- Poți trage imaginile direct de pe desktop în spațiul de lucru
- Adaugă o bază combinând relieful imaginii cu un [Cub](../../primitives/cube.md)

## Articole conexe

- [Imagine în traseu](image-to-path.md) - Trasează contururi în loc să creeze o hartă de înălțime
- [Litofanie](lithophane.md) - Creează afișaje de imagini iluminate din spate
- [Obiect Imagine](../../primitives/image-object.md) - Versiunea primitivă a importului de imagini
