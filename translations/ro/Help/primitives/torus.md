---
title: Tor
articleKey: TorusObject3D
parent: "Primitives"
nav_order: 17
source_hash: aaec1652de4d6713bd01a707964cf4985d3fb5f6
source_lang: en
---
# Tor

Un inel în formă de gogoașă, cu control independent asupra dimensiunii generale și a grosimii secțiunii transversale a inelului.

<!--  Screenshot of a Torus primitive on the workspace -->
![20260318 184240 paste 20260318 184240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184240-paste-20260318-184240.jpg)


## Parametri

- **Diametru exterior** - Lățimea totală a torului (implicit: 20mm)
- **Diametru interior** - Diametrul orificiului din centru (implicit: 10mm)
- **Laturi** - Numărul de segmente de-a lungul inelului principal (implicit: 40)

### Parametri avansați

Activați modul **Avansat** pentru controale suplimentare:

- **Unghi inițial** - Unghiul la care începe torul (implicit: 0)
- **Unghi final** - Unghiul la care se termină torul (implicit: 360). Setați o valoare mai mică de 360 pentru un inel deschis sau un arc
- **Laturi inel** - Numărul de segmente de-a lungul secțiunii transversale a inelului (implicit: 15). Mai multe = profil de tub mai neted
- **Unghi de fază inel** - Rotește profilul secțiunii transversale (implicit: 0)

## Sfaturi

- Grosimea tubului inelului este determinată de diferența dintre Diametru exterior și Diametru interior
- Folosiți Unghi inițial și Unghi final pentru a crea segmente de inel deschise, arce sau forme de C
- Util pentru crearea de garnituri inelare (O-ring), mânere, inele decorative și coturi de țeavă

## Articole conexe

- [Inel](ring.md) - Un cilindru gol cu pereți drepți (tub)
- [Sferă](sphere.md) - O formă de bilă plină
- [Jumătate de sferă](half-sphere.md) - O formă de cupolă
