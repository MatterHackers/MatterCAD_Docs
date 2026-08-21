---
title: Nyheter
nav_order: 105
source_hash: 172343b8320204d2b0ec52419324f0efd2be95a1
source_lang: en
---
# MatterCAD 2.2026.8

# Nyheter

* **Rediger underelementer**
  * Dobbeltklikk på et objekt for å gå inn i det og redigere delene det er bygget av, rett på plattformen
  * En brødsmulesti viser hvor du er — klikk på et hvilket som helst nivå for å folde endringene dine tilbake inn
  * ![MatterCAD 2.2026.8](https://www.matterhackers.com/r/qgG4VA)

* **Ett boolsk verktøy**
  * Kombiner, Trekk fra, Skjæring og Trekk fra og erstatt er nå én operasjon — bytt modus med et klikk i stedet for å slette og bruke på nytt
  <!-- Boolean property panel showing the four-icon operation row with Subtract selected. ~500x350px -->
  * ![One Boolean Tool](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)

* **Boolske operasjoner som bare virker**
  * En ny motor er raskere og lykkes med masker som tidligere mislyktes
  * Kombiner reparerer deler med hull automatisk og navngir alt den ikke kunne slå sammen; Plankutt gir nå et vanntett, utskrivbart solid

* **Bedre 2D-baneredigering**
  * Punktmodi, direkte Speil-symmetri, rutenettfesting, dra-merking og Esc for å avbryte en dra-bevegelse
  <!-- Turn on Mirror, drag a point and watch its partner follow, then drag it onto the axis to merge. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

## Forbedringer

* **Navigasjon** — Trykk Z med en 2D-bane valgt for å få en redigeringsvisning ovenfra
* **Skarpere tekst** — Subpiksel-tekstgjengivelse slås nå på automatisk når skjermen din støtter det
* **Modellering** — Lineær ekstrudering kan avfase nederste kant med egen stil, radius og segmentantall

## Viktigste feilrettinger

* **Pålitelig lagring** — En mislykket lagring kan ikke lenger ødelegge filen den skulle erstatte, og den varsler deg om at den mislyktes
* **Skybibliotek** — Når du lagrer et skyelement til disk, beholdes fanenavnet, og fanen overlever en omstart
* **Fillasting** — Rettet at 3MF-deler ble utelatt uten varsel ved lasting
* **Baneredigering** — Rettet et krasj ved sletting av et kurvepunkt, og at sømpunkter tilbakestilte modusen du valgte
* **Bakgrunnsoppgaver** — Stopp-knappen på en pågående oppgave er nå klikkbar og avbryter faktisk

## Du kan se de fullstendige versjonsmerknadene [Her](release-notes.md).
