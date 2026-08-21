---
title: Strângere radială
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: 95ef5847767e5cfcdbae9df9aaa1cb1727da2f5e
source_lang: en
---
# Strângere radială

Strângere radială comprimă un obiect spre interior pornind de la un punct central, folosind o curbă de profil personalizabilă. Spre deosebire de [Strângere](pinch.md) obișnuită, care acționează dinspre spate spre față, Strângere radială comprimă simetric în jurul unei axe centrale.

<!--  Before and after showing an object with radial pinch applied, creating a waisted shape -->
![20260506 155741 paste 20260506 155741](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155741-paste-20260506-155741.jpg)

## Mod de utilizare

1. Selectați un obiect
2. Aplicați operațiunea **Strângere radială** din meniul Remodelează
3. Editați profilul căii pentru a defini cât de multă strângere se aplică la fiecare înălțime
4. Ajustați numărul de felii pentru netezime

## Parametri

- **Cale** - Un editor de curbă de profil care definește valoarea strângerii la fiecare nivel de înălțime. Editați curba pentru a crea profiluri de strângere personalizate
- **Felii** - Numărul de tăieturi orizontale pentru o strângere lină, distribuite uniform pe înălțimea piesei. Mai multe felii = rezultate mai netede

### Parametri avansați

- **Tip de strângere** - Direcția de comprimare:
  - **Radial** - Comprimă în mod egal din toate părțile spre centru
  - **Axa X** - Comprimă doar de-a lungul axei X
  - **Axa Y** - Comprimă doar de-a lungul axei Y
- **Decalaj rotație** - Deplasează centrul efectului de strângere

## Sfaturi

- Folosiți editorul de cale pentru a crea forme de clepsidră, sticlă sau vază
- Strângerea radială este ideală pentru a crea forme organice, rotunjite, din obiecte cilindrice
- Măriți valoarea Felii pentru curbe mai netede, în special la profiluri de strângere pronunțate

## Asociate

- [Strângere](pinch.md) - Comprimare simplă dinspre spate spre față
- [Răsucire](twist.md) - Rotație în spirală pe înălțime
- [Curbă](curve.md) - Îndoire sub formă de arc
