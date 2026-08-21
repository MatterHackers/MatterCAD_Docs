---
title: Radiální stažení
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: 95ef5847767e5cfcdbae9df9aaa1cb1727da2f5e
source_lang: en
---
# Radiální stažení

Radiální stažení stlačuje objekt směrem dovnitř od středového bodu podle upravitelné profilové křivky. Na rozdíl od běžného [Zaškrcení](pinch.md), které působí zezadu dopředu, Radiální stažení stlačuje objekt symetricky kolem středové osy.

<!--  Before and after showing an object with radial pinch applied, creating a waisted shape -->
![20260506 155741 paste 20260506 155741](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155741-paste-20260506-155741.jpg)

## Jak jej použít

1. Vyberte objekt
2. Použijte operaci **Radiální stažení** z nabídky Přetvarovat
3. Upravte profil cesty a určete, jak velké stažení se použije v jednotlivých výškách
4. Nastavte počet řezů pro dosažení hladkého výsledku

## Parametry

- **Cesta** – Editor profilové křivky, který určuje míru stažení v každé výškové úrovni. Úpravou křivky vytvoříte vlastní profily stažení
- **Řezy** – Počet vodorovných řezů pro plynulé stažení, rovnoměrně rozmístěných po výšce dílu. Více řezů = hladší výsledek

### Rozšířené parametry

- **Typ zaškrcení** – Směr stlačení:
  - **Radiální** – Stlačení rovnoměrně ze všech stran ke středu
  - **Osa X** – Stlačení pouze podél osy X
  - **Osa Y** – Stlačení pouze podél osy Y
- **Odsazení rotace** – Posun středu efektu stažení

## Tipy

- Pomocí editoru cesty vytvoříte tvary připomínající přesýpací hodiny, láhev nebo vázu
- Radiální stažení je ideální pro vytváření organických, zaoblených tvarů z válcových objektů
- Zvyšte hodnotu Řezy pro hladší křivky, zejména u výrazných profilů stažení

## Související

- [Zaškrcení](pinch.md) – Jednoduché stlačení zezadu dopředu
- [Zkroucení](twist.md) – Spirálová rotace po výšce
- [Křivka](curve.md) – Ohnutí do oblouku
