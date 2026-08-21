---
title: Gruppér
parent: "Workspace"
nav_order: 3
source_hash: 82b506a886e270535b5bd58c3913f49328abc4d5
source_lang: en
---
# Gruppér

Gruppering kombinerer flere objekter til én enhed, der kan flyttes, kopieres og bearbejdes som ét objekt. I modsætning til [Kombinér](../operations/boolean/combine.md) fletter gruppering ikke geometrien -- hvert objekt forbliver adskilt inde i gruppen.

<!-- Screenshot showing objects before and after grouping, with the design tree showing the group hierarchy -->
![20260318 193104 paste 20260318 193104](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193104-paste-20260318-193104.jpg)

![20260318 193235 paste 20260318 193235](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193235-paste-20260318-193235.jpg)

![20260318 193138 paste 20260318 193138](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193138-paste-20260318-193138.jpg)


## Sådan bruges den

### Gruppering af objekter

1. Vælg to eller flere objekter (Shift-klik eller Ctrl-klik for at markere flere)
2. Klik på knappen **Gruppér** på værktøjslinjen
3. Objekterne er nu grupperet -- de flytter sig sammen som én enhed

### Opdeling af grupper

1. Vælg en gruppe
2. Klik på knappen **Opdel gruppe** på værktøjslinjen
3. ![20260318 193354 paste 20260318 193354](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193354-paste-20260318-193354.jpg)
4. De enkelte objekter gendannes som separate elementer

Opdel gruppe forsøger også at adskille flere legemer i én enkelt importeret STL-fil, hvis de findes.

## Gruppér vs. Kombinér

| Funktion | Gruppér | Kombinér |
|---------|-------|---------|
| Objekter forbliver adskilte | Ja | Nej |
| Kan opdeles senere | Ja | Nej (destruktiv) |
| Fletter overlappende geometri | Nej | Ja |
| Objekter kan have forskellige farver | Ja | Farver bevares pr. flade |
| Anvendelse | Organisering og flytning | Oprettelse af enkelte massive former |

## Tips

- Grupper kan indlejres -- du kan gruppere objekter, der allerede indgår i grupper
- Vælg en gruppe, og se i designtræet for at se og vælge de enkelte objekter i den
- Gruppering er ikke-destruktiv og kan altid fortrydes med Opdel gruppe

## Relateret

- [Kombinér](../operations/boolean/combine.md) - Flet objekter til ét massivt legeme i stedet for at gruppere dem
- [Markering](selection.md) - Sådan vælger du flere objekter til gruppering
- [Komponenter](components.md) - Opret genanvendelige parameteriserede grupper
