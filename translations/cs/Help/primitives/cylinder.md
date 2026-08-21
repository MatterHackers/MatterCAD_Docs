---
title: Válec
articleKey: CylinderObject3D
parent: "Primitives"
nav_order: 5
source_hash: ab8394a14de799f83dc9c39eb86b8eaf2aab37b7
source_lang: en
---
# Válec

Kulatý sloupovitý tvar s nastavitelným průměrem, výškou a počtem stran. Válec je nezbytný pro vytváření kolíků, tyček, otvorů a kulatých prvků.

<!--  Screenshot of a Cylinder primitive on the workspace -->
![20260318 183248 paste 20260318 183248](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183248-paste-20260318-183248.jpg)


## Parametry

- **Průměr** – Šířka válce (výchozí: 20mm)
- **Výška** – Jak vysoký válec je (výchozí: 20mm)
- **Strany** – Počet segmentů po obvodu (výchozí: 40). Nižší hodnoty vytvářejí mnohoúhelníkové tvary (např. 6 pro šestiúhelník)

### Rozšířené parametry

Zapněte režim **Rozšířené** pro přístup k dalším ovládacím prvkům:

- **Průměr nahoře** – Nastavte odlišný průměr pro horní část válce a vytvořte tak zkosené nebo komolé kuželové tvary (výchozí: odpovídá parametru Průměr)
- **Počáteční úhel** – Úhel, kde válec začíná (výchozí: 0). Použijte společně s parametrem Koncový úhel pro vytvoření částečných válců
- **Koncový úhel** – Úhel, kde válec končí (výchozí: 360). Nastavte méně než 360 pro tvary ve tvaru výseče

## Tipy

- Nastavte Strany na nízké číslo a vytvořte pravidelné mnohoúhelníky – 6 pro šestiúhelníky, 8 pro osmiúhelníky atd.
- Použijte odlišné hodnoty Průměr a Průměr nahoře pro vytvoření komolých kuželů a zkosených tvarů
- Nastavte Počáteční úhel a Koncový úhel pro vytvoření tvarů výseče nebo oblouku
- Válce jsou vynikajícími řeznými nástroji pro vytváření kulatých otvorů pomocí operace [Odečíst](../operations/boolean/subtract.md)

## Související

- [Kužel](cone.md) – Válec, který se zužuje do špičky
- [Poloviční válec](half-cylinder.md) – Válec rozříznutý podélně na polovinu
- [Prstenec](ring.md) – Dutý válec (trubka)
