---
title: Flyt
articleKey: TranslateObject3D
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c05550dee2397bdb58dc2e247a068a544233a71d
source_lang: en
---
# Flyt

Flyt forskyder et objekt en bestemt afstand langs X-, Y- og/eller Z-aksen. I modsætning til at trække et objekt med musen kan du med Flyt indtaste præcise forskydningsværdier.

<!--  Screenshot showing the Translate operation properties with X, Y, Z offset fields -->
![20260506 160828 paste 20260506 160828](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160828-paste-20260506-160828.jpg)


## Sådan bruges den

1. Vælg et objekt
2. Anvend handlingen **Flyt** fra menuen Transformér
3. Indtast de ønskede forskydningsværdier for X, Y og Z i panelet Egenskaber

## Parametre

- **X, Y, Z** (Forskydning) – Afstanden objektet skal flyttes langs hver akse, i millimeter. Understøtter [udtryk](../../workspace/expressions.md) til beregnede værdier.

## Tips

- Brug Flyt, når du har brug for præcis, gentagelig placering, som du kan justere senere
- Forskydningsværdierne er relative i forhold til objektets nuværende position – hvis du indtaster 10 for X, flyttes det 10 mm til højre fra dets nuværende placering
- Til hurtig omplacering kan du også trække objekter direkte i visningen. Se [Redigering af objekter](../../getting-started/editing-objects.md)

## Relateret

- [Roter](rotate.md) – Roter et objekt med en bestemt vinkel
- [Skalér](scale.md) – Ændr størrelsen på et objekt præcist
- [Justér](../placement/align.md) – Placer objekter i forhold til hinanden
