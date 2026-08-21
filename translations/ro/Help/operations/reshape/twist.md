---
title: Răsucire
articleKey: TwistObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: 8ea8d2017c16f20dc42b433bcf91815262bb5380
source_lang: en
---
# Răsucire

Răsucire rotește partea de sus a unui obiect față de partea de jos, creând un efect de spirală sau de torsiune de-a lungul înălțimii. În mod implicit, rotația progresează uniform de jos în sus; sub Avansat poți desena unde anume, de-a lungul înălțimii, are loc efectiv rotirea.

<!--  Before and after showing a cube being twisted into a spiral column -->
![20260506 155620 paste 20260506 155620](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155620-paste-20260506-155620.jpg)

## Mod de utilizare

1. Selectează un obiect
2. Aplică operația **Răsucire** din meniul Remodelează
3. Setează unghiul de răsucire și ajustează felierea pentru netezime
4. Activează **Avansat** dacă vrei să desenezi cum este distribuită răsucirea pe înălțimea piesei

## Profilul de răsucire

Sub Avansat, curba **Profil de răsucire** decide unde are loc răsucirea. Cantitatea totală de răsucire este stabilită tot de controlul Unghi (sau Distanță de rotație) - curba doar o distribuie:

- **Pe verticala curbei** este înălțimea pe piesă, în procente - 0 la bază, 100 la vârf. O linie de ghidaj de-a latul editorului marchează 100 la sută și este etichetată cu înălțimea reală a piesei, în mm.
- **Pe orizontala curbei** este procentul din răsucirea totală atins la acea înălțime - 0 pentru deloc, 100 pentru toată.

O Răsucire nouă începe cu o diagonală dreaptă de la 0 la 100, adică exact răsucirea uniformă simplă pe care o obții fără Avansat.

O porțiune plată din curbă este o bandă a piesei care nu se răsucește. Acolo unde curba nu acoperă întreaga înălțime, se menține capătul cel mai apropiat al ei, așa că o curbă desenată doar între 40 și 60 la sută lasă piesa rigidă dedesubt și deasupra - astfel pornești și oprești o răsucire la mijlocul înălțimii.

O porțiune care coboară pe măsură ce urcă desface răsucirea: acea bandă a piesei se rotește în sens invers, înapoi spre punctul de plecare. Desenarea profilului peste 100 și apoi înapoi în jos este modul în care depășești totalul și revii la el.

## Parametri

- **Tip rotație** - Alege între:
  - **Unghi** - Specifică unghiul total de răsucire în grade (3-360)
  - **Distanță** - Specifică răsucirea ca o distanță de-a lungul circumferinței
- **Felii** - Numărul de tăieturi orizontale adăugate pentru o răsucire netedă, distribuite uniform pe înălțimea piesei. Mai multe felii = răsucire mai netedă
- **Laturi minime** - Numărul minim de laturi pe care ar trebui să le aibă piesa în jurul axei de răsucire. O formă grosieră, cum ar fi un cub, nu are geometrie pe perimetru care să preia rotația, așa că fețele ei plane se fațetează în loc să se curbeze; aceasta adaugă tăieturi verticale prin axa de răsucire, astfel încât acele fețe să poată urma răsucirea. 0 (valoarea implicită) lasă piesa neschimbată
- **Răsucire la dreapta** - Direcția răsucirii: la dreapta (în sensul acelor de ceasornic) sau la stânga (în sens invers acelor de ceasornic)
- **Rază preferată** - Doar pentru citire: raza raportată de piesa însăși sau cea sugerată de forma ei, în jurul căreia se măsoară o distanță de răsucire (doar în modul Distanță)
- **Editare rază** - Dezactivează raza raportată pentru a o putea seta pe a ta (doar în modul Distanță și doar când piesa raportează una)
- **Suprascrie raza** - Rază personalizată pentru calculul răsucirii (doar în modul Distanță)

### Parametri avansați

- **Profil de răsucire** - Editorul de curbă descris mai sus: procentul din răsucirea totală atins la fiecare înălțime, în procente
- **Decalaj rotație** - Deplasează centrul în jurul căruia este rotită piesa, față de mijlocul piesei

## Sfaturi

- Valorile mai mari pentru Felii produc rezultate mai netede, dar generează mai multă geometrie
- Dacă un cub răsucit sau altă formă cu fețe plane pare fațetată în loc de curbată, crește valoarea pentru Laturi minime
- Desenează profilul plat la bază și în creștere după aceea pentru a lăsa o bază dreaptă sub o coloană răsucită
- O răsucire de 90 de grade pe o coloană pătrată creează un efect arhitectural elegant
- Desenează două porțiuni plate unite printr-o urcare scurtă pentru a răsuci mijlocul piesei și a lăsa ambele capete rigide

## Articole conexe

- [Curbă](curve.md) - Îndoaie un obiect într-un arc
- [Strângere](pinch.md) - Comprimă spre centru
- [Strângere radială](radial-pinch.md) - Modelează profilul cu o curbă, în același mod
