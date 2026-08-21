---
title: Notes de version
nav_order: 104
source_hash: 3ac9ea595f4f14d23496f8e287ff115f5a7738ff
source_lang: en
---
# MatterCAD 2.2026.8 (13 août 2026)
[Téléchargement Windows](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## Nouvelles fonctionnalités

* **Modifier les enfants**
  * Double-cliquez sur un objet posé sur le plateau ou présent dans l'arborescence de la scène pour entrer dedans et modifier les pièces qui le composent — sans fenêtre ni onglet séparé
  * Pour des opérations comme Soustraire, vous modifiez les pièces sources et le résultat est reconstruit lorsque vous ressortez
  * Un fil d'Ariane en haut de l'arborescence de la scène affiche le chemin complet ; cliquer sur un niveau intègre vos modifications en une seule étape annulable, et chaque niveau conserve son propre historique d'annulation
  <!-- Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->
  * ![Drill In](https://www.matterhackers.com/r/qgG4VA)

* **Un seul outil booléen**
  * Combiner, Soustraire, Intersecter et Soustraire et remplacer ne forment plus qu'une seule opération, dotée d'une rangée d'icônes en haut de son panneau — changez de mode d'un clic au lieu de supprimer puis de réappliquer
  * La même opération prend en charge aussi bien les maillages 3D que les chemins 2D, et affiche la progression pendant l'exécution d'un booléen lourd
  * Les conceptions enregistrées avec les anciens objets booléens séparés continuent de s'ouvrir normalement
  <!-- Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->
  * ![20260810 181041 paste 20260810 181041](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)


* **Des booléens qui fonctionnent enfin**
  * Les booléens s'appuient sur un nouveau moteur natif, plus rapide et capable de traiter des maillages qui échouaient auparavant
  * Combiner répare automatiquement les pièces comportant des trous : les réparations propres rejoignent l'union, les pièces qui ne peuvent pas être fusionnées en toute sécurité sont conservées à côté et nommées pour vous, et une pièce qui n'a pas pu être réparée conserve votre géométrie d'origine
  * Coupe par plan est désormais une véritable intersection solide : le résultat est étanche et imprimable au lieu d'être une coque ouverte
  * Nouvelles options Conserver la géométrie inversée et Réparer l'ordre d'enroulement pour les maillages importés problématiques


## Améliorations

* **Éditeur de chemin 2D**
  * Quatre modes de point — Anguleux, Symétrique, Aligné et Libre — appliqués d'un seul clic, aussi bien dans l'éditeur 2D que dans la vue 3D
  * Symétrie est désormais un mode de symétrie en direct : les modifications sont reflétées de part et d'autre du centre au fur et à mesure, et faire glisser une paire symétrique sur l'axe la fusionne en un seul point
  * Sélectionnez des points par rectangle de sélection, déplacez-les en groupe, alignez-les sur la grille et appuyez sur Échap pour annuler un déplacement
  * Lisser fait passer une courbe par les points que vous avez placés, en une seule étape
  <!-- gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

* **Affichage et navigation**
  * Appuyez sur Z lorsqu'un chemin plat est sélectionné pour passer, avec animation, à une vue d'édition en plongée verticale ajustée au chemin
  * Le rendu de texte sous-pixel est désormais activé automatiquement lorsque votre écran le prend en charge, et reste activable ou désactivable dans les paramètres Avancé

* **Modélisation**
  * Extrusion linéaire peut chanfreiner l'arête inférieure avec son propre style, son rayon et son nombre de segments
  * Les objets réservés à l'éditeur (Courbe 3D, Outil de mesure, Description, Feuille) restent affichés mais sont exclus de l'export

## Principales corrections de bugs

  * Un enregistrement interrompu en cours de route pouvait tronquer le fichier qu'il remplaçait tout en signalant une réussite. Les enregistrements se terminent désormais entièrement, puis remplacent la destination de manière atomique — la même protection couvre les enregistrements dans la bibliothèque et les exports
  * Un enregistrement échoué laisse la conception marquée comme non enregistrée, afin que la fermeture de l'application ne puisse pas supprimer silencieusement votre travail
  * L'enregistrement sur disque d'un élément cloud conservait l'ancien nom d'onglet et perdait l'onglet au redémarrage
  * Correction de sous-modèles 3MF ignorés silencieusement au chargement, et de fichiers 3MF chargés en même temps qui se contaminaient mutuellement
  * Correction de plantages, d'un filtre d'histogramme défectueux et de copies d'une pièce image qui ne restaient pas synchronisées avec l'original
  * Correction d'un plantage lors de la suppression d'un point de courbe, et de points situés à la jonction d'un chemin fermé qui annulaient le mode choisi
  * Le bouton Arrêter d'une tâche en cours est désormais cliquable et l'annule réellement

---

# MatterCAD 2.2026.5 (8 mai 2026)
[Téléchargement Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMiMyt-ICwwLEgZVcGxvYWQYgIDI7IHKkwoM)

## Nouvelles fonctionnalités

* **Outil Réseau repensé**
  * Une seule opération Réseau unifiée remplace les anciens Réseau linéaire, Réseau radial et Réseau avancé
  * Mode **Linéaire** : copies selon une direction, avec rotation facultative et mise à l'échelle progressive
  * Mode **Radial** : copies autour d'un axe central, avec rayon, angle de balayage et motifs en arc ou en cercle complet configurables
  * Mode **Transformer** : copies pas à pas à l'aide d'une transformation manuelle ou de la transformation d'un objet frère nommé
  * Le mode de rotation Composition dans Linéaire crée naturellement des spirales, des éventails et des hélices
  * Option L'échelle affecte le décalage pour des dispositions en coquille de nautile et en progression géométrique
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **Favoris de la bibliothèque**
  * Marquez d'une étoile n'importe quel élément de la bibliothèque pour l'ajouter à un dossier Favoris persistant
  * Accédez rapidement, depuis un seul endroit, à vos primitives, générateurs et pièces enregistrées les plus utilisés
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## Améliorations

* **Aligner**
  * L'alignement Empilé est désormais un bouton de mode direct au lieu d'une option de liste déroulante
  * Ajout de modes Simple, Décalage et Empilé plus clairs pour aligner les arêtes, ajouter des écarts précis et construire des piles ordonnées
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **Prise en charge des fichiers**
  * Ajout de la prise en charge du format d'image WEBP dans les opérations basées sur des images
  * Analyse des fichiers SVG améliorée pour des imports plus fiables

* **Fiabilité**
  * Vitesse et fiabilité du chargement des fichiers 3MF améliorées
  * Meilleure restauration des onglets entre les sessions

## Principales corrections de bugs

* **Connexion et accès à la Bibliothèque cloud**
  * La connexion et l'accès à la Bibliothèque cloud sont rétablis après une mise à niveau du serveur principal qui avait cassé l'authentification.
  * MatterCAD vous invite désormais à vous connecter de nouveau lorsque l'accès au cloud détecte des identifiants expirés ou non valides.

* **Sélection dans l'arborescence de la scène**
  * Correction d'un comportement de sélection incohérent lors du choix d'objets dans l'arborescence de la scène.

* **Navigation dans l'aide**
  * Correction de problèmes de navigation dans l'aide intégrée et la documentation des versions.

* **Clic droit dans la bibliothèque**
  * Correction du comportement du clic droit dans l'arborescence de la bibliothèque.

* **Feuilles**
  * Correction d'un plantage pouvant survenir lors du travail avec des feuilles.

---

# MatterCAD 2.2026.3 (12 mars 2026)
[Téléchargement Windows](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## Nouvelles fonctionnalités

* **Tout nouveau moteur de rendu Direct3D 11**
  * Migration complète d'OpenGL vers Direct3D 11 pour des performances nettement supérieures
  * Anticrénelage FXAA pour des arêtes nettes et propres
  * Double depth peeling pour une transparence correcte indépendante de l'ordre
  * Ombres du plateau accélérées par le matériel
  * Contours des objets et visuels de sélection améliorés
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **Transparence des objets**
  * Définissez l'alpha/la transparence de n'importe quel objet de la scène
  * Les maillages à couleur par face prennent en charge l'alpha sans altération des couleurs
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **Verrouiller et masquer les objets**
  * Verrouillez des objets pour empêcher toute sélection ou modification accidentelle
  * Masquez des objets pour réduire l'encombrement visuel pendant que vous travaillez sur des pièces précises
  * Commandes Tout afficher et Tout déverrouiller pour rétablir rapidement la visibilité
  * Les objets verrouillés et masqués sont correctement exclus de la sélection par rayon
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **Soustraire booléen amélioré**
  * Les opérations de soustraction multiple sont nettement plus fiables et précises

## Améliorations

* **Gestion des fichiers**
  * Les projets sont désormais enregistrés au format 3MF par défaut au lieu de STL, ce qui préserve les couleurs, les matériaux et l'historique de conception
  * Prise en charge améliorée du glisser-déposer de fichiers et de dossiers dans la vue 3D

* **Flux de travail**
  * Les boîtes de dialogue Enregistrer sous et Déplacer mémorisent votre dernier dossier
  * Les champs d'expression prennent désormais en charge `pi`, `tau`, `e` et `count`
  * La touche Échap effectue une annulation dans les contextes d'édition de conception
  * Les contrôles 3D restent visibles lorsque la souris quitte la scène

* **Performances et stabilité**
  * Correction de plantages au démarrage et de problèmes de chargement récursif
  * Correction de bugs de rendu liés à l'éclairage et au mipmapping
  * Mises à jour améliorées de l'arborescence de la bibliothèque
  * Calculs dynamiques des plans proche/lointain pour un meilleur comportement du zoom
  * Mise à niveau vers .NET 10

---

# MatterCAD 2.2025.6 (20 juin 2025)
[Téléchargement Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## Nouvelles fonctionnalités

* **Prise en charge des fichiers SVG**  
  * Prise en charge complète du glisser-déposer pour les fichiers SVG
  * Conversion directe de graphiques SVG en objets 3D
  * Intégration transparente aux flux de travail CAO existants

* **Gestion avancée des fichiers OBJ**  
  * Prise en charge du chargement de matériaux depuis des archives ZIP
  * Analyse des fichiers OBJ et gestion des matériaux améliorées
  * Meilleure prise en charge des modèles 3D complexes comportant plusieurs matériaux

* **Système de gestion des onglets amélioré**
  * Les onglets de la Bibliothèque cloud persistent désormais correctement - votre travail reste exactement là où vous l'avez laissé
  * Organisation et navigation des onglets améliorées
  * Restauration automatique des onglets ouverts entre les sessions

## Améliorations de l'expérience utilisateur

* **Interface simplifiée**
  * Menu Récents réorganisé pour un accès plus rapide
  * Meilleur retour visuel pendant les opérations longues
  * Temps de démarrage et réactivité de l'application améliorés

* **Fiabilité**
  * Correction de plantages critiques lors des interactions avec la scène 3D
  * Résolution de problèmes de gestion de la mémoire
  * Stabilité de l'application améliorée sur toutes les plateformes

---

# MatterCAD 2.21.5 (13 février 2025)

[Téléchargement Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# Fonctionnalités existantes

*Les fonctionnalités suivantes constituent la base dont MatterCAD hérite de MatterControl :*

* Ajout de la fonction Creux  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* Ajout de Réduire les polygones  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* Ajout de Réparer le maillage  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* Ajout des supports entièrement automatiques (supports hérités) en option, en plus de la nouvelle option de supports manuels
* Ajout de la prise en charge de gsSlicer (nouveau moteur de découpe expérimental)
* Correction de bugs

## Changements

* Dégroupage des maillages amélioré (division en plusieurs maillages)
    * Suppression des faces dégénérées
    * Suppression des détails discrets microscopiques

## Changements

* Ajout d'une barre de recherche pour l'application
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* Barre d'outils de conception améliorée
    * Ajout d'un regroupement pour certains éléments
    * Ajout d'un bouton d'alignement double
    * Ajout d'un bouton Tout disposer
* Déplacez les éléments sur le plateau avec les touches fléchées
* Le dossier Téléchargements est trié par date

## Changements

* Améliorations de l'interface
    * Mises à jour plus rapides dans les dossiers de la Bibliothèque cloud
    * Restauration de l'interface à la réouverture
    * Meilleure prise en charge de la navigation au clavier
* Nouveau système de détection d'erreurs et d'avertissements
    * Davantage d'erreurs matérielles prises en charge
* Améliorations et optimisations des Outils de conception
    * Nouveaux outils Torsion 
    * Outil Courbe amélioré
    * Aligner amélioré


## Changements

* Aplatissement amélioré
* Prise en charge de l'annulation améliorée
* Historique de conception amélioré

## Changements
* Gestion des versions : passage à un numéro de version (version).(année).(mois). Plus facile à lire et plus informatif.
* Nouvelles opérations Soustraire, Combiner et Intersecter à la pointe de la technologie (Windows uniquement)
* L'application démarre désormais par une « visite guidée des fonctionnalités » pour aider les nouveaux utilisateurs à s'orienter

## Changements
* Outils de conception - La possibilité de modéliser en 3D avec un ensemble complet de primitives de modélisation
* Utilisez une primitive pour créer vos propres supports personnalisés
* Applications de conception - Applications de conception : des conceptions sophistiquées et personnalisables
* Traitement 64 bits
