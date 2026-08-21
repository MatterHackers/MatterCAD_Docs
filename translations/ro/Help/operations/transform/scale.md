---
title: Scalare
articleKey: ScaleObject3D_3
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b3b5419c3db29550b2544bb6aca91ca3ce6fa715
source_lang: en
---
# Scalare

Scalarea redimensionează un obiect cu control precis asupra dimensiunilor, proporțiilor și conversiei unităților. Puteți scala uniform, puteți bloca împreună anumite axe sau puteți redimensiona fiecare axă independent.

<!--  Screenshot showing the Scale operation properties with dimension fields and lock proportion options -->
![20260506 160759 paste 20260506 160759](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160759-paste-20260506-160759.jpg)

## Mod de utilizare

1. Selectați un obiect
2. Aplicați operația **Scalare** din meniul Transformare
3. Alegeți metoda de scalare și introduceți valorile dorite

De asemenea, puteți scala obiectele în fereastra de vizualizare făcând clic și trăgând de controalele de scalare din colțurile unui obiect selectat.

## Parametri

### Tip de scalare

Alegeți o presetare sau o scalare personalizată:

- **Personalizat** - Introduceți propriile dimensiuni sau procente
- **Țoli în mm** - Înmulțire cu 25,4 (conversie din sistemul imperial în cel metric)
- **mm în inch** - Înmulțire cu 0,0393 (conversie din sistemul metric în cel imperial)
- **mm în cm** - Înmulțire cu 0,1
- **cm în mm** - Înmulțire cu 10

### Metodă de scalare (modul Personalizat)

- **Direct** - Introduceți Lățimea, Adâncimea și Înălțimea dorite în milimetri
- **Procentaj** - Introduceți Lățimea, Adâncimea și Înălțimea ca procente din dimensiunea originală

### Blochează proporția

- **Niciunul (Scalare liberă)** - Fiecare axă se scalează independent
- **X și Y** - Lățimea și Adâncimea sunt blocate împreună; Înălțimea se scalează independent
- **X, Y și Z** - Toate cele trei axe se scalează uniform, împreună

### Dimensiuni

- **Lățime** - Dimensiunea pe axa X
- **Adâncime** - Dimensiunea pe axa Y
- **Înălțime** - Dimensiunea pe axa Z

## Sfaturi

- Folosiți „Țoli în mm” dacă ați importat un fișier STL proiectat în țoli și care apare prea mic
- Setați Blochează proporția pe X, Y și Z pentru o scalare uniformă -- modificarea oricărei dimensiuni le actualizează pe toate
- Poziția bazei obiectului este menținută în timpul scalării, astfel încât acesta rămâne pe suprafața spațiului de lucru
- Puteți introduce valori exacte pentru o dimensionare precisă sau puteți folosi glisoarele pentru ajustări rapide

## Articole conexe

- [Translatare](translate.md) - Mută un obiect
- [Rotire](rotate.md) - Rotește un obiect
- [Încadrare în limite](../placement/fit-to-bounds.md) - Scalare pentru a se încadra într-o dimensiune anume
