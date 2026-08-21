---
title: Cale umflare
articleKey: InflatePathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: c0e11d3d24c5f832f797cde4d392e26a4694733d
source_lang: en
---
# Cale umflare

Cale umflare extinde o cale 2D spre exterior, mărind forma și păstrându-i în același timp aspectul general. Este similar cu aplicarea unei decalări uniforme pe toate muchiile.

<!--  Before and after showing a path inflated outward -->
![20260506 100652 paste 20260506 100652](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100652-paste-20260506-100652.jpg)


## Mod de utilizare

1. Selectați o cale 2D
2. Aplicați **Cale umflare** din meniul de operații Cale
3. Ajustați valoarea umflării

## Umflarea unei linii deschise

Umflare este modul în care transformați o linie într-o formă. Debifați **Închis** pe un [Traseu personalizat](../../2d-paths/custom-path.md) pentru a desena o linie deschisă, apoi umflați-o: rezultatul este o bandă plină, la fel de lată de fiecare parte a liniei cât valoarea stabilită de dumneavoastră. De acolo se extrudează la fel ca orice altă cale.

**Stil** stabilește modul în care sunt terminate cele două capete ale liniei, precum și modul în care se îmbină colțurile acesteia:

- **Plat** oprește banda drept, la fiecare punct terminal
- **Rotund** adaugă un semicerc dincolo de fiecare punct terminal
- **Ascuțit** adaugă un pătrat dincolo de fiecare punct terminal

O linie deschisă nu are un interior în care să se contracte, așa că o valoare zero sau negativă nu ar lăsa absolut nimic. Când calea este *în întregime* deschisă, Umflare ridică valoarea până la un număr pozitiv mic și scrie numărul limitat înapoi în casetă, ca să vedeți ce s-a întâmplat.

O cale care combină contururi deschise și închise nu este limitată: contururile închise se contractă normal, iar cele deschise pur și simplu dispar. Căile închise se contractă în continuare la valori negative exact ca întotdeauna.

## Sfaturi

- Folosiți valori negative pentru a contracta calea spre interior în loc să o extindeți
- Umflare este utilă pentru crearea decalărilor de toleranță în jurul formelor
- Combinați cu [Cale contur](outline-path.md) pentru a crea contururi cu lățimi specifice

## Similare

- [Cale contur](outline-path.md) - Creează un contur dintr-o cale
- [Traseu contur](border-path.md) - Adaugă o decalare de contur
- [Traseu netezit](smooth-path.md) - Rotunjește colțurile unei căi
