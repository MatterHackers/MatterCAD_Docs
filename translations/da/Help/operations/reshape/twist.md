---
title: Vrid
articleKey: TwistObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: 8ea8d2017c16f20dc42b433bcf91815262bb5380
source_lang: en
---
# Vrid

Vrid roterer toppen af et objekt i forhold til bunden og skaber en spiral- eller vrideffekt langs højden. Som standard skrider rotationen jævnt frem fra bunden til toppen; under Avanceret kan du tegne, hvor langs højden drejningen faktisk sker.

<!--  Before and after showing a cube being twisted into a spiral column -->
![20260506 155620 paste 20260506 155620](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155620-paste-20260506-155620.jpg)

## Sådan bruges den

1. Vælg et objekt
2. Anvend handlingen **Vrid** fra menuen Omform
3. Indstil vridningsvinklen, og juster antallet af skiver for jævnhed
4. Slå **Avanceret** til, hvis du vil tegne, hvordan vridningen fordeles op ad emnet

## Vridningsprofilen

Under Avanceret bestemmer kurven **Vridningsprofil**, hvor vridningen sker. Den samlede vridningsmængde fastsættes stadig af kontrollen Vinkel (eller Rotationsafstand) – kurven fordeler den blot:

- **Op ad kurven** er højden på emnet i procent – 0 i bunden, 100 i toppen. En hjælpelinje tværs over editoren markerer 100 procent og er mærket med emnets faktiske højde i mm.
- **Tværs over kurven** er den procentdel af den samlede vridning, der er nået ved den højde – 0 for ingen af den, 100 for det hele.

En ny Vrid starter med en lige diagonal fra 0 til 100, hvilket er den helt jævne vridning, du får helt uden Avanceret.

Et vandret forløb i kurven er et bånd af emnet, der ikke vrides. Hvor kurven ikke dækker hele højden, fastholdes den nærmeste ende af den, så en kurve, der kun er tegnet mellem 40 og 60 procent, efterlader emnet stift under og over den – det er sådan, du starter og stopper en vridning et stykke oppe.

Et forløb, der falder tilbage, mens det går opad, vikler op: det bånd af emnet drejer den anden vej, tilbage mod udgangspunktet. At tegne profilen op forbi 100 og derefter ned igen er måden, hvorpå du overskrider den samlede vridning og vender tilbage til den.

## Parametre

- **Rotationstype** – Vælg mellem:
  - **Vinkel** – Angiv den samlede vridningsvinkel i grader (3-360)
  - **Afstand** – Angiv vridningen som en afstand langs omkredsen
- **Skiver** – Antal vandrette snit, der tilføjes for jævn vridning, fordelt jævnt op ad emnet. Flere skiver = jævnere vridning
- **Minimum antal sider** – Det mindste antal sider, emnet bør have omkring vridningsaksen. En grov form som en terning har ingen geometri omkring sin omkreds til at bære rotationen, så dens flade sider facetteres i stedet for at krumme; dette tilføjer lodrette snit gennem vridningsaksen, så disse flader kan følge vridningen. 0 (standard) lader emnet være urørt
- **Vrid til højre** – Vridningens retning: højre (med uret) eller venstre (mod uret)
- **Foretrukken radius** – Skrivebeskyttet: den radius, emnet selv angiver, eller den, som dets form indebærer, og det er den, en vridningsafstand måles omkring (kun i tilstanden Afstand)
- **Rediger radius** – Slå den angivne radius fra, så du kan indstille din egen (kun i tilstanden Afstand, og kun når emnet angiver en)
- **Tilsidesæt radius** – Brugerdefineret radius til vridningsberegningen (kun i tilstanden Afstand)

### Avancerede parametre

- **Vridningsprofil** – Kurveeditoren beskrevet ovenfor: den procentdel af den samlede vridning, der er nået ved hver højde i procent
- **Rotationsforskydning** – Forskyd det centrum, emnet drejes om, væk fra midten af emnet

## Tips

- Højere værdier for Skiver giver jævnere resultater, men genererer mere geometri
- Hvis en vredet terning eller anden form med flade sider ser facetteret ud i stedet for krum, så hæv Minimum antal sider
- Tegn profilen vandret i bunden og stigende derefter for at efterlade en lige base under en vredet søjle
- En vridning på 90 grader på en firkantet søjle skaber en elegant arkitektonisk effekt
- Tegn to vandrette forløb forbundet af en kort stigning for at vride midten af emnet og lade begge ender forblive stive

## Relateret

- [Kurve](curve.md) – Bøj et objekt til en bue
- [Knib](pinch.md) – Komprimer mod centrum
- [Radial sammentrækning](radial-pinch.md) – Form profilen med en kurve på samme måde
