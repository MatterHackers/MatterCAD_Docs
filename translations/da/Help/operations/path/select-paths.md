---
title: Vælg stier
articleKey: SelectPathsObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: f7df7bb24841030643e4634febedcfce6e92ada9
source_lang: en
---
# Vælg stier

Vælg stier filtrerer, hvilke understier fra et komplekst stiobjekt der bevares. Det er især nyttigt, når du arbejder med dekorative skrifttyper eller skrifttyper i flere dele, hvor du har brug for de ydre bogstavformer og de indre udskæringer som separate dele — for eksempel for at 3D-printe dem i to forskellige farver.

<!--  Screenshot showing Select Paths applied to decorative text with outer paths highlighted -->
![20260506 154655 paste 20260506 154655](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154655-paste-20260506-154655.jpg)

## Sådan fungerer stidybde

Når et stiobjekt indeholder former med lukkede områder (som det indvendige af bogstavet "O" eller hulrummet i en dekorativ snirkel), er disse lukkede områder **huller** på dybde 1. Den ydre kontur af hvert bogstav eller hver form ligger på **dybde 0**.

```
Depth 0 — outer contour of each letter or shape
Depth 1 — first level of enclosed holes (inside an "O", "A", etc.)
Depth 2 — shapes nested inside a hole (rarely used)
```

## Filterforudindstillinger

### Alle
Inkluderer alle stier uændret. Dette er standarden og svarer til slet ikke at anvende Vælg stier.

### Kun ydre stier
Bevarer kun den ydre kontur af hver form (dybde == 0). Brug denne til kun at få bogstavernes omrids fra en dekorativ skrifttype uden de indre udskæringer.

### Kun huller
Bevarer kun de lukkede huller (dybde > 0). Brug denne til kun at få de indre udskårne områder af bogstaver og former.

### Efter gruppeindeks
Bevarer kun stier, der hører til én sammenhængende form. Gruppe 0 er den første form, gruppe 1 er den anden og så videre. Brug denne til at isolere et enkelt tegn fra et ord.

### Brugerdefineret
Skriv et udtryk, der evalueres for hver sti. Stien **inkluderes**, når udtrykket er forskelligt fra nul, og **udelades**, når det er nul.

Udtryk skal begynde med `=` for at aktivere variabelsubstitution. Uden `=` behandles værdien som et almindeligt tal (f.eks. inkluderer `1` altid, og `0` udelader altid).

## Eksempler på brugerdefinerede udtryk

| Udtryk | Effekt |
|------------|--------|
| `=PathDepth==0` | Kun ydre konturer (samme som Kun ydre stier) |
| `=PathDepth>0` | Kun huller (samme som Kun huller) |
| `=GroupIndex==0` | Kun den første sammenhængende form |
| `=PathArea>100` | Former med et areal større end 100 mm² |
| `=PathLength>50` | Former med en omkreds længere end 50 mm |

## Variabler i brugerdefinerede udtryk

| Variabel | Betydning |
|----------|---------|
| `PathDepth` | 0 = ydre kontur; 1+ = hul eller indlejret form |
| `GroupIndex` | Indeks for den sammenhængende form (0, 1, 2…) |
| `GroupOuterArea` | Areal af den ydre sti for denne gruppe |
| `GroupOuterLength` | Omkreds af den ydre sti for denne gruppe |
| `ChildCount` | Antal huller inden i denne gruppes ydre sti |
| `PathIndex` | Fortløbende indeks for denne sti inden for dens gruppe |
| `PathArea` | Areal af denne enkelte sti |
| `PathLength` | Omkreds af denne enkelte sti |

## Eksempel: Flerfarvet udskrift med juleskrifttype

En almindelig anvendelse af Vælg stier er udskrivning af dekorativ tekst, hvor bogstaverne har indre udskæringer. Sådan udskriver du de ydre bogstaver i én farve og de indre udskæringer i en anden farve:

1. Tilføj et **Tekst**-objekt, og indstil det til **2D-output**
2. Anvend **Vælg stier** → indstil forudindstillingen til **Kun ydre stier**
3. Anvend **Lineær ekstrudering** for at give det højde → tildel din første filamentfarve
4. Gå tilbage til det oprindelige tekstobjekt
5. Anvend endnu en **Vælg stier** → indstil forudindstillingen til **Kun huller**
6. Anvend **Lineær ekstrudering** med samme højde → tildel din anden filamentfarve
7. Placer det ene ekstruderede objekt oven på det andet — de to farver flugter perfekt

## Relateret

- [Lineær ekstrudering](linear-extrude.md) — Giv de filtrerede stier højde for at skabe et 3D-objekt
- [Roter profil](revolve.md) — Drej filtrerede stier omkring en akse
- [SVG-objekt](../../primitives/svg-object.md) — Importer vektorstier, der kan indeholde flere understier
- [Tekst](../../primitives/text.md) — Tekstobjekter i 2D-tilstand producerer output med flere stier
