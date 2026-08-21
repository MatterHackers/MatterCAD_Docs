---
title: Pole
articleKey: ArrayObject3D_2
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c547fa24e5f47e0d60f0cec0eac979700d946daf
source_lang: en
---
# Pole

Pole vytváří několik kopií objektu uspořádaných do vzoru. Vyberte režim pomocí tlačítek nahoře — **Lineární**, **Radiální** nebo **Transformace** — pro přepnutí mezi typy vzorů.

<!--  Screenshot of the Array operation panel showing the mode buttons at the top (Linear | Radial | Transform) -->
![20260506 080647 paste 20260506 080647](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080647-paste-20260506-080647.jpg)


## Použití

1. Vyberte objekt
2. Použijte operaci **Pole** z nabídky Duplikace
3. Zvolte režim (Lineární, Radiální nebo Transformace)
4. Upravte parametry zvoleného režimu

## Režim: Lineární

Lineární režim umísťuje kopie podél směru s volitelnou progresí rotace a měřítka.

**Počet** — Počet kopií (celé číslo nebo výraz). Zdrojový objekt je první kopie; další kopie jsou od něj odsazeny.

**Metoda odsazení** — Jak se počítají rozestupy:
- **Relativní** — Odsazení se násobí velikostí ohraničujícího kvádru objektu. Relativní odsazení (1, 0, 0) rozmístí kopie přesně o jednu šířku objektu od sebe podél osy X.
- **Odsazení** — Pevná vzdálenost ve světovém prostoru v mm na kopii.
- **Koncový bod** — Nastavte pozici poslední kopie; rozestupy se rovnoměrně rozdělí mezi kopie.

**Relativní odsazení** / **Odsazení** / **Koncový bod** — Vektor rozestupu podle zvolené Metody odsazení.

**Režim rotace** — Jak se rotace sčítá napříč kopiemi:
- **Lokální** — Každá kopie se otáčí na místě kolem vlastního středu; směr odsazení zůstává ve světových osách.
- **Skládání** — Rotace se sčítá a řídí odsazení, čímž vznikají spirály, vějíře a šroubovice.

**Rotace** — Rotace na kopii ve stupních pro každou osu.

**Měřítko** — Kumulativní měřítko na kopii pro každou osu. Hodnoty menší než 1 kopie zmenšují, hodnoty větší než 1 je zvětšují.

**Měřítko ovlivňuje offset** — Když je zapnuto, mění se s každým krokem i rozestup mezi kopiemi. Použijte to pro utahující se spirály a geometrické progrese (lastury loděnky, skládané křivky typu nail-shell).

## Režim: Radiální

Radiální režim rozmisťuje kopie rovnoměrně kolem středové osy v pevném poloměru.

<!--  Screenshot of Array in Radial mode showing 6 copies arranged in a circle, with Radius and Central Axis parameters visible -->
![20260506 092618 paste 20260506 092618](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-092618-paste-20260506-092618.jpg)


**Metoda počítání** — Jak se určuje počet kopií:
- **Počet** — Explicitní počet kopií.
- **Vzdálenost** — Úhlová mezera mezi kopiemi ve stupních; počet se vypočítá tak, aby vyplnil tažení.

**Počet** / **Úhlová vzdálenost** — Počet kopií (režim Počet) nebo úhlový rozestup ve stupních (režim Vzdálenost). Podporuje výrazy.

**Středová osa** — Osa, kolem které se rotuje (výchozí: Z).

**Kruhový segment** — Zda kopie zaplní celý kruh 360° (**Plné**), nebo jen část oblouku (**Oblouk**).

**Poloměr** — Vzdálenost od středové osy ke každé kopii.

**Úhel tažení** — Počet stupňů oblouku, který se má vyplnit (zobrazí se, když je Kruhový segment nastaven na Oblouk). Podporuje výrazy.

**Zarovnat rotaci** — Otočí každou kopii tak, aby její osa dopředu směřovala ven od středu.

**Osa dopředu** — Která osa kopie se pro zarovnání považuje za „dopředu" (zobrazí se, když je zapnuto Zarovnat rotaci).

## Režim: Transformace

Režim Transformace krokuje kopie pomocí ruční transformace nebo podle transformace jiného objektu.

**Počet** — Počet kopií (celé číslo nebo výraz).

**Reference transformace** — Odkud pochází transformace jednoho kroku:
- **Vstup** — Posunutí, rotaci a měřítko zadáváte přímo.
- **Objekt** — Transformace se načte z pojmenovaného sourozeneckého objektu.

**Posunutí** — Odsazení ve světovém prostoru na krok v mm (zobrazí se, když je Reference nastavena na Vstup).

**Rotace** — Rotace na krok ve stupních pro každou osu (zobrazí se, když je Reference nastavena na Vstup).

**Měřítko** / **Osy měřítka** — Rovnoměrné měřítko a měřítko po osách použité v každém kroku (zobrazí se, když je Reference nastavena na Vstup).

**Název transformace** — Název sourozeneckého objektu, jehož transformace se použije jako přírůstek na krok (zobrazí se, když je Reference nastavena na Objekt).

**Relativní prostor** — Když je zapnuto, transformace každé kopie se skládá v lokálním rámci předchozí kopie; když je vypnuto, každý krok se aplikuje ve světovém prostoru (zobrazí se, když je Reference nastavena na Objekt).

## Randomizovat

Zapněte **Randomizovat** pro přidání variace do všech kopií.

- **Náhodné odsazení** — Maximální náhodné odsazení pozice na osu v mm.
- **Náhodná rotace** — Maximální náhodná rotace na osu ve stupních.
- **Osy náhodného měřítka** — Maximální náhodná variace měřítka na osu.
- **Vynechat první** — Ponechá první kopii na přesně vypočtené pozici (výchozí: zapnuto).
- **Vynechat poslední** — Ponechá poslední kopii na přesně vypočtené pozici.
- **Náhodné semínko** — Změnou získáte jiné náhodné uspořádání. Podporuje výrazy.

## Sloučit

- **Vytvořit jednu síť** — Sloučí všechny kopie do jednoho spojeného objektu sítě.
- **Sloučit vrcholy** — Svaří vrcholy v rámci prahové vzdálenosti sloučení (zobrazí se, když je zapnuto Vytvořit jednu síť).
- **Vzdálenost** — Práh sloučení v mm (zobrazí se, když je zapnuto Sloučit vrcholy).

## Tipy

- Pro vytvoření parametrických vzorů použijte výrazy u Počtu, Rotace nebo Koncového bodu
- Pro kruhové vzory použijte režim Radiální — nastavte Poloměr pro řízení velikosti kruhu a zapněte Zarovnat rotaci, pokud mají kopie směřovat ven
- Skládání rotace v Lineárním režimu vytváří spirály a vějíře bez ručního výpočtu úhlových odsazení
- Měřítko ovlivňuje offset přirozeně vytváří rozvržení typu lastury loděnky a geometrické progrese
- Zkombinujte Pole s [Vybrat potomka](select-child.md) pro vytvoření vzorů, kde každá kopie zobrazuje jinou variantu

## Související

- [Zarovnat](../placement/align.md) - Umístění objektů vůči sobě navzájem
- [Vybrat potomka](select-child.md) - Výběr konkrétní kopie z pole podle indexu nebo názvu
