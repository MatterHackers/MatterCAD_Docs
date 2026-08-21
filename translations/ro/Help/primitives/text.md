---
title: Text
articleKey: TextObject3D_2
parent: "Primitives"
nav_order: 16
source_hash: 526f3190c7b2150243499b5874ac455d74810bb2
source_lang: en
---
# Text

Creați text 3D extrudat cu conținut, font, dimensiune și înălțime personalizabile. Obiectele text sunt excelente pentru etichete, indicatoare, plăcuțe cu nume și litere decorative.

<!--  Screenshot of a 3D Text object on the workspace showing extruded letters -->
![20260318 184207 paste 20260318 184207](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184207-paste-20260318-184207.jpg)


## Mod de utilizare

1. Adăugați o primitivă **Text** din panoul Primitive
2. Introduceți textul în câmpul **Nume** din panoul Proprietăți
3. Ajustați fontul, dimensiunea și înălțimea de extrudare după necesități

## Parametri

- **Nume** - Conținutul textului care va fi afișat
- **Dimensiune punct** - Dimensiunea fontului. Este exactă în raport cu dimensionarea standard de tipar -- o dimensiune de 12 puncte în MatterCAD corespunde caracterelor de 12 puncte la o imprimantă 2D
- **Înălțime** - Înălțimea de extrudare (cât de mult iese textul în relief de pe suprafață)
- **Font** - Selectați dintre fonturile de sistem disponibile

## Sfaturi

- Folosiți [Scădere](../operations/boolean/subtract.md) pentru a grava textul într-o suprafață în loc să îl ridicați în relief
- Pentru text foarte mic, măriți Dimensiune punct și apoi aplicați [Scalare](../operations/transform/scale.md) în jos pentru întregul obiect, pentru un nivel de detaliu mai bun
- Fiecare literă din text este un traseu separat care este extrudat împreună cu celelalte

## Articole conexe

- [Braille](braille.md) - Generează text Braille imprimabil 3D
- [Cod QR](qr-code.md) - Generează un cod QR ca obiect 3D
- [Obiect Imagine](image-object.md) - Convertiți imagini în 3D
