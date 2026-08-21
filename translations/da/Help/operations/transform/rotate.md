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

Roter drejer et objekt omkring en angivet akse med en given vinkel. Du kan rotere omkring en hvilken som helst akseretning og vælge rotationens centrum.

<!--  Screenshot showing the Rotate operation with the rotation gizmo visible in the viewport -->
![20260506 160726 paste 20260506 160726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160726-paste-20260506-160726.jpg)

## Sådan bruges den

1. Vælg et objekt
2. Anvend handlingen **Roter** fra menuen Transformér
3. Angiv rotationsvinklen og aksen i panelet Egenskaber

Du kan også rotere objekter direkte i viewporten ved at klikke på rotationshåndtagene i hjørnerne af et valgt objekt. Når du bevæger musen hen over vinkelindikatorerne, fastlåses den i trin på 45 grader.

## Parametre

- **Vinkel** - Rotationsvinklen i grader (interval: 3-360). Understøtter [udtryk](../../workspace/expressions.md).
- **Roter om** - Definerer rotationsaksen og origo. Du kan rotere omkring X-, Y- eller Z-aksen eller angive en brugerdefineret retning.

## Tips

- Rotationen centreres som standard om midten af objektets afgrænsningsboks
- Ved 90-graders rotationer gør fastlåsningsindikatorerne det nemt at ramme præcise værdier
- Brug handlingen Roter (i stedet for viewportens håndtag), når du har brug for en præcis vinkel, der ikke er et multiplum af 45 grader
- Du kan ændre rotationsaksen, efter at handlingen er anvendt, ved at redigere egenskaben Roter om

## Relateret

- [Flyt](translate.md) - Flyt et objekt en bestemt afstand
- [Skalér](scale.md) - Ændr størrelsen på et objekt
- [Spejl](mirror.md) - Opret en spejlvendt kopi
