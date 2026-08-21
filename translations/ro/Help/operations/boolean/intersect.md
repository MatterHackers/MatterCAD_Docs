---
title: Intersectare
articleKey: IntersectionObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b997cfc4f6d2f02559346365311f217388a6a2da
source_lang: en
---
# Intersectare

Intersectare păstrează doar volumul comun tuturor obiectelor și elimină restul.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->
![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)

[Combină](combine.md), [Scădere](subtract.md), Intersectare și [Scădere și înlocuire](subtract-and-replace.md) sunt efectuate toate de un singur obiect boolean -- butonul din bara de instrumente îl creează cu Intersectare deja selectată, iar poți comuta oricând la oricare dintre celelalte trei din rândul de pictograme **Operație** aflat în partea de sus a panoului Proprietăți.

Intersectare funcționează atât pe solide, cât și pe trasee 2D. Analizează ceea ce i-ai dat și execută tipul potrivit de operație, astfel încât intersectarea a două trasee produce un traseu, iar intersectarea a două rețele produce un solid.

## Mod de utilizare

1. Selectează două sau mai multe obiecte
2. Apasă **Intersectare** în bara de instrumente
3. Te poți răzgândi oricând apăsând o altă pictogramă din rândul **Operație** aflat în partea de sus a panoului Proprietăți -- forma se reconstruiește cu noua operație

## Parametri

- **Operație** - Ce operație booleană se execută. Afișată ca un rând de pictograme în partea de sus a panoului
- **Păstrează geometria inversată** - Tratează un înveliș inversat ca material solid, în loc să îl lase să anuleze volumul din jurul său. Activează această opțiune când un model care ar trebui să fie solid revine cu părți lipsă. Forțează utilizarea motorului boolean exact, mai lent
- **Repară ordinea de înfășurare** - Reînfășoară învelișurile inversate ale fiecărei părți înainte de rularea operației booleene. Aceasta corectează geometria o singură dată, în loc să schimbe ceea ce fiecare operație ulterioară consideră solid, și este de obicei cea mai bună dintre cele două soluții pentru un model inversat

## Sfaturi

- Obiectele trebuie să se suprapună. Dacă nu se suprapun efectiv, rezultatul este gol
- Cu mai mult de două obiecte, se lucrează în ordinea listei: primele două se intersectează, apoi acel rezultat se intersectează cu al treilea și așa mai departe
- Dacă un rezultat pare greșit, verifică dacă obiectele sursă sunt etanșe. **Repară ordinea de înfășurare** corectează învelișurile inversate; [Repară](../mesh/repair.md) corectează deteriorări mai extinse din modelele importate

## Articole conexe

- [Combină](combine.md) - Îmbină mai multe obiecte într-o singură formă solidă
- [Scădere](subtract.md) - Decupează o formă din alta
- [Scădere și înlocuire](subtract-and-replace.md) - Scade o formă și păstrează bucata care a fost decupată
- [Tăiere cu plan](../reshape/plane-cut.md) - Taie cu un plan plat în loc de altă formă
- [Repară](../mesh/repair.md) - Repară rețelele importate deteriorate înainte de o operație booleană

Această pagină acoperă și obiectele Intersecție mai vechi, întâlnite încă în proiectele salvate înainte de unificarea operațiilor. Ele funcționează în continuare exact ca înainte; proiectele noi folosesc obiectul boolean comun, cu operația Intersectare selectată.
