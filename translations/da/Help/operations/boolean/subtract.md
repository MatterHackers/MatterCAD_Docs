---
title: Træk fra
articleKey: SubtractObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 59685bd0a635b70d7f938780f71e90be595dd993
source_lang: en
---
# Træk fra

Træk fra skærer de dele, du vælger, ud af de dele, du ikke vælger. Brug **Del(e) der skal trækkes fra** til at vælge de skærende former; alt andet er grundformen, der bliver skåret i.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->
![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)

[Kombinér](combine.md), Træk fra, [Skær](intersect.md) og [Træk fra og erstat](subtract-and-replace.md) udføres alle af ét boolesk objekt -- værktøjslinjeknappen opretter det med Træk fra allerede valgt, og du kan når som helst skifte til en af de tre andre fra ikonrækken **Handling** øverst i panelet Egenskaber.

Træk fra virker på solide objekter og på 2D-baner. Den ser på det, du giver den, og udfører den rigtige type handling, så når du trækker én bane fra en anden, får du en bane, og når du trækker ét mesh fra et andet, får du et solidt objekt.

## Sådan bruges den

1. Vælg to eller flere objekter
2. Klik på **Træk fra** i værktøjslinjen -- en standarddel, der skal skæres væk, vælges for dig, så der sker noget med det samme
3. Brug **Del(e) der skal trækkes fra** til at vælge, hvilke underobjekter der er de skærende former
4. Skift mening når som helst ved at klikke på et andet ikon i rækken **Handling** øverst i panelet Egenskaber -- formen genopbygges med den nye handling

## Parametre

- **Handling** - Hvilken boolesk handling der skal udføres. Vises som en ikonrække øverst i panelet
- **Del(e) der skal trækkes fra** - Hvilke underobjekter der er de skærende former
- **Behold fratrukne dele** - Lad de dele, der blev skåret væk, blive i scenen i stedet for at kassere dem
- **Behold vrangvendt geometri** - Behandl en vrangvendt skal som solidt materiale i stedet for at lade den ophæve rumfanget omkring sig. Slå dette til, når en model, der burde være solid, kommer tilbage med manglende dele. Det fremtvinger den langsommere, eksakte booleske motor
- **Reparer viklingsrækkefølge** - Vend viklingsrækkefølgen på hver dels vrangvendte skaller, før den booleske handling køres. Dette retter geometrien én gang i stedet for at ændre, hvad enhver senere handling opfatter som solidt, og er som regel den bedste af de to løsninger på en vrangvendt model

## Tips

- Objekterne skal overlappe, for at Træk fra gør noget
- For at skære et gennemgående hul skal du sikre dig, at det skærende objekt går helt igennem grundformen
- Til et simpelt hul er primitivet [Hul](../../primitives/hole.md) allerede sat op til at trække fra
- De skærende objekter bliver i designtræet, så du kan flytte eller ændre størrelse på dem, og udskæringen opdateres
- Hvis et resultat ser forkert ud, så kontrollér, at kildeobjekterne er vandtætte. **Reparer viklingsrækkefølge** retter vrangvendte skaller; [Reparer](../mesh/repair.md) retter mere omfattende skader i importerede modeller

## Relateret

- [Kombinér](combine.md) - Flet flere objekter til én solid form
- [Skær](intersect.md) - Behold kun det rumfang, hvor objekterne overlapper
- [Træk fra og erstat](subtract-and-replace.md) - Træk én form fra og behold det stykke, der blev skåret væk
- [Planskæring](../reshape/plane-cut.md) - Skær med et fladt plan i stedet for med en anden form
- [Hul](../../primitives/hole.md) - En terning, der på forhånd er sat op til at trække fra
- [Reparer](../mesh/repair.md) - Ret beskadigede importerede meshes før en boolesk handling

Denne side dækker også de ældre Træk fra-objekter, som stadig findes i designs gemt, før handlingerne blev slået sammen. De fungerer nøjagtigt som før; nye designs bruger det fælles booleske objekt med handlingen Træk fra valgt.
