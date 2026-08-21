---
title: Matrice
articleKey: ArrayObject3D_2
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c547fa24e5f47e0d60f0cec0eac979700d946daf
source_lang: en
---
# Matrice

**Matrice** creează mai multe copii ale unui obiect aranjate după un model. Selectați un mod din butoanele din partea de sus — **Liniar**, **Radial** sau **Transformare** — pentru a comuta între tipurile de model.

<!--  Screenshot of the Array operation panel showing the mode buttons at the top (Linear | Radial | Transform) -->
![20260506 080647 paste 20260506 080647](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080647-paste-20260506-080647.jpg)


## Mod de utilizare

1. Selectați un obiect
2. Aplicați operația **Matrice** din meniul Duplicare
3. Alegeți un mod (Liniar, Radial sau Transformare)
4. Ajustați parametrii pentru modul ales

## Mod: Liniar

Modul Liniar plasează copiile de-a lungul unei direcții, cu rotație și progresie a scalării opționale.

**Număr** — Numărul de copii (număr întreg sau expresie). Obiectul sursă este prima copie; copiile suplimentare sunt decalate față de aceasta.

**Metodă decalaj** — Modul în care se calculează spațierea:
- **Relativ** — Decalajul este înmulțit cu dimensiunea casetei de încadrare a obiectului. Un **Decalaj relativ** de (1, 0, 0) distanțează copiile exact cu o lățime de obiect de-a lungul axei X.
- **Decalaj** — Distanță fixă în spațiul global, în mm, pentru fiecare copie.
- **Punct final** — Setează poziția ultimei copii; spațierea este împărțită uniform între copii.

**Decalaj relativ** / **Decalaj** / **Punct final** — Vectorul de spațiere, în funcție de Metodă decalaj selectată.

**Mod rotație** — Modul în care rotația se acumulează de la o copie la alta:
- **Local** — Fiecare copie se rotește pe loc, în jurul propriului centru; direcția decalajului rămâne pe axele globale.
- **Compunere** — Rotația se acumulează și orientează decalajul, producând spirale, evantaie și elice.

**Rotație** — Rotația pe fiecare axă, în grade, pentru fiecare copie.

**Scalare** — Scalarea cumulativă pe fiecare axă, pentru fiecare copie. Valorile mai mici decât 1 micșorează copiile; valorile mai mari decât 1 le măresc.

**Scalarea afectează decalajul** — Când este activată, spațierea dintre copii se scalează și ea la fiecare pas. Folosiți această opțiune pentru spirale care se strâng și progresii geometrice (cochilii de nautilus, curbe suprapuse de tip cochilie).

## Mod: Radial

Modul Radial distribuie copiile uniform în jurul unei axe centrale, la o rază fixă.

<!--  Screenshot of Array in Radial mode showing 6 copies arranged in a circle, with Radius and Central Axis parameters visible -->
![20260506 092618 paste 20260506 092618](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-092618-paste-20260506-092618.jpg)


**Metodă de numărare** — Modul în care se determină numărul de copii:
- **Număr** — Număr explicit de copii.
- **Distanță** — Intervalul unghiular dintre copii, în grade; numărul este calculat pentru a umple baleierea.

**Număr** / **Distanță unghiulară** — Numărul de copii (modul Număr) sau spațierea unghiulară în grade (modul Distanță). Acceptă expresii.

**Axă centrală** — Axa în jurul căreia se face rotația (implicit: Z).

**Segment de cerc** — Dacă copiile acoperă un cerc complet de 360° (**Complet**) sau un arc parțial (**Arc**).

**Rază** — Distanța de la axa centrală până la fiecare copie.

**Unghi de baleiere** — Gradele de arc de umplut (afișat când Segment de cerc este Arc). Acceptă expresii.

**Aliniere rotație** — Rotește fiecare copie astfel încât axa sa înainte să fie orientată spre exterior, dinspre centru.

**Axă înainte** — Care axă a copiei este tratată drept „înainte” la aliniere (afișat când Aliniere rotație este activată).

## Mod: Transformare

Modul Transformare avansează copiile folosind o transformare manuală sau urmând transformarea altui obiect.

**Număr** — Numărul de copii (număr întreg sau expresie).

**Referință transformare** — De unde provine transformarea aplicată la fiecare pas:
- **Intrare** — Specificați direct translația, rotația și scalarea.
- **Obiect** — Transformarea este citită dintr-un obiect frate cu numele indicat.

**Translație** — Decalajul în spațiul global, în mm, pentru fiecare pas (afișat când Referință transformare este Intrare).

**Rotație** — Rotația pe fiecare axă, în grade, pentru fiecare pas (afișat când Referință transformare este Intrare).

**Scalare** / **Axe de scalare** — Scalarea uniformă și pe fiecare axă aplicată la fiecare pas (afișat când Referință transformare este Intrare).

**Nume transformare** — Numele obiectului frate a cărui transformare este folosită drept increment la fiecare pas (afișat când Referință transformare este Obiect).

**Spațiu relativ** — Când este activată, transformarea fiecărei copii se compune în sistemul local al copiei precedente; când este dezactivată, fiecare pas se aplică în spațiul global (afișat când Referință transformare este Obiect).

## Aleatorizează

Activați **Aleatorizează** pentru a adăuga variație tuturor copiilor.

- **Decalaj aleatoriu** — Decalajul aleatoriu maxim de poziție pe fiecare axă, în mm.
- **Rotație aleatorie** — Rotația aleatorie maximă pe fiecare axă, în grade.
- **Axe scalare aleatorie** — Variația aleatorie maximă a scalării pe fiecare axă.
- **Exclude primul** — Păstrează prima copie exact în poziția calculată (implicit: activat).
- **Exclude ultimul** — Păstrează ultima copie exact în poziția calculată.
- **Sămânță aleatorie** — Modificați această valoare pentru a obține un alt aranjament aleatoriu. Acceptă expresii.

## Îmbinare

- **Creare rețea unică** — Combină toate copiile într-un singur obiect cu plasă îmbinată.
- **Îmbinare vârfuri** — Sudează vârfurile aflate sub pragul distanței de îmbinare (afișat când Creare rețea unică este activată).
- **Distanță** — Pragul de îmbinare în mm (afișat când Îmbinare vârfuri este activată).

## Sfaturi

- Folosiți expresii pentru Număr, Rotație sau Punct final pentru a crea modele parametrice
- Pentru modele circulare, folosiți modul Radial — setați Rază pentru a controla dimensiunea cercului și activați Aliniere rotație dacă doriți ca fiecare copie să fie orientată spre exterior
- Rotația cu Compunere în modul Liniar creează spirale și evantaie fără a calcula manual decalajele de unghi
- Scalarea afectează decalajul creează în mod natural aranjamente de tip cochilie de nautilus și progresie geometrică
- Combinați Matrice cu [Selectare copil](select-child.md) pentru a crea modele în care fiecare copie afișează o variantă diferită

## Articole conexe

- [Aliniere](../placement/align.md) - Poziționează obiectele unul față de altul
- [Selectare copil](select-child.md) - Alege o anumită copie dintr-o matrice, după index sau după nume
