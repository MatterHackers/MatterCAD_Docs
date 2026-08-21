---
title: Traseu personalizat
articleKey: CustomPathObject3D
parent: "2D Paths"
nav_order: 3
source_hash: 3633c708477de3ac77d3547b730c33f7e4431cf6
source_lang: en
---
# Traseu personalizat

Desenează-ți propria cale 2D cu puncte de control. Aceasta îți oferă libertate completă de a crea orice formă 2D care poate fi apoi extrudată sau supusă unei revoluții pentru a obține un obiect 3D.

<!-- Screenshot showing a custom path being edited with control points -->
![20260506 080247 paste 20260506 080247](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080247-paste-20260506-080247.jpg)


## Mod de utilizare

1. Adaugă un **Traseu personalizat** din biblioteca de căi 2D
2. Editează punctele de control pentru a defini forma dorită
3. Aplică [Extrudare liniară](../operations/path/linear-extrude.md) sau alte operații pe cale pentru a crea un obiect 3D

## Căi deschise și închise

Caseta de bifare **Închis** controlează dacă respectiva cale își unește ultimul punct înapoi cu primul.

- **Închis** (valoarea implicită) face ca respectiva cale să contureze o regiune. Aceasta este ceea ce umple [Extrudare liniară](../operations/path/linear-extrude.md) și [Revoluție](../operations/path/revolve.md).
- **Deschide** transformă calea într-o linie. O linie nu închide nimic, așa că apare în scenă ca o panglică subțire de-a lungul ei, nu ca o formă plină. Folosește [Cale umflare](../operations/path/inflate-path.md) pentru a-i da o lățime și a o transforma din nou în ceva solid.

Două lucruri de știut înainte de a debifa **Închis**:

- **Reînchiderea nu este o anulare.** Deschiderea unei căi elimină segmentul ei de închidere. Dacă acel segment era curbat, bifarea din nou a opțiunii **Închis** aduce înapoi o linie dreaptă, nu curba. Folosește în schimb Ctrl+Z - anularea restaurează exact calea originală.
- **Unele contururi refuză să se deschidă.** Un contur care ar rămâne cu mai puțin de două puncte - o picătură desenată ca un singur punct și o curbă care se întoarce în buclă la el - rămâne închis, în loc să se prăbușească în ceva ce nu ai mai putea vedea sau selecta cu clic. La fel se întâmplă și cu un contur care conține o curbă pătratică, ceea ce un fișier SVG importat poate include: deschiderea lui ar aplatiza curba într-un colț. Refuzul se aplică pe fiecare contur în parte, așa că restul căii se deschide totuși.

Dacă o cale are mai multe contururi și acestea nu concordă, caseta de bifare apare ca deschisă. Bifarea ei aliniază toate contururile.

Operațiile care au nevoie de o regiune vor închide în locul tău o cale deschisă, în loc să o refuze. Extrudare liniară, Revoluție, Scădere și celelalte operații booleene fac toate acest lucru, așa că o cale deschisă se extrudează în același solid ca și versiunea sa închisă.

## Sfaturi

- Folosește Traseu personalizat atunci când niciuna dintre formele de cale predefinite nu corespunde nevoilor tale
- Pentru importarea formelor din editoare vectoriale externe, vezi [Obiect SVG](../primitives/svg-object.md)
- Pentru a desena o linie și a o transforma într-o piesă, debifează **Închis**, aplică [Cale umflare](../operations/path/inflate-path.md) pentru a-i da o grosime, apoi [Extrudare liniară](../operations/path/linear-extrude.md) pentru a-i da înălțime

## Articole conexe

- [Cale Cerc](circle-path.md) - Un cerc gata făcut
- [Cale Cutie](box-path.md) - Un dreptunghi gata făcut
- [Obiect SVG](../primitives/svg-object.md) - Importă căi vectoriale din fișiere SVG
- [Extrudare liniară](../operations/path/linear-extrude.md) - Dă înălțime căilor
