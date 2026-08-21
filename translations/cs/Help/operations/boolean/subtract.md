---
title: Odečíst
articleKey: SubtractObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 59685bd0a635b70d7f938780f71e90be595dd993
source_lang: en
---
# Odečíst

Odečíst vyřízne díly, které vyberete, z dílů, které jste nevybrali. Pomocí **Díly k odečtení** zvolte řezné tvary; vše ostatní tvoří základ, do kterého se řeže.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->
![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)

[Sloučit](combine.md), Odečíst, [Průnik](intersect.md) a [Odečíst a nahradit](subtract-and-replace.md) provádí jeden a tentýž booleovský objekt -- tlačítko na panelu nástrojů jej vytvoří s již zvolenou operací Odečíst a kdykoli můžete přepnout na kteroukoli ze zbývajících tří pomocí řady ikon **Operace** v horní části panelu Vlastnosti.

Odečíst funguje na tělesech i na 2D drahách. Podívá se na to, co jste mu předali, a provede odpovídající druh operace, takže odečtení jedné dráhy od druhé vytvoří dráhu a odečtení jedné sítě od druhé vytvoří těleso.

## Použití

1. Vyberte dva nebo více objektů
2. Klikněte na **Odečíst** na panelu nástrojů -- výchozí díl k odříznutí se zvolí za vás, takže operace hned něco udělá
3. Pomocí **Díly k odečtení** zvolte, které podřízené objekty jsou řezné tvary
4. Své rozhodnutí můžete kdykoli změnit kliknutím na jinou ikonu v řadě **Operace** v horní části panelu Vlastnosti -- tvar se přestaví podle nové operace

## Parametry

- **Operace** - Která booleovská operace se provede. Zobrazuje se jako řada ikon v horní části panelu
- **Díly k odečtení** - Které podřízené objekty jsou řezné tvary
- **Ponechat odečtené díly** - Ponechá odříznuté díly ve scéně namísto jejich zahození
- **Ponechat obrácenou geometrii** - Považuje obrácený plášť za plný materiál místo toho, aby rušil objem kolem sebe. Zapněte tuto volbu, když se model, který má být plný, vrátí s chybějícími částmi. Vynutí pomalejší, ale přesné booleovské jádro
- **Opravit orientaci ploch** - Před spuštěním booleovské operace přeorientuje obrácené pláště každého dílu. Tím se geometrie opraví jednou provždy, místo aby se měnilo, co každá další operace považuje za plné, a obvykle je to lepší z obou řešení obráceného modelu

## Tipy

- Aby Odečíst něco udělalo, musí se objekty překrývat
- Chcete-li vyříznout průchozí otvor, ujistěte se, že řezný objekt prochází základem úplně skrz
- Pro jednoduchý otvor je primitivum [Otvor](../../primitives/hole.md) již nastaveno na odečítání
- Řezné objekty zůstávají ve stromu návrhu, takže s nimi můžete pohybovat nebo měnit jejich velikost a řez se aktualizuje
- Pokud výsledek vypadá špatně, zkontrolujte, zda jsou zdrojové objekty vodotěsné. **Opravit orientaci ploch** opraví obrácené pláště; [Opravit](../mesh/repair.md) opraví rozsáhlejší poškození u importovaných modelů

## Související

- [Sloučit](combine.md) - Spojí více objektů do jednoho plného tvaru
- [Průnik](intersect.md) - Ponechá pouze objem, kde se objekty překrývají
- [Odečíst a nahradit](subtract-and-replace.md) - Odečte jeden tvar a ponechá odříznutý kus
- [Řez rovinou](../reshape/plane-cut.md) - Řeže plochou rovinou místo jiného tvaru
- [Otvor](../../primitives/hole.md) - Krychle přednastavená k odečítání
- [Opravit](../mesh/repair.md) - Opraví poškozené importované sítě před booleovskou operací

Tato stránka se týká i starších objektů Odečíst, které se stále vyskytují v návrzích uložených před sloučením operací. Fungují přesně jako dříve; nové návrhy používají společný booleovský objekt se zvolenou operací Odečíst.
