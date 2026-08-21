---
title: Nouveautés
nav_order: 105
source_hash: 172343b8320204d2b0ec52419324f0efd2be95a1
source_lang: en
---
# MatterCAD 2.2026.8

# Nouveautés

* **Modifier les enfants**
  * Double-cliquez sur n'importe quel objet pour entrer dedans et modifier les pièces qui le composent, directement sur le plateau
  * Un fil d'Ariane indique où vous vous trouvez — cliquez sur n'importe quel niveau pour réintégrer vos modifications
  * ![MatterCAD 2.2026.8](https://www.matterhackers.com/r/qgG4VA)

* **Un seul outil booléen**
  * Combiner, Soustraire, Intersecter ainsi que Soustraire et remplacer ne forment plus qu'une seule opération — changez de mode d'un clic au lieu de supprimer puis réappliquer
  <!-- Boolean property panel showing the four-icon operation row with Subtract selected. ~500x350px -->
  * ![One Boolean Tool](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)

* **Des booléens qui fonctionnent enfin**
  * Un nouveau moteur, plus rapide, réussit sur des maillages qui échouaient auparavant
  * Combiner répare automatiquement les pièces comportant des trous et nomme tout ce qu'il n'a pas pu fusionner ; Coupe par plan produit désormais un solide étanche et imprimable

* **Meilleure édition des chemins 2D**
  * Modes de point, Symétrie en direct, magnétisme sur la grille, sélection par glissement et Échap pour annuler un glissement
  <!-- Turn on Mirror, drag a point and watch its partner follow, then drag it onto the axis to merge. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

## Améliorations

* **Navigation** — Appuyez sur Z avec un chemin 2D sélectionné pour obtenir une vue d'édition de dessus
* **Texte plus net** — Le rendu de texte sous-pixel est désormais activé automatiquement lorsque votre écran le prend en charge
* **Modélisation** — Extrusion linéaire peut chanfreiner l'arête inférieure avec son propre style, son rayon et son nombre de segments

## Principales corrections de bugs

* **Fiabilité de l'enregistrement** — Un enregistrement échoué ne peut plus endommager le fichier qu'il remplaçait, et il vous signale son échec
* **Bibliothèque cloud** — L'enregistrement d'un élément cloud sur le disque conserve le nom de son onglet, et l'onglet est conservé après un redémarrage
* **Chargement de fichiers** — Correction de pièces 3MF ignorées silencieusement au chargement
* **Édition de chemins** — Correction d'un plantage lors de la suppression d'un point de courbe, et des points de raccord qui rétablissaient le mode choisi
* **Tâches en arrière-plan** — Le bouton Arrêter d'une tâche en cours est désormais cliquable et annule réellement la tâche

## Vous pouvez consulter les notes de version complètes [Ici](release-notes.md).
