---
title: Array
articleKey: ArrayObject3D_2
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c547fa24e5f47e0d60f0cec0eac979700d946daf
source_lang: en
---
# Array

Array opretter flere kopier af et objekt, arrangeret i et mønster. Vælg en tilstand med knapperne øverst — **Lineær**, **Radial** eller **Transformér** — for at skifte mellem mønstertyper.

<!--  Screenshot of the Array operation panel showing the mode buttons at the top (Linear | Radial | Transform) -->
![20260506 080647 paste 20260506 080647](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080647-paste-20260506-080647.jpg)


## Sådan bruges den

1. Vælg et objekt
2. Anvend handlingen **Array** fra menuen Duplikering
3. Vælg en tilstand (Lineær, Radial eller Transformér)
4. Justér parametrene for den valgte tilstand

## Tilstand: Lineær

Lineær tilstand placerer kopier langs en retning med valgfri progression af rotation og skalering.

**Antal** — Antal kopier (heltal eller udtryk). Kildeobjektet er den første kopi; yderligere kopier forskydes fra det.

**Forskydningsmetode** — Hvordan afstanden beregnes:
- **Relativ** — Forskydningen ganges med objektets afgrænsningsrammes størrelse. En Relativ forskydning på (1, 0, 0) placerer kopierne præcis én objektbredde fra hinanden langs X.
- **Forskydning** — Fast afstand i verdensrummet i mm pr. kopi.
- **Slutpunkt** — Angiv positionen for den sidste kopi; afstanden fordeles jævnt mellem kopierne.

**Relativ forskydning** / **Forskydning** / **Slutpunkt** — Afstandsvektoren, afhængigt af den valgte Forskydningsmetode.

**Rotationstilstand** — Hvordan rotationen akkumuleres på tværs af kopierne:
- **Lokal** — Hver kopi roterer på stedet om sit eget centrum; forskydningsretningen forbliver i verdensakserne.
- **Sammensætning** — Rotationen akkumuleres og styrer forskydningen, hvilket giver spiraler, vifter og helixer.

**Rotation** — Rotation pr. kopi i grader om hver akse.

**Skalér** — Kumulativ skalering pr. kopi om hver akse. Værdier under 1 formindsker kopierne; værdier over 1 forstørrer dem.

**Skalering påvirker forskydning** — Når den er slået til, skaleres afstanden mellem kopierne også for hvert trin. Brug dette til strammende spiraler og geometriske progressioner (nautilusskaller, stablede sneglekurver).

## Tilstand: Radial

Radial tilstand fordeler kopierne jævnt omkring en centerakse med en fast radius.

<!--  Screenshot of Array in Radial mode showing 6 copies arranged in a circle, with Radius and Central Axis parameters visible -->
![20260506 092618 paste 20260506 092618](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-092618-paste-20260506-092618.jpg)


**Optællingsmetode** — Hvordan antallet af kopier bestemmes:
- **Antal** — Eksplicit antal kopier.
- **Afstand** — Vinkelmellemrum mellem kopier i grader; antallet beregnes, så sweepet fyldes ud.

**Antal** / **Vinkelafstand** — Antal kopier (tilstanden Antal) eller vinkelafstand i grader (tilstanden Afstand). Understøtter udtryk.

**Centerakse** — Aksen, der roteres omkring (standard: Z).

**Cirkelsegment** — Om kopierne spænder over en fuld 360°-cirkel (**Fuld**) eller en delvis bue (**Bue**).

**Radius** — Afstand fra centeraksen til hver kopi.

**Sweep-vinkel** — Antal grader af buen, der skal fyldes ud (vises, når Cirkelsegment er Bue). Understøtter udtryk.

**Justér rotation** — Roter hver kopi, så dens fremadakse peger udad fra centrum.

**Fremadakse** — Hvilken akse på kopien der behandles som "fremad" ved justering (vises, når Justér rotation er slået til).

## Tilstand: Transformér

Tilstanden Transformér forskyder kopierne trinvist ved hjælp af en manuel transformation eller ved at følge et andet objekts transformation.

**Antal** — Antal kopier (heltal eller udtryk).

**Transformationsreference** — Hvor transformationen pr. trin kommer fra:
- **Input** — Du angiver forskydning, rotation og skalering direkte.
- **Objekt** — Transformationen læses fra et navngivet sideordnet objekt.

**Forskydning** — Forskydning pr. trin i verdensrummet i mm (vises, når Reference er Input).

**Rotation** — Rotation pr. trin i grader pr. akse (vises, når Reference er Input).

**Skalér** / **Skalér akser** — Ensartet og akse-specifik skalering anvendt ved hvert trin (vises, når Reference er Input).

**Transformationsnavn** — Navnet på det sideordnede objekt, hvis transformation bruges som trinvis tilvækst (vises, når Reference er Objekt).

**Relativt rum** — Når den er slået til, sammensættes hver kopis transformation i den forrige kopis lokale referenceramme; når den er slået fra, anvendes hvert trin i verdensrummet (vises, når Reference er Objekt).

## Gør tilfældig

Aktivér **Gør tilfældig** for at tilføje variation til alle kopier.

- **Tilfældig forskydning** — Maksimal tilfældig positionsforskydning pr. akse i mm.
- **Tilfældig rotation** — Maksimal tilfældig rotation pr. akse i grader.
- **Tilfældige skaleringsakser** — Maksimal tilfældig skaleringsvariation pr. akse.
- **Udelad første** — Behold den første kopi på dens præcist beregnede position (standard: til).
- **Udelad sidste** — Behold den sidste kopi på dens præcist beregnede position.
- **Tilfældigt starttal** — Skift dette for at få en anden tilfældig placering. Understøtter udtryk.

## Flet

- **Opret enkelt mesh** — Kombinér alle kopier til ét sammenflettet mesh-objekt.
- **Flet punkter** — Svejs punkter sammen inden for fletteafstandens grænseværdi (vises, når Opret enkelt mesh er slået til).
- **Afstand** — Grænseværdi for fletning i mm (vises, når Flet punkter er slået til).

## Tips

- Brug udtryk til Antal, Rotation eller Slutpunkt for at skabe parametriske mønstre
- Til cirkulære mønstre bruges tilstanden Radial — angiv Radius for at styre cirklens størrelse, og aktivér Justér rotation, hvis kopierne skal vende udad
- Sammensætning af rotation i tilstanden Lineær skaber spiraler og vifter, uden at du manuelt skal beregne vinkelforskydninger
- Skalering påvirker forskydning skaber helt naturligt layouts med nautilusskaller og geometriske progressioner
- Kombinér Array med [Vælg underelement](select-child.md) for at skabe mønstre, hvor hver kopi viser en forskellig variant

## Relateret

- [Justér](../placement/align.md) - Placér objekter i forhold til hinanden
- [Vælg underelement](select-child.md) - Vælg en bestemt kopi fra en array ud fra indeks eller navn
