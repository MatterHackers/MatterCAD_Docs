---
title: Scade și înlocuiește
articleKey: SubtractAndReplaceObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c1698bab75faca8046b23cc148803c8063ba0678
source_lang: en
---
# Scade și înlocuiește

Scade și înlocuiește scade piesele alese din piesele nealese, dar păstrează bucata decupată ca piesă de sine stătătoare, în loc să o elimine. Folosește **Piesă/piese de scăzut** pentru a alege formele care taie; tot restul reprezintă baza care este tăiată.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->
![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)

[Combină](combine.md), [Scădere](subtract.md), [Intersectare](intersect.md) și Scade și înlocuiește sunt realizate toate de un singur obiect boolean -- butonul din bara de instrumente îl creează cu **Scade și înlocuiește** deja selectată, iar tu poți comuta oricând la oricare dintre celelalte trei din rândul de pictograme **Operație** aflat în partea de sus a panoului Proprietăți.

Scade și înlocuiește nu este disponibilă pentru traseele 2D -- o regiune nu are volum eliminat care să poată fi returnat.

## Mod de utilizare

1. Selectează două sau mai multe obiecte
2. Apasă **Scade și înlocuiește** în bara de instrumente
3. Folosește **Piesă/piese de scăzut** pentru a alege care obiecte-copil sunt formele care taie
4. Te poți răzgândi oricând apăsând o altă pictogramă din rândul **Operație** aflat în partea de sus a panoului Proprietăți -- forma se reconstruiește cu noua operație

## Parametri

- **Operație** - Ce operație booleană se execută. Afișată ca un rând de pictograme în partea de sus a panoului
- **Piesă/piese de scăzut** - Care obiecte-copil sunt formele care taie
- **Păstrează geometria inversată** - Tratează o coajă inversată ca material solid, în loc să o lase să anuleze volumul din jurul ei. Activează această opțiune când un model care ar trebui să fie solid apare cu porțiuni lipsă. Forțează utilizarea motorului boolean exact, mai lent
- **Repară ordinea de înfășurare** - Reface înfășurarea cojilor inversate ale fiecărei piese înainte de executarea operației booleene. Aceasta corectează geometria o singură dată, în loc să schimbe ceea ce fiecare operație ulterioară consideră solid, și este de obicei cea mai bună dintre cele două soluții pentru un model inversat

## Sfaturi

- Cele două piese se potrivesc perfect, pentru că provin din aceeași operație
- Folosește-o pentru modele multicolore, ansambluri care se îmbină și incrustații
- Dacă rezultatul pare greșit, verifică dacă obiectele sursă sunt etanșe. **Repară ordinea de înfășurare** corectează cojile inversate; [Repară](../mesh/repair.md) remediază deteriorări mai extinse în modelele importate

## Articole conexe

- [Combină](combine.md) - Îmbină mai multe obiecte într-o singură formă solidă
- [Scădere](subtract.md) - Taie o formă din alta
- [Intersectare](intersect.md) - Păstrează doar volumul în care obiectele se suprapun
- [Tăiere cu plan](../reshape/plane-cut.md) - Taie cu un plan plat în loc de o altă formă
- [Repară](../mesh/repair.md) - Repară plasele importate deteriorate înainte de o operație booleană

Această pagină acoperă și obiectele mai vechi Scade și înlocuiește, întâlnite încă în modelele salvate înainte de unificarea operațiilor. Ele funcționează exact ca înainte; modelele noi folosesc obiectul boolean comun, cu operația Scade și înlocuiește selectată.
