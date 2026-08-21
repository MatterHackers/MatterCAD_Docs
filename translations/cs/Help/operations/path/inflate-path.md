---
title: Nafouknout cestu
articleKey: InflatePathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: c0e11d3d24c5f832f797cde4d392e26a4694733d
source_lang: en
---
# Nafouknout cestu

Nafouknout cestu rozšíří 2D cestu směrem ven, čímž tvar zvětší při zachování jeho celkové podoby. Je to obdoba použití rovnoměrného odsazení na všechny hrany.

<!--  Before and after showing a path inflated outward -->
![20260506 100652 paste 20260506 100652](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100652-paste-20260506-100652.jpg)


## Jak postupovat

1. Vyberte 2D cestu
2. Použijte **Nafouknout cestu** z nabídky operací s cestou
3. Upravte míru nafouknutí

## Nafouknutí otevřené čáry

Nafouknutí je způsob, jak z čáry udělat tvar. Zrušte zaškrtnutí volby **Uzavřeno** u [Vlastní cesta](../../2d-paths/custom-path.md), nakreslete otevřenou čáru a poté ji nafoukněte: výsledkem je vyplněný pás, který je na obě strany od čáry tak široký, jakou hodnotu nastavíte. Odtud se vytahuje stejně jako kterákoli jiná cesta.

**Styl** určuje, jak jsou zakončeny oba konce čáry a jak jsou napojeny její rohy:

- **Plochý** ukončí pás rovně v každém koncovém bodě
- **Zaoblení** přidá za každý koncový bod půlkruh
- **Ostrý** přidá za každý koncový bod čtverec

Otevřená čára nemá vnitřek, do kterého by se mohla smrštit, takže nulová nebo záporná hodnota by nezanechala vůbec nic. Když je cesta *zcela* otevřená, Nafouknout omezí hodnotu na malé kladné číslo a toto omezené číslo zapíše zpět do pole, abyste viděli, co se stalo.

Cesta, která kombinuje otevřené a uzavřené obrysy, omezena není: uzavřené obrysy se smrští běžným způsobem a otevřené jednoduše vypadnou. Uzavřené cesty se při záporných hodnotách stále smršťují přesně tak jako dosud.

## Tipy

- Zápornými hodnotami cestu místo rozšíření zmenšíte směrem dovnitř
- Nafouknutí se hodí pro vytváření tolerančních odsazení kolem tvarů
- Zkombinujte s [Obrysová cesta](outline-path.md) pro vytváření okrajů s konkrétní šířkou

## Související

- [Obrysová cesta](outline-path.md) – Vytvoří obrys z cesty
- [Cesta okraje](border-path.md) – Přidá odsazení okraje
- [Vyhladit cestu](smooth-path.md) – Zaoblí rohy cesty
