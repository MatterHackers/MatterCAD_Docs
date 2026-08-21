---
title: Selectare copil
articleKey: SelectChildObject3D
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: f6f71d2b457b82126f272ea9354f877c36570df0
source_lang: en
---
# Selectare copil

Selectare copil alege un singur copil dintr-un grup de obiecte, pe baza unui număr de index sau a unui nume. Acest lucru este deosebit de util în proiectele scriptate și parametrice, unde dorești să alegi dinamic ce obiect să fie afișat.

<!-- IMAGE: Screenshot showing Select Child operation with multiple children and one selected by index -->
![20260506 080526 paste 20260506 080526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080526-paste-20260506-080526.jpg)


## Mod de utilizare

1. Selectează două sau mai multe obiecte
2. Aplică operația **Selectare copil** din meniul Duplicare
3. Alege **După index** sau **După nume** pentru a controla modul în care este selectat copilul
4. Setează numărul de index sau numele care trebuie să corespundă

## Parametri

- **Metodă de selecție** - Alege între **După index** (selectare după poziție) sau **După nume** (selectare după numele obiectului). Afișată sub formă de butoane.
- **Index copil** - Indexul copilului de selectat, pornind de la zero (afișat când se folosește După index). Acceptă [expresii](../../workspace/expressions.md).
- **Nume copil** - Numele copilului de selectat (afișat când se folosește După nume). Acceptă [expresii](../../workspace/expressions.md).

Dacă indexul este în afara intervalului sau numele nu corespunde niciunui copil, este returnat primul copil ca soluție de rezervă. Dacă nu există copii, nu se returnează nimic.

## Utilizare în Scriptare

Selectare copil este concepută să funcționeze cu expresii și cu funcția `rand()` pentru a crea proiecte dinamice, bazate pe date. De exemplu, poți construi o scenă cu mai multe obiecte variante ca și copii și poți folosi o expresie precum `rand(42)` ca sămânță pentru index, pentru a alege unul la întâmplare.

**Exemplu: recuzită de cărți aleatorii pentru un spectacol de scenă**

1. Importă 5 rețele diferite de cărți ca și copii ai unei operații Selectare copil
2. Setează Metodă de selecție la **După index**
3. Folosește o expresie pentru Index copil, precum `floor(rand(seed) * 5)`, unde `seed` este o variabilă de foaie
4. Duplică operația Selectare copil de mai multe ori, fiecare cu altă valoare a semințelor
5. Fiecare instanță alege aleatoriu o carte diferită din set

Acest tipar funcționează pentru orice scenariu în care trebuie să alegi dintr-un set de variante: mobilier, decorațiuni, elemente arhitecturale sau orice colecție de piese interschimbabile.

## Sfaturi

- Combină cu [Matrice](array.md) pentru a crea tipare variate, în care fiecare copiere selectează un alt copil
- Folosește variabile de foaie pentru index sau nume, pentru a controla selecția dintr-o foaie de calcul
- Comportamentul de revenire la primul copil înseamnă că proiectul tău nu se strică niciodată, chiar dacă indexul sau numele este greșit

## Articole conexe

- [Matrice](array.md) - Duplică obiecte în tipare liniare, radiale, pe curbă și prin transformare
