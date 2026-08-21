---
title: Roți dințate
articleKey: GearObject3D
parent: "Mechanical Parts"
nav_order: 2
source_hash: 23098f94da8cd032e0617fbf346621504446347f
source_lang: en
---
# Roți dințate

Creați roți dințate 3D cu geometria dinților complet configurabilă. MatterCAD generează profiluri evolventice corecte, care angrenează corect cu alte roți dințate având același modul și același unghi de presiune.

<!-- AUTO_IMAGE: type=from_thumbnail item=gear file=mechanical_gears -->
![mechanical_gears](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_gears.png)

## Mod de utilizare

1. Adăugați o **Roată dințată** din instrumentele Mecanic sau din panoul Primitive
2. Setați numărul de dinți și ceilalți parametri
3. Profilul roții dințate este generat automat

## Parametri

### Caracteristici

- **Tip roată dințată** - Roată dințată Extern sau Cremalieră (bară dreaptă cu dinți)
- **Înălțime** - Grosimea roții dințate (înălțimea de extrudare)
- **Număr de dinți** - Numărul de dinți de pe circumferința roții dințate (implicit: 30, interval: 4-60)
- **Pas circular** - Distanța pe arc dintre dinți, măsurată pe cercul de divizare (interval: 3-30). Aceasta determină dimensiunea generală.
- **Diametru gaură centrală** - Diametrul găurii centrale pentru arbore (implicit: 4mm, setați 0 pentru nicio gaură). Doar pentru roțile dințate externe.
- **Lățime margine exterioară** - Lățimea marginii din exteriorul dinților interiori
- **Număr dinți roată interioară** - Numărul de dinți al roții dințate interioare conjugate

### Avansat

- **Unghi de presiune** - Unghiul suprafeței de contact a dintelui (valori uzuale: 14.5, 20 sau 25 grade). Toate roțile dințate care angrenează trebuie să folosească același unghi de presiune.
- **Joc** - Distanța minimă dintre vârful dintelui și golul dintelui conjugat
- **Joc mecanic** - Distanța minimă dintre dinții roților dințate aflate în angrenare, pentru a preveni blocarea

### Date roată dințată (doar citire)

- **Rază de divizare** - Raza la care roțile dințate angrenează între ele
- **Diametru exterior** - Diametrul total, până la vârful dinților

## Sfaturi

- Două roți dințate vor angrena corect atunci când au același Pas circular și același Unghi de presiune
- Folosiți valorile Rază de divizare pentru a distanța corect roțile dințate aflate în angrenare -- distanța dintre centrele roților dințate trebuie să fie egală cu suma razelor lor de divizare
- Adăugați Joc mecanic pentru roțile dințate imprimate 3D, pentru a compensa toleranțele de imprimare
- Pentru profiluri de roți dințate 2D (pentru utilizare cu Extrudare), consultați [Roată dințată 2D](gear-2d.md)

## Articole conexe

- [Roată dințată 2D](gear-2d.md) - Traseu 2D de roată dințată pentru operații pe trasee
- [Filete](threads.md) - Creați caracteristici filetate
