---
title: Extrudare liniară
articleKey: LinearExtrudeObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cdfdb9cfe4c3339e70a23ddfb2f5071b1e8c5557
source_lang: en
---
# Extrudare liniară

Extrudarea liniară dă înălțime unei căi 2D, transformând o formă plană într-un solid 3D. Aceasta este principala metodă de a converti căile în obiecte 3D.

<!--  Before and after showing a 2D star path extruded into a 3D star -->
![20260506 100726 paste 20260506 100726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100726-paste-20260506-100726.jpg)


## Mod de utilizare

1. Selectează o cale 2D sau un obiect bazat pe o cale
2. Aplică **Extrudare liniară** din meniul de operații Cale
3. Setează înălțimea dorită

## Parametri

- **Înălțime** - Cât de înaltă este extrudarea (implicit: 5mm, interval: 0.1-50mm)
- **Teșitură sus** - Adaugă o muchie teșită (rotunjită) în partea de sus a extrudării (implicit: dezactivat)

### Parametrii teșiturii (vizibili când Teșitură sus este activată)

- **Stil** - Stilul profilului teșiturii (Ascuțit sau rotunjit)
- **Rază** - Cât de mult se extinde teșitura (implicit: 3mm)
- **Segmente** - Netezimea curbei teșiturii (implicit: 9)

## Sfaturi

- Funcționează cu orice cale 2D: [Cerc](../../2d-paths/circle-path.md), [Cutie](../../2d-paths/box-path.md), [Stea](../../2d-paths/star-path.md), [SVG](../../primitives/svg-object.md) și căi [Personalizat](../../2d-paths/custom-path.md)
- Activează Teșitură sus pentru un aspect mai rafinat și profesional
- Pentru a roti o cale în jurul unei axe în loc să o extrudezi drept în sus, vezi [Revoluție](revolve.md)

## Articole conexe

- [Revoluție](revolve.md) - Rotește o cale în jurul unei axe
- [Căi 2D](../../2d-paths/index.md) - Formele de cale disponibile
- [Text](../../primitives/text.md) - Textul este extrudat automat
