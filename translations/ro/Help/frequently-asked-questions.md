---
title: Întrebări frecvente
nav_order: 101
source_hash: 929ea9e89d3f5008996615341418ba715d3f6075
source_lang: en
---
# De ce obiectele mele au scara greșită?
- Fișierele STL nu stochează informații despre unitățile de măsură. MatterCAD se așteaptă ca dimensiunile STL să fie în milimetri, în timp ce majoritatea programelor CAD exportă în unitățile lor native (de obicei inci). Acest lucru cauzează discrepanțe de scară la importul proiectelor.

- Cea mai bună soluție este să configurați programul de proiectare astfel încât să exporte fișierele STL în milimetri. De exemplu, în SolidWorks, folosiți butonul Opțiuni din fereastra Salvare ca pentru a seta parametrii de export STL.

- Ca alternativă, puteți redimensiona piesa direct în MatterCAD. În Vizualizare 3D, intrați în modul Editare și selectați SCALARE din bara de instrumente din dreapta. Folosiți meniul derulant pentru factorii de conversie uzuali sau introduceți dimensiuni specifice în câmpurile axelor.

# Cum șterg datele aplicației?

- Dacă reinstalarea nu rezolvă o problemă, este posibil să fie nevoie să ștergeți datele stocate de MatterCAD. Aceste date rămân și după dezinstalare. Pentru a reveni complet la setările implicite, efectuați eliminarea folderului aplicației. De asemenea, puteți redenumi temporar fișierul bazei de date SQLite (MatterCAD.db) pentru a testa dacă setările cauzează probleme.
![20260318 194137 paste 20260318 194137](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194137-paste-20260318-194137.jpg)

![20260318 194200 paste 20260318 194200](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194200-paste-20260318-194200.jpg)

![20260318 194218 paste 20260318 194218](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194218-paste-20260318-194218.jpg)


- Windows
  - Biblioteca utilizatorului și setările sunt stocate în C:\Users\{user}\AppData\Local\MatterCAD.
