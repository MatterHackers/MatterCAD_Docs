---
title: Groeperen
parent: "Workspace"
nav_order: 3
source_hash: 82b506a886e270535b5bd58c3913f49328abc4d5
source_lang: en
---
# Groeperen

Met groeperen combineert u meerdere objecten tot één geheel dat als één object kan worden verplaatst, gekopieerd en bewerkt. In tegenstelling tot [Combineren](../operations/boolean/combine.md) voegt groeperen de geometrie niet samen -- elk object blijft afzonderlijk binnen de groep bestaan.

<!-- Screenshot showing objects before and after grouping, with the design tree showing the group hierarchy -->
![20260318 193104 paste 20260318 193104](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193104-paste-20260318-193104.jpg)

![20260318 193235 paste 20260318 193235](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193235-paste-20260318-193235.jpg)

![20260318 193138 paste 20260318 193138](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193138-paste-20260318-193138.jpg)


## Gebruik

### Objecten groeperen

1. Selecteer twee of meer objecten (Shift-klik of Ctrl-klik om meerdere te selecteren)
2. Klik op de knop **Groeperen** in de werkbalk
3. De objecten zijn nu gegroepeerd -- ze bewegen samen als één geheel

### Groepering van objecten opheffen

1. Selecteer een groep
2. Klik op de knop **Groepering opheffen** in de werkbalk
3. ![20260318 193354 paste 20260318 193354](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193354-paste-20260318-193354.jpg)
4. De afzonderlijke objecten worden hersteld als losse items

Groepering opheffen probeert ook meerdere volumes binnen één geïmporteerd STL-bestand te scheiden, als die aanwezig zijn.

## Groeperen versus Combineren

| Kenmerk | Groeperen | Combineren |
|---------|-------|---------|
| Objecten blijven afzonderlijk | Ja | Nee |
| Groepering later op te heffen | Ja | Nee (destructief) |
| Voegt overlappende geometrie samen | Nee | Ja |
| Objecten kunnen verschillende kleuren hebben | Ja | Kleuren blijven per vlak behouden |
| Toepassing | Ordenen en verplaatsen | Eén massieve vorm maken |

## Tips

- Groepen kunnen genest worden -- u kunt objecten groeperen die al in groepen zitten
- Selecteer een groep en kijk in de ontwerpboom om afzonderlijke objecten daarin te bekijken en te selecteren
- Groeperen is niet-destructief en kan altijd ongedaan worden gemaakt met Groepering opheffen

## Gerelateerd

- [Combineren](../operations/boolean/combine.md) - Objecten samenvoegen tot één massief object in plaats van ze te groeperen
- [Selectie](selection.md) - Meerdere objecten selecteren om te groeperen
- [Componenten](components.md) - Herbruikbare geparametriseerde groepen maken
