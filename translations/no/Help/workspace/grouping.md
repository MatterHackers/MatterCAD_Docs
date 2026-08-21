---
title: Gruppering
parent: "Workspace"
nav_order: 3
source_hash: 82b506a886e270535b5bd58c3913f49328abc4d5
source_lang: en
---
# Gruppering

Gruppering kombinerer flere objekter til én enhet som kan flyttes, kopieres og bearbeides som ett objekt. I motsetning til [Kombiner](../operations/boolean/combine.md) slår ikke gruppering sammen geometrien – hvert objekt forblir separat inne i gruppen.

<!-- Screenshot showing objects before and after grouping, with the design tree showing the group hierarchy -->
![20260318 193104 paste 20260318 193104](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193104-paste-20260318-193104.jpg)

![20260318 193235 paste 20260318 193235](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193235-paste-20260318-193235.jpg)

![20260318 193138 paste 20260318 193138](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193138-paste-20260318-193138.jpg)


## Slik bruker du det

### Gruppere objekter

1. Velg to eller flere objekter (Shift-klikk eller Ctrl-klikk for å velge flere)
2. Klikk på **Grupper**-knappen i verktøylinjen
3. Objektene er nå gruppert – de flyttes sammen som én enhet

### Løse opp grupper

1. Velg en gruppe
2. Klikk på **Løs opp gruppe**-knappen i verktøylinjen
3. ![20260318 193354 paste 20260318 193354](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193354-paste-20260318-193354.jpg)
4. De enkelte objektene gjenopprettes som separate elementer

Løs opp gruppe forsøker også å skille flere volumer i én importert STL-fil, hvis de finnes.

## Grupper kontra Kombiner

| Funksjon | Grupper | Kombiner |
|---------|-------|---------|
| Objektene forblir separate | Ja | Nei |
| Kan løses opp senere | Ja | Nei (destruktiv) |
| Slår sammen overlappende geometri | Nei | Ja |
| Objektene kan ha ulike farger | Ja | Farger bevares per flate |
| Bruksområde | Organisering og forflytning | Lage enkeltstående solide former |

## Tips

- Grupper kan nestes – du kan gruppere objekter som allerede ligger i grupper
- Velg en gruppe og se i designtreet for å se og velge enkeltobjekter inne i den
- Gruppering er ikke-destruktiv og kan alltid reverseres med Løs opp gruppe

## Relatert

- [Kombiner](../operations/boolean/combine.md) – Slå sammen objekter til én solid form i stedet for å gruppere dem
- [Utvalg](selection.md) – Slik velger du flere objekter for gruppering
- [Komponenter](components.md) – Opprett gjenbrukbare parameteriserte grupper
