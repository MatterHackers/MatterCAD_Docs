---
title: Justér
articleKey: AlignObject3D_3
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 1fadae72ba00cb06e36a21f0b96962dcff3f60ad
source_lang: en
---
# Justér

Justér placerer flere objekter præcist i forhold til et ankerobjekt. Brug den til at rette kanter ind, centrere dele på hinanden, placere et objekt oven på et andet eller oprette jævnt fordelte stabler.

<!--  Screenshot showing two objects being aligned with alignment options visible -->
![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)


## Sådan bruges den

1. Vælg to eller flere objekter.
2. Anvend handlingen **Justér** fra menuen **Placering**.
3. Vælg **Anker**-objektet. Ankeret bliver stående, og de øvrige objekter flyttes.
4. Indstil justeringen for X-, Y- og Z-aksen uafhængigt af hinanden.
5. Brug **Anvend**, når du vil indbrænde de justerede positioner i objekttræet.

## Parametre

### Anker

Listen **Anker** vælger det underobjekt, der bruges som reference. Ankeret flytter sig ikke. Alle andre underobjekter i handlingen Justér flyttes i forhold til ankeret, medmindre en akse bruger tilstanden **Stablet**.

### Aksekontroller

Hver akse har sine egne kontroller. Du kan justere på én akse, to akser eller alle tre. Minimum- og maksimumkanterne er navngivet efter aksen:

- **X-akse** – Min er venstre, Maks er højre.
- **Y-akse** – Min er forrest, Maks er bagest.
- **Z-akse** – Min er nederst, Maks er øverst.

For hver akse:

- **Justér** – Vælger ankerets referencepunkt for den akse. Brug **Ingen** for at lade positionerne være uændrede på den akse.
- **Tilstand** – Styrer, hvordan den valgte justering anvendes:
  - **Simpel** – Match hvert flyttet objekts tilsvarende kant, centrum eller nulpunkt med ankeret. Der bruges ingen forskydning.
  - **Forskydning** – Vælg, hvilken del af det flyttede objekt der skal lande på ankerreferencen, og tilføj derefter afstand med **Forskydning**.
  - **Stablet** – Placér objekterne efter hinanden langs den akse med **Forskydning** som mellemrum mellem dem.
- **Underjuster** – Tilgængelig i tilstanden **Forskydning**. Vælger den del af det flyttede objekt, der skal placeres på ankerreferencen. Hvis **Underjuster** er **Ingen**, bruger Justér den samme kant, det samme centrum eller det samme nulpunkt, som er valgt under **Justér**.
- **Forskydning** – Tilgængelig i tilstandene **Forskydning** og **Stablet**. Tilføjer afstand langs den akse og understøtter [udtryk](../../workspace/expressions.md).

## Justeringstilstande

### Simpel

Brug **Simpel**, når du matcher ens positioner med hinanden. For eksempel flytter **X-justering: Centrer** alle objekter, der ikke er anker, så deres X-centrum matcher ankerets X-centrum. **Z-justering: Min** flytter alle objekter, der ikke er anker, så deres underside ligger i ankerets bundhøjde.

### Forskydning

Brug **Forskydning**, når den del af det flyttede objekt, der skal bruges, er en anden end ankerreferencen. For eksempel, for at placere et objekt oven på ankeret:

1. Sæt **Z-justering** til **Maks** (top).
2. Sæt **Z-tilstand** til **Forskydning**.
3. Sæt **Z-underjuster** til **Bund**.
4. Sæt **Z-forskydning** til det ønskede mellemrum, eller lad den stå på `0` for direkte kontakt.

Dette placerer undersiden af det flyttede objekt på ankerets top, eventuelt med afstand.

### Stablet

Brug **Stablet** til at kæde flere objekter sammen langs en akse. Objekter behandles efter navn og derefter efter internt ID, så tydelig navngivning af objekterne giver en forudsigelig stabelrækkefølge.

I tilstanden **Stablet** placeres hvert flyttet objekt op mod den forrige reference på den akse:

- Justeringen **Min** stabler mod den positive retning, f.eks. fra venstre mod højre på X eller nedefra og op på Z.
- Justeringen **Maks** stabler mod den negative retning, f.eks. fra højre mod venstre på X eller oppefra og ned på Z.
- Justeringerne **Centrer** og **Nulpunkt** bruger forskydningen mellem hvert objekts centrum eller nulpunkt.

Brug **Forskydning** i tilstanden **Stablet** til at angive mellemrummet mellem objekterne.

## Eksempler

- **Centrér objekter på printpladens område** – Vælg det objekt, der skal blive stående, som **Anker**, og sæt derefter **X-justering** og **Y-justering** til **Centrer**.
- **Placér et objekt oven på et andet** – Sæt **Z-justering** til **Maks** (top), **Z-tilstand** til **Forskydning** og **Z-underjuster** til **Bund**.
- **Tilføj et præcist mellemrum fra en kant** – Brug tilstanden **Forskydning**, vælg det flyttede objekts kant med **Underjuster**, og sæt derefter **Forskydning** til den ønskede afstand.
- **Stil flere objekter op ende mod ende** – Sæt **X-justering** til **Min** (venstre), **X-tilstand** til **Stablet**, og brug **X-forskydning** til mellemrummet.
- **Byg en lodret stabel** – Sæt **Z-justering** til **Min** (bund), **Z-tilstand** til **Stablet**, og brug **Z-forskydning** til afstanden mellem objekterne.

## Tips

- Ankerobjektet bliver stående; de øvrige objekter flytter sig for at blive justeret efter det.
- Du kan bruge forskellige tilstande på forskellige akser, f.eks. **Stablet** på X, mens du bruger **Centrer** og **Simpel** på Y.
- Brug objektnavne til at styre rækkefølgen for **Stablet**, når flere objekter justeres på én gang.
- Justér er ikke-destruktiv, indtil den anvendes. Du kan når som helst ændre indstillingerne for at justere underobjekterne på ny.
- Brug **Nulpunkt**, når du skal rette modelleringsnulpunkter ind i stedet for kanterne på afgrænsningsrammen.

## Relateret

- [Tilpas til grænser](fit-to-bounds.md) – Skalér et objekt, så det passer til bestemte mål
- [Flyt](../transform/translate.md) – Flyt en bestemt afstand
- [Gruppering](../../workspace/grouping.md) – Gruppér justerede objekter for at holde dem samlet
