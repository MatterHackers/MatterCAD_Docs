---
title: Udtryk
parent: "Workspace"
nav_order: 2
source_hash: 79a2f2c42d81f7fca56a87ad89f69e4303ed0ae5
source_lang: en
---
# Udtryk

Mange parametre i MatterCAD accepterer matematiske udtryk i stedet for almindelige tal. Det muliggør parametrisk design, hvor ændring af én værdi automatisk opdaterer relaterede mål.

<!--  Screenshot showing an expression being entered in a parameter field -->
![20260318 193631 paste 20260318 193631](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193631-paste-20260318-193631.jpg)


## Sådan bruges de

I stedet for at skrive et almindeligt tal i et parameterfelt kan du skrive et matematisk udtryk. For eksempel:

- `20 + 5` giver 25
- `pi * 10` giver 31,416
- `width * 2` henviser til en anden parameter med navnet "width"

## Tilgængelige konstanter

- **pi** – 3,14159... (forholdet mellem omkreds og diameter)
- **tau** – 6,28318... (2 * pi, en hel omdrejning i radianer)

## Understøttede operationer

- Addition: `+`
- Subtraktion: `-`
- Multiplikation: `*`
- Division: `/`
- Parenteser: `(` og `)` til gruppering

## Tips

- Udtryk understøttes i alle felter, der viser `DoubleOrExpression`, `IntOrExpression` eller `StringOrExpression` i koden – i praksis accepterer de fleste numeriske felter i designværktøjerne dem
- Brug udtryk til at skabe sammenhænge mellem parametre – sæt for eksempel et huls diameter til `outer_diameter - 4`, så det altid har 2 mm vægge
- Udtryk opdateres automatisk, når de refererede værdier ændres
- Brug et [Variabelark](variable-sheet.md), når flere objekter skal dele de samme navngivne værdier eller formler
- Du kan bruge udtryk i [Array](../operations/array/index.md)-handlinger til at oprette parametriske mønstre

## Relateret

- [Komponenter](components.md) – Opret genbrugelige parametriserede designs
- [Variabelark](variable-sheet.md) – Gem fælles værdier og formler til et design
- [Redigering af objekter](../getting-started/editing-objects.md) – Arbejde med objektparametre
