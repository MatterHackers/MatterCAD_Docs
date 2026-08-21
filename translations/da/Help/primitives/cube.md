---
title: Terning
articleKey: CubeObject3D
parent: "Primitives"
nav_order: 4
source_hash: a376a9c78d88d995f3c6ce21dd5098672d6c1dfb
source_lang: en
---
# Terning

En rektangulær kasseform med justerbar bredde, dybde, højde og valgfrie afrundede kanter. Terning er en af de mest anvendte primitiver til opbygning af designs.

<!--  Screenshot of a Cube primitive on the workspace -->
![20260318 183230 paste 20260318 183230](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183230-paste-20260318-183230.jpg)


## Parametre

- **Bredde** - Størrelse langs X-aksen (standard: 20mm)
- **Dybde** - Størrelse langs Y-aksen (standard: 20mm)
- **Højde** - Størrelse langs Z-aksen (standard: 20mm)
- **Rund** - Aktivér afrundede kanter
- **Radius** - Størrelsen på afrundingen (synlig, når Rund er aktiveret)
- **Rundingssegmenter** - Blødheden af afrundingen, flere segmenter = blødere kurver (synlig, når Rund er aktiveret)

## Tips

- Brug en Terning som udgangspunkt for kasser, plader, beslag og kabinetter
- Aktivér Rund for bløde, professionelt udseende kanter
- Radius kan ikke overstige halvdelen af den mindste dimension
- Kombinér en Terning med [Træk fra](../operations/boolean/subtract.md) for at lave rektangulære udskæringer og slidser

## Relateret

- [Cylinder](cylinder.md) - Rund søjleform
- [Pyramide](pyramid.md) - Tilspidset firesidet form
- [Hul](hole.md) - En terning forudindstillet til boolesk fratrækning
