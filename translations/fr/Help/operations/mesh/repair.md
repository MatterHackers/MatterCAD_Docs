---
title: Réparer
articleKey: RepairObject3D_2
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: f637470dee4f722b595f07d2da9dcdaac5e8da72
source_lang: en
---
# Réparer

Réparer corrige les problèmes courants de la géométrie du maillage, notamment les arêtes non manifold, les trous, l'orientation des faces incohérente et les sommets presque coïncidents. Cette opération est particulièrement utile pour les fichiers STL et OBJ importés susceptibles de comporter des erreurs.

![20260324 080517 paste 20260324 080517](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080517-paste-20260324-080517.jpg)


## Utilisation

1. Sélectionnez un objet présentant des problèmes de maillage
2. Appliquez l'opération **Réparer** depuis le menu Maillage
3. Examinez les statistiques avant/après pour voir ce qui a été corrigé

## Statistiques (lecture seule)

- **Sommets initiaux / Sommets finaux** - Nombre de sommets avant et après la réparation
- **Faces initiales / Faces finales** - Nombre de faces avant et après la réparation
- **Arêtes non manifold initiales / Arêtes non manifold finales** - Nombre d'arêtes problématiques avant et après

### Options avancées

Activez le mode **Avancé** pour un contrôle précis :

- **Souder les sommets** - Fusionne les sommets presque coïncidents (par défaut : activé)
- **Tolérance de soudure** - Distance maximale entre deux sommets pour qu'ils soient fusionnés
- **Orientation des faces** - Retourne les coques inversées dans le bon sens, afin que chaque corps soit interprété comme solide. Chaque coque est évaluée séparément : un modèle creux conserve donc ses cavités au lieu de les voir comblées. Les coques dont les faces se contredisent entre elles sont laissées telles quelles plutôt que traitées par supposition, et les modèles qui ne sont pas étanches font l'objet d'une réparation plus tolérante - exécutez d'abord **Combler les trous** si l'orientation seule ne les corrige pas.
- **Souder les arêtes** - Répare les petites fissures et les jointures défectueuses
- **Combler les trous** - Comble les lacunes de la surface du maillage
- **Mode Retrait** - Supprime la géométrie interne ou masquée :
  - **Aucun** - Conserve toute la géométrie
  - **Intérieur** - Supprime les corps internes cachés à l'intérieur de la forme principale
  - **Masqué** - Supprime les faces non visibles depuis l'extérieur

## Conseils

- Essayez d'abord Réparer si les opérations booléennes (Combiner, Soustraire) donnent des résultats inattendus sur des modèles importés
- Les réglages par défaut (Souder les sommets activé, tout le reste désactivé) corrigent les problèmes les plus courants
- Activez Combler les trous si vous apercevez des lacunes traversantes dans le modèle
- Utilisez le Mode Retrait Intérieur pour nettoyer les modèles contenant de la géométrie cachée à l'intérieur

## Voir aussi

- [Décimer](decimate.md) - Réduire le nombre de polygones
- [Ajouter des objets existants](../../getting-started/adding-existing-objects.md) - Importer des modèles susceptibles de nécessiter une réparation
