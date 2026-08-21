---
title: Velg baner
articleKey: SelectPathsObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: f7df7bb24841030643e4634febedcfce6e92ada9
source_lang: en
---
# Velg baner

Velg baner filtrerer hvilke underbaner fra et komplekst baneobjekt som beholdes. Det er spesielt nyttig når du arbeider med dekorative skrifter eller skrifter med flere deler, der du trenger de ytre bokstavformene og de indre utskjæringsformene som separate deler — for eksempel for å 3D-printe dem i to ulike farger.

<!--  Screenshot showing Select Paths applied to decorative text with outer paths highlighted -->
![20260506 154655 paste 20260506 154655](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154655-paste-20260506-154655.jpg)

## Slik fungerer banedybde

Når et baneobjekt inneholder former med lukkede områder (som innsiden av bokstaven «O», eller hulrommet i en dekorativ krusedull), er disse lukkede områdene **hull** på dybde 1. Den ytre konturen til hver bokstav eller form er på **dybde 0**.

```
Depth 0 — outer contour of each letter or shape
Depth 1 — first level of enclosed holes (inside an "O", "A", etc.)
Depth 2 — shapes nested inside a hole (rarely used)
```

## Filterforhåndsinnstillinger

### Alle
Inkluderer alle baner uendret. Dette er standardvalget og tilsvarer å ikke bruke Velg baner i det hele tatt.

### Bare ytre baner
Beholder bare den ytre konturen til hver form (dybde == 0). Bruk dette for å få kun bokstavomrissene fra en dekorativ skrift, uten de indre utskjæringsområdene.

### Bare hull
Beholder bare de lukkede hullene (dybde > 0). Bruk dette for å få kun de indre utskjæringsområdene i bokstaver og former.

### Etter gruppeindeks
Beholder bare baner som tilhører én usammenhengende form. Gruppe 0 er den første formen, gruppe 1 er den andre, og så videre. Bruk dette for å isolere ett enkelt tegn fra et ord.

### Egendefinert
Skriv et uttrykk som evalueres for hver bane. Banen **inkluderes** når uttrykket er ulik null, og **utelates** når det er null.

Uttrykk må starte med `=` for å aktivere variabelsubstitusjon. Uten `=` behandles verdien som et vanlig tall (f.eks. inkluderer `1` alltid, `0` utelater alltid).

## Eksempler på egendefinerte uttrykk

| Uttrykk | Virkning |
|------------|--------|
| `=PathDepth==0` | Bare ytre konturer (samme som Bare ytre baner) |
| `=PathDepth>0` | Bare hull (samme som Bare hull) |
| `=GroupIndex==0` | Bare den første usammenhengende formen |
| `=PathArea>100` | Former med areal større enn 100 mm² |
| `=PathLength>50` | Former med omkrets lengre enn 50 mm |

## Variabler for egendefinerte uttrykk

| Variabel | Betydning |
|----------|---------|
| `PathDepth` | 0 = ytre kontur; 1+ = hull eller nøstet form |
| `GroupIndex` | Indeks til den usammenhengende formen (0, 1, 2 …) |
| `GroupOuterArea` | Areal av den ytre banen for denne gruppen |
| `GroupOuterLength` | Omkrets av den ytre banen for denne gruppen |
| `ChildCount` | Antall hull inne i denne gruppens ytre bane |
| `PathIndex` | Sekvensiell indeks for denne banen innenfor gruppen |
| `PathArea` | Areal av denne enkeltbanen |
| `PathLength` | Omkrets av denne enkeltbanen |

## Eksempel: Utskrift av julemotiv-skrift i flere farger

En vanlig bruk av Velg baner er utskrift av dekorativ tekst der bokstavene har indre utskjæringsformer. Slik skriver du ut de ytre bokstavene i én farge og de indre utskjæringene i en annen farge:

1. Legg til et **Tekst**-objekt og sett det til **2D-utdata**
2. Bruk **Velg baner** → sett forhåndsinnstillingen til **Bare ytre baner**
3. Bruk **Lineær ekstrudering** for å gi det høyde → tilordne den første filamentfargen din
4. Gå tilbake til det opprinnelige tekstobjektet
5. Bruk en ny **Velg baner** → sett forhåndsinnstillingen til **Bare hull**
6. Bruk **Lineær ekstrudering** med samme høyde → tilordne den andre filamentfargen din
7. Plasser det ene ekstruderte objektet oppå det andre — de to fargene flukter perfekt

## Relatert

- [Lineær ekstrudering](linear-extrude.md) — Gi de filtrerte banene høyde for å lage et 3D-objekt
- [Roter rundt akse](revolve.md) — Spinn filtrerte baner rundt en akse
- [SVG-objekt](../../primitives/svg-object.md) — Importer vektorbaner som kan inneholde flere underbaner
- [Tekst](../../primitives/text.md) — Tekstobjekter i 2D-modus gir utdata med flere baner
