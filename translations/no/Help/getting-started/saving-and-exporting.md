---
title: Lagrer og eksporterer
parent: "Getting Started"
nav_order: 4
source_hash: 020d4bf43f07d3ab7dbd7d585e13c99309f0c0b8
source_lang: en
---
# Lagrer og eksporterer

MatterCAD støtter flere filformater for lagring og eksport av designene dine. Hvilket format du velger, avhenger av hvordan du planlegger å bruke filen.

## Lagringsformater

### MCX (opprinnelig format)

MCX er MatterCADs opprinnelige filformat og det beste valget for design du vil fortsette å redigere senere. Det bevarer:

- Hele designtreet med alle objekter og hierarkiet deres
- Alle parametere og innstillinger for hvert objekt
- Boolske operasjoner, matriser og andre operasjoner i redigerbar form
- Komponentrelasjoner

**Bruk MCX når:** Du vil lagre arbeidet ditt og fortsette å redigere det senere.

### STL

STL er det mest brukte formatet for 3D-utskrift. Det inneholder bare den ferdige trekantnettgeometrien, uten designhistorikk eller parametere.

**Bruk STL når:** Du vil 3D-printe designet ditt eller dele det med noen som ikke bruker MatterCAD.

### OBJ

OBJ (Wavefront) er et vanlig 3D-format som støttes av de fleste 3D-programmer. Som STL inneholder det kun nettgeometri.

**Bruk OBJ når:** Du må åpne designet ditt i annen 3D-programvare, som Blender eller en spillmotor.

### SVG

SVG-eksport lager en 2D-vektorfil fra designet sett ovenfra. Dette er nyttig for laserskjæring eller CNC-fresing.

**Bruk SVG når:** Du trenger et 2D-omriss av designet ditt for laserskjæring eller gravering.

## Slik lagrer du

![20260324 080726 paste 20260324 080726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080726-paste-20260324-080726.jpg)

1. Åpne **merkemenyen** (MatterCAD-logoen øverst til venstre)
2. Velg **Lagre som** for å velge plassering og format
3. Velg filformatet fra formatnedtrekkslisten
4. Velg hvor filen skal lagres, og klikk **Lagre**

Designet ditt lagres også automatisk mens du arbeider, så du mister ikke endringer hvis du lukker programmet.

## Tips

- Lagre alltid en MCX-kopi av designet ditt før du eksporterer til STL eller OBJ, slik at du kan gjøre endringer senere
- Når du eksporterer til STL, slås alle objekter i scenen sammen til ett enkelt nett
- Hvis du skal dele et design med noen som bruker MatterCAD, send MCX-filen for å bevare full redigerbarhet
- Du kan også lagre design i [Skybibliotek](../library/cloud-library.md) for tilgang fra hvilken som helst datamaskin

## Relatert

- [Legg til eksisterende objekter](adding-existing-objects.md) – Importer filer inn i MatterCAD
- [Bibliotek](../library/index.md) – Organiser de lagrede designene dine
- [Skybibliotek](../library/cloud-library.md) – Lagre design i skyen
