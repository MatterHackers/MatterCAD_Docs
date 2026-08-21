---
title: Prstenec
articleKey: RingObject3D
parent: "Primitives"
nav_order: 13
source_hash: fd16c400f3d8c8af13416ab57ddd8407e761d93a
source_lang: en
---
# Prstenec

Dutý válec (trubka) s nezávislým vnitřním a vnějším průměrem a zadanou výškou. Známý také jako trubka nebo potrubí.

<!--  Screenshot of a Ring primitive on the workspace -->
![20260318 183848 paste 20260318 183848](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183848-paste-20260318-183848.jpg)


## Parametry

- **Vnější průměr** - Vnější šířka prstence (výchozí: 20mm)
- **Vnitřní průměr** - Průměr dutého středu (výchozí: 15mm)
- **Výška** - Jak vysoký prstenec je (výchozí: 5mm)
- **Strany** - Počet segmentů po obvodu (výchozí: 40)

### Rozšířené parametry

Pro další ovládací prvky zapněte režim **Rozšířené**:

- **Počáteční úhel** - Úhel, ve kterém prstenec začíná (výchozí: 0)
- **Koncový úhel** - Úhel, ve kterém prstenec končí (výchozí: 360). Nastavte méně než 360 pro částečný prstenec
- **Zaoblení** - Přidá zaoblení hran (Žádný, Nahoru nebo Dolů)
- **Směr** - Zaoblení směrem k vnitřní nebo vnější hraně (viditelné, když je Zaoblení zapnuté)
- **Segmenty zaoblení** - Hladkost zaoblení (viditelné, když je Zaoblení zapnuté)

## Tipy

- Tloušťka stěny se rovná (Vnější průměr - Vnitřní průměr) / 2
- Použijte pro podložky, distanční vložky, pouzdra a prvky ve tvaru trubky
- Nastavte velkou výšku pro potrubí nebo malou pro ploché podložky
- Použijte Počáteční úhel a Koncový úhel pro částečné tvary prstence, jako jsou C-klipy

## Související

- [Torus](torus.md) - Prstenec ve tvaru koblihy s kruhovým průřezem
- [Válec](cylinder.md) - Plný kulatý sloup (bez dutého středu)
