---
title: Skær
articleKey: IntersectionObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b997cfc4f6d2f02559346365311f217388a6a2da
source_lang: en
---
# Skær

Skær beholder kun det volumen, som alle objekter deler, og kasserer resten.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->
![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)

[Kombinér](combine.md), [Træk fra](subtract.md), Skær og [Træk fra og erstat](subtract-and-replace.md) udføres alle af ét boolesk objekt -- værktøjslinjeknappen opretter det med Skær allerede valgt, og du kan når som helst skifte til en af de tre andre fra ikonrækken **Handling** øverst i panelet Egenskaber.

Skær virker på faste emner og på 2D-baner. Den ser på det, du giver den, og udfører den rigtige slags handling, så skæring af to baner giver én bane, og skæring af to masker giver ét fast emne.

## Sådan bruges den

1. Vælg to eller flere objekter
2. Klik på **Skær** i værktøjslinjen
3. Skift mening når som helst ved at klikke på et andet ikon i rækken **Handling** øverst i panelet Egenskaber -- formen genopbygges med den nye handling

## Parametre

- **Handling** - Hvilken boolesk operation der skal udføres. Vises som en ikonrække øverst i panelet
- **Behold vrangvendt geometri** - Behandl en vrangvendt skal som massivt materiale i stedet for at lade den ophæve volumenet omkring sig. Slå dette til, når en model, der burde være massiv, kommer tilbage med manglende dele. Det gennemtvinger den langsommere, eksakte booleske motor
- **Reparer viklingsrækkefølge** - Vend viklingen på hver dels vrangvendte skaller, før den booleske operation køres. Dette retter geometrien én gang i stedet for at ændre, hvad enhver senere handling regner for massivt, og er som regel det bedste af de to svar på en vrangvendt model

## Tips

- Objekterne skal overlappe hinanden. Hvis de ikke reelt overlapper, bliver resultatet tomt
- Med mere end to objekter arbejder den ned gennem listen: de første to skæres, derefter skæres det resultat med det tredje og så videre
- Hvis et resultat ser forkert ud, så kontrollér, at kildeobjekterne er vandtætte. **Reparer viklingsrækkefølge** retter vrangvendte skaller; [Reparer](../mesh/repair.md) retter mere omfattende skader i importerede modeller

## Relateret

- [Kombinér](combine.md) - Flet flere objekter sammen til én massiv form
- [Træk fra](subtract.md) - Klip én form ud af en anden
- [Træk fra og erstat](subtract-and-replace.md) - Træk én form fra og behold det stykke, der blev skåret væk
- [Planskæring](../reshape/plane-cut.md) - Klip med et fladt plan i stedet for med en anden form
- [Reparer](../mesh/repair.md) - Ret beskadigede importerede masker før en boolesk operation

Denne side dækker også de ældre Skæring-objekter, som stadig findes i designs, der er gemt, før handlingerne blev flettet sammen. De fungerer nøjagtigt som før; nye designs bruger det fælles booleske objekt med handlingen Skær valgt.
