---
title: Radial sammentrækning
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: 95ef5847767e5cfcdbae9df9aaa1cb1727da2f5e
source_lang: en
---
# Radial sammentrækning

Radial sammentrækning komprimerer et objekt indad fra et centerpunkt med en profilkurve, du selv kan tilpasse. I modsætning til almindelig [Knib](pinch.md), som virker bagfra og fremad, komprimerer Radial sammentrækning symmetrisk omkring en centerakse.

<!--  Before and after showing an object with radial pinch applied, creating a waisted shape -->
![20260506 155741 paste 20260506 155741](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155741-paste-20260506-155741.jpg)

## Sådan bruges den

1. Vælg et objekt
2. Anvend handlingen **Radial sammentrækning** fra menuen Omform
3. Rediger stiprofilen for at definere, hvor meget knib der anvendes i hver højde
4. Juster antallet af skiver for at opnå glathed

## Parametre

- **Sti** - En profilkurve-editor, der definerer knibmængden på hvert højdeniveau. Rediger kurven for at oprette brugerdefinerede knibprofiler
- **Skiver** - Antal vandrette snit til glat knib, fordelt jævnt op ad emnet. Flere skiver = glattere resultat

### Avancerede parametre

- **Knibtype** - Kompressionens retning:
  - **Radial** - Komprimer lige meget fra alle sider mod centrum
  - **X-akse** - Komprimer kun langs X-aksen
  - **Y-akse** - Komprimer kun langs Y-aksen
- **Rotationsforskydning** - Forskyd centrum for knibeffekten

## Tip

- Brug sti-editoren til at skabe timeglas-, flaske- eller vaselignende former
- Radial sammentrækning er ideel til at skabe organiske, afrundede former ud fra cylindriske objekter
- Øg Skiver for at få glattere kurver, især ved skarpe knibprofiler

## Relateret

- [Knib](pinch.md) - Simpel kompression bagfra og fremad
- [Vrid](twist.md) - Spiralrotation langs højden
- [Kurve](curve.md) - Bøj til en bue
