---
title: Scădere
articleKey: SubtractObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 59685bd0a635b70d7f938780f71e90be595dd993
source_lang: en
---
# Scădere

Scăderea decupează piesele pe care le alegi din piesele pe care nu le-ai ales. Folosește **Piesă/piese de scăzut** pentru a selecta formele de decupare; tot restul reprezintă baza care este decupată.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->
![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)

[Combină](combine.md), Scădere, [Intersectare](intersect.md) și [Scădere și înlocuire](subtract-and-replace.md) sunt toate realizate de un singur obiect boolean -- butonul din bara de instrumente îl creează având deja selectată operația Scădere, iar poți comuta oricând la oricare dintre celelalte trei din rândul de pictograme **Operație** aflat în partea de sus a panoului Proprietăți.

Scăderea funcționează pe solide și pe trasee 2D. Analizează ceea ce i-ai furnizat și execută tipul corect de operație, astfel încât scăderea unui traseu din altul produce un traseu, iar scăderea unei rețele din alta produce un solid.

## Mod de utilizare

1. Selectează două sau mai multe obiecte
2. Apasă **Scădere** în bara de instrumente -- o piesă implicită de decupat este aleasă pentru tine, astfel încât operația face ceva imediat
3. Folosește **Piesă/piese de scăzut** pentru a alege ce obiecte-copil sunt formele de decupare
4. Te poți răzgândi oricând apăsând o altă pictogramă din rândul **Operație** din partea de sus a panoului Proprietăți -- forma se reconstruiește cu noua operație

## Parametri

- **Operație** - Ce operație booleană se execută. Afișată ca rând de pictograme în partea de sus a panoului
- **Piesă/piese de scăzut** - Care dintre obiectele-copil sunt formele de decupare
- **Păstrează piesele scăzute** - Lasă în scenă piesele care au fost decupate, în loc să le elimine
- **Păstrează geometria inversată** - Tratează un înveliș întors pe dos ca material solid, în loc să îl lase să anuleze volumul din jurul său. Activează această opțiune atunci când un model care ar trebui să fie solid revine cu porțiuni lipsă. Forțează utilizarea motorului boolean exact, mai lent
- **Repară ordinea de înfășurare** - Reînfășoară învelișurile întoarse pe dos ale fiecărei piese înainte de rularea operației booleene. Aceasta corectează geometria o singură dată, în loc să schimbe ceea ce fiecare operație ulterioară consideră solid, și este de obicei cel mai bun dintre cele două răspunsuri pentru un model întors pe dos

## Sfaturi

- Obiectele trebuie să se suprapună pentru ca Scăderea să aibă vreun efect
- Pentru a decupa o gaură străpunsă, asigură-te că obiectul de decupare trece complet prin bază
- Pentru o gaură simplă, primitiva [Gaură](../../primitives/hole.md) este deja configurată pentru scădere
- Obiectele de decupare rămân în arborele proiectului, astfel încât le poți muta sau redimensiona, iar decuparea se actualizează
- Dacă un rezultat pare greșit, verifică dacă obiectele sursă sunt etanșe. **Repară ordinea de înfășurare** corectează învelișurile întoarse pe dos; [Repară](../mesh/repair.md) corectează deteriorări mai extinse în modelele importate

## Subiecte conexe

- [Combină](combine.md) - Îmbină mai multe obiecte într-o singură formă solidă
- [Intersectare](intersect.md) - Păstrează doar volumul în care obiectele se suprapun
- [Scădere și înlocuire](subtract-and-replace.md) - Scade o formă și păstrează bucata care a fost decupată
- [Tăiere cu plan](../reshape/plane-cut.md) - Decupează cu un plan drept în loc de altă formă
- [Gaură](../../primitives/hole.md) - Un cub preconfigurat pentru scădere
- [Repară](../mesh/repair.md) - Repară rețelele importate deteriorate înainte de o operație booleană

Această pagină acoperă și obiectele Scădere mai vechi, întâlnite încă în proiectele salvate înainte de îmbinarea operațiilor. Acestea funcționează exact ca înainte; proiectele noi folosesc obiectul boolean comun, cu operația Scădere selectată.
