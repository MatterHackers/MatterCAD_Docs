---
title: Inel
articleKey: RingObject3D
parent: "Primitives"
nav_order: 13
source_hash: fd16c400f3d8c8af13416ab57ddd8407e761d93a
source_lang: en
---
# Inel

Un cilindru gol (tub) cu diametre interior și exterior independente și o înălțime specificată. Cunoscut și ca formă de țeavă sau tub.

<!--  Screenshot of a Ring primitive on the workspace -->
![20260318 183848 paste 20260318 183848](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183848-paste-20260318-183848.jpg)


## Parametri

- **Diametru exterior** - Lățimea exterioară a inelului (implicit: 20mm)
- **Diametru interior** - Diametrul centrului gol (implicit: 15mm)
- **Înălțime** - Cât de înalt este inelul (implicit: 5mm)
- **Laturi** - Numărul de segmente de pe perimetru (implicit: 40)

### Parametri avansați

Activează modul **Avansat** pentru comenzi suplimentare:

- **Unghi inițial** - Unghiul de la care începe inelul (implicit: 0)
- **Unghi final** - Unghiul la care se termină inelul (implicit: 360). Setează o valoare mai mică de 360 pentru un inel parțial
- **Rotund** - Adaugă rotunjire muchiilor (Niciunul, Sus sau Jos)
- **Direcție** - Rotunjire spre muchia interioară sau exterioară (vizibil când **Rotund** este activat)
- **Segmente de rotunjire** - Netezimea rotunjirii (vizibil când **Rotund** este activat)

## Sfaturi

- Grosimea peretelui este egală cu (Diametru exterior - Diametru interior) / 2
- Folosește această formă pentru șaibe, distanțiere, bucșe și elemente de tip tub
- Setează o înălțime mare pentru țevi sau una mică pentru șaibe plate
- Folosește **Unghi inițial** și **Unghi final** pentru forme de inel parțial, precum clemele în C

## Similare

- [Tor](torus.md) - Un inel în formă de gogoașă, cu secțiune transversală rotundă
- [Cilindru](cylinder.md) - O coloană rotundă plină (fără centru gol)
