---
title: Foaie de variabile
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 3
source_hash: 3137a4da2b9d2086d4dcace156435caca288dd79
source_lang: en
---
# Foaie de variabile

Foaia de variabile stochează valori comune pentru un proiect. Folosiți-o atunci când mai multe obiecte trebuie să facă referire la aceleași dimensiuni, numere, etichete sau formule. Modificarea unei valori din foaie recalculează obiectele dependente, astfel încât proiectele parametrice rămân consecvente fără a edita fiecare obiect în parte.

<!--  Screenshot of the Variable Sheet editor showing named cells, formulas, and the Documentation button -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## Cum se adaugă o Foaie de variabile

1. Deschideți biblioteca și adăugați **Foaie de variabile** în scenă.
2. Selectați obiectul Foaie de variabile pentru a afișa editorul de foaie.
3. Selectați o celulă, apoi introduceți un **Nume** și o valoare sau o formulă.
4. Folosiți numele celulei din alte câmpuri ale proiectului care acceptă expresii.

## Editarea celulelor

Fiecare celulă are două părți editabile:

- **Nume** - Un nume opțional de variabilă pentru celulă. Numele nu țin cont de majuscule, spațiile sunt convertite în linii de subliniere, iar numele duplicate sunt ajustate automat.
- **Expresie** - Valoarea celulei. Textul simplu sau numerele sunt stocate direct. Formulele încep cu `=`.

Celulele pot fi referite și după adresă, de exemplu `A1` sau `B2`. Celulele denumite sunt de obicei mai clare pentru parametrii de proiectare, deoarece descriu intenția, cum ar fi `wall_thickness`, `outer_diameter` sau `hole_count`.

## Formule

Începeți o formulă cu `=` pentru ca aceasta să fie evaluată în foaie:

- `=20 + 5` returnează `25`
- `=pi * 10` returnează `31.41592653589793`
- `=A1 * 2` face referire la o altă celulă după adresă
- `=wall_thickness + 4` face referire la o celulă denumită

Foaia acceptă operații aritmetice, paranteze, operatori de comparație, funcții `Math` uzuale precum `sin`, `cos`, `sqrt` și `round`, precum și constante, inclusiv `pi`, `tau` și `e`.

## Utilizarea valorilor din foaie în obiecte

Majoritatea câmpurilor numerice din MatterCAD acceptă expresii. Pentru a folosi o valoare din foaie într-un parametru al unui obiect, prefixați referința cu `=`:

- Setați **Lățime** unui Cub la `=case_width`.
- Setați **Număr** unei Matrice la `=hole_count`.
- Setați o valoare **Decalaj** a unei Translatări la `=wall_thickness * 2`.

Când foaia se modifică, MatterCAD recalculează obiectele care depind de ea.

## Text și funcții ajutătoare

Celulele Foii de variabile pot conține atât text, cât și numere. Valorile text sunt utile pentru etichete generate, coduri de piese, date importate și aplicații de proiectare personalizate.

Funcții ajutătoare utile:

- `concat()` sau `strcat()` - Unesc texte sau valori.
- `substring()` - Extrage o parte dintr-o valoare text.
- `split()` - Divizează textul și returnează un element.
- `count()` - Numără elementele delimitate dintr-un text.
- `substitute()` - Înlocuiește text.
- `rand(seed)` - Generează o valoare aleatorie deterministă atunci când se furnizează o sămânță.
- `importdata()` - Citește o valoare dintr-un URL sau dintr-o cale de fișier locală.

## Sfaturi

- Preferați nume descriptive în locul adreselor de celule pentru valorile folosite de alte obiecte.
- Păstrați dimensiunile principale în apropierea colțului din stânga sus al foii, pentru a fi ușor de găsit.
- Folosiți formule pentru valorile derivate, cum ar fi `inner_diameter = outer_diameter - wall_thickness * 2`.
- Evitați folosirea cuvintelor rezervate precum `pi`, `e`, `true`, `false` sau a numelor de funcții ca nume de celule.
- Dacă o formulă nu poate fi interpretată, MatterCAD păstrează datele introduse inițial ca text.

## Articole conexe

- [Expresii](expressions.md) - Folosiți expresii în parametrii obiectelor
- [Componente](components.md) - Creați proiecte parametrizate reutilizabile
- [Matrice](../operations/array/array.md) - Creați modele repetate controlate de valorile din foaie
