---
title: Repară
articleKey: RepairObject3D_2
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: f637470dee4f722b595f07d2da9dcdaac5e8da72
source_lang: en
---
# Repară

Repară corectează problemele frecvente ale geometriei plasei, inclusiv muchii non-manifold, găuri, orientare inconsecventă a fețelor și vârfuri aproape coincidente. Este utilă în special pentru fișierele STL și OBJ importate, care pot conține erori.

![20260324 080517 paste 20260324 080517](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080517-paste-20260324-080517.jpg)


## Mod de utilizare

1. Selectați un obiect cu probleme de plasă
2. Aplicați operația **Repară** din meniul Plasă
3. Consultați statisticile dinainte/după pentru a vedea ce s-a corectat

## Statistici (doar citire)

- **Vârfuri inițiale / Vârfuri finale** - Numărul de vârfuri înainte și după reparare
- **Fețe inițiale / Fețe finale** - Numărul de fețe înainte și după reparare
- **Muchii non-manifold inițiale / Muchii non-manifold finale** - Numărul de muchii problematice înainte și după

### Opțiuni avansate

Activați modul **Avansat** pentru un control detaliat:

- **Sudare vârfuri** - Îmbină vârfurile aproape coincidente (implicit: activat)
- **Toleranță de sudare** - Cât de apropiate trebuie să fie vârfurile pentru a fi îmbinate
- **Orientare fețe** - Întoarce cojile inversate în poziția corectă, astfel încât fiecare corp să fie interpretat ca solid. Fiecare coajă este evaluată separat, deci un model gol își păstrează cavitățile în loc ca acestea să fie umplute. Cojile ale căror fețe nu concordă între ele sunt lăsate neatinse, în loc să se facă presupuneri, iar modelele care nu sunt etanșe beneficiază de o reparare mai tolerantă - rulați mai întâi **Umplere găuri** dacă orientarea singură nu le corectează.
- **Sudare muchii** - Repară fisurile mici și îmbinările defectuoase
- **Umplere găuri** - Umple golurile din suprafața plasei
- **Mod eliminare** - Elimină geometria internă sau ocluzată:
  - **Niciunul** - Păstrează întreaga geometrie
  - **Interior** - Elimină corpurile interne ascunse în interiorul formei principale
  - **Ocluzat** - Elimină fețele care nu sunt vizibile din exterior

## Sfaturi

- Încercați mai întâi Repară dacă operațiile booleene (Combină, Scădere) produc rezultate neașteptate pe modelele importate
- Setările implicite (Sudare vârfuri activat, restul dezactivate) rezolvă cele mai frecvente probleme
- Activați Umplere găuri dacă se vede prin golurile din model
- Utilizați Mod eliminare Interior pentru a curăța modelele care au geometrie ascunsă în interior

## Articole conexe

- [Decimare](decimate.md) - Reduce numărul de poligoane
- [Adăugarea obiectelor existente](../../getting-started/adding-existing-objects.md) - Importați modele care pot necesita reparare
