---
title: Sferă
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
source_hash: c227e98ac116c3481bb2af73c55801de84e70b1e
source_lang: en
---
# Sferă

O formă rotundă de bilă, cu diametru și nivel de detaliu reglabile.

<!--  Screenshot of a Sphere primitive on the workspace -->
![20260318 183909 paste 20260318 183909](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183909-paste-20260318-183909.jpg)


## Parametri

- **Diametru** - Lățimea sferei (implicit: 20mm)
- **Laturi** - Numărul de segmente de pe perimetru (implicit: 40). Mai multe laturi = suprafață mai netedă

### Parametri avansați

Activați modul **Avansat** pentru controale suplimentare:

- **Unghi inițial** - Unghiul de la care începe suprafața sferei (implicit: 0)
- **Unghi final** - Unghiul la care se termină suprafața sferei (implicit: 360). Setați o valoare mai mică de 360 pentru forme sferice parțiale
- **Laturi latitudine** - Numărul de segmente de sus până jos (implicit: 30). Mai multe = poli mai netezi

## Sfaturi

- Pentru imprimare 3D, 40 de laturi sunt de obicei suficiente. Valorile mai mari creează suprafețe mai netede, dar fișiere mai mari
- Folosiți Unghi inițial și Unghi final pentru a crea forme sferice parțiale, precum boluri sau cupole
- Combinați cu [Scădere](../operations/boolean/subtract.md) pentru a crea cavități sferice

## Înrudite

- [Jumătate de sferă](half-sphere.md) - Doar emisfera superioară
- [Tor](torus.md) - O formă de gogoașă
