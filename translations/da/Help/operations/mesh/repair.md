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

Reparer retter almindelige problemer i mesh-geometri, herunder ikke-manifolde kanter, huller, uensartet fladeorientering og næsten sammenfaldende knudepunkter. Det er især nyttigt til importerede STL- og OBJ-filer, der kan indeholde fejl.

![20260324 080517 paste 20260324 080517](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080517-paste-20260324-080517.jpg)


## Sådan bruges den

1. Vælg et objekt med mesh-problemer
2. Anvend handlingen **Reparer** fra Mesh-menuen
3. Gennemgå statistikken før/efter for at se, hvad der blev rettet

## Statistik (skrivebeskyttet)

- **Oprindelige hjørnepunkter / Endelige knudepunkter** - Antal knudepunkter før og efter reparation
- **Oprindelige flader / Endelige flader** - Antal flader før og efter reparation
- **Oprindelige ikke-manifolde kanter / Endelige ikke-manifolde kanter** - Antal problematiske kanter før og efter

### Avancerede indstillinger

Slå tilstanden **Avanceret** til for at få detaljeret kontrol:

- **Svejs knudepunkter** - Flet næsten sammenfaldende knudepunkter (standard: til)
- **Svejsetolerance** - Hvor tæt knudepunkter skal være på hinanden for at blive flettet
- **Fladeorientering** - Vender vrangvendte skaller den rigtige vej, så hvert emne aflæses som massivt. Hver skal vurderes for sig, så en hul model beholder sine hulrum i stedet for at få dem fyldt ud. Skaller, hvis egne flader er indbyrdes uenige, lades urørte i stedet for at blive gættet på, og modeller, der ikke er vandtætte, falder tilbage på en mere tolerant reparation - kør **Udfyld huller** først, hvis orientering alene ikke løser problemet.
- **Svejs kanter** - Reparer små revner og dårlige samlinger
- **Udfyld huller** - Fyld huller i mesh-overfladen
- **Fjernetilstand** - Fjern intern eller skjult geometri:
  - **Ingen** - Behold al geometri
  - **Indre** - Fjern indvendige emner, der er skjult inde i hovedformen
  - **Skjult** - Fjern flader, der er spærret for udsyn udefra

## Tips

- Prøv Reparer først, hvis boolske handlinger (Kombinér, Træk fra) giver uventede resultater på importerede modeller
- Standardindstillingerne (Svejs knudepunkter slået til, alt andet fra) retter de mest almindelige problemer
- Slå Udfyld huller til, hvis du kan se igennem huller i modellen
- Brug Fjern indre til at rydde op i modeller, der har skjult geometri indeni

## Relateret

- [Decimér](decimate.md) - Reducér antallet af polygoner
- [Tilføj eksisterende objekter](../../getting-started/adding-existing-objects.md) - Importer modeller, der kan have brug for reparation
