---
title: Træk fra og erstat
articleKey: SubtractAndReplaceObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c1698bab75faca8046b23cc148803c8063ba0678
source_lang: en
---
# Træk fra og erstat

Træk fra og erstat trækker de dele, du vælger, fra de dele, du ikke valgte, men beholder det bortskårne stykke som sin egen del i stedet for at kassere det. Brug **Del(e) der skal trækkes fra** til at vælge skæreformerne; alt andet er grundlegemet, der bliver skåret i.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->
![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)

[Kombinér](combine.md), [Træk fra](subtract.md), [Skær](intersect.md) og Træk fra og erstat udføres alle af ét boolesk objekt -- værktøjslinjeknappen opretter det med Træk fra og erstat allerede valgt, og du kan når som helst skifte til en af de tre andre fra ikonrækken **Handling** øverst i panelet Egenskaber.

Træk fra og erstat tilbydes ikke for 2D-baner -- en region har ingen fjernet volumen at give tilbage.

## Sådan bruges den

1. Vælg to eller flere objekter
2. Klik på **Træk fra og erstat** i værktøjslinjen
3. Brug **Del(e) der skal trækkes fra** til at vælge, hvilke underobjekter der er skæreformerne
4. Skift mening når som helst ved at klikke på et andet ikon i rækken **Handling** øverst i panelet Egenskaber -- formen genopbygges med den nye handling

## Parametre

- **Handling** - Hvilken boolesk operation der skal udføres. Vises som en ikonrække øverst i panelet
- **Del(e) der skal trækkes fra** - Hvilke underobjekter der er skæreformerne
- **Behold vrangvendt geometri** - Behandl en vrangvendt skal som massivt materiale i stedet for at lade den ophæve volumenet omkring sig. Slå dette til, når en model, der burde være massiv, kommer tilbage med manglende dele. Det fremtvinger den langsommere, eksakte booleske motor
- **Reparer viklingsrækkefølge** - Vend hver dels vrangvendte skaller om, før den booleske operation køres. Dette retter geometrien én gang i stedet for at ændre, hvad enhver senere handling regner som massivt, og er som regel det bedste af de to svar på en vrangvendt model

## Tips

- De to dele passer nøjagtigt sammen, fordi de kom ud af den samme handling
- Brug det til flerfarvede designs, sammenlåsende samlinger og indlæg
- Hvis et resultat ser forkert ud, så kontrollér, at kildeobjekterne er vandtætte. **Reparer viklingsrækkefølge** retter vrangvendte skaller; [Reparer](../mesh/repair.md) retter mere omfattende skader i importerede modeller

## Relateret

- [Kombinér](combine.md) - Flet flere objekter til én massiv form
- [Træk fra](subtract.md) - Skær én form ud af en anden
- [Skær](intersect.md) - Behold kun volumenet, hvor objekter overlapper
- [Planskæring](../reshape/plane-cut.md) - Skær med et fladt plan i stedet for en anden form
- [Reparer](../mesh/repair.md) - Reparer beskadigede importerede masker før en boolesk operation

Denne side dækker også de ældre Træk fra og erstat-objekter, som stadig findes i designs gemt, før handlingerne blev slået sammen. De fungerer nøjagtigt som hidtil; nye designs bruger det fælles booleske objekt med handlingen Træk fra og erstat valgt.
