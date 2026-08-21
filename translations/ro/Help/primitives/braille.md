---
title: Braille
articleKey: BrailleObject3D
parent: "Primitives"
nav_order: 2
source_hash: d1d9d4aeb9b87efbe32045f2a96cfea49048f95f
source_lang: en
---
# Braille

Generează text Braille imprimabil 3D pornind de la text standard în limba engleză. Instrumentul Braille acceptă atât codificarea Braille de gradul 1 (literă cu literă), cât și cea de gradul 2 (contractată).

<!-- Screenshot of a Braille object showing raised dots on the workspace -->
![20260318 182800 paste 20260318 182800](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-182800-paste-20260318-182800.jpg)


## Mod de utilizare

1. Adaugă o primitivă **Braille** din panoul Primitive
2. Tastează textul în câmpul **Text de codificat**
3. Instrumentul îl convertește automat în modelul corect de puncte Braille

## Parametri

- **Text de codificat** - Textul în limba engleză care va fi convertit în Braille
- **Scalare** - Ajustează dimensiunea generală a rezultatului Braille
- **Înălțime** - Înălțimea punctelor Braille în relief

## Sfaturi

- Braille de gradul 2 folosește contracții și abrevieri pentru cuvinte și combinații de litere frecvente, rezultatul fiind mai compact
- Sunt utilizate dimensiunile standard ale celulei Braille pentru a asigura lizibilitatea rezultatului
- Combină cu o bază plată [Cub](cube.md) pentru a crea o etichetă sau un indicator Braille complet
- Pentru carduri Braille cu bază integrată, vezi [Card Braille](braille-card.md)

## Articole conexe

- [Card Braille](braille-card.md) - Braille cu bază de card integrată
- [Text](text.md) - Text 3D standard
