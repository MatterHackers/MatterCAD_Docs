---
title: Tannhjul
articleKey: GearObject3D
parent: "Mechanical Parts"
nav_order: 2
source_hash: 23098f94da8cd032e0617fbf346621504446347f
source_lang: en
---
# Tannhjul

Lag 3D-tannhjul med fullt konfigurerbar tanngeometri. MatterCAD genererer korrekte evolvent-tannprofiler som griper riktig inn i andre tannhjul med samme modul og trykkvinkel.

<!-- AUTO_IMAGE: type=from_thumbnail item=gear file=mechanical_gears -->
![mechanical_gears](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_gears.png)

## Slik bruker du det

1. Legg til et **Tannhjul** fra Mekanisk-verktøyene eller Primitiver-panelet
2. Angi antall tenner og andre parametere
3. Tannprofilen genereres automatisk

## Parametere

### Funksjoner

- **Tannhjultype** - Ekstern tannhjul eller Tannstang (rett stang med tenner)
- **Høyde** - Tannhjulets tykkelse (ekstruderingshøyde)
- **Antall tenner** - Antall tenner rundt tannhjulet (standard: 30, område: 4-60)
- **Sirkulær deling** - Buelengden mellom tennene langs stigningssirkelen (område: 3-30). Dette bestemmer den totale størrelsen.
- **Senterhulldiameter** - Diameter på senterakselhullet (standard: 4mm, sett til 0 for ingen hull). Kun eksterne tannhjul.
- **Ytre kantbredde** - Bredden på kanten utenfor de indre tennene
- **Antall tenner på indre tannhjul** - Antall tenner på det inngripende indre tannhjulet

### Avansert

- **Trykkvinkel** - Vinkelen på tannens kontaktflate (vanlige verdier: 14,5, 20 eller 25 grader). Alle tannhjul som griper inn i hverandre må bruke samme trykkvinkel.
- **Klaring** - Minste avstand mellom tanntoppen og bunnen på den inngripende tannen
- **Slark** - Minste avstand mellom tenner som griper inn i hverandre, for å hindre at de setter seg fast

### Tannhjuldata (skrivebeskyttet)

- **Stigningsradius** - Radiusen der tannhjulene griper inn i hverandre
- **Ytre diameter** - Den totale diameteren ut til tanntoppene

## Tips

- To tannhjul griper riktig inn i hverandre når de har samme Sirkulær deling og Trykkvinkel
- Bruk verdiene for Stigningsradius til å plassere inngripende tannhjul riktig -- avstanden mellom tannhjulsentrene skal være lik summen av stigningsradiene deres
- Legg til Slark for 3D-printede tannhjul for å ta høyde for printetoleranser
- For 2D-tannprofiler (til bruk med Ekstruder), se [Tannhjul 2D](gear-2d.md)

## Relatert

- [Tannhjul 2D](gear-2d.md) - 2D-tannhjulbane for baneoperasjoner
- [Gjenger](threads.md) - Lag gjengede funksjoner
