---
title: Încadrare în limite
articleKey: FitToBoundsObject3D_4
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: 91b9c917cb636f28403c291a4d56f22bf6758b70
source_lang: en
---
# Încadrare în limite

Încadrare în limite scalează un obiect astfel încât să se încadreze în dimensiunile specificate de lățime, adâncime și înălțime. Puteți controla modul în care obiectul se întinde și se aliniază în interiorul limitelor țintă.

<!--  Screenshot showing an object being fit to specific bounding dimensions -->
![20260506 154930 paste 20260506 154930](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154930-paste-20260506-154930.jpg)

## Mod de utilizare

1. Selectați un obiect
2. Aplicați operația **Încadrare în limite** din meniul Amplasare
3. Introduceți dimensiunile țintă
4. Alegeți blocarea proporțiilor și comportamentul de întindere

## Parametri

- **Blochează proporția** - Modul de constrângere a proporțiilor:
  - **Niciunul** - Fiecare axă poate fi setată independent
  - **X și Y** - Lățimea și adâncimea sunt blocate împreună
  - **X, Y și Z** - Scalare uniformă pe toate axele
- **Lățime** - Lățimea țintă (dimensiunea X)
- **Adâncime** - Adâncimea țintă (dimensiunea Y)
- **Înălțime** - Înălțimea țintă (dimensiunea Z)

### Când Blochează proporția este X și Y sau X, Y și Z

- **Întindere** - Modul în care se încadrează obiectul:
  - **Interior** - Scalare în jos pentru a se încadra complet în limite (pot rămâne spații libere)
  - **Extinde** - Scalare în sus pentru a umple limitele (poate depăși pe unele dimensiuni)

### Când Blochează proporția este Niciunul

Fiecare axă are propriile setări:

- **Întindere** - Interior sau Extinde pentru fiecare axă
- **Aliniere** - Unde se poziționează în interiorul limitelor (Min, Centru, Max)

## Sfaturi

- Folosiți această operație pentru a redimensiona modelele importate la dimensiuni țintă exacte
- Blocați toate proporțiile pentru o scalare uniformă care păstrează forma originală
- Folosiți controlul pe fiecare axă atunci când trebuie să respectați o anumită lățime, dar celelalte dimensiuni nu contează

## Similare

- [Scalare](../transform/scale.md) - Scalare după raport sau procent în loc de dimensiune țintă
- [Potrivire pe cilindru](fit-to-cylinder.md) - Încadrarea într-o limită cilindrică
- [Aliniere](align.md) - Poziționarea obiectelor unele față de altele
