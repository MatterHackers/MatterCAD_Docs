---
title: Roter
articleKey: RotateObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 9bdc210c5c375fe3179050e8a8916d895455ce5f
source_lang: en
---
# Roter

Roter dreier et objekt rundt en angitt akse med en gitt vinkel. Du kan rotere rundt en hvilken som helst akseretning og velge rotasjonens senterpunkt.

<!--  Screenshot showing the Rotate operation with the rotation gizmo visible in the viewport -->
![20260506 160726 paste 20260506 160726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160726-paste-20260506-160726.jpg)

## Slik bruker du den

1. Velg et objekt
2. Bruk operasjonen **Roter** fra Transformer-menyen
3. Angi rotasjonsvinkelen og aksen i Egenskaper-panelet

Du kan også rotere objekter direkte i visningsområdet ved å klikke på rotasjonskontrollene i hjørnene av et valgt objekt. Når du beveger musen over vinkelindikatorene, festes den til trinn på 45 grader.

## Parametere

- **Vinkel** – Rotasjonsvinkelen i grader (område: 3–360). Støtter [uttrykk](../../workspace/expressions.md).
- **Roter om** – Definerer rotasjonsaksen og origopunktet. Du kan rotere rundt X-, Y- eller Z-aksen, eller angi en egendefinert retning.

## Tips

- Rotasjonen sentreres som standard om senteret i objektets avgrensningsboks
- For rotasjoner på 90 grader gjør festeindikatorene det enkelt å få eksakte verdier
- Bruk operasjonen Roter (i stedet for kontrollene i visningsområdet) når du trenger en nøyaktig vinkel som ikke er et multiplum av 45 grader
- Du kan endre rotasjonsaksen etter at operasjonen er brukt ved å redigere egenskapen Roter om

## Relatert

- [Flytt](translate.md) – Flytt et objekt en bestemt avstand
- [Skaler](scale.md) – Endre størrelsen på et objekt
- [Speil](mirror.md) – Opprett en speilvendt refleksjon
