---
title: Note de versiune
nav_order: 104
source_hash: 3ac9ea595f4f14d23496f8e287ff115f5a7738ff
source_lang: en
---
# MatterCAD 2.2026.8 (13 august 2026)
[Descărcare pentru Windows](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## Caracteristici noi

* **Editare elemente subordonate**
  * Faceți dublu clic pe un obiect de pe platformă sau din arborele scenei pentru a intra în el și a edita părțile din care este construit — fără fereastră sau filă separată
  * Pentru operații precum Scădere, editați părțile sursă, iar rezultatul se reconstruiește când ieșiți înapoi
  * O bară de navigare în partea de sus a arborelui scenei afișează calea completă; un clic pe un nivel integrează modificările ca un singur pas ce poate fi anulat, iar fiecare nivel își păstrează propriul istoric de anulări
  <!-- Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->
  * ![Drill In](https://www.matterhackers.com/r/qgG4VA)

* **Un singur instrument boolean**
  * Combină, Scădere, Intersectare și Scădere și înlocuire sunt acum o singură operație, cu un rând de pictograme în partea de sus a panoului — schimbați modul cu un clic, în loc să ștergeți și să reaplicați
  * Aceeași operație gestionează atât mesh-urile 3D, cât și căile 2D, și afișează progresul în timpul unei operații booleene solicitante
  * Proiectele salvate cu vechile obiecte booleene separate se deschid în continuare normal
  <!-- Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->
  * ![20260810 181041 paste 20260810 181041](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)


* **Operații booleene care funcționează pur și simplu**
  * Operațiile booleene rulează pe un nou motor nativ, care este mai rapid și reușește pe mesh-uri care anterior eșuau
  * Combină repară automat părțile cu goluri: reparațiile curate se alătură reuniunii, părțile care nu pot fi îmbinate în siguranță sunt păstrate alături și denumite pentru dvs., iar o parte care nu a putut fi reparată își păstrează geometria originală
  * Tăiere cu plan este acum o adevărată intersecție solidă, astfel încât rezultatul este etanș și imprimabil, în loc de un înveliș deschis
  * Noile opțiuni Păstrează geometria inversată și Repară ordinea de înfășurare pentru mesh-uri importate problematice


## Îmbunătățiri

* **Editor de cale 2D**
  * Patru moduri de puncte — Ascuțit, Simetric, Aliniat și Liber — aplicate cu un singur clic, atât în editorul 2D, cât și în vizualizarea 3D
  * Oglindire este acum un mod de simetrie în timp real: modificările se oglindesc peste centru pe măsură ce le faceți, iar tragerea unei perechi oglindite pe axă o îmbină într-un singur punct
  * Selectați puncte prin tragere cu un dreptunghi de selecție, mutați-le ca grup, aliniați-le la grilă și apăsați Esc pentru a anula o tragere
  * Netezire potrivește o curbă prin punctele marcate cu clic, într-un singur pas
  <!-- gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

* **Vizualizare și navigare**
  * Apăsați Z cu o cale plană selectată pentru a anima trecerea la o vizualizare de editare perpendiculară, încadrată pe cale
  * Randarea textului la nivel de subpixel este acum activată automat când afișajul o acceptă și poate fi în continuare activată sau dezactivată în setările Avansat

* **Modelare**
  * Extrudare liniară poate teși muchia inferioară cu propriul stil, rază și număr de segmente
  * Obiectele destinate doar editorului (Curbă 3D, Instrument de măsurare, Descriere, Foaie) sunt afișate în continuare, dar sunt excluse din export

## Principalele remedieri de erori

  * O salvare eșuată la jumătate putea trunchia fișierul pe care îl înlocuia, raportând totuși succes. Acum salvările se finalizează complet, apoi înlocuiesc destinația în mod atomic — aceeași protecție acoperă salvările în bibliotecă și exporturile
  * O salvare eșuată lasă proiectul marcat ca nesalvat, astfel încât închiderea aplicației nu vă poate pierde munca în tăcere
  * Salvarea pe disc a unui element din cloud păstra vechiul nume al filei și pierdea fila la repornire
  * S-a remediat eliminarea silențioasă a sub-modelelor 3MF la încărcare, precum și contaminarea reciprocă a fișierelor 3MF încărcate simultan
  * S-au remediat blocaje, un filtru de histogramă defect și copiile unei părți de imagine care nu rămâneau sincronizate cu originalul
  * S-a remediat un blocaj la ștergerea unui punct de curbă, precum și punctele de la cusătura unei căi închise care anulau modul ales
  * Butonul Stop al unei sarcini în curs poate fi acum apăsat și chiar anulează operația

---

# MatterCAD 2.2026.5 (8 mai 2026)
[Descărcare pentru Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMiMyt-ICwwLEgZVcGxvYWQYgIDI7IHKkwoM)

## Caracteristici noi

* **Instrumentul Matrice reproiectat**
  * O singură operație Matrice unificată înlocuiește vechile Serie liniară, Matrice radială și Matrice avansată
  * Modul **Liniar**: copii de-a lungul unei direcții, cu rotație opțională și scalare progresivă
  * Modul **Radial**: copii în jurul unei axe centrale, cu rază, unghi de baleiere și modele de arc sau de cerc complet configurabile
  * Modul **Transformare**: copii pas cu pas folosind o transformare manuală sau transformarea unui obiect frate denumit
  * Modul de rotație Compunere din Liniar creează spirale, evantaie și elice în mod natural
  * Opțiunea Scalarea afectează decalajul pentru dispuneri de tip cochilie de nautil și progresie geometrică
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **Favorite în bibliotecă**
  * Marcați cu stea orice element din bibliotecă pentru a-l adăuga într-un dosar Favorite persistent
  * Accesați rapid, dintr-un singur loc, primitivele, generatoarele și părțile salvate pe care le folosiți cel mai des
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## Îmbunătățiri

* **Aliniere**
  * Alinierea Stivuit este acum un buton de mod direct, în loc de o opțiune dintr-o listă derulantă
  * S-au adăugat moduri mai clare Simplu, Decalaj și Stivuit pentru alinierea muchiilor, adăugarea de spații precise și construirea de stive ordonate
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **Suport pentru fișiere**
  * S-a adăugat suport pentru formatul de imagine WEBP în operațiile bazate pe imagini
  * Analiză îmbunătățită a fișierelor SVG pentru importuri mai fiabile

* **Fiabilitate**
  * Viteză și fiabilitate îmbunătățite la încărcarea fișierelor 3MF
  * Restaurare mai bună a filelor între sesiuni

## Principalele remedieri de erori

* **Autentificare și acces la Bibliotecă cloud**
  * Autentificarea și accesul la Bibliotecă cloud au fost restaurate după ce o actualizare a serverului backend a stricat autentificarea.
  * MatterCAD vă solicită acum să vă autentificați din nou atunci când accesul la cloud găsește credențiale expirate sau invalide.

* **Selecție în arborele scenei**
  * S-a remediat comportamentul inconsecvent al selecției la alegerea obiectelor din arborele scenei.

* **Navigare în ajutor**
  * S-au remediat problemele de navigare din documentația de ajutor și de versiune inclusă.

* **Clic dreapta în bibliotecă**
  * S-a remediat comportamentul clicului dreapta în vizualizarea arborescentă a bibliotecii.

* **Foi**
  * S-a remediat un blocaj care putea apărea în timpul lucrului cu foi.

---

# MatterCAD 2.2026.3 (12 martie 2026)
[Descărcare pentru Windows](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## Caracteristici noi

* **Motor de randare Direct3D 11 complet nou**
  * Migrare completă de la OpenGL la Direct3D 11 pentru performanțe mult mai bune
  * Anti-aliasing FXAA pentru muchii clare și curate
  * Dual depth peeling pentru transparență corectă, independentă de ordine
  * Umbre pe platformă accelerate hardware
  * Contururi de obiecte și elemente vizuale de selecție îmbunătățite
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **Transparență obiect**
  * Setați alfa/transparența pentru orice obiect individual din scenă
  * Mesh-urile cu culoare pe față acceptă alfa fără deteriorarea culorilor
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **Blocarea și ascunderea obiectelor**
  * Blocați obiecte pentru a preveni selectarea sau editarea accidentală
  * Ascundeți obiecte pentru a reduce dezordinea vizuală în timp ce lucrați la anumite părți
  * Comenzile Afișează tot și Deblochează tot pentru a restabili rapid vizibilitatea
  * Obiectele blocate și ascunse sunt excluse corect din selecția bazată pe raze
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **Scădere booleană îmbunătățită**
  * Operațiile de scădere multiplă sunt semnificativ mai fiabile și mai precise

## Îmbunătățiri

* **Gestionarea fișierelor**
  * Proiectele se salvează acum implicit ca 3MF în loc de STL, păstrând culorile, materialele și istoricul de proiectare
  * Suport îmbunătățit pentru glisarea și plasarea fișierelor și folderelor în vizualizarea 3D

* **Flux de lucru**
  * Dialogurile Salvare ca și Mutare rețin ultima locație de folder
  * Câmpurile de expresii acceptă acum `pi`, `tau`, `e` și `count`
  * Tasta Esc efectuează anularea în contextele de editare a proiectelor
  * Controalele 3D rămân vizibile când mouse-ul părăsește scena

* **Performanță și stabilitate**
  * S-au remediat blocajele la pornire și problemele de încărcare recursivă
  * S-au remediat erorile de randare privind iluminarea și mipmapping-ul
  * Actualizări îmbunătățite ale vizualizării arborescente a bibliotecii
  * Calcule dinamice ale planurilor apropiat/îndepărtat pentru un comportament mai bun al zoomului
  * Actualizare la .NET 10

---

# MatterCAD 2.2025.6 (20 iunie 2025)
[Descărcare pentru Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## Caracteristici noi

* **Suport pentru Fișier SVG**  
  * Suport complet de glisare și plasare pentru fișiere SVG
  * Conversie directă din grafică SVG în obiecte 3D
  * Integrare perfectă cu fluxurile de lucru CAD existente

* **Gestionare avansată a fișierelor OBJ**  
  * Suport pentru încărcarea materialelor din arhive ZIP
  * Analiză îmbunătățită a fișierelor OBJ și gestionare îmbunătățită a materialelor
  * Suport mai bun pentru modele 3D complexe, cu materiale multiple

* **Sistem îmbunătățit de gestionare a filelor**
  * Filele bibliotecii cloud persistă acum corect — munca dvs. rămâne exact acolo unde ați lăsat-o
  * Organizare și navigare îmbunătățite ale filelor
  * Restaurarea automată a filelor deschise între sesiuni

## Îmbunătățiri ale experienței utilizatorului

* **Interfață simplificată**
  * Meniu Recente reorganizat pentru acces mai rapid
  * Feedback vizual mai bun în timpul operațiilor lungi
  * Timp de pornire și reactivitate îmbunătățite ale aplicației

* **Fiabilitate**
  * S-au remediat blocaje critice în interacțiunile cu scena 3D
  * S-au rezolvat probleme de gestionare a memoriei
  * Stabilitate îmbunătățită a aplicației pe toate platformele

---

# MatterCAD 2.21.5 (13 feb. 2025)

[Descărcare pentru Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# Caracteristici existente

*Următoarele caracteristici reprezintă fundația pe care MatterCAD o construiește pornind de la moștenirea MatterControl:*

* S-a adăugat caracteristica Gol  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* S-a adăugat Reducere poligoane  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* S-a adăugat Repară mesh  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* S-a inclus suportul complet automat (suport moștenit) ca opțiune, pe lângă noua opțiune de suport manual
* S-a adăugat suport pentru gsSlicer (motor experimental nou de feliere)
* S-au remediat erori

## Modificări

* Degrupare îmbunătățită a mesh-urilor (împărțire în mai multe mesh-uri)
    * Eliminarea fețelor degenerate
    * Eliminarea caracteristicilor discrete microscopice

## Modificări

* S-a adăugat o bară de căutare pentru aplicație
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* Bară de instrumente de proiectare îmbunătățită
    * S-a adăugat gruparea unor elemente
    * S-a adăugat buton de aliniere duală
    * S-a adăugat butonul Aranjare toate
* Deplasați elementele de pe platformă cu tastele săgeți
* Dosarul Descărcări este sortat după dată

## Modificări

* Îmbunătățiri ale interfeței
    * Actualizări mai rapide în dosarele Bibliotecă cloud
    * Restaurarea interfeței la redeschidere
    * Suport îmbunătățit pentru navigarea cu tastatura
* Sistem nou de detectare a erorilor și de avertizare
    * Mai multe erori hardware gestionate
* Îmbunătățiri și optimizări ale instrumentelor de proiectare
    * Instrumente noi de Răsucire 
    * Instrument Curbă îmbunătățit
    * Aliniere îmbunătățită


## Modificări

* Aplatizare îmbunătățită
* Suport îmbunătățit pentru anulare
* Istoric de proiectare îmbunătățit

## Modificări
* Versionare: trecerea la un număr de versiune de forma (versiune).(an).(lună). Mai ușor de citit și mai informativ.
* Noile Scădere, Combină și Intersecție de ultimă generație (doar Windows)
* Aplicația pornește acum cu un „Tur al caracteristicilor” care îi ajută pe utilizatorii noi să se orienteze

## Modificări
* Instrumente de proiectare - Posibilitatea de a modela 3D cu un set complet de primitive de modelare
* Folosiți o primitivă pentru a crea propriile suporturi personalizate
* Aplicații de proiectare - Aplicații de proiectare: modele sofisticate și personalizabile
* Procesare pe 64 de biți
