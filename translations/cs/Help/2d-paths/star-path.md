---
title: Hvězdicová cesta
articleKey: StarPathObject3D
parent: "2D Paths"
nav_order: 5
source_hash: 74d92e4171c452cd10069921636e45d7ef9dc70e
source_lang: en
---
# Hvězdicová cesta

2D cesta ve tvaru hvězdy s nastavitelným počtem cípů a vnitřním/vnějším poloměrem. Použijte ji spolu s [Lineární extruze](../operations/path/linear-extrude.md) k vytvoření 3D hvězdicových tvarů.

<!-- Screenshot of a Star Path on the workspace -->
![20260506 080319 paste 20260506 080319](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080319-paste-20260506-080319.jpg)


## Parametry

- **Body** – Počet cípů hvězdy
- **Vnější poloměr** – Vzdálenost od středu ke špičce každého cípu
- **Vnitřní poloměr** – Vzdálenost od středu k prohlubním mezi cípy

## Tipy

- Poměr mezi vnitřním a vnějším poloměrem určuje, jak je hvězda „špičatá“. Malý vnitřní poloměr vytváří ostré, výrazné cípy.
- Nastavte **Body** na 5 pro klasickou hvězdu, na 6 pro Davidovu hvězdu nebo na vyšší hodnotu pro tvary připomínající ozubené kolo
- Použijte [Vyhladit cestu](../operations/path/smooth-path.md) na hvězdicovou cestu a získáte hvězdy se zaoblenými tvary

## Související

- [Kruhová cesta](circle-path.md) – Hladký kruh
- [Ozubené kolo 2D](../mechanical/gear-2d.md) – Skutečný profil ozubeného kola
- [Lineární extruze](../operations/path/linear-extrude.md) – Dodá cestám výšku
