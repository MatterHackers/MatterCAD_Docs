---
title: Foire aux questions
nav_order: 101
source_hash: 929ea9e89d3f5008996615341418ba715d3f6075
source_lang: en
---
# Pourquoi mes objets sont-ils à la mauvaise échelle ?
- Les fichiers STL ne conservent aucune information d'unité. MatterCAD s'attend à des dimensions STL exprimées en millimètres, alors que la plupart des logiciels de CAO exportent dans leurs unités natives (généralement des pouces). Cela provoque des écarts d'échelle lors de l'importation des conceptions.

- La meilleure solution consiste à configurer votre logiciel de conception pour qu'il exporte les fichiers STL en millimètres. Par exemple, dans SolidWorks, utilisez le bouton Options de la boîte de dialogue **Enregistrer sous** pour définir les paramètres d'exportation STL.

- Vous pouvez aussi redimensionner la pièce directement dans MatterCAD. Dans l'**Affichage** 3D, passez en mode **Modifier** et sélectionnez ÉCHELLE dans la barre d'outils de droite. Utilisez le menu déroulant pour appliquer les facteurs de conversion courants ou saisissez des dimensions précises dans les champs des axes.

# Comment effacer les données de l'application ?

- Si la réinstallation ne résout pas un problème, il peut être nécessaire de supprimer les données enregistrées par MatterCAD. Ces données subsistent après la désinstallation. Pour rétablir complètement les paramètres par défaut, supprimez le dossier de l'application. Vous pouvez aussi renommer temporairement le fichier de base de données SQLite (MatterCAD.db) afin de vérifier si les paramètres sont à l'origine du problème.
![20260318 194137 paste 20260318 194137](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194137-paste-20260318-194137.jpg)

![20260318 194200 paste 20260318 194200](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194200-paste-20260318-194200.jpg)

![20260318 194218 paste 20260318 194218](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194218-paste-20260318-194218.jpg)


- Windows
  - La bibliothèque utilisateur et les paramètres sont stockés dans C:\Users\{user}\AppData\Local\MatterCAD.
