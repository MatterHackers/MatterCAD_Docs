---
title: Odečíst a nahradit
articleKey: SubtractAndReplaceObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c1698bab75faca8046b23cc148803c8063ba0678
source_lang: en
---
# Odečíst a nahradit

Odečíst a nahradit odečte vámi zvolené díly od dílů, které jste nezvolili, ale odříznutou část zachová jako samostatný díl místo toho, aby ji zahodila. Pomocí **Díly k odečtení** vyberte řezací tvary; vše ostatní je základ, do kterého se řeže.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->
![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)

[Sloučit](combine.md), [Odečíst](subtract.md), [Průnik](intersect.md) i Odečíst a nahradit provádí jeden booleovský objekt -- tlačítko na panelu nástrojů jej vytvoří s již vybranou operací Odečíst a nahradit a kdykoli můžete přepnout na kteroukoli ze zbývajících tří pomocí řádku ikon **Operace** v horní části panelu Vlastnosti.

Odečíst a nahradit není u 2D drah k dispozici -- oblast nemá žádný odebraný objem, který by bylo možné vrátit.

## Jak používat

1. Vyberte dva nebo více objektů
2. Klikněte na **Odečíst a nahradit** na panelu nástrojů
3. Pomocí **Díly k odečtení** zvolte, které podřízené objekty jsou řezací tvary
4. Kdykoli si to můžete rozmyslet kliknutím na jinou ikonu v řádku **Operace** v horní části panelu Vlastnosti -- tvar se přestaví s novou operací

## Parametry

- **Operace** - Která booleovská operace se provede. Zobrazena jako řádek ikon v horní části panelu
- **Díly k odečtení** - Které podřízené objekty jsou řezací tvary
- **Ponechat obrácenou geometrii** - Považovat obrácený plášť za plný materiál místo toho, aby rušil objem kolem sebe. Zapněte tuto volbu, když se model, který má být plný, vrátí s chybějícími částmi. Vynutí pomalejší, ale přesný booleovský engine
- **Opravit orientaci ploch** - Před spuštěním booleovské operace přeorientovat obrácené pláště každého dílu. Tím se geometrie opraví jednou provždy, místo aby se měnilo, co všechny následující operace považují za plný materiál, a obvykle jde o lepší ze dvou řešení obráceného modelu

## Tipy

- Oba díly do sebe přesně zapadají, protože vznikly stejnou operací
- Použijte to pro vícebarevné návrhy, do sebe zapadající sestavy a vsazované prvky
- Pokud výsledek vypadá špatně, zkontrolujte, zda jsou zdrojové objekty vodotěsné. **Opravit orientaci ploch** opraví obrácené pláště; [Opravit](../mesh/repair.md) opraví rozsáhlejší poškození importovaných modelů

## Související

- [Sloučit](combine.md) - Sloučí více objektů do jediného plného tvaru
- [Odečíst](subtract.md) - Vyřízne jeden tvar z druhého
- [Průnik](intersect.md) - Zachová pouze objem, kde se objekty překrývají
- [Řez rovinou](../reshape/plane-cut.md) - Řez plochou rovinou místo jiným tvarem
- [Opravit](../mesh/repair.md) - Opraví poškozené importované sítě před booleovskou operací

Tato stránka se týká i starších objektů Odečíst a nahradit, které se stále vyskytují v návrzích uložených před sloučením operací. Fungují přesně tak jako dříve; nové návrhy používají sdílený booleovský objekt s vybranou operací Odečíst a nahradit.
