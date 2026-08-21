---
title: Průnik
articleKey: IntersectionObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b997cfc4f6d2f02559346365311f217388a6a2da
source_lang: en
---
# Průnik

Průnik ponechá pouze objem, který sdílejí všechny objekty, a zbytek zahodí.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->
![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)

[Sloučit](combine.md), [Odečíst](subtract.md), Průnik a [Odečíst a nahradit](subtract-and-replace.md) provádí jeden a tentýž booleovský objekt – tlačítko na panelu nástrojů jej vytvoří s již vybranou operací Průnik a kdykoli můžete přepnout na kteroukoli ze zbývajících tří pomocí řádku ikon **Operace** v horní části panelu Vlastnosti.

Průnik funguje na tělesech i na 2D drahách. Rozpozná, co jste mu zadali, a provede odpovídající typ operace, takže průnik dvou drah vytvoří jednu dráhu a průnik dvou sítí vytvoří jedno těleso.

## Jak jej použít

1. Vyberte dva nebo více objektů
2. Klikněte na **Průnik** na panelu nástrojů
3. Kdykoli si to můžete rozmyslet a kliknout na jinou ikonu v řádku **Operace** v horní části panelu Vlastnosti – tvar se přestaví podle nové operace

## Parametry

- **Operace** – Která booleovská operace se má provést. Zobrazeno jako řádek ikon v horní části panelu
- **Ponechat obrácenou geometrii** – Obrácenou skořepinu bere jako plný materiál, místo aby jí nechal odečíst okolní objem. Zapněte tuto volbu, když se model, který má být plný, vrátí s chybějícími částmi. Vynutí pomalejší, ale přesné booleovské jádro
- **Opravit orientaci ploch** – Před spuštěním booleovské operace přeorientuje obrácené skořepiny každé části. Tím se geometrie opraví jednou provždy, místo aby se měnilo, co všechny následující operace považují za plný materiál, a obvykle je to lepší z obou řešení obráceného modelu

## Tipy

- Objekty se musí překrývat. Pokud se ve skutečnosti nepřekrývají, výsledek je prázdný
- U více než dvou objektů se postupuje po seznamu: nejprve se vytvoří průnik prvních dvou, ten se pak protne se třetím a tak dále
- Pokud výsledek vypadá špatně, zkontrolujte, zda jsou zdrojové objekty vodotěsné. **Opravit orientaci ploch** opraví obrácené skořepiny; [Opravit](../mesh/repair.md) odstraní rozsáhlejší poškození importovaných modelů

## Související

- [Sloučit](combine.md) – Sloučí více objektů do jediného tělesa
- [Odečíst](subtract.md) – Vyřízne jeden tvar z druhého
- [Odečíst a nahradit](subtract-and-replace.md) – Odečte jeden tvar a zachová odříznutou část
- [Řez rovinou](../reshape/plane-cut.md) – Řeže rovinou místo jiného tvaru
- [Opravit](../mesh/repair.md) – Opraví poškozené importované sítě před booleovskou operací

Tato stránka se týká i starších objektů Průsečík, které se stále vyskytují v návrzích uložených před sloučením operací. Fungují přesně jako dříve; nové návrhy používají společný booleovský objekt s vybranou operací Průnik.
