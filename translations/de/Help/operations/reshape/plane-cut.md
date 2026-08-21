---
title: Ebenenschnitt
articleKey: PlaneCutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 5
source_hash: 64a9901bf54b71cd2ecc12c8db189b6e2fcde25e
source_lang: en
---
# Ebenenschnitt

Ebenenschnitt schneidet ein Objekt auf einer angegebenen Höhe mit einer horizontalen Ebene und behält nur den Teil unterhalb des Schnitts. Die Schnittfläche wird mit einer ebenen Fläche geschlossen.

<!--  Before and after showing an object being sliced at a specific height -->
![20260506 155526 paste 20260506 155526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155526-paste-20260506-155526.jpg)

## Verwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie die Operation **Ebenenschnitt** aus dem Menü Umformen an
3. Legen Sie die Schnitthöhe fest

## Parameter

- **Schnitthöhe** – Die Z-Höhe, auf der das Objekt geschnitten wird (Standard: 10 mm, Bereich: 1–200 mm)

## Tipps

- Verwenden Sie Ebenenschnitt, um die Oberseite eines Modells auf einer bestimmten Höhe abzuflachen
- Nützlich zum Beschneiden importierter Modelle oder zum Erzeugen ebener Standflächen
- Um mit einer nicht ebenen Form zu schneiden, verwenden Sie stattdessen [Subtrahieren](../boolean/subtract.md) mit einem anderen Objekt
- Um mit einer geneigten Ebene zu schneiden, drehen Sie zuerst das Objekt, wenden Sie Ebenenschnitt an und drehen Sie es anschließend zurück

## Verwandte Themen

- [Verschneiden](../boolean/intersect.md) – Nur den Überlappungsbereich der Objekte behalten
- [Subtrahieren](../boolean/subtract.md) – Mit einer beliebigen Form schneiden, nicht nur mit einer Ebene
- [Aushöhlen](hollow-out.md) – Eine hohle Schale erzeugen
