---
title: Otvor
articleKey: CubeHoleObject3D
parent: "Primitives"
nav_order: 9
source_hash: c6c802f54eaaccbd4caad827b9f967aa46b059a6
source_lang: en
---
# Otvor

Objekt ve tvaru kvádru, který je přednastaven tak, aby fungoval jako nástroj pro booleovské odečítání. Když použijete [Sloučit](../operations/boolean/combine.md), objekty typu Otvor se od ostatních tvarů automaticky odečtou místo toho, aby se k nim přičetly.

<!--  Screenshot showing a Hole object being used to cut a rectangular slot in another shape -->
![20260318 183619 paste 20260318 183619](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183619-paste-20260318-183619.jpg)


## Jak to funguje

Primitivum Otvor funguje stejně jako [Kvádr](cube.md), ale má typ výstupu nastaven na „Otvor“. Když sloučíte objekty, mezi nimiž je Otvor, objem Otvoru se z výsledku odebere.

## Parametry

Stejné jako u [Kvádr](cube.md):

- **Šířka** – Velikost podél osy X
- **Hloubka** – Velikost podél osy Y
- **Výška** – Velikost podél osy Z

## Tipy

- Umístěte Otvor tak, aby se překrýval s objektem, který chcete oříznout
- Nechte Otvor procházet zcela skrz cílový objekt, pokud chcete průchozí otvor
- Pro stejný účinek můžete použít běžné tvary s operací [Odečíst](../operations/boolean/subtract.md), ale Otvory jsou pohodlné, protože fungují automaticky s operací [Sloučit](../operations/boolean/combine.md)
- Pro kulaté otvory použijte raději [Válec](cylinder.md) s operací Odečíst

## Související

- [Kvádr](cube.md) – Stejný tvar bez chování otvoru
- [Sloučit](../operations/boolean/combine.md) – Sloučí tvary a automaticky odečte Otvory
- [Odečíst](../operations/boolean/subtract.md) – Ruční odečtení libovolného tvaru od jiného
