---
title: Gemmer og eksporterer
parent: "Getting Started"
nav_order: 4
source_hash: 020d4bf43f07d3ab7dbd7d585e13c99309f0c0b8
source_lang: en
---
# Gemmer og eksporterer

MatterCAD understøtter flere filformater til at gemme og eksportere dine designs. Hvilket format du vælger, afhænger af, hvordan du vil bruge filen.

## Gemmeformater

### MCX (oprindeligt format)

MCX er MatterCADs oprindelige filformat og det bedste valg til designs, du vil fortsætte med at redigere senere. Det bevarer:

- Hele designtræet med alle objekter og deres hierarki
- Alle parametre og indstillinger for hvert objekt
- Booleske operationer, arrays og andre operationer i redigerbar form
- Komponentrelationer

**Brug MCX, når:** Du vil gemme dit arbejde og fortsætte med at redigere det senere.

### STL

STL er det mest udbredte format til 3D-print. Det indeholder kun den endelige trekantsnetgeometri uden designhistorik eller parametre.

**Brug STL, når:** Du vil 3D-printe dit design eller dele det med nogen, der ikke bruger MatterCAD.

### OBJ

OBJ (Wavefront) er et almindeligt 3D-format, som understøttes af de fleste 3D-programmer. Ligesom STL indeholder det kun netgeometri.

**Brug OBJ, når:** Du har brug for at åbne dit design i andre 3D-programmer som Blender eller en spilmotor.

### SVG

SVG-eksport opretter en 2D-vektorfil ud fra dit designs visning oppefra. Det er nyttigt til laserskæring eller CNC-fræsning.

**Brug SVG, når:** Du har brug for et 2D-omrids af dit design til laserskæring eller gravering.

## Sådan gemmer du

![20260324 080726 paste 20260324 080726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080726-paste-20260324-080726.jpg)

1. Åbn **brandmenuen** (MatterCAD-logoet i øverste venstre hjørne)
2. Vælg **Gem som** for at vælge en placering og et format
3. Vælg filformatet i formatrullemenuen
4. Vælg, hvor filen skal gemmes, og klik på **Gem**

Dit design gemmes også automatisk, mens du arbejder, så du ikke mister ændringer, hvis du lukker programmet.

## Tips

- Gem altid en MCX-kopi af dit design, før du eksporterer til STL eller OBJ, så du kan foretage ændringer senere
- Når du eksporterer til STL, sammenflettes alle objekter i scenen til ét enkelt net
- Hvis du vil dele et design med nogen, der bruger MatterCAD, så send MCX-filen for at bevare den fulde redigerbarhed
- Du kan også gemme designs i dit [Skybibliotek](../library/cloud-library.md), så du har adgang til dem fra enhver computer

## Relateret

- [Tilføj eksisterende objekter](adding-existing-objects.md) – Importer filer til MatterCAD
- [Bibliotek](../library/index.md) – Organisér dine gemte designs
- [Skybibliotek](../library/cloud-library.md) – Gem designs i skyen
