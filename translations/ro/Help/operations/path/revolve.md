---
title: Revoluție
articleKey: RevolveObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: a63ebb08d982178e0e59f0b9f07c3c0dca53148b
source_lang: en
---
# Revoluție

**Revoluție** rotește o cale 2D în jurul unei axe pentru a crea un solid de revoluție 3D. Astfel creezi vaze, boluri, roți și alte obiecte cu simetrie de rotație.

<!--  Before and after showing a profile path being revolved into a vase shape -->
![20260506 102004 paste 20260506 102004](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-102004-paste-20260506-102004.jpg)


## Mod de utilizare

1. Selectează o cale 2D
2. Aplică **Revoluție** din meniul de operații **Cale**
3. Ajustează intervalul de rotație, poziția axei și numărul de laturi

## Parametri

- **Rotație** - Unghiul total de rotație pentru revoluție (implicit: 0, interval: 0-360). Setează 360 pentru o revoluție completă.
- **Poziție axă** - Decalajul axei de rotație față de centrul căii (implicit: 0, interval: -30 până la 30). Valorile pozitive îndepărtează axa de cale, creând o deschidere mai mare.
- **Unghi inițial** - Locul unde începe revoluția (implicit: 0)
- **Unghi final** - Locul unde se termină revoluția (implicit: 45). Setează 360 pentru o revoluție completă.
- **Laturi** - Numărul de segmente de-a lungul revoluției (implicit: 30). Mai multe = suprafață mai netedă.

## Sfaturi

- Folosește **Poziție axă** pentru a controla diametrul interior al formei obținute prin revoluție
- Setează **Unghi inițial** și **Unghi final** la mai puțin de 360 pentru a crea revoluții parțiale (arcade, jgheaburi)
- Desenează o cale de profil pentru forma vazei sau a bolului, apoi aplică revoluția pentru o simetrie perfectă
- O [Cale Cerc](../../2d-paths/circle-path.md) supusă revoluției creează un tor

## Similare

- [Extrudare liniară](linear-extrude.md) - Extrudează drept în sus în loc de revoluție
- [Căi 2D](../../2d-paths/index.md) - Creează căi de profil pentru revoluție
- [Tor](../../primitives/torus.md) - O formă inelară gata făcută, obținută prin revoluție
