---
title: Expressions
parent: "Workspace"
nav_order: 2
source_hash: 79a2f2c42d81f7fca56a87ad89f69e4303ed0ae5
source_lang: en
---
# Expressions

De nombreux paramètres de MatterCAD acceptent des expressions mathématiques au lieu de simples nombres. Cela permet une conception paramétrique où la modification d'une valeur met automatiquement à jour les cotes associées.

<!--  Screenshot showing an expression being entered in a parameter field -->
![20260318 193631 paste 20260318 193631](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193631-paste-20260318-193631.jpg)


## Utilisation

Au lieu de saisir un simple nombre dans un champ de paramètre, vous pouvez saisir une expression mathématique. Par exemple :

- `20 + 5` est évalué à 25
- `pi * 10` est évalué à 31,416
- `width * 2` fait référence à un autre paramètre nommé « width »

## Constantes disponibles

- **pi** - 3,14159... (le rapport entre la circonférence et le diamètre)
- **tau** - 6,28318... (2 * pi, une révolution complète en radians)

## Opérations prises en charge

- Addition : `+`
- Soustraction : `-`
- Multiplication : `*`
- Division : `/`
- Parenthèses : `(` et `)` pour le regroupement

## Astuces

- Les expressions sont prises en charge dans tout champ affichant `DoubleOrExpression`, `IntOrExpression` ou `StringOrExpression` dans le code -- en pratique, la plupart des champs numériques des outils de conception les acceptent
- Utilisez les expressions pour créer des relations entre les paramètres -- par exemple, définissez le diamètre d'un trou sur `outer_diameter - 4` afin qu'il conserve toujours des parois de 2 mm
- Les expressions se mettent à jour automatiquement lorsque les valeurs référencées changent
- Utilisez une [Feuille de variables](variable-sheet.md) lorsque plusieurs objets doivent partager les mêmes valeurs nommées ou les mêmes formules
- Vous pouvez utiliser des expressions dans les opérations [Réseau](../operations/array/index.md) pour créer des motifs paramétriques

## Voir aussi

- [Composants](components.md) - Créez des conceptions paramétrées réutilisables
- [Feuille de variables](variable-sheet.md) - Stockez les valeurs et formules partagées d'une conception
- [Modifier les objets](../getting-started/editing-objects.md) - Travailler avec les paramètres d'objet
