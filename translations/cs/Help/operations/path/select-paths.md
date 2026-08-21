---
title: Vybrat cesty
articleKey: SelectPathsObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: f7df7bb24841030643e4634febedcfce6e92ada9
source_lang: en
---
# Vybrat cesty

Vybrat cesty filtruje, které dílčí cesty ze složitého objektu typu cesta se zachovají. Je to obzvlášť užitečné při práci s dekorativními nebo vícedílnými fonty, kde potřebujete vnější tvary písmen a vnitřní vyříznuté tvary jako samostatné části — například pro 3D tisk ve dvou různých barvách.

<!--  Screenshot showing Select Paths applied to decorative text with outer paths highlighted -->
![20260506 154655 paste 20260506 154655](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154655-paste-20260506-154655.jpg)

## Jak funguje hloubka cesty

Když objekt typu cesta obsahuje tvary s uzavřenými oblastmi (jako je vnitřek písmene „O“ nebo dutina dekorativní vlnovky), jsou tyto uzavřené oblasti **otvory** v hloubce 1. Vnější obrys každého písmene nebo tvaru je v **hloubce 0**.

```
Depth 0 — outer contour of each letter or shape
Depth 1 — first level of enclosed holes (inside an "O", "A", etc.)
Depth 2 — shapes nested inside a hole (rarely used)
```

## Předvolby filtru

### Vše
Zahrnuje všechny cesty beze změny. Toto je výchozí nastavení a odpovídá tomu, jako by se Vybrat cesty vůbec nepoužilo.

### Pouze vnější cesty
Zachová pouze vnější obrys každého tvaru (hloubka == 0). Použijte to, když chcete z dekorativního fontu získat jen obrysy písmen bez vnitřních vyříznutých oblastí.

### Pouze otvory
Zachová pouze uzavřené otvory (hloubka > 0). Použijte to, když chcete získat jen vnitřní vyříznuté oblasti písmen a tvarů.

### Podle indexu skupiny
Zachová pouze cesty patřící k jednomu nespojenému tvaru. Skupina 0 je první tvar, skupina 1 druhý a tak dále. Použijte to k izolaci jediného znaku ze slova.

### Vlastní
Napište výraz, který se vyhodnotí pro každou cestu. Cesta je **zahrnuta**, když je výraz nenulový, a **vyloučena**, když je nulový.

Výrazy musí začínat `=`, aby se povolilo dosazování proměnných. Bez `=` je hodnota považována za prosté číslo (např. `1` vždy zahrnuje, `0` vždy vylučuje).

## Příklady vlastních výrazů

| Výraz | Účinek |
|------------|--------|
| `=PathDepth==0` | Pouze vnější obrysy (stejné jako Pouze vnější cesty) |
| `=PathDepth>0` | Pouze otvory (stejné jako Pouze otvory) |
| `=GroupIndex==0` | Pouze první nespojený tvar |
| `=PathArea>100` | Tvary s plochou větší než 100 mm² |
| `=PathLength>50` | Tvary s obvodem delším než 50 mm |

## Proměnné vlastních výrazů

| Proměnná | Význam |
|----------|---------|
| `PathDepth` | 0 = vnější obrys; 1 a více = otvor nebo vnořený tvar |
| `GroupIndex` | Index nespojeného tvaru (0, 1, 2…) |
| `GroupOuterArea` | Plocha vnější cesty této skupiny |
| `GroupOuterLength` | Obvod vnější cesty této skupiny |
| `ChildCount` | Počet otvorů uvnitř vnější cesty této skupiny |
| `PathIndex` | Pořadový index této cesty v rámci její skupiny |
| `PathArea` | Plocha této jednotlivé cesty |
| `PathLength` | Obvod této jednotlivé cesty |

## Příklad: Vícebarevný tisk vánočního fontu

Běžným využitím funkce Vybrat cesty je tisk dekorativního textu, kde mají písmena vnitřní vyříznuté tvary. Chcete-li vytisknout vnější písmena v jedné barvě a vnitřní výřezy v druhé barvě:

1. Přidejte objekt **Text** a nastavte jej na **2D výstup**
2. Použijte **Vybrat cesty** → nastavte předvolbu na **Pouze vnější cesty**
3. Použijte **Lineární extruze**, abyste mu dodali výšku → přiřaďte první barvu filamentu
4. Vraťte se k původnímu textovému objektu
5. Použijte druhé **Vybrat cesty** → nastavte předvolbu na **Pouze otvory**
6. Použijte **Lineární extruze** se stejnou výškou → přiřaďte druhou barvu filamentu
7. Umístěte jeden vytažený objekt na druhý — obě barvy se dokonale zarovnají

## Související

- [Lineární extruze](linear-extrude.md) — Dodejte filtrovaným cestám výšku a vytvořte 3D objekt
- [Rotovat](revolve.md) — Otočte filtrované cesty kolem osy
- [SVG objekt](../../primitives/svg-object.md) — Importujte vektorové cesty, které mohou obsahovat více dílčích cest
- [Text](../../primitives/text.md) — Textové objekty v režimu 2D vytvářejí výstup s více cestami
