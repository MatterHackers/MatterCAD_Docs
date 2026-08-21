---
title: Cilindru
articleKey: CylinderObject3D
parent: "Primitives"
nav_order: 5
source_hash: ab8394a14de799f83dc9c39eb86b8eaf2aab37b7
source_lang: en
---
# Cilindru

O formă de coloană rotundă cu diametru, înălțime și număr de laturi configurabile. Cilindrul este esențial pentru crearea de știfturi, tije, găuri și elemente rotunde.

<!--  Screenshot of a Cylinder primitive on the workspace -->
![20260318 183248 paste 20260318 183248](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183248-paste-20260318-183248.jpg)


## Parametri

- **Diametru** - Lățimea de-a lungul cilindrului (implicit: 20mm)
- **Înălțime** - Cât de înalt este cilindrul (implicit: 20mm)
- **Laturi** - Numărul de segmente de pe perimetru (implicit: 40). Valorile mai mici creează forme poligonale (de ex., 6 pentru un hexagon)

### Parametri avansați

Activați modul **Avansat** pentru a accesa comenzi suplimentare:

- **Diametru superior** - Setați un diametru diferit pentru partea de sus a cilindrului pentru a crea forme conice sau de trunchi de con (implicit: identic cu Diametru)
- **Unghi inițial** - Unghiul de la care începe cilindrul (implicit: 0). Utilizați-l împreună cu Unghi final pentru a crea cilindri parțiali
- **Unghi final** - Unghiul la care se termină cilindrul (implicit: 360). Setați o valoare mai mică de 360 pentru forme de felie de tort

## Sfaturi

- Setați Laturi la un număr mic pentru a crea poligoane regulate -- 6 pentru hexagoane, 8 pentru octogoane etc.
- Utilizați valori diferite pentru Diametru și Diametru superior pentru a crea trunchiuri de con și forme conice
- Setați Unghi inițial și Unghi final pentru a crea forme de felie de tort sau de arc
- Cilindrii sunt instrumente de tăiere excelente pentru crearea de găuri rotunde cu [Scădere](../operations/boolean/subtract.md)

## Asociate

- [Con](cone.md) - Un cilindru care se îngustează într-un vârf
- [Jumătate de cilindru](half-cylinder.md) - Un cilindru tăiat în două pe lungime
- [Inel](ring.md) - Un cilindru gol (tub)
