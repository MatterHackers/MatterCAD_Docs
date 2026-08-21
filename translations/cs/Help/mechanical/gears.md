---
title: Ozubená kola
articleKey: GearObject3D
parent: "Mechanical Parts"
nav_order: 2
source_hash: 23098f94da8cd032e0617fbf346621504446347f
source_lang: en
---
# Ozubená kola

Vytvářejte 3D ozubená kola s plně konfigurovatelnou geometrií zubů. MatterCAD generuje správné evolventní profily zubů, které správně zabírají s dalšími koly stejného modulu a úhlu záběru.

<!-- AUTO_IMAGE: type=from_thumbnail item=gear file=mechanical_gears -->
![mechanical_gears](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_gears.png)

## Použití

1. Přidejte **Ozubené kolo** z nástrojů Mechanické nebo z panelu Základní tělesa
2. Nastavte počet zubů a další parametry
3. Profil ozubeného kola se vygeneruje automaticky

## Parametry

### Prvky

- **Typ ozubeného kola** – Vnější kolo nebo Hřeben (rovná tyč se zuby)
- **Výška** – Tloušťka ozubeného kola (výška vytažení)
- **Počet zubů** – Počet zubů po obvodu kola (výchozí: 30, rozsah: 4–60)
- **Roztečná vzdálenost** – Délka oblouku mezi zuby na roztečné kružnici (rozsah: 3–30). Určuje celkovou velikost.
- **Průměr středového otvoru** – Průměr středového otvoru pro hřídel (výchozí: 4 mm, hodnota 0 znamená bez otvoru). Pouze pro vnější kola.
- **Šířka vnější hrany** – Šířka hrany vně vnitřních zubů
- **Počet zubů vnitřního kola** – Počet zubů zabírajícího vnitřního kola

### Rozšířené

- **Úhel záběru** – Úhel dotykové plochy zubu (běžné hodnoty: 14,5, 20 nebo 25 stupňů). Všechna zabírající kola musí mít stejný úhel záběru.
- **Vůle** – Minimální mezera mezi hlavou zubu a patou zabírajícího zubu
- **Vůle** – Minimální mezera mezi zabírajícími zuby, která zabraňuje zadírání

### Data ozubeného kola (pouze pro čtení)

- **Roztečný průměr** – Poloměr, na kterém do sebe kola zabírají
- **Vnější průměr** – Celkový průměr až po hlavy zubů

## Tipy

- Dvě ozubená kola do sebe správně zaberou, když mají stejnou Roztečnou vzdálenost a Úhel záběru
- Podle hodnot Roztečný průměr správně rozmístěte zabírající kola – vzdálenost mezi středy kol by měla odpovídat součtu jejich roztečných poloměrů
- U 3D tištěných kol přidejte Vůli, abyste zohlednili tiskové tolerance
- Pro 2D profily ozubených kol (k použití s funkcí Vytáhnout) viz [Ozubené kolo 2D](gear-2d.md)

## Související

- [Ozubené kolo 2D](gear-2d.md) – 2D dráha ozubeného kola pro operace s dráhami
- [Závity](threads.md) – Vytváření závitových prvků
