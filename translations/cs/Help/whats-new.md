---
title: Novinky
nav_order: 105
source_hash: 172343b8320204d2b0ec52419324f0efd2be95a1
source_lang: en
---
# MatterCAD 2.2026.8

# Novinky

* **Upravit potomky**
  * Dvojklikem na libovolný objekt do něj vstoupíte a upravíte díly, ze kterých je sestaven, přímo na podložce
  * Drobečková navigace ukazuje, kde se nacházíte — kliknutím na libovolnou úroveň své úpravy zapracujete zpět
  * ![MatterCAD 2.2026.8](https://www.matterhackers.com/r/qgG4VA)

* **Jediný booleovský nástroj**
  * Sloučit, Odečíst, Průnik a Odečíst a nahradit jsou nyní jedna operace — režimy přepnete kliknutím místo mazání a opětovného použití
  <!-- Boolean property panel showing the four-icon operation row with Subtract selected. ~500x350px -->
  * ![One Boolean Tool](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)

* **Booleovské operace, které prostě fungují**
  * Nové jádro je rychlejší a uspěje i na sítích, které dříve selhávaly
  * Sloučit automaticky opraví díly s otvory a pojmenuje vše, co se nepodařilo sloučit; Řez rovinou nyní zanechává vodotěsné, tisknutelné těleso

* **Lepší úpravy 2D cest**
  * Režimy bodů, živá symetrie Zrcadlit, přichytávání k mřížce, výběr tažením a Esc pro zrušení tažení
  <!-- Turn on Mirror, drag a point and watch its partner follow, then drag it onto the axis to merge. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

## Vylepšení

* **Navigace** — Stiskněte Z s vybranou 2D cestou pro pohled shora při úpravách
* **Ostřejší text** — Subpixelové vykreslování textu se nyní zapne automaticky, pokud jej váš displej podporuje
* **Modelování** — Lineární extruze umí zkosit spodní hranu s vlastním stylem, poloměrem a počtem segmentů

## Nejdůležitější opravy chyb

* **Spolehlivost ukládání** — Neúspěšné uložení již nemůže poškodit soubor, který nahrazovalo, a oznámí vám, že selhalo
* **Cloudová knihovna** — Uložení cloudové položky na disk zachová název její karty a karta přežije restart
* **Načítání souborů** — Opraveno tiché vynechávání dílů 3MF při načítání
* **Úpravy cest** — Opraven pád při mazání bodu křivky a vracení zvoleného režimu u bodů švu
* **Úlohy na pozadí** — Tlačítko Zastavit u běžící úlohy je nyní klikatelné a skutečně ji zruší

## Úplné poznámky k vydání si můžete prohlédnout [zde](release-notes.md).
