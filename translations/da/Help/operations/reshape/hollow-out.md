---
title: Udhul
articleKey: HollowOutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cc2c5555723ecfe77475fef9e7a2090cdf760204
source_lang: en
---
# Udhul

Udhul skaber en hul skal ud fra et massivt objekt ved at forskyde overfladen indad. Resultatet er en tyndvægget udgave af den oprindelige form.

<!--  Cross-section view showing a solid object hollowed out with visible wall thickness -->
![20260506 155412 paste 20260506 155412](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155412-paste-20260506-155412.jpg)

## Sådan bruges den

1. Vælg et massivt objekt
2. Anvend handlingen **Udhul** fra Omform-menuen
3. Angiv den ønskede vægtykkelse

## Parametre

- **Afstand** - Vægtykkelsen i millimeter (standard: 2 mm). Dette er, hvor tyk den resulterende skal bliver.
- **Antal celler** - Opløsningen for udhulingsalgoritmen (standard: 64). Højere værdier giver glattere indvendige overflader, men tager længere tid at beregne.

## Tips

- Udhul er nyttig til at lave kabinetter, beholdere, vaser og lette dele
- En vægtykkelse på 1-2 mm er typisk for de fleste 3D-printede dele
- Øg Antal celler, hvis den indvendige overflade virker ru eller kantet
- Udhulingen giver en åben bund -- kombinér med en [Terning](../../primitives/cube.md), hvis du har brug for en lukket bund
- Ved komplekse former kan beregningen tage nogle få sekunder

## Relateret

- [Planskæring](plane-cut.md) - Skær et objekt i en bestemt højde
- [Træk fra](../boolean/subtract.md) - Fjern materiale manuelt
