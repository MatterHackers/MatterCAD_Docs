---
title: Golire interioară
articleKey: HollowOutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cc2c5555723ecfe77475fef9e7a2090cdf760204
source_lang: en
---
# Golire interioară

Golire interioară creează o coajă goală dintr-un obiect solid prin decalarea suprafeței spre interior. Rezultatul este o versiune cu pereți subțiri a formei originale.

<!--  Cross-section view showing a solid object hollowed out with visible wall thickness -->
![20260506 155412 paste 20260506 155412](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155412-paste-20260506-155412.jpg)

## Mod de utilizare

1. Selectați un obiect solid
2. Aplicați operația **Golire interioară** din meniul Remodelează
3. Stabiliți grosimea dorită a peretelui

## Parametri

- **Distanță** - Grosimea peretelui în milimetri (implicit: 2mm). Aceasta este grosimea cojii rezultate.
- **Nr. celule** - Rezoluția algoritmului de golire (implicit: 64). Valorile mai mari creează suprafețe interne mai netede, dar necesită mai mult timp de calcul.

## Sfaturi

- Golire interioară este utilă pentru crearea de carcase, recipiente, vaze și piese ușoare
- O grosime a peretelui de 1-2mm este tipică pentru majoritatea pieselor imprimate 3D
- Măriți valoarea Nr. celule dacă suprafața internă apare aspră sau în trepte
- Golirea creează o bază deschisă -- combinați cu un [Cub](../../primitives/cube.md) dacă aveți nevoie de o bază închisă
- Pentru forme complexe, calculul poate dura câteva secunde

## Subiecte conexe

- [Tăiere cu plan](plane-cut.md) - Tăiați un obiect la o anumită înălțime
- [Scădere](../boolean/subtract.md) - Îndepărtați material manual
