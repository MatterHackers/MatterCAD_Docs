---
title: Reeks
articleKey: ArrayObject3D_2
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c547fa24e5f47e0d60f0cec0eac979700d946daf
source_lang: en
---
# Reeks

Met Reeks maak je meerdere kopieën van een object die in een patroon worden geplaatst. Kies een modus met de knoppen bovenaan — **Lineair**, **Radiaal** of **Transformeren** — om tussen patroontypen te wisselen.

<!--  Screenshot of the Array operation panel showing the mode buttons at the top (Linear | Radial | Transform) -->
![20260506 080647 paste 20260506 080647](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080647-paste-20260506-080647.jpg)


## Gebruik

1. Selecteer een object
2. Pas de bewerking **Reeks** toe vanuit het menu Duplicatie
3. Kies een modus (Lineair, Radiaal of Transformeren)
4. Pas de parameters van de gekozen modus aan

## Modus: Lineair

In de modus Lineair worden kopieën langs een richting geplaatst, met optionele rotatie- en schaalprogressie.

**Aantal** — Aantal kopieën (geheel getal of expressie). Het bronobject is de eerste kopie; extra kopieën worden daarvan verschoven.

**Offsetmethode** — Hoe de tussenruimte wordt berekend:
- **Relatief** — De offset wordt vermenigvuldigd met de grootte van de bounding box van het object. Een Relatieve offset van (1, 0, 0) plaatst kopieën precies één objectbreedte uit elkaar langs X.
- **Offset** — Vaste afstand in mm in de wereldruimte per kopie.
- **Eindpunt** — Stel de positie van de laatste kopie in; de tussenruimte wordt gelijkmatig over de kopieën verdeeld.

**Relatieve offset** / **Offset** / **Eindpunt** — De afstandsvector, afhankelijk van de geselecteerde Offsetmethode.

**Rotatiemodus** — Hoe rotatie zich over de kopieën opbouwt:
- **Lokaal** — Elke kopie roteert ter plaatse om haar eigen middelpunt; de offsetrichting blijft in de wereldassen.
- **Samenvoegen** — De rotatie stapelt zich op en stuurt de offset, wat spiralen, waaiers en helixen oplevert.

**Rotatie** — Rotatie per kopie in graden op elke as.

**Schalen** — Cumulatieve schaal per kopie op elke as. Waarden kleiner dan 1 verkleinen de kopieën; waarden groter dan 1 vergroten ze.

**Schaal beïnvloedt offset** — Wanneer dit aanstaat, schaalt ook de tussenruimte tussen kopieën met elke stap mee. Gebruik dit voor steeds nauwere spiralen en meetkundige reeksen (nautilusschelpen, gestapelde schelpkrommen).

## Modus: Radiaal

In de modus Radiaal worden kopieën gelijkmatig rond een middenas op een vaste straal verdeeld.

<!--  Screenshot of Array in Radial mode showing 6 copies arranged in a circle, with Radius and Central Axis parameters visible -->
![20260506 092618 paste 20260506 092618](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-092618-paste-20260506-092618.jpg)


**Telmethode** — Hoe het aantal kopieën wordt bepaald:
- **Aantal** — Expliciet aantal kopieën.
- **Afstand** — Hoekafstand tussen kopieën in graden; het aantal wordt berekend om de sweep te vullen.

**Aantal** / **Hoekafstand** — Aantal kopieën (modus Aantal) of hoekafstand in graden (modus Afstand). Ondersteunt expressies.

**Middenas** — De as waaromheen wordt geroteerd (standaard: Z).

**Cirkelsegment** — Of de kopieën een volledige cirkel van 360° beslaan (**Volledig**) of een gedeeltelijke boog (**Boog**).

**Straal** — Afstand van de middenas tot elke kopie.

**Sweep-hoek** — Aantal graden boog dat gevuld moet worden (zichtbaar wanneer Cirkelsegment op Boog staat). Ondersteunt expressies.

**Rotatie uitlijnen** — Roteer elke kopie zodat de voorwaartse as naar buiten wijst vanaf het midden.

**Voorwaartse as** — Welke as van de kopie als "voorwaarts" wordt beschouwd bij het uitlijnen (zichtbaar wanneer Rotatie uitlijnen aanstaat).

## Modus: Transformeren

In de modus Transformeren worden kopieën stapsgewijs geplaatst met een handmatige transformatie of door de transformatie van een ander object te volgen.

**Aantal** — Aantal kopieën (geheel getal of expressie).

**Transformatiereferentie** — Waar de transformatie per stap vandaan komt:
- **Invoer** — Je geeft verplaatsing, rotatie en schaal rechtstreeks op.
- **Object** — De transformatie wordt gelezen van een genoemd nevengeschikt object.

**Verplaatsing** — Offset per stap in de wereldruimte in mm (zichtbaar wanneer Referentie op Invoer staat).

**Rotatie** — Rotatie per stap in graden per as (zichtbaar wanneer Referentie op Invoer staat).

**Schalen** / **Assen schalen** — Uniforme schaal en schaal per as die bij elke stap wordt toegepast (zichtbaar wanneer Referentie op Invoer staat).

**Transformatienaam** — Naam van het nevengeschikte object waarvan de transformatie als increment per stap wordt gebruikt (zichtbaar wanneer Referentie op Object staat).

**Relatieve ruimte** — Wanneer dit aanstaat, wordt de transformatie van elke kopie opgebouwd in het lokale assenstelsel van de vorige kopie; wanneer het uitstaat, wordt elke stap in de wereldruimte toegepast (zichtbaar wanneer Referentie op Object staat).

## Willekeurig maken

Schakel **Willekeurig maken** in om variatie aan alle kopieën toe te voegen.

- **Willekeurige verschuiving** — Maximale willekeurige positieverschuiving per as in mm.
- **Willekeurige rotatie** — Maximale willekeurige rotatie per as in graden.
- **Willekeurige schaalassen** — Maximale willekeurige schaalvariatie per as.
- **Eerste uitsluiten** — Houd de eerste kopie op de exact berekende positie (standaard: aan).
- **Laatste uitsluiten** — Houd de laatste kopie op de exact berekende positie.
- **Willekeurige seed** — Wijzig deze waarde voor een andere willekeurige schikking. Ondersteunt expressies.

## Samenvoegen

- **Enkele mesh maken** — Combineer alle kopieën tot één samengevoegd mesh-object.
- **Vertices samenvoegen** — Las vertices samen binnen de drempelwaarde voor samenvoegafstand (zichtbaar wanneer Enkele mesh maken aanstaat).
- **Afstand** — Samenvoegdrempel in mm (zichtbaar wanneer Vertices samenvoegen aanstaat).

## Tips

- Gebruik expressies voor Aantal, Rotatie of Eindpunt om parametrische patronen te maken
- Gebruik voor cirkelvormige patronen de modus Radiaal — stel Straal in om de grootte van de cirkel te bepalen en schakel Rotatie uitlijnen in als de kopieën naar buiten moeten wijzen
- Met Samenvoegen als rotatie in de modus Lineair maak je spiralen en waaiers zonder handmatig hoekoffsets te berekenen
- Schaal beïnvloedt offset levert vanzelf indelingen op met nautilusschelpen en meetkundige reeksen
- Combineer Reeks met [Onderliggend item selecteren](select-child.md) om patronen te maken waarin elke kopie een andere variant toont

## Gerelateerd

- [Uitlijnen](../placement/align.md) - Objecten ten opzichte van elkaar positioneren
- [Onderliggend item selecteren](select-child.md) - Een specifieke kopie uit een reeks kiezen op index of naam
