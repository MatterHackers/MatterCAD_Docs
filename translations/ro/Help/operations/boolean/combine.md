---
title: Combină
articleKey: CombineObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: a3066faa634b5a88a2fe1650a4e2ac278ac50e24
source_lang: en
---
# Combină

Combină unește totul într-un singur solid. Fețele interne, acolo unde formele se suprapuneau, sunt eliminate, astfel încât rezultatul este o singură plasă continuă, nu învelișuri suprapuse.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->
![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)

Combină, [Scădere](subtract.md), [Intersectare](intersect.md) și [Scădere și Înlocuiește](subtract-and-replace.md) sunt toate efectuate de un singur obiect boolean -- butonul din bara de instrumente îl creează având deja selectată operația Combină, iar tu poți comuta oricând la oricare dintre celelalte trei din rândul de pictograme **Operație** aflat în partea de sus a panoului Proprietăți.

Combină funcționează atât pe solide, cât și pe trasee 2D. Analizează ce i-ai dat și execută tipul potrivit de operație, astfel încât combinarea a două trasee produce un traseu, iar combinarea a două plase produce un solid.

## Mod de utilizare

1. Selectează două sau mai multe obiecte
2. Fă clic pe **Combină** în bara de instrumente
3. Te poți răzgândi oricând făcând clic pe o altă pictogramă din rândul **Operație** aflat în partea de sus a panoului Proprietăți -- forma se reconstruiește cu noua operație

## Parametri

- **Operație** - Ce operație booleană se execută. Afișată ca un rând de pictograme în partea de sus a panoului
- **Păstrează geometria inversată** - Tratează un înveliș inversat ca material solid, în loc să îl lase să anuleze volumul din jurul său. Activează această opțiune atunci când un model care ar trebui să fie solid apare cu porțiuni lipsă. Forțează utilizarea motorului boolean exact, mai lent
- **Repară ordinea de înfășurare** - Reînfășoară învelișurile inversate ale fiecărei părți înainte de rularea operației booleene. Aceasta corectează geometria o singură dată, în loc să schimbe ce anume consideră solid fiecare operație ulterioară, și este de obicei cel mai bun dintre cele două răspunsuri la un model inversat

## Sfaturi

- Combină va uni într-o singură plasă și obiectele care nu se suprapun, dar acestea rămân separate vizual
- Combină se ocupă în locul tău de obiectele Gaură: orice este marcat ca gaură este scăzut din rezultat, în loc să fie adăugat la acesta
- Combină preia culorile pe fețe din obiectele originale
- Dacă un rezultat arată greșit, verifică dacă obiectele sursă sunt etanșe. **Repară ordinea de înfășurare** corectează învelișurile inversate; [Repară](../mesh/repair.md) corectează deteriorări mai extinse din modelele importate

## Articole conexe

- [Scădere](subtract.md) - Decupează o formă din alta
- [Intersectare](intersect.md) - Păstrează doar volumul în care obiectele se suprapun
- [Scădere și Înlocuiește](subtract-and-replace.md) - Scade o formă și păstrează bucata care a fost decupată
- [Tăiere cu plan](../reshape/plane-cut.md) - Taie cu un plan plat în loc de o altă formă
- [Gaură](../../primitives/hole.md) - Un cub preconfigurat pentru scădere
- [Repară](../mesh/repair.md) - Repară plasele importate deteriorate înainte de o operație booleană

Această pagină acoperă și obiectele Combină mai vechi, întâlnite încă în proiectele salvate înainte de unificarea operațiilor. Ele funcționează exact ca înainte; proiectele noi folosesc obiectul boolean comun, cu operația Combină selectată.
