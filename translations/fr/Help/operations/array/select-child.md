---
title: Sélectionner l'enfant
articleKey: SelectChildObject3D
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: f6f71d2b457b82126f272ea9354f877c36570df0
source_lang: en
---
# Sélectionner l'enfant

Sélectionner l'enfant choisit un enfant parmi un groupe d'objets, en se basant soit sur un numéro d'index, soit sur un nom. C'est particulièrement utile dans les conceptions scriptées et paramétriques où vous souhaitez choisir dynamiquement l'objet à afficher.

<!-- IMAGE: Screenshot showing Select Child operation with multiple children and one selected by index -->
![20260506 080526 paste 20260506 080526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080526-paste-20260506-080526.jpg)


## Utilisation

1. Sélectionnez deux objets ou plus
2. Appliquez l'opération **Sélectionner l'enfant** depuis le menu Duplication
3. Choisissez **Par index** ou **Par nom** pour définir la façon dont l'enfant est sélectionné
4. Définissez le numéro d'index ou le nom à faire correspondre

## Paramètres

- **Méthode de sélection** - Choisissez entre **Par index** (sélection par position) ou **Par nom** (sélection par nom d'objet). Affichée sous forme de boutons.
- **Index enfant** - L'index de l'enfant à sélectionner, en base zéro (affiché lors de l'utilisation de Par index). Prend en charge les [expressions](../../workspace/expressions.md).
- **Nom enfant** - Le nom de l'enfant à sélectionner (affiché lors de l'utilisation de Par nom). Prend en charge les [expressions](../../workspace/expressions.md).

Si l'index est hors plage ou si le nom ne correspond à aucun enfant, le premier enfant est renvoyé comme solution de repli. S'il n'y a aucun enfant, rien n'est renvoyé.

## Utilisation dans le Scriptage

Sélectionner l'enfant est conçu pour fonctionner avec les expressions et la fonction `rand()` afin de créer des conceptions dynamiques pilotées par les données. Par exemple, vous pouvez construire une scène comportant plusieurs variantes d'objets comme enfants et utiliser une expression telle que `rand(42)` comme graine d'index pour en choisir une au hasard.

**Exemple : accessoires de livres aléatoires pour un décor de scène**

1. Importez 5 maillages de livres différents comme enfants d'une opération Sélectionner l'enfant
2. Réglez la Méthode de sélection sur **Par index**
3. Utilisez une expression pour Index enfant, telle que `floor(rand(seed) * 5)` où `seed` est une variable de feuille
4. Dupliquez plusieurs fois l'opération Sélectionner l'enfant, chacune avec une valeur de graine différente
5. Chaque instance choisit au hasard un livre différent dans l'ensemble

Ce schéma fonctionne pour tout scénario où vous devez choisir parmi un ensemble de variantes : mobilier, décorations, éléments architecturaux ou toute collection de pièces interchangeables.

## Astuces

- Combinez avec [Réseau](array.md) pour créer des motifs variés où chaque copie sélectionne un enfant différent
- Utilisez des variables de feuille pour l'index ou le nom afin de piloter la sélection depuis un tableur
- Le comportement de repli sur le premier enfant garantit que votre conception ne casse jamais, même si l'index ou le nom est incorrect

## Voir aussi

- [Réseau](array.md) - Dupliquer des objets selon des motifs linéaires, radiaux, sur courbe et par transformation
