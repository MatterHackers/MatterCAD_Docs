---
title: Oglindire
articleKey: MirrorObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 8a8de28f5e429177d4b0092d0756387eb6b83a70
source_lang: en
---
# Oglindire

Oglindire creează o copie reflectată a unui obiect față de una dintre cele trei axe principale. Rezultatul este o versiune oglindită a formei originale.

<!--  Before and after showing an object mirrored across the X axis -->
![20260506 160651 paste 20260506 160651](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160651-paste-20260506-160651.jpg)


## Mod de utilizare

1. Selectați un obiect
2. Aplicați operația **Oglindire** din meniul Transformare
3. Alegeți axa față de care se face oglindirea

## Parametri

- **Oglindire activă** - Axa față de care se face oglindirea:
  - **Axa X** - Răstoarnă obiectul de la stânga la dreapta
  - **Axa Y** - Răstoarnă obiectul din față în spate
  - **Axa Z** - Răstoarnă obiectul de sus în jos

## Sfaturi

- Oglindirea este centrată pe caseta de încadrare a obiectului, astfel încât rezultatul oglindit ocupă același spațiu ca originalul
- Normalele fețelor sunt corectate automat după oglindire, pentru a menține o randare corectă
- Folosiți Oglindire pentru a crea modele simetrice -- modelați o jumătate, apoi oglindiți-o și folosiți [Combină](../boolean/combine.md) cu originalul
- Oglindire este nedistructivă: puteți schimba oricând axa de oglindire

## Articole conexe

- [Rotire](rotate.md) - Rotiți un obiect în loc să îl oglindiți
- [Scalare](scale.md) - Redimensionați un obiect
- [Combină](../boolean/combine.md) - Îmbinare a originalului și a copiei oglindite într-un singur obiect
