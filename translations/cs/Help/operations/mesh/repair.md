---
title: Opravit
articleKey: RepairObject3D_2
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: f637470dee4f722b595f07d2da9dcdaac5e8da72
source_lang: en
---
# Opravit

Opravit odstraňuje běžné problémy v geometrii síťoviny, včetně nemanifoldních hran, dutin, nekonzistentní orientace ploch a téměř splývajících vrcholů. To je obzvlášť užitečné u importovaných souborů STL a OBJ, které mohou obsahovat chyby.

![20260324 080517 paste 20260324 080517](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080517-paste-20260324-080517.jpg)


## Jak postupovat

1. Vyberte objekt s problémy síťoviny
2. Použijte operaci **Opravit** z nabídky Síťovina
3. Prohlédněte si statistiky před opravou a po ní a zjistěte, co bylo opraveno

## Statistiky (pouze pro čtení)

- **Počáteční vrcholy / Konečné vrcholy** – Počet vrcholů před opravou a po ní
- **Počáteční plochy / Konečné stěny** – Počet ploch před opravou a po ní
- **Počáteční nemanifoldní hrany / Konečné nemanifoldní hrany** – Počet problematických hran před opravou a po ní

### Rozšířené možnosti

Zapněte režim **Rozšířené** pro jemné nastavení:

- **Svařit vrcholy** – Sloučí téměř splývající vrcholy (výchozí: zapnuto)
- **Tolerance svaření** – Jak blízko u sebe musí vrcholy být, aby se sloučily
- **Orientace plochy** – Otočí naruby obrácené skořepiny správným směrem, aby se každé těleso četlo jako plné. Každá skořepina se posuzuje samostatně, takže dutý model si své dutiny zachová, místo aby byly zaplněny. Skořepiny, jejichž vlastní plochy si vzájemně odporují, zůstanou beze změny, místo aby se jejich orientace odhadovala, a u modelů, které nejsou vodotěsné, se použije tolerantnější oprava – pokud samotná orientace problém nevyřeší, spusťte nejprve **Zaplnit dutiny**.
- **Svařit hrany** – Opraví drobné praskliny a vadné švy
- **Zaplnit dutiny** – Zaplní mezery v povrchu síťoviny
- **Režim odebírání** – Odebere vnitřní nebo zakrytou geometrii:
  - **Žádný** – Zachová veškerou geometrii
  - **Vnitřek** – Odebere vnitřní tělesa skrytá uvnitř hlavního tvaru
  - **Zakrytý** – Odebere plochy, které nejsou zvenčí vidět

## Tipy

- Pokud booleovské operace (Sloučit, Odečíst) dávají u importovaných modelů neočekávané výsledky, zkuste nejprve Opravit
- Výchozí nastavení (Svařit vrcholy zapnuto, vše ostatní vypnuto) vyřeší nejběžnější problémy
- Zapněte Zaplnit dutiny, pokud jsou v modelu mezery, kterými je vidět skrz
- Použijte Režim odebírání Vnitřek k vyčištění modelů, které mají uvnitř skrytou geometrii

## Související

- [Decimace](decimate.md) – Sníží počet polygonů
- [Přidávání existujících objektů](../../getting-started/adding-existing-objects.md) – Importujte modely, které mohou potřebovat opravu
