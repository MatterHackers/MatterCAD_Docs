---
title: Combiner
articleKey: CombineObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: a3066faa634b5a88a2fe1650a4e2ac278ac50e24
source_lang: en
---
# Combiner

Combiner fusionne tout en un seul solide. Les faces internes situées là où les formes se chevauchaient sont supprimées : le résultat est donc un maillage continu unique plutôt que des coques qui se chevauchent.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->
![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)

Combiner, [Soustraire](subtract.md), [Intersecter](intersect.md) et [Soustraire et Remplacer](subtract-and-replace.md) sont tous réalisés par un même objet booléen : le bouton de la barre d'outils le crée avec Combiner déjà sélectionné, et vous pouvez basculer à tout moment vers l'une des trois autres opérations depuis la rangée d'icônes **Opération** en haut du panneau Propriétés.

Combiner fonctionne sur les solides comme sur les tracés 2D. L'opération analyse ce que vous lui fournissez et applique le type de traitement approprié : combiner deux tracés produit donc un tracé, et combiner deux maillages produit un solide.

## Utilisation

1. Sélectionnez deux objets ou plus
2. Cliquez sur **Combiner** dans la barre d'outils
3. Changez d'avis à tout moment en cliquant sur une autre icône de la rangée **Opération** en haut du panneau Propriétés : la forme est reconstruite avec la nouvelle opération

## Paramètres

- **Opération** - Le booléen à effectuer. Présenté sous forme de rangée d'icônes en haut du panneau
- **Conserver la géométrie inversée** - Traiter une coque inversée comme de la matière solide au lieu de la laisser annuler le volume qui l'entoure. Activez cette option lorsqu'un modèle censé être plein revient avec des parties manquantes. Elle impose le moteur booléen exact, plus lent
- **Réparer l'ordre d'enroulement** - Réoriente les coques inversées de chaque pièce avant l'exécution du booléen. Cette option corrige la géométrie une bonne fois pour toutes plutôt que de modifier ce que chaque opération ultérieure considère comme solide : c'est généralement la meilleure des deux réponses à un modèle inversé

## Astuces

- Combiner réunit malgré tout des objets qui ne se chevauchent pas en un seul maillage, mais ils restent visuellement séparés
- Combiner gère les objets Trou pour vous : tout ce qui est marqué comme trou est soustrait du résultat au lieu de lui être ajouté
- Combiner conserve les couleurs par face des objets d'origine
- Si un résultat semble incorrect, vérifiez que les objets sources sont étanches. **Réparer l'ordre d'enroulement** corrige les coques inversées ; [Réparer](../mesh/repair.md) corrige des dommages plus étendus dans les modèles importés

## Voir aussi

- [Soustraire](subtract.md) - Découper une forme dans une autre
- [Intersecter](intersect.md) - Ne conserver que le volume où les objets se chevauchent
- [Soustraire et Remplacer](subtract-and-replace.md) - Soustraire une forme et conserver la pièce retirée
- [Coupe par plan](../reshape/plane-cut.md) - Couper avec un plan plutôt qu'avec une autre forme
- [Trou](../../primitives/hole.md) - Un cube préconfiguré pour être soustrait
- [Réparer](../mesh/repair.md) - Corriger les maillages importés endommagés avant un booléen

Cette page couvre également les anciens objets Combiner que l'on trouve encore dans les conceptions enregistrées avant la fusion des opérations. Ils continuent de fonctionner exactement comme avant ; les nouvelles conceptions utilisent l'objet booléen commun avec l'opération Combiner sélectionnée.
