---
title: Uitlijnen
articleKey: AlignObject3D_3
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 1fadae72ba00cb06e36a21f0b96962dcff3f60ad
source_lang: en
---
# Uitlijnen

Uitlijnen positioneert meerdere objecten nauwkeurig ten opzichte van een ankerobject. Gebruik het om randen op één lijn te brengen, onderdelen op elkaar te centreren, een object boven op een ander te plaatsen of gelijkmatig gespreide stapels te maken.

<!--  Screenshot showing two objects being aligned with alignment options visible -->
![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)


## Gebruik

1. Selecteer twee of meer objecten.
2. Pas de bewerking **Uitlijnen** toe via het menu **Plaatsing**.
3. Kies het **Anker**-object. Het anker blijft op zijn plaats en de andere objecten verplaatsen.
4. Stel de uitlijning voor de X-, Y- en Z-as onafhankelijk van elkaar in.
5. Gebruik **Toepassen** wanneer je de uitgelijnde posities definitief in de objectstructuur wilt vastleggen.

## Parameters

### Anker

Met de lijst **Anker** selecteer je het onderliggende object dat als referentie dient. Het anker verplaatst niet. Elk ander onderliggend object in de bewerking Uitlijnen wordt ten opzichte van het anker herpositioneerd, tenzij voor een as de modus **Gestapeld** wordt gebruikt.

### Asbesturing

Elke as heeft zijn eigen besturing. Je kunt uitlijnen op één as, twee assen of alle drie. De minimum- en maximumranden zijn per as benoemd:

- **X-as** - Min is links, Max is rechts.
- **Y-as** - Min is voor, Max is achter.
- **Z-as** - Min is onder, Max is boven.

Voor elke as:

- **Uitlijnen** - Kiest het referentiepunt van het anker voor die as. Gebruik **Geen** om de posities op die as ongewijzigd te laten.
- **Modus** - Bepaalt hoe de gekozen uitlijning wordt toegepast:
  - **Eenvoudig** - Laat de overeenkomstige rand, het midden of de oorsprong van elk bewegend object samenvallen met het anker. Er wordt geen offset gebruikt.
  - **Offset** - Kies welk deel van het bewegende object op de ankerreferentie moet komen en voeg vervolgens ruimte toe met **Offset**.
  - **Gestapeld** - Plaatst objecten na elkaar langs die as, waarbij **Offset** de tussenruimte bepaalt.
- **Subuitlijnen** - Beschikbaar in de modus **Offset**. Kiest het deel van het bewegende object dat op de ankerreferentie wordt geplaatst. Als **Subuitlijnen** op **Geen** staat, gebruikt Uitlijnen dezelfde rand, hetzelfde midden of dezelfde oorsprong als geselecteerd bij **Uitlijnen**.
- **Offset** - Beschikbaar in de modi **Offset** en **Gestapeld**. Voegt afstand toe langs die as en ondersteunt [expressies](../../workspace/expressions.md).

## Uitlijningsmodi

### Eenvoudig

Gebruik **Eenvoudig** wanneer je gelijksoortige posities op elkaar afstemt. Zo verplaatst **X-uitlijning: Midden** elk niet-ankerobject zodat het X-midden samenvalt met het X-midden van het anker. **Z uitlijnen: Min** verplaatst elk niet-ankerobject zodat de onderkant op de onderkanthoogte van het anker ligt.

### Offset

Gebruik **Offset** wanneer het deel van het bewegende object moet verschillen van de ankerreferentie. Bijvoorbeeld om een object boven op het anker te plaatsen:

1. Stel **Z uitlijnen** in op **Max** (boven).
2. Stel **Z-modus** in op **Offset**.
3. Stel **Z Subuitlijnen** in op **Onder**.
4. Stel **Z-offset** in op de gewenste tussenruimte, of laat het op `0` staan voor direct contact.

Hierdoor komt de onderkant van het bewegende object op de bovenkant van het anker te liggen, met optionele tussenruimte.

### Gestapeld

Gebruik **Gestapeld** om meerdere objecten achter elkaar langs een as te plaatsen. Objecten worden verwerkt op naam en vervolgens op interne ID, dus duidelijke objectnamen geven een voorspelbare stapelvolgorde.

In de modus **Gestapeld** wordt elk bewegend object tegen de vorige referentie op die as geplaatst:

- Uitlijning op **Min** stapelt in de positieve richting, zoals van links naar rechts op X of van onder naar boven op Z.
- Uitlijning op **Max** stapelt in de negatieve richting, zoals van rechts naar links op X of van boven naar onder op Z.
- Uitlijning op **Midden** en **Oorsprong** gebruikt de offset tussen het midden of de oorsprong van elk object.

Gebruik **Offset** in de modus **Gestapeld** om de tussenruimte tussen objecten in te stellen.

## Voorbeelden

- **Objecten centreren op het bedoppervlak** - Kies het object dat vast moet blijven als **Anker** en stel vervolgens **X-uitlijning** en **Y-uitlijning** in op **Midden**.
- **Een object boven op een ander plaatsen** - Stel **Z uitlijnen** in op **Max** (boven), **Z-modus** op **Offset** en **Z Subuitlijnen** op **Onder**.
- **Een nauwkeurige tussenruimte vanaf een rand toevoegen** - Gebruik de modus **Offset**, kies de rand van het bewegende object met **Subuitlijnen** en stel **Offset** in op de gewenste afstand.
- **Meerdere objecten achter elkaar uitlijnen** - Stel **X-uitlijning** in op **Min** (links), **X-modus** op **Gestapeld** en gebruik **X-offset** voor de tussenruimte.
- **Een verticale stapel bouwen** - Stel **Z uitlijnen** in op **Min** (onder), **Z-modus** op **Gestapeld** en gebruik **Z-offset** voor de ruimte tussen objecten.

## Tips

- Het ankerobject blijft op zijn plaats; andere objecten verplaatsen om erop uit te lijnen.
- Je kunt verschillende modi op verschillende assen gebruiken, bijvoorbeeld **Gestapeld** op X terwijl je **Midden** en **Eenvoudig** op Y gebruikt.
- Gebruik objectnamen om de volgorde bij **Gestapeld** te bepalen wanneer meerdere objecten tegelijk worden uitgelijnd.
- Uitlijnen is niet-destructief totdat het wordt toegepast. Je kunt de instellingen op elk moment wijzigen om de onderliggende objecten opnieuw uit te lijnen.
- Gebruik **Oorsprong** wanneer je modelleeroorsprongen wilt uitlijnen in plaats van de randen van het omhullende kader.

## Gerelateerd

- [Passend maken aan grenzen](fit-to-bounds.md) - Een object schalen zodat het binnen specifieke afmetingen past
- [Verplaatsen](../transform/translate.md) - Verplaatsen over een specifieke afstand
- [Groeperen](../../workspace/grouping.md) - Uitgelijnde objecten groeperen om ze bij elkaar te houden
