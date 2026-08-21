---
title: Redigere objekter
parent: "Getting Started"
nav_order: 3
source_hash: 5190f3e59be7ea02497903b15c1956ed68b4d270
source_lang: en
---
# Redigere objekter

MatterCAD har intuitive kontroller innebygd direkte i 3D-visningen for å flytte, rotere og skalere objektene dine. Du kan også redigere objektparametere i Egenskaper-panelet.

## Flytte deler


- **Dra på byggeplaten** - Klikk og dra et hvilket som helst objekt for å skyve det rundt på arbeidsflaten
- **Flytt opp og ned** - Bruk den vertikale pilkontrollen øverst på et valgt objekt for å justere høyden (Z-posisjonen)
- For nøyaktig plassering, bruk operasjonen [Flytt](../operations/transform/translate.md) eller skriv inn eksakte verdier i Egenskaper-panelet

## Rotere deler

![20260324 080843 paste 20260324 080843](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080843-paste-20260324-080843.jpg)

Klikk på en av **hjørnekontrollene for rotasjon** som vises når du velger et objekt. Med disse kan du rotere objektet i planet til den aktuelle kontrollen.

- Flytt musepekeren over en av vinkelindikatorene for å låse rotasjonen til **trinn på 45 grader**
- For nøyaktig rotasjon, bruk operasjonen [Roter](../operations/transform/rotate.md) og skriv inn en eksakt vinkel

## Skalere deler

![20260324 080819 paste 20260324 080819](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080819-paste-20260324-080819.jpg)


Klikk på en av **hjørnekontrollene for skalering** for å endre størrelsen på delen i arbeidsområdet.

- Dra et hjørne for å skalere proporsjonalt
- For nøyaktig størrelse eller ikke-uniform skalering, bruk operasjonen [Skaler](../operations/transform/scale.md), der du kan angi eksakte mål eller skalere hver akse uavhengig

## Redigere parametere

Når du velger et objekt, vises parameterne i Egenskaper-panelet på høyre side av skjermen. For eksempel:

- En **Kube** viser Bredde, Dybde, Høyde og valgfrie kontroller for avrunding
- En **Sylinder** viser Diameter, Høyde og Sider
- Et **Tekst**-objekt viser tekstinnholdet, skrifttypen, størrelsen og høyden

Du kan skrive inn verdier direkte, bruke glidebrytere eller angi [uttrykk](../workspace/expressions.md) for parametriske sammenhenger.

## Kontekstmeny

Høyreklikk på et objekt for å få tilgang til flere alternativer, blant annet:

- Kopier, Klipp ut, Slett
- Grupper / Løs opp gruppe
- Tilgjengelige operasjoner for det valgte objektet
- Hjelp for den bestemte objekttypen (når det er tilgjengelig)

## Tips

- Hold inne **Shift** mens du klikker for å velge flere objekter, og flytt dem eller kjør operasjoner på dem samlet
- Trykk **Ctrl+Z** for å angre en endring du har gjort
- Bruk [Juster](../operations/placement/align.md) for å plassere flere objekter nøyaktig i forhold til hverandre
- Trykk **Mellomrom** for å oppheve utvalget

## Relatert

- [Navigering i visningsvinduet](viewport-navigation.md) - Slik roterer, panorerer og zoomer du visningen
- [Utvalg](../workspace/selection.md) - Detaljert beskrivelse av utvalgsatferd
- [Transformer-operasjoner](../operations/transform/index.md) - Nøyaktige transformasjonskontroller
- [Hurtigtaster](../workspace/keyboard-shortcuts.md) - Alle tilgjengelige hurtigtaster
