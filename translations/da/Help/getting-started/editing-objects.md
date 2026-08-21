---
title: Redigering af objekter
parent: "Getting Started"
nav_order: 3
source_hash: 5190f3e59be7ea02497903b15c1956ed68b4d270
source_lang: en
---
# Redigering af objekter

MatterCAD har intuitive kontroller indbygget direkte i 3D-visningen til at flytte, rotere og skalere dine objekter. Du kan også redigere objektparametre i panelet Egenskaber.

## Flytning af dele


- **Træk på pladen** - Klik og træk et vilkårligt objekt for at flytte det rundt på arbejdsfladen
- **Flyt op og ned** - Brug den lodrette pilekontrol øverst på et markeret objekt til at justere dets højde (Z-position)
- Brug handlingen [Flyt](../operations/transform/translate.md) til præcis placering, eller indtast eksakte værdier i panelet Egenskaber

## Rotation af dele

![20260324 080843 paste 20260324 080843](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080843-paste-20260324-080843.jpg)

Klik på en af de **hjørnekontroller til rotation**, der vises, når du markerer et objekt. Med dem kan du rotere objektet i den pågældende kontrols plan.

- Før musen hen over en af vinkelindikatorerne for at fastlåse rotationen til **spring på 45 grader**
- Brug handlingen [Roter](../operations/transform/rotate.md) til præcis rotation, og indtast en eksakt vinkel

## Skalering af dele

![20260324 080819 paste 20260324 080819](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080819-paste-20260324-080819.jpg)


Klik på en af de **hjørnekontroller til skalering** for at ændre størrelsen på din del på arbejdsfladen.

- Træk i et hjørne for at skalere proportionalt
- Brug handlingen [Skalér](../operations/transform/scale.md) til præcis størrelse eller ikke-ensartet skalering, hvor du kan angive eksakte mål eller skalere hver akse uafhængigt

## Redigering af parametre

Når du markerer et objekt, vises dets parametre i panelet Egenskaber i højre side af skærmen. For eksempel:

- En **Terning** viser Bredde, Dybde, Højde og valgfrie kontroller til afrunding
- En **Cylinder** viser Diameter, Højde og Sider
- Et **Tekst**-objekt viser tekstindholdet, skrifttypen, størrelsen og højden

Du kan indtaste værdier direkte, bruge skydere eller indtaste [udtryk](../workspace/expressions.md) til parametriske sammenhænge.

## Kontekstmenu

Højreklik på et vilkårligt objekt for at få adgang til yderligere muligheder, blandt andet:

- Kopiér, Klip, Slet
- Gruppér / Opdel gruppe
- Tilgængelige handlinger for det markerede objekt
- Hjælp til den specifikke objekttype (når den er tilgængelig)

## Tips

- Hold **Shift** nede, mens du klikker, for at markere flere objekter, og flyt eller bearbejd dem derefter samlet
- Tryk **Ctrl+Z** for at fortryde en ændring, du har foretaget
- Brug [Justér](../operations/placement/align.md) til at placere flere objekter præcist i forhold til hinanden
- Tryk **mellemrum** for at rydde din markering

## Relateret

- [Navigation i visningsområdet](viewport-navigation.md) - Sådan roterer, panorerer og zoomer du i visningen
- [Markering](../workspace/selection.md) - Detaljeret beskrivelse af markeringsadfærd
- [Transformér-handlinger](../operations/transform/index.md) - Præcise transformationskontroller
- [Tastaturgenveje](../workspace/keyboard-shortcuts.md) - Alle tilgængelige genveje
