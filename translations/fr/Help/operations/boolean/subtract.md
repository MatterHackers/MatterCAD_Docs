---
title: Soustraire
articleKey: SubtractObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 59685bd0a635b70d7f938780f71e90be595dd993
source_lang: en
---
# Soustraire

Soustraire découpe les pièces que vous choisissez dans celles que vous n'avez pas choisies. Utilisez **Pièce(s) à soustraire** pour désigner les formes de découpe ; tout le reste constitue la base qui sera découpée.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->
![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)

[Combiner](combine.md), Soustraire, [Intersecter](intersect.md) et [Soustraire et remplacer](subtract-and-replace.md) sont tous réalisés par un seul objet booléen -- le bouton de la barre d'outils le crée avec Soustraire déjà sélectionné, et vous pouvez basculer vers l'une des trois autres opérations à tout moment depuis la rangée d'icônes **Opération** située en haut du panneau Propriétés.

Soustraire fonctionne sur les solides comme sur les tracés 2D. L'opération analyse ce que vous lui fournissez et effectue le type de traitement approprié : soustraire un tracé d'un autre produit un tracé, et soustraire un maillage d'un autre produit un solide.

## Utilisation

1. Sélectionnez deux objets ou plus
2. Cliquez sur **Soustraire** dans la barre d'outils -- une pièce à découper par défaut est choisie pour vous, afin que l'opération produise immédiatement un résultat
3. Utilisez **Pièce(s) à soustraire** pour choisir quels enfants sont les formes de découpe
4. Changez d'avis à tout moment en cliquant sur une autre icône de la rangée **Opération** en haut du panneau Propriétés -- la forme est reconstruite avec la nouvelle opération

## Paramètres

- **Opération** - Quelle opération booléenne effectuer. Présentée sous forme de rangée d'icônes en haut du panneau
- **Pièce(s) à soustraire** - Quels enfants sont les formes de découpe
- **Conserver les pièces soustraites** - Laisse dans la scène les pièces qui ont été découpées au lieu de les supprimer
- **Conserver la géométrie inversée** - Traite une coque inversée comme de la matière solide au lieu de la laisser annuler le volume qui l'entoure. Activez cette option lorsqu'un modèle censé être plein revient avec des parties manquantes. Elle impose le moteur booléen exact, plus lent
- **Réparer l'ordre d'enroulement** - Réoriente les coques inversées de chaque pièce avant l'exécution de l'opération booléenne. Cela corrige la géométrie une bonne fois pour toutes au lieu de modifier ce que chaque opération ultérieure considère comme plein ; c'est généralement la meilleure des deux réponses à un modèle inversé

## Astuces

- Les objets doivent se chevaucher pour que Soustraire produise un effet
- Pour créer un trou débouchant, assurez-vous que l'objet de découpe traverse complètement la base
- Pour un trou simple, la primitive [Trou](../../primitives/hole.md) est déjà configurée pour soustraire
- Les objets de découpe restent dans l'arborescence de conception : vous pouvez donc les déplacer ou les redimensionner, et la découpe se met à jour
- Si un résultat semble incorrect, vérifiez que les objets sources sont étanches. **Réparer l'ordre d'enroulement** corrige les coques inversées ; [Réparer](../mesh/repair.md) corrige des dommages plus étendus dans les modèles importés

## Voir aussi

- [Combiner](combine.md) - Fusionner plusieurs objets en une seule forme solide
- [Intersecter](intersect.md) - Ne conserver que le volume où les objets se chevauchent
- [Soustraire et remplacer](subtract-and-replace.md) - Soustraire une forme et conserver la pièce qui a été découpée
- [Coupe par plan](../reshape/plane-cut.md) - Découper avec un plan plutôt qu'avec une autre forme
- [Trou](../../primitives/hole.md) - Un cube préconfiguré pour soustraire
- [Réparer](../mesh/repair.md) - Corriger les maillages importés endommagés avant une opération booléenne

Cette page couvre également les anciens objets Soustraire que l'on trouve encore dans les conceptions enregistrées avant la fusion des opérations. Ils continuent de fonctionner exactement comme avant ; les nouvelles conceptions utilisent l'objet booléen commun avec l'opération Soustraire sélectionnée.
