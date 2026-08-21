---
title: Sloučit
articleKey: CombineObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: a3066faa634b5a88a2fe1650a4e2ac278ac50e24
source_lang: en
---
# Sloučit

Sloučit spojí vše do jediného tělesa. Vnitřní plochy v místech, kde se tvary překrývaly, jsou odebrány, takže výsledkem je jedna souvislá síť namísto překrývajících se skořepin.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->
![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)

Operace Sloučit, [Odečíst](subtract.md), [Průnik](intersect.md) a [Odečíst a nahradit](subtract-and-replace.md) provádí jeden booleovský objekt -- tlačítko na panelu nástrojů jej vytvoří s již vybranou operací Sloučit a kdykoli můžete přepnout na kteroukoli ze zbývajících tří v řádku ikon **Operace** v horní části panelu Vlastnosti.

Sloučit funguje na tělesech i na 2D drahách. Podívá se na to, co jste mu zadali, a provede odpovídající typ operace, takže sloučením dvou drah vznikne jedna dráha a sloučením dvou sítí vznikne jedno těleso.

## Jak používat

1. Vyberte dva nebo více objektů
2. Klikněte na **Sloučit** na panelu nástrojů
3. Kdykoli si to můžete rozmyslet kliknutím na jinou ikonu v řádku **Operace** v horní části panelu Vlastnosti -- tvar se přestaví podle nové operace

## Parametry

- **Operace** – Která booleovská operace se má provést. Zobrazuje se jako řádek ikon v horní části panelu
- **Ponechat obrácenou geometrii** – Považovat obrácenou skořepinu za plný materiál místo toho, aby odečetla objem kolem sebe. Zapněte tuto volbu, pokud se u modelu, který má být plný, objeví chybějící části. Vynutí pomalejší, ale přesné booleovské jádro
- **Opravit orientaci ploch** – Před spuštěním booleovské operace přeorientuje obrácené skořepiny každé části. Tím se geometrie opraví jednou provždy, místo aby se měnilo, co všechny následující operace považují za plný materiál; obvykle jde o lepší z obou řešení obráceného modelu

## Tipy

- Sloučit spojí do jedné sítě i objekty, které se nepřekrývají, ale ty zůstanou vizuálně oddělené
- Sloučit se za vás postará o objekty Otvor: cokoli je označeno jako otvor, se od výsledku odečte, místo aby se k němu přidalo
- Sloučit přenáší barvy jednotlivých ploch z původních objektů
- Pokud výsledek vypadá špatně, zkontrolujte, zda jsou zdrojové objekty uzavřené. **Opravit orientaci ploch** opraví obrácené skořepiny; [Opravit](../mesh/repair.md) řeší rozsáhlejší poškození importovaných modelů

## Související

- [Odečíst](subtract.md) – Vyjme jeden tvar z druhého
- [Průnik](intersect.md) – Zachová pouze objem, kde se objekty překrývají
- [Odečíst a nahradit](subtract-and-replace.md) – Odečte jeden tvar a zachová odebranou část
- [Řez rovinou](../reshape/plane-cut.md) – Řez plochou rovinou místo jiným tvarem
- [Otvor](../../primitives/hole.md) – Krychle přednastavená k odečtení
- [Opravit](../mesh/repair.md) – Oprava poškozených importovaných sítí před booleovskou operací

Tato stránka se týká i starších objektů Sloučit, které se stále vyskytují v návrzích uložených před sloučením operací. Fungují přesně jako dříve; nové návrhy používají společný booleovský objekt s vybranou operací Sloučit.
