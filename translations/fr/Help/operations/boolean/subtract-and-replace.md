---
title: Soustraire et remplacer
articleKey: SubtractAndReplaceObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c1698bab75faca8046b23cc148803c8063ba0678
source_lang: en
---
# Soustraire et remplacer

Soustraire et remplacer soustrait les pièces que vous choisissez de celles que vous n'avez pas choisies, mais conserve la portion découpée comme pièce à part entière au lieu de la supprimer. Utilisez **Pièce(s) à soustraire** pour désigner les formes de coupe ; tout le reste constitue la base qui sera découpée.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->
![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)

[Combiner](combine.md), [Soustraire](subtract.md), [Intersecter](intersect.md) et Soustraire et remplacer sont tous réalisés par un même objet booléen : le bouton de la barre d'outils le crée avec Soustraire et remplacer déjà sélectionné, et vous pouvez basculer vers l'une des trois autres opérations à tout moment depuis la rangée d'icônes **Opération**, en haut du panneau Propriétés.

Soustraire et remplacer n'est pas proposé pour les tracés 2D : une région n'a aucun volume retiré à restituer.

## Utilisation

1. Sélectionnez au moins deux objets
2. Cliquez sur **Soustraire et remplacer** dans la barre d'outils
3. Utilisez **Pièce(s) à soustraire** pour choisir quels enfants sont les formes de coupe
4. Changez d'avis à tout moment en cliquant sur une autre icône de la rangée **Opération**, en haut du panneau Propriétés : la forme est reconstruite avec la nouvelle opération

## Paramètres

- **Opération** - Booléen à effectuer. Présenté sous forme de rangée d'icônes en haut du panneau
- **Pièce(s) à soustraire** - Quels enfants sont les formes de coupe
- **Conserver la géométrie inversée** - Traite une coque inversée comme de la matière pleine au lieu de la laisser annuler le volume qui l'entoure. Activez cette option lorsqu'un modèle censé être plein revient avec des parties manquantes. Elle impose le moteur booléen exact, plus lent
- **Réparer l'ordre d'enroulement** - Réoriente les coques inversées de chaque pièce avant l'exécution du booléen. Cela corrige la géométrie une bonne fois pour toutes plutôt que de modifier ce que chaque opération ultérieure considère comme plein, et constitue généralement la meilleure des deux réponses à un modèle inversé

## Astuces

- Les deux pièces s'emboîtent parfaitement, puisqu'elles sont issues de la même opération
- Utilisez cette opération pour les créations multicolores, les assemblages emboîtables et les incrustations
- Si un résultat semble incorrect, vérifiez que les objets source sont étanches. **Réparer l'ordre d'enroulement** corrige les coques inversées ; [Réparer](../mesh/repair.md) corrige les dommages plus étendus des modèles importés

## Voir aussi

- [Combiner](combine.md) - Fusionner plusieurs objets en une seule forme pleine
- [Soustraire](subtract.md) - Découper une forme dans une autre
- [Intersecter](intersect.md) - Conserver uniquement le volume où les objets se chevauchent
- [Coupe par plan](../reshape/plane-cut.md) - Couper avec un plan au lieu d'une autre forme
- [Réparer](../mesh/repair.md) - Corriger les maillages importés endommagés avant un booléen

Cette page couvre également les anciens objets Soustraire et remplacer que l'on trouve encore dans les créations enregistrées avant la fusion des opérations. Ils continuent de fonctionner exactement comme avant ; les nouvelles créations utilisent l'objet booléen commun avec l'opération Soustraire et remplacer sélectionnée.
