---
title: Reducér
articleKey: DecimateObject3D
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 58a2573b968808e98203832142fa8bacf7a9cf99
source_lang: en
---
# Reducér (Decimering)

Reducér sænker polygonantallet i et mesh, samtidig med at den overordnede form bevares. Det er nyttigt til at forenkle meget detaljerede modeller, reducere filstørrelsen og fremskynde operationer på kompleks geometri.

![20260324 080430 paste 20260324 080430](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080430-paste-20260324-080430.jpg)


## Sådan bruges den

1. Vælg et objekt
2. Anvend operationen **Reducér** fra Mesh-menuen
3. Vælg dit mål (antal eller procentdel) og justér

## Parametre

- **Tilstand** - Vælg, hvordan målet angives:
  - **Procent** - Behold en procentdel af de oprindelige polygoner (standard: 50 %)
  - **Antal** - Sigt efter et bestemt polygonantal
- **Kildepolygonantal** - Oprindeligt antal polygoner (skrivebeskyttet)
- **Målprocent** - Procentdel af polygoner, der skal beholdes (synlig i tilstanden Procent)
- **Målantal** - Nøjagtigt antal polygoner, der skal beholdes (synlig i tilstanden Antal)
- **Antal efter procentreduktion** - Endeligt polygonantal efter procentreduktion (skrivebeskyttet)
- **Bevar overflade** - Projicér knudepunkter tilbage på den oprindelige overflade for højere nøjagtighed (langsommere, men mere tro mod den oprindelige form)

## Tips

- En reduktion på 50 % bevarer som regel den visuelle kvalitet godt
- Aktivér Bevar overflade, når nøjagtighed betyder mere end hastighed
- Et lavere polygonantal fremskynder booleske operationer på komplekse importerede modeller
- Meget lave polygonantal forringer formen synligt -- kontrollér resultatet, før du går videre

## Relateret

- [Reparer](repair.md) - Ret problemer i mesh
