---
title: Selectare trasee
articleKey: SelectPathsObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: f7df7bb24841030643e4634febedcfce6e92ada9
source_lang: en
---
# Selectare trasee

Selectare trasee filtrează sub-căile păstrate dintr-un obiect cale complex. Este utilă mai ales atunci când lucrați cu fonturi decorative sau formate din mai multe părți, unde aveți nevoie ca formele exterioare ale literelor și formele decupate interioare să fie piese separate — de exemplu, pentru a le imprima 3D în două culori diferite.

<!--  Screenshot showing Select Paths applied to decorative text with outer paths highlighted -->
![20260506 154655 paste 20260506 154655](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154655-paste-20260506-154655.jpg)

## Cum funcționează adâncimea căii

Atunci când un obiect cale conține forme cu zone închise (precum interiorul literei „O” sau golul unei spirale decorative), acele zone închise sunt **găuri** la adâncimea 1. Conturul exterior al fiecărei litere sau forme se află la **adâncimea 0**.

```
Depth 0 — outer contour of each letter or shape
Depth 1 — first level of enclosed holes (inside an "O", "A", etc.)
Depth 2 — shapes nested inside a hole (rarely used)
```

## Presetări de filtru

### Toate
Include fiecare cale nemodificată. Aceasta este valoarea implicită și echivalează cu a nu aplica deloc Selectare trasee.

### Doar căile exterioare
Păstrează doar conturul exterior al fiecărei forme (adâncime == 0). Folosiți această opțiune pentru a obține doar conturele literelor dintr-un font decorativ, fără zonele decupate interioare.

### Doar găurile
Păstrează doar găurile închise (adâncime > 0). Folosiți această opțiune pentru a obține doar zonele tăiate interioare ale literelor și formelor.

### După indexul grupului
Păstrează doar căile care aparțin unei singure forme deconectate. Grupul 0 este prima formă, grupul 1 este a doua și așa mai departe. Folosiți această opțiune pentru a izola un singur caracter dintr-un cuvânt.

### Personalizat
Scrieți o expresie care este evaluată pentru fiecare cale. Calea este **inclusă** atunci când expresia este diferită de zero și **exclusă** atunci când este zero.

Expresiile trebuie să înceapă cu `=` pentru a activa substituirea variabilelor. Fără `=`, valoarea este tratată ca un simplu număr (de exemplu, `1` include întotdeauna, `0` exclude întotdeauna).

## Exemple de expresii personalizate

| Expresie | Efect |
|------------|--------|
| `=PathDepth==0` | Doar conturele exterioare (la fel ca Doar căile exterioare) |
| `=PathDepth>0` | Doar găurile (la fel ca Doar găurile) |
| `=GroupIndex==0` | Doar prima formă deconectată |
| `=PathArea>100` | Forme cu aria mai mare de 100 mm² |
| `=PathLength>50` | Forme cu perimetrul mai lung de 50 mm |

## Variabile pentru expresii personalizate

| Variabilă | Semnificație |
|----------|---------|
| `PathDepth` | 0 = contur exterior; 1+ = gaură sau formă imbricată |
| `GroupIndex` | Indexul formei deconectate (0, 1, 2…) |
| `GroupOuterArea` | Aria căii exterioare a acestui grup |
| `GroupOuterLength` | Perimetrul căii exterioare a acestui grup |
| `ChildCount` | Numărul de găuri din interiorul căii exterioare a acestui grup |
| `PathIndex` | Indexul secvențial al acestei căi în cadrul grupului său |
| `PathArea` | Aria acestei căi individuale |
| `PathLength` | Perimetrul acestei căi individuale |

## Exemplu: imprimare multicoloră cu un font de Crăciun

O utilizare frecventă a operației Selectare trasee este imprimarea unui text decorativ ale cărui litere au forme decupate în interior. Pentru a imprima literele exterioare într-o culoare și decupajele interioare într-o a doua culoare:

1. Adăugați un obiect **Text** și setați-l pe **ieșire 2D**
2. Aplicați **Selectare trasee** → setați presetarea la **Doar căile exterioare**
3. Aplicați **Extrudare liniară** pentru a-i da înălțime → atribuiți prima culoare de filament
4. Reveniți la obiectul text original
5. Aplicați o a doua operație **Selectare trasee** → setați presetarea la **Doar găurile**
6. Aplicați **Extrudare liniară** cu aceeași înălțime → atribuiți a doua culoare de filament
7. Poziționați un obiect extrudat peste celălalt — cele două culori se aliniază perfect

## Articole conexe

- [Extrudare liniară](linear-extrude.md) — Dați înălțime căilor filtrate pentru a crea un obiect 3D
- [Revoluție](revolve.md) — Rotiți căile filtrate în jurul unei axe
- [Obiect SVG](../../primitives/svg-object.md) — Importați căi vectoriale care pot conține mai multe sub-căi
- [Text](../../primitives/text.md) — Obiectele text în modul 2D produc o ieșire cu mai multe căi
