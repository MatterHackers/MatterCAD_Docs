---
title: Měřítko
articleKey: ScaleObject3D_3
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b3b5419c3db29550b2544bb6aca91ca3ce6fa715
source_lang: en
---
# Měřítko

Měřítko změní velikost objektu s přesnou kontrolou nad rozměry, proporcemi a převodem jednotek. Můžete měnit velikost rovnoměrně, zamknout určité osy k sobě, nebo měnit velikost každé osy nezávisle.

<!--  Screenshot showing the Scale operation properties with dimension fields and lock proportion options -->
![20260506 160759 paste 20260506 160759](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160759-paste-20260506-160759.jpg)

## Jak používat

1. Vyberte objekt
2. Použijte operaci **Měřítko** z nabídky Transformace
3. Zvolte způsob změny velikosti a zadejte požadované hodnoty

Můžete také měnit velikost objektů přímo ve výřezu kliknutím a tažením za rohové ovládací prvky měřítka na vybraném objektu.

## Parametry

### Typ měřítka

Zvolte předvolbu nebo vlastní změnu velikosti:

- **Vlastní** – Zadejte vlastní rozměry nebo procenta
- **Palce na mm** – Vynásobí 25,4 (převod imperiálních jednotek na metrické)
- **mm na palce** – Vynásobí 0,0393 (převod metrických jednotek na imperiální)
- **mm na cm** – Vynásobí 0,1
- **cm na mm** – Vynásobí 10

### Metoda změny velikosti (režim Vlastní)

- **Přímý** – Zadejte požadovanou Šířku, Hloubku a Výšku v milimetrech
- **Procenta** – Zadejte Šířku, Hloubku a Výšku jako procenta původní velikosti

### Zamknout proporce

- **Žádný (Volné měřítko)** – Každá osa se mění nezávisle
- **X a Y** – Šířka a Hloubka jsou zamknuty k sobě; Výška se mění nezávisle
- **X, Y a Z** – Všechny tři osy se mění rovnoměrně společně

### Rozměry

- **Šířka** – Velikost podél osy X
- **Hloubka** – Velikost podél osy Y
- **Výška** – Velikost podél osy Z

## Tipy

- Použijte „Palce na mm“, pokud jste importovali soubor STL navržený v palcích a jeví se příliš malý
- Nastavte Zamknout proporce na X, Y a Z pro rovnoměrnou změnu velikosti – změna kteréhokoli rozměru aktualizuje všechny
- Poloha základny objektu je při změně velikosti zachována, takže objekt zůstává na povrchu pracovní plochy
- Můžete zadat přesné hodnoty pro precizní rozměry, nebo použít posuvníky pro rychlé úpravy

## Související

- [Posunout](translate.md) – Přesunout objekt
- [Otočit](rotate.md) – Otočit objekt
- [Přizpůsobit hranicím](../placement/fit-to-bounds.md) – Změnit velikost tak, aby se objekt vešel do zadaných rozměrů
