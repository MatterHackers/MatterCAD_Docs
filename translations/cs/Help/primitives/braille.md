---
title: Braillovo písmo
articleKey: BrailleObject3D
parent: "Primitives"
nav_order: 2
source_hash: d1d9d4aeb9b87efbe32045f2a96cfea49048f95f
source_lang: en
---
# Braillovo písmo

Generujte 3D tisknutelný text v Braillově písmu ze standardního anglického textu. Nástroj Braillovo písmo podporuje kódování Braillova písma stupně 1 (písmeno po písmenu) i stupně 2 (zkratkopis).

<!-- Screenshot of a Braille object showing raised dots on the workspace -->
![20260318 182800 paste 20260318 182800](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-182800-paste-20260318-182800.jpg)


## Jak nástroj používat

1. Přidejte základní těleso **Braillovo písmo** z panelu Základní tělesa
2. Do pole **Text ke kódování** napište svůj text
3. Nástroj jej automaticky převede na správný bodový vzor Braillova písma

## Parametry

- **Text ke kódování** – Anglický text, který se má převést do Braillova písma
- **Měřítko** – Upravuje celkovou velikost výstupu v Braillově písmu
- **Výška** – Výška vystouplých bodů Braillova písma

## Tipy

- Braillovo písmo stupně 2 používá pro běžná slova a kombinace písmen zkratky, díky čemuž je kompaktnější
- Používají se standardní rozměry braillské buňky, aby byl výstup čitelný
- Sloučit s plochou základnou [Kvádr](cube.md) a vytvořit tak kompletní štítek nebo ceduli v Braillově písmu
- Pro braillské karty s integrovanou základnou viz [Braillova karta](braille-card.md)

## Související

- [Braillova karta](braille-card.md) – Braillovo písmo s integrovanou základnou karty
- [Text](text.md) – Standardní 3D text
