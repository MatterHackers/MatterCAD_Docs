---
title: Kurve
articleKey: CurveObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 6adde5da3bb469384f59eb5e9dfe5cb642b3eec5
source_lang: en
---
# Kurve

Kurve bøjer et lige objekt til en bue eller en cirkulær form. Du kan styre bøjningen ved at angive enten en vinkel eller en diameter, som objektet skal vikles omkring.

<!--  Before and after showing a straight bar being curved into an arc -->
![20260506 155243 paste 20260506 155243](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155243-paste-20260506-155243.jpg)

## Sådan bruges den

1. Vælg et objekt
2. Anvend handlingen **Kurve** fra menuen Omform
3. Vælg mellem bøjningstypen Vinkel eller Diameter
4. Juster parametrene for at opnå den ønskede krumning

## Parametre

- **Bøjningstype** - Vælg mellem:
  - **Vinkel** - Angiv bøjningsvinklen direkte (1-360 grader)
  - **Diameter** - Angiv diameteren på den cirkel, som emnet vikles omkring
- **Bukkeretning** - Buk op eller Bøj ned
- **Startprocent** - Hvor langs objektet bøjningen skal starte (0-100 %)
- **Opdel mesh** - Opdel mesh for at få bløde kurver (standard: til)
- **Min. sider pr. rotation** - Mindste antal mesh-segmenter pr. hel omdrejning. Højere værdier = blødere kurver

### Avancerede parametre

- **Startbøjningsprocent** - Procentdel fra venstre, hvor bøjningen starter
- **Slutbøjningsprocent** - Procentdel fra venstre, hvor bøjningen slutter

## Tip

- Brug Kurve til at lave buer, ringe og bøjede beslag ud fra lige grundformer
- Hvis vinklen sættes til 360, vikles objektet til en komplet ring
- Forøg Min. sider pr. rotation for at få blødere resultater ved skarpe bøjninger
- Objektet bøjes langs sin længde (X-aksen)

## Relateret

- [Vrid](twist.md) - Roter langs højden i stedet for at bøje
- [Torus](../../primitives/torus.md) - En færdig ringform
