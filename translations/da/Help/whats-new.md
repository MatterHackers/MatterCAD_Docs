---
title: Nyheder
nav_order: 105
source_hash: 172343b8320204d2b0ec52419324f0efd2be95a1
source_lang: en
---
# MatterCAD 2.2026.8

# Nyheder

* **Rediger underelementer**
  * Dobbeltklik på et objekt for at gå ind i det og redigere de dele, det er bygget af — direkte på pladen
  * En brødkrummesti viser, hvor du er — klik på et vilkårligt niveau for at folde dine ændringer tilbage
  * ![MatterCAD 2.2026.8](https://www.matterhackers.com/r/qgG4VA)

* **Ét boolesk værktøj**
  * Kombinér, Træk fra, Skær samt Træk fra og erstat er nu én operation — skift tilstand med et klik i stedet for at slette og anvende igen
  <!-- Boolean property panel showing the four-icon operation row with Subtract selected. ~500x350px -->
  * ![One Boolean Tool](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)

* **Booleske operationer, der bare virker**
  * En ny motor er hurtigere og lykkes med masker, der tidligere fejlede
  * Kombinér reparerer automatisk dele med huller og navngiver alt, den ikke kunne sammenføje; Planskæring efterlader nu et vandtæt, printbart massivt emne

* **Bedre redigering af 2D-stier**
  * Punkttilstande, live Spejl-symmetri, gittersnap, træk-markering og Esc for at annullere et træk
  <!-- Turn on Mirror, drag a point and watch its partner follow, then drag it onto the axis to merge. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

## Forbedringer

* **Navigation** — Tryk på Z med en 2D-sti valgt for at få en redigeringsvisning oppefra
* **Skarpere tekst** — Subpixel-tekstgengivelse slås nu automatisk til, når din skærm understøtter det
* **Modellering** — Lineær ekstrudering kan affase den nederste kant med sin egen stil, radius og antal segmenter

## Vigtigste fejlrettelser

* **Pålidelig lagring** — En mislykket lagring kan ikke længere beskadige den fil, den var ved at erstatte, og du får besked om, at den mislykkedes
* **Skybibliotek** — Når et skyelement gemmes på disken, bevares fanens navn, og fanen overlever en genstart
* **Indlæsning af filer** — Rettet, at 3MF-dele lydløst blev udeladt ved indlæsning
* **Redigering af stier** — Rettet et nedbrud ved sletning af et kurvepunkt samt at sømpunkter nulstillede den tilstand, du havde valgt
* **Baggrundsopgaver** — Stop-knappen på en kørende opgave kan nu klikkes og annullerer rent faktisk

## Du kan se de fulde udgivelsesnoter [Her](release-notes.md).
