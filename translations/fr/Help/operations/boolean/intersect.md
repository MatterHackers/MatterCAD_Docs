---
title: Intersecter
articleKey: IntersectionObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b997cfc4f6d2f02559346365311f217388a6a2da
source_lang: en
---
# Intersecter

Intersecter ne conserve que le volume commun à tous les objets et supprime le reste.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->
![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)

[Combiner](combine.md), [Soustraire](subtract.md), Intersecter et [Soustraire et remplacer](subtract-and-replace.md) sont tous réalisés par un seul objet booléen -- le bouton de la barre d'outils le crée avec Intersecter déjà sélectionné, et vous pouvez passer à l'une des trois autres à tout moment depuis la rangée d'icônes **Opération** en haut du panneau Propriétés.

Intersecter fonctionne sur les solides comme sur les tracés 2D. L'outil examine ce que vous lui donnez et effectue le type d'opération approprié : l'intersection de deux tracés produit donc un tracé, et l'intersection de deux maillages produit un solide.

## Utilisation

1. Sélectionnez deux objets ou plus
2. Cliquez sur **Intersecter** dans la barre d'outils
3. Changez d'avis à tout moment en cliquant sur une autre icône de la rangée **Opération** en haut du panneau Propriétés -- la forme est reconstruite avec la nouvelle opération

## Paramètres

- **Opération** - Le booléen à effectuer. Affiché sous forme de rangée d'icônes en haut du panneau
- **Conserver la géométrie inversée** - Traite une coque inversée comme de la matière solide au lieu de la laisser annuler le volume qui l'entoure. Activez cette option lorsqu'un modèle censé être plein revient avec des parties manquantes. Elle impose le moteur booléen exact, plus lent
- **Réparer l'ordre d'enroulement** - Réoriente les coques inversées de chaque pièce avant l'exécution du booléen. Cette option corrige la géométrie une bonne fois pour toutes au lieu de modifier ce que chaque opération ultérieure considère comme solide ; c'est en général la meilleure des deux réponses à un modèle inversé

## Astuces

- Les objets doivent se chevaucher. S'ils ne se chevauchent pas réellement, le résultat est vide
- Avec plus de deux objets, l'opération progresse dans la liste : les deux premiers sont intersectés, puis ce résultat est intersecté avec le troisième, et ainsi de suite
- Si un résultat semble incorrect, vérifiez que les objets sources sont étanches. **Réparer l'ordre d'enroulement** corrige les coques inversées ; [Réparer](../mesh/repair.md) corrige des dommages plus étendus dans les modèles importés

## Voir aussi

- [Combiner](combine.md) - Fusionner plusieurs objets en une seule forme solide
- [Soustraire](subtract.md) - Découper une forme dans une autre
- [Soustraire et remplacer](subtract-and-replace.md) - Soustraire une forme et conserver la pièce retirée
- [Coupe par plan](../reshape/plane-cut.md) - Couper avec un plan plutôt qu'avec une autre forme
- [Réparer](../mesh/repair.md) - Corriger les maillages importés endommagés avant un booléen

Cette page couvre également les anciens objets Intersection que l'on trouve encore dans les conceptions enregistrées avant la fusion des opérations. Ils continuent de fonctionner exactement comme avant ; les nouvelles conceptions utilisent l'objet booléen commun avec l'opération Intersecter sélectionnée.
