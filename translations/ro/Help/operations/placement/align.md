---
title: Aliniere
articleKey: AlignObject3D_3
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 1fadae72ba00cb06e36a21f0b96962dcff3f60ad
source_lang: en
---
# Aliniere

Aliniere poziționează cu precizie mai multe obiecte în raport cu un obiect de ancorare. Folosește-o pentru a alinia muchii, pentru a centra piese unele pe altele, pentru a așeza un obiect deasupra altuia sau pentru a crea stive distanțate uniform.

<!--  Screenshot showing two objects being aligned with alignment options visible -->
![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)


## Cum se utilizează

1. Selectează două sau mai multe obiecte.
2. Aplică operația **Aliniere** din meniul **Amplasare**.
3. Alege obiectul **Ancoră**. Ancora rămâne pe loc, iar celelalte obiecte se deplasează.
4. Stabilește alinierea pentru axele X, Y și Z în mod independent.
5. Folosește **Aplică** atunci când vrei să fixezi pozițiile aliniate în arborele de obiecte.

## Parametri

### Ancoră

Lista **Ancoră** selectează obiectul copil folosit ca referință. Ancora nu se deplasează. Orice alt copil din operația Aliniere este repoziționat în raport cu ancora, cu excepția cazului în care o axă folosește modul **Stivuit**.

### Comenzi pe axă

Fiecare axă are propriile comenzi. Poți alinia pe o axă, pe două axe sau pe toate trei. Muchiile minimă și maximă sunt denumite în funcție de axă:

- **Axa X** - Min este stânga, Max este dreapta.
- **Axa Y** - Min este față, Max este spate.
- **Axa Z** - Min este jos, Max este sus.

Pentru fiecare axă:

- **Aliniere** - Alege punctul de referință al ancorei pentru acea axă. Folosește **Niciunul** pentru a lăsa pozițiile neschimbate pe acea axă.
- **Mod** - Controlează modul în care se aplică alinierea selectată:
  - **Simplu** - Potrivește muchia, centrul sau originea corespunzătoare a fiecărui obiect mobil cu cea a ancorei. Nu se folosește niciun decalaj.
  - **Decalaj** - Alege ce parte a obiectului mobil trebuie să ajungă la referința ancorei, apoi adaugă distanță cu **Decalaj**.
  - **Stivuit** - Așază obiectele unul după altul de-a lungul acelei axe, folosind **Decalaj** ca spațiu între ele.
- **SubAliniere** - Disponibilă în modul **Decalaj**. Alege partea obiectului mobil care va fi așezată pe referința ancorei. Dacă **SubAliniere** este **Niciunul**, Aliniere folosește aceeași muchie, același centru sau aceeași origine selectată de **Aliniere**.
- **Decalaj** - Disponibil în modurile **Decalaj** și **Stivuit**. Adaugă distanță de-a lungul acelei axe și acceptă [expresii](../../workspace/expressions.md).

## Moduri de aliniere

### Simplu

Folosește **Simplu** atunci când potrivești poziții similare între ele. De exemplu, **Aliniere X: Centru** deplasează fiecare obiect care nu este ancoră astfel încât centrul său pe X să coincidă cu centrul pe X al ancorei. **Aliniere Z: Min** deplasează fiecare obiect care nu este ancoră astfel încât baza sa să se afle la înălțimea bazei ancorei.

### Decalaj

Folosește **Decalaj** atunci când partea obiectului mobil trebuie să fie diferită de referința ancorei. De exemplu, pentru a așeza un obiect deasupra ancorei:

1. Setează **Aliniere Z** la **Max** (sus).
2. Setează **Mod Z** la **Decalaj**.
3. Setează **SubAliniere Z** la **Jos**.
4. Setează **Decalaj Z** la spațiul dorit sau lasă-l la `0` pentru contact direct.

Astfel, baza obiectului mobil ajunge la partea superioară a ancorei, cu spațiere opțională.

### Stivuit

Folosește **Stivuit** pentru a înlănțui mai multe obiecte de-a lungul unei axe. Obiectele sunt procesate după nume, apoi după ID-ul intern, astfel încât denumirea clară a obiectelor oferă o ordine previzibilă a stivei.

În modul **Stivuit**, fiecare obiect mobil este așezat lângă referința anterioară pe acea axă:

- Alinierea **Min** stivuiește în direcția pozitivă, de exemplu de la stânga la dreapta pe X sau de jos în sus pe Z.
- Alinierea **Max** stivuiește în direcția negativă, de exemplu de la dreapta la stânga pe X sau de sus în jos pe Z.
- Alinierea **Centru** și **Origine** folosește decalajul dintre centrul sau originea fiecărui obiect.

Folosește **Decalaj** în modul **Stivuit** pentru a stabili spațiul dintre obiecte.

## Exemple

- **Centrarea obiectelor pe suprafața platformei** - Alege obiectul care trebuie să rămână fix ca **Ancoră**, apoi setează **Aliniere X** și **Aliniere Y** la **Centru**.
- **Așezarea unui obiect deasupra altuia** - Setează **Aliniere Z** la **Max** (sus), **Mod Z** la **Decalaj** și **SubAliniere Z** la **Jos**.
- **Adăugarea unui spațiu precis față de o muchie** - Folosește modul **Decalaj**, alege muchia obiectului mobil cu **SubAliniere**, apoi setează **Decalaj** la distanța de care ai nevoie.
- **Alinierea mai multor obiecte cap la cap** - Setează **Aliniere X** la **Min** (stânga), **Mod X** la **Stivuit** și folosește **Decalaj X** pentru spațiu.
- **Construirea unei stive verticale** - Setează **Aliniere Z** la **Min** (jos), **Mod Z** la **Stivuit** și folosește **Decalaj Z** pentru spațiul dintre obiecte.

## Sfaturi

- Obiectul ancoră rămâne pe loc; celelalte obiecte se deplasează pentru a se alinia cu el.
- Poți folosi moduri diferite pe axe diferite, de exemplu **Stivuit** pe X, în timp ce pe Y folosești **Centru** și **Simplu**.
- Folosește numele obiectelor pentru a controla ordinea **Stivuit** atunci când se aliniază simultan mai multe obiecte.
- Aliniere este nedistructivă până la aplicare. Poți schimba oricând setările pentru a realinia obiectele copil.
- Folosește **Origine** atunci când trebuie să aliniezi originile de modelare, nu muchiile casetei de încadrare.

## Articole conexe

- [Încadrare în limite](fit-to-bounds.md) - Scalează un obiect pentru a se încadra în dimensiuni specifice
- [Translatare](../transform/translate.md) - Deplasare cu o distanță specificată
- [Grupare](../../workspace/grouping.md) - Grupează obiectele aliniate pentru a le păstra împreună
