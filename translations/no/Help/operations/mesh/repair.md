---
title: Reparer
articleKey: RepairObject3D_2
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: f637470dee4f722b595f07d2da9dcdaac5e8da72
source_lang: en
---
# Reparer

Reparer retter opp vanlige problemer i nettgeometri, blant annet ikke-manifolde kanter, hull, inkonsistent flateorientering og nesten sammenfallende hjørnepunkter. Dette er spesielt nyttig for importerte STL- og OBJ-filer som kan inneholde feil.

![20260324 080517 paste 20260324 080517](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080517-paste-20260324-080517.jpg)


## Slik bruker du den

1. Velg et objekt med nettproblemer
2. Bruk operasjonen **Reparer** fra Nett-menyen
3. Gå gjennom statistikken før/etter for å se hva som ble rettet

## Statistikk (skrivebeskyttet)

- **Innledende hjørnepunkter / Endelige punkter** - Antall hjørnepunkter før og etter reparasjon
- **Innledende flater / Endelige flater** - Antall flater før og etter reparasjon
- **Innledende ikke-manifolde kanter / Endelige ikke-manifolde kanter** - Antall problemkanter før og etter

### Avanserte alternativer

Slå på **Avansert**-modus for detaljert kontroll:

- **Sveis hjørnepunkter** - Slå sammen nesten sammenfallende hjørnepunkter (standard: på)
- **Sveisetoleranse** - Hvor nær hjørnepunktene må være for å slås sammen
- **Flateorientering** - Snur skall som vender inn og ut riktig vei, slik at hvert legeme leses som massivt. Hvert skall vurderes for seg, slik at en hul modell beholder hulrommene sine i stedet for å få dem fylt igjen. Skall der flatene er uenige med hverandre, blir latt i fred i stedet for gjettet på, og modeller som ikke er vanntette faller tilbake på en mer tolerant reparasjon - kjør **Fyll hull** først hvis orientering alene ikke løser det.
- **Sveis kanter** - Reparer små sprekker og dårlige sømmer
- **Fyll hull** - Fyll åpninger i nettoverflaten
- **Fjerningsmodus** - Fjern innvendig eller skjult geometri:
  - **Ingen** - Behold all geometri
  - **Innvendig** - Fjern innvendige legemer som er skjult inne i hovedformen
  - **Skjult** - Fjern flater som er blokkert fra utsiden

## Tips

- Prøv Reparer først hvis boolske operasjoner (Kombiner, Trekk fra) gir uventede resultater på importerte modeller
- Standardinnstillingene (Sveis hjørnepunkter på, alt annet av) retter de vanligste problemene
- Slå på Fyll hull hvis du kan se gjennom åpninger i modellen
- Bruk Fjern innvendig for å rydde opp i modeller som har skjult geometri inni

## Relatert

- [Desimer](decimate.md) - Reduser antall polygoner
- [Legge til eksisterende objekter](../../getting-started/adding-existing-objects.md) - Importer modeller som kan trenge reparasjon
