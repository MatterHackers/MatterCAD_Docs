---
title: Kombinér
articleKey: CombineObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: a3066faa634b5a88a2fe1650a4e2ac278ac50e24
source_lang: en
---
# Kombinér

Kombinér fletter alt sammen til ét solidt objekt. Interne flader, hvor formerne overlappede, fjernes, så resultatet er ét sammenhængende mesh i stedet for overlappende skaller.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->
![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)

Kombinér, [Træk fra](subtract.md), [Skær](intersect.md) og [Træk fra og erstat](subtract-and-replace.md) udføres alle af ét boolesk objekt -- værktøjslinjeknappen opretter det med Kombinér allerede valgt, og du kan når som helst skifte til en af de tre andre i ikonrækken **Handling** øverst i Egenskaber-panelet.

Kombinér virker på solide objekter og på 2D-baner. Den ser på, hvad du har givet den, og udfører den rigtige type handling, så kombination af to baner giver én bane, og kombination af to meshes giver ét solidt objekt.

## Sådan bruger du den

1. Vælg to eller flere objekter
2. Klik på **Kombinér** i værktøjslinjen
3. Skift mening når som helst ved at klikke på et andet ikon i rækken **Handling** øverst i Egenskaber-panelet -- formen genopbygges med den nye handling

## Parametre

- **Handling** - Hvilken boolesk operation der skal udføres. Vises som en ikonrække øverst i panelet
- **Behold vrangvendt geometri** - Behandl en vrangvendt skal som fast materiale i stedet for at lade den ophæve rumfanget omkring sig. Slå dette til, når en model, der burde være solid, kommer tilbage med manglende dele. Det fremtvinger den langsommere, eksakte booleske motor
- **Reparer viklingsrækkefølge** - Vend hver dels vrangvendte skaller om, før den booleske operation køres. Dette retter geometrien én gang i stedet for at ændre, hvad alle senere handlinger regner for solidt, og er som regel det bedste af de to svar på en vrangvendt model

## Tips

- Kombinér samler stadig ikke-overlappende objekter i ét mesh, men de forbliver visuelt adskilte
- Kombinér håndterer Hul-objekter for dig: alt, der er markeret som et hul, trækkes fra resultatet i stedet for at blive lagt til
- Kombinér fører farver pr. flade med over fra de oprindelige objekter
- Hvis et resultat ser forkert ud, så kontrollér, at kildeobjekterne er vandtætte. **Reparer viklingsrækkefølge** retter vrangvendte skaller; [Reparer](../mesh/repair.md) retter mere omfattende skader i importerede modeller

## Relateret

- [Træk fra](subtract.md) - Skær én form ud af en anden
- [Skær](intersect.md) - Behold kun rumfanget, hvor objekter overlapper
- [Træk fra og erstat](subtract-and-replace.md) - Træk én form fra, og behold det stykke, der blev skåret væk
- [Planskæring](../reshape/plane-cut.md) - Skær med et fladt plan i stedet for med en anden form
- [Hul](../../primitives/hole.md) - En terning, der er forudkonfigureret til at blive trukket fra
- [Reparer](../mesh/repair.md) - Reparer beskadigede importerede meshes før en boolesk operation

Denne side dækker også de ældre Kombinér-objekter, som stadig findes i designs, der er gemt, før handlingerne blev slået sammen. De fungerer nøjagtigt som før; nye designs bruger det fælles booleske objekt med handlingen Kombinér valgt.
