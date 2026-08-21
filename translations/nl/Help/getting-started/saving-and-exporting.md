---
title: Bezig met opslaan en Exporteren
parent: "Getting Started"
nav_order: 4
source_hash: 020d4bf43f07d3ab7dbd7d585e13c99309f0c0b8
source_lang: en
---
# Bezig met opslaan en Exporteren

MatterCAD ondersteunt verschillende bestandsformaten voor het opslaan en exporteren van je ontwerpen. Welk formaat je kiest, hangt af van hoe je het bestand wilt gebruiken.

## Opslagformaten

### MCX (native formaat)

MCX is het eigen bestandsformaat van MatterCAD en de beste keuze voor ontwerpen die je later verder wilt bewerken. Het behoudt:

- De volledige ontwerpboom met alle objecten en hun hiërarchie
- Alle parameters en instellingen van elk object
- Booleaanse bewerkingen, arrays en andere bewerkingen in bewerkbare vorm
- Componentrelaties

**Gebruik MCX wanneer:** je je werk wilt opslaan en het later verder wilt bewerken.

### STL

STL is het meest gebruikte formaat voor 3D-printen. Het bevat alleen de uiteindelijke driehoeksmesh-geometrie, zonder ontwerpgeschiedenis of parameters.

**Gebruik STL wanneer:** je je ontwerp wilt 3D-printen of wilt delen met iemand die MatterCAD niet gebruikt.

### OBJ

OBJ (Wavefront) is een veelgebruikt 3D-formaat dat door de meeste 3D-software wordt ondersteund. Net als STL bevat het alleen mesh-geometrie.

**Gebruik OBJ wanneer:** je je ontwerp moet openen in andere 3D-software, zoals Blender of een game-engine.

### SVG

Bij het exporteren naar SVG wordt een 2D-vectorbestand gemaakt op basis van het bovenaanzicht van je ontwerp. Dat is handig voor lasersnijden of CNC-frezen.

**Gebruik SVG wanneer:** je een 2D-omtrek van je ontwerp nodig hebt voor lasersnijden of graveren.

## Hoe je opslaat

![20260324 080726 paste 20260324 080726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080726-paste-20260324-080726.jpg)

1. Open het **merkmenu** (het MatterCAD-logo in de linkerbovenhoek)
2. Selecteer **Opslaan als** om een locatie en formaat te kiezen
3. Selecteer het bestandsformaat in de formaatkeuzelijst
4. Kies waar je het bestand wilt opslaan en klik op **Opslaan**

Je ontwerp wordt ook automatisch opgeslagen terwijl je werkt, dus je verliest geen wijzigingen als je de applicatie sluit.

## Tips

- Sla altijd een MCX-kopie van je ontwerp op voordat je naar STL of OBJ exporteert, zodat je later nog wijzigingen kunt aanbrengen
- Bij het exporteren naar STL worden alle objecten in de scène samengevoegd tot één mesh
- Wil je een ontwerp delen met iemand die MatterCAD gebruikt, stuur dan het MCX-bestand om de volledige bewerkbaarheid te behouden
- Je kunt ook ontwerpen opslaan in je [Cloudbibliotheek](../library/cloud-library.md) zodat je er vanaf elke computer bij kunt

## Gerelateerd

- [Bestaande objecten toevoegen](adding-existing-objects.md) - Bestanden importeren in MatterCAD
- [Bibliotheek](../library/index.md) - Je opgeslagen ontwerpen ordenen
- [Cloudbibliotheek](../library/cloud-library.md) - Ontwerpen in de cloud opslaan
