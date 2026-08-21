---
title: Zarovnat
articleKey: AlignObject3D_3
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 1fadae72ba00cb06e36a21f0b96962dcff3f60ad
source_lang: en
---
# Zarovnat

Zarovnat přesně umístí více objektů vzhledem k ukotvenému objektu. Použijte jej k zarovnání hran, vystředění dílů na sobě, položení jednoho objektu na druhý nebo vytvoření rovnoměrně rozmístěných stohů.

<!--  Screenshot showing two objects being aligned with alignment options visible -->
![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)


## Postup použití

1. Vyberte dva nebo více objektů.
2. Použijte operaci **Zarovnat** z nabídky **Umístění**.
3. Zvolte objekt **Ukotvení**. Ukotvený objekt zůstane na místě a ostatní objekty se přesunou.
4. Nastavte zarovnání pro osy X, Y a Z nezávisle.
5. Až budete chtít zarovnané pozice zapsat do stromu objektů, použijte **Použít**.

## Parametry

### Ukotvení

Seznam **Ukotvení** vybírá podřízený objekt použitý jako referenci. Ukotvený objekt se nepohybuje. Každý další podřízený objekt v operaci Zarovnat je přemístěn vzhledem k ukotvení, pokud daná osa nepoužívá režim **Skládaný**.

### Ovládání os

Každá osa má vlastní ovládací prvky. Můžete zarovnat na jedné ose, na dvou osách nebo na všech třech. Minimální a maximální hrany jsou pojmenovány podle osy:

- **Osa X** – Min je vlevo, Max je vpravo.
- **Osa Y** – Min je vpředu, Max je vzadu.
- **Osa Z** – Min je dole, Max je nahoře.

Pro každou osu:

- **Zarovnat** – Volí referenční bod ukotvení pro danou osu. Pomocí **Žádný** ponecháte pozice na této ose beze změny.
- **Režim** – Určuje, jak se zvolené zarovnání použije:
  - **Jednoduché** – Přiřadí odpovídající hranu, střed nebo počátek každého přesouvaného objektu k ukotvení. Nepoužívá se žádné odsazení.
  - **Odsazení** – Zvolte, která část přesouvaného objektu má dosednout na referenci ukotvení, a poté přidejte mezeru pomocí **Odsazení**.
  - **Skládaný** – Umístí objekty jeden za druhým podél dané osy, přičemž **Odsazení** slouží jako mezera mezi nimi.
- **Podřízené zarovnání** – Dostupné v režimu **Odsazení**. Volí část přesouvaného objektu, která se umístí na referenci ukotvení. Pokud je **Podřízené zarovnání** nastaveno na **Žádný**, použije Zarovnat stejnou hranu, střed nebo počátek zvolený v **Zarovnat**.
- **Odsazení** – Dostupné v režimech **Odsazení** a **Skládaný**. Přidává vzdálenost podél dané osy a podporuje [výrazy](../../workspace/expressions.md).

## Režimy zarovnání

### Jednoduché

Režim **Jednoduché** použijte, když přiřazujete stejnou pozici ke stejné. Například **Zarovnání X: Střed** přesune každý neukotvený objekt tak, aby se jeho střed v ose X shodoval se středem X ukotvení. **Zarovnání Z: Min** přesune každý neukotvený objekt tak, aby jeho spodní strana byla ve výšce spodní strany ukotvení.

### Odsazení

Režim **Odsazení** použijte, když se má část přesouvaného objektu lišit od reference ukotvení. Například pro umístění objektu na horní stranu ukotvení:

1. Nastavte **Zarovnání Z** na **Max** (nahoře).
2. Nastavte **Režim Z** na **Odsazení**.
3. Nastavte **Podřízené zarovnání Z** na **Dole**.
4. Nastavte **Odsazení Z** na požadovanou mezeru, nebo jej ponechte na `0` pro přímý kontakt.

Tím se spodní strana přesouvaného objektu umístí na horní stranu ukotvení, případně s mezerou.

### Skládaný

Režim **Skládaný** použijte k řetězení více objektů podél osy. Objekty se zpracovávají podle názvu a poté podle interního ID, takže srozumitelné pojmenování objektů zajistí předvídatelné pořadí ve stohu.

V režimu **Skládaný** je každý přesouvaný objekt umístěn k předchozí referenci na dané ose:

- Zarovnání **Min** skládá objekty kladným směrem, například zleva doprava v ose X nebo zdola nahoru v ose Z.
- Zarovnání **Max** skládá objekty záporným směrem, například zprava doleva v ose X nebo shora dolů v ose Z.
- Zarovnání **Střed** a **Počátek** používají odsazení mezi středy nebo počátky jednotlivých objektů.

Pomocí **Odsazení** v režimu **Skládaný** nastavíte mezeru mezi objekty.

## Příklady

- **Vystředění objektů na půdorysu podložky** – Zvolte objekt, který má zůstat na místě, jako **Ukotvení**, a poté nastavte **Zarovnání X** a **Zarovnání Y** na **Střed**.
- **Umístění jednoho objektu na druhý** – Nastavte **Zarovnání Z** na **Max** (nahoře), **Režim Z** na **Odsazení** a **Podřízené zarovnání Z** na **Dole**.
- **Přidání přesné mezery od hrany** – Použijte režim **Odsazení**, zvolte hranu přesouvaného objektu pomocí **Podřízené zarovnání** a poté nastavte **Odsazení** na potřebnou mezeru.
- **Seřazení několika objektů za sebou** – Nastavte **Zarovnání X** na **Min** (vlevo), **Režim X** na **Skládaný** a pro mezeru použijte **Odsazení X**.
- **Vytvoření svislého stohu** – Nastavte **Zarovnání Z** na **Min** (dole), **Režim Z** na **Skládaný** a pro mezeru mezi objekty použijte **Odsazení Z**.

## Tipy

- Ukotvený objekt zůstává na místě; ostatní objekty se přesunou, aby se s ním zarovnaly.
- Na různých osách můžete použít různé režimy, například **Skládaný** v ose X a zároveň **Střed** a **Jednoduché** v ose Y.
- Pomocí názvů objektů řídíte pořadí režimu **Skládaný**, když je zarovnáváno několik objektů najednou.
- Zarovnat je až do použití nedestruktivní. Nastavení můžete kdykoli změnit a podřízené objekty znovu zarovnat.
- **Počátek** použijte, když potřebujete zarovnat počátky modelů namísto hran ohraničujícího kvádru.

## Související

- [Přizpůsobit hranicím](fit-to-bounds.md) – Změna měřítka objektu tak, aby odpovídal konkrétním rozměrům
- [Posunout](../transform/translate.md) – Přesun o konkrétní vzdálenost
- [Seskupování](../../workspace/grouping.md) – Seskupení zarovnaných objektů, aby zůstaly pohromadě
