---
title: Release-opmerkingen
nav_order: 104
source_hash: 3ac9ea595f4f14d23496f8e287ff115f5a7738ff
source_lang: en
---
# MatterCAD 2.2026.8 (13 augustus 2026)
[Windows-download](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## Nieuwe functies

* **Onderliggende items bewerken**
  * Dubbelklik op een object op het bed of in de scèneboom om erin te stappen en de onderdelen te bewerken waaruit het is opgebouwd — geen apart venster of tabblad nodig
  * Bij bewerkingen zoals Aftrekken bewerk je de brononderdelen en wordt het resultaat opnieuw opgebouwd zodra je weer naar buiten stapt
  * Een kruimelpad boven aan de scèneboom toont het volledige pad; door op een niveau te klikken worden je bewerkingen als één ongedaan te maken stap doorgevoerd, en elk niveau houdt zijn eigen geschiedenis van ongedaan maken bij
  <!-- Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->
  * ![Drill In](https://www.matterhackers.com/r/qgG4VA)

* **Eén booleaans gereedschap**
  * Combineren, Aftrekken, Doorsnijden en Aftrekken en Vervangen zijn nu één bewerking met een rij pictogrammen boven aan het paneel — schakel met één klik tussen modi in plaats van te verwijderen en opnieuw toe te passen
  * Dezelfde bewerking verwerkt zowel 3D-meshes als 2D-paden en toont de voortgang terwijl een zware booleaanse bewerking loopt
  * Ontwerpen die met de oudere afzonderlijke booleaanse objecten zijn opgeslagen, openen gewoon zoals voorheen
  <!-- Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->
  * ![20260810 181041 paste 20260810 181041](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)


* **Booleaanse bewerkingen die gewoon werken**
  * Booleaanse bewerkingen draaien op een nieuwe native engine die sneller is en slaagt op meshes die eerder faalden
  * Combineren repareert onderdelen met gaten automatisch: schone reparaties gaan op in de vereniging, onderdelen die niet veilig samengevoegd kunnen worden blijven ernaast staan en krijgen een naam, en een onderdeel dat niet gerepareerd kon worden behoudt je oorspronkelijke geometrie
  * Vlaksnede is nu een echte massieve doorsnede, waardoor het resultaat waterdicht en printbaar is in plaats van een open schaal
  * Nieuwe opties Binnenstebuiten geometrie behouden en Wikkelrichting repareren voor lastige geïmporteerde meshes


## Verbeteringen

* **2D-padeditor**
  * Vier puntmodi — Scherp, Symmetrisch, Uitgelijnd en Vrij — met één klik toe te passen, zowel in de 2D-editor als in de 3D-weergave
  * Spiegelen is nu een live symmetriemodus: bewerkingen worden tijdens het werken gespiegeld over het midden, en als je een gespiegeld paar op de as sleept, wordt het samengevoegd tot één punt
  * Selecteer punten met een sleepkader, verplaats ze als groep, laat ze op het raster vastklikken en druk op Esc om een sleepactie te annuleren
  * Gladmaken past in één stap een curve door je aangeklikte punten
  <!-- gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

* **Weergave en navigatie**
  * Druk op Z terwijl een vlak pad is geselecteerd om vloeiend naar een recht van boven gerichte bewerkingsweergave te gaan die op het pad is ingepast
  * Subpixel-tekstweergave staat nu automatisch aan wanneer je beeldscherm dit ondersteunt, en kan nog steeds worden in- of uitgeschakeld bij de instellingen onder Geavanceerd

* **Modelleren**
  * Lineaire extrusie kan de onderrand afschuinen met een eigen stijl, straal en aantal segmenten
  * Objecten die alleen in de editor bestaan (3D-curve, Meetgereedschap, Beschrijving, Blad) worden nog steeds weergegeven, maar zijn uitgesloten van export

## Belangrijkste opgeloste fouten

  * Een opslagactie die halverwege mislukte, kon het bestand dat werd vervangen afkappen terwijl succes werd gemeld. Opslaan wordt nu volledig afgerond en vervangt daarna de bestemming atomair — dezelfde bescherming geldt voor opslaan in de bibliotheek en voor exports
  * Een mislukte opslagactie laat het ontwerp als niet-opgeslagen gemarkeerd, zodat het sluiten van de app je werk niet stilzwijgend kan weggooien
  * Bij het opslaan van een clouditem naar schijf bleef de oude tabbladnaam staan en ging het tabblad verloren bij het opnieuw opstarten
  * Opgelost dat 3MF-submodellen stilzwijgend werden weggelaten bij het laden en dat gelijktijdig geladen 3MF-bestanden elkaar besmetten
  * Crashes, een defect histogramfilter en kopieën van een afbeeldingsonderdeel die niet synchroon bleven met het origineel zijn opgelost
  * Opgelost: een crash bij het verwijderen van een curvepunt en punten op de naad van een gesloten pad die de door jou gekozen modus terugzetten
  * De knop Stoppen bij een lopende taak is nu klikbaar en annuleert daadwerkelijk

---

# MatterCAD 2.2026.5 (8 mei 2026)
[Windows-download](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMiMyt-ICwwLEgZVcGxvYWQYgIDI7IHKkwoM)

## Nieuwe functies

* **Opnieuw ontworpen arraygereedschap**
  * Eén samengevoegde Array-bewerking vervangt de oude Lineaire reeks, Radiaal patroon en Geavanceerde array
  * Modus **Lineair**: kopieën langs een richting met optionele rotatie en geleidelijke schaling
  * Modus **Radiaal**: kopieën rond een centrale as met instelbare straal, zwenkhoek en boog- of volledige-cirkelpatronen
  * Modus **Transformeren**: kopieën stapsgewijs plaatsen met een handmatige transformatie of de transformatie van een benoemd broerobject
  * De rotatiemodus Samenvoegen in Lineair maakt spiralen, waaiers en helices op natuurlijke wijze
  * Optie Schaal beïnvloedt offset voor indelingen als nautilusschelpen en meetkundige reeksen
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **Favorieten in de Bibliotheek**
  * Geef elk bibliotheekitem een ster om het toe te voegen aan een blijvende map Favorieten
  * Snelle toegang tot je meest gebruikte primitieven, generatoren en opgeslagen onderdelen vanaf één plek
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## Verbeteringen

* **Uitlijnen**
  * Gestapeld uitlijnen is nu een directe modusknop in plaats van een optie in een vervolgkeuzelijst
  * Duidelijkere modi Eenvoudig, Offset en Gestapeld toegevoegd voor het uitlijnen van randen, het toevoegen van nauwkeurige tussenruimtes en het bouwen van geordende stapels
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **Bestandsondersteuning**
  * Ondersteuning toegevoegd voor het WEBP-afbeeldingsformaat in bewerkingen op basis van afbeeldingen
  * Verbeterde verwerking van SVG-bestanden voor betrouwbaardere imports

* **Betrouwbaarheid**
  * Verbeterde snelheid en betrouwbaarheid bij het laden van 3MF-bestanden
  * Beter herstel van tabbladen tussen sessies

## Belangrijkste opgeloste fouten

* **Aanmelden en toegang tot de Cloudbibliotheek**
  * Aanmelden en toegang tot de Cloudbibliotheek zijn hersteld nadat een upgrade van de backendserver het aanmelden had verstoord.
  * MatterCAD vraagt je nu opnieuw om aan te melden wanneer de cloudtoegang verlopen of ongeldige inloggegevens aantreft.

* **Selectie in de scèneboom**
  * Inconsistent selectiegedrag bij het kiezen van objecten in de scèneboom is opgelost.

* **Navigatie in Help**
  * Navigatieproblemen in de meegeleverde help- en releasedocumentatie zijn opgelost.

* **Rechtsklikken in de Bibliotheek**
  * Het gedrag bij rechtsklikken in de boomweergave van de bibliotheek is opgelost.

* **Bladen**
  * Een crash die kon optreden tijdens het werken met bladen is opgelost.

---

# MatterCAD 2.2026.3 (12 maart 2026)
[Windows-download](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## Nieuwe functies

* **Volledig nieuwe Direct3D 11-renderengine**
  * Volledige migratie van OpenGL naar Direct3D 11 voor aanzienlijk betere prestaties
  * FXAA-antialiasing voor scherpe, strakke randen
  * Dual depth peeling voor correcte volgorde-onafhankelijke transparantie
  * Hardwareversnelde schaduwen op het bed
  * Verbeterde objectomlijningen en selectieweergave
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **Transparantie van objecten**
  * Stel alfa/transparantie in op elk afzonderlijk object in de scène
  * Meshes met kleur per facet ondersteunen alfa zonder kleurverlies
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **Objecten vergrendelen en verbergen**
  * Vergrendel objecten om onbedoelde selectie of bewerking te voorkomen
  * Verberg objecten om visuele rommel te verminderen terwijl je aan specifieke onderdelen werkt
  * De opdrachten Alles zichtbaar maken en Alles ontgrendelen om de zichtbaarheid snel te herstellen
  * Vergrendelde en verborgen objecten worden correct uitgesloten van selectie op basis van stralen
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **Verbeterde booleaanse Aftrekken**
  * Bewerkingen met meerdere aftrekkingen zijn aanzienlijk betrouwbaarder en nauwkeuriger

## Verbeteringen

* **Bestandsverwerking**
  * Projecten worden nu standaard opgeslagen als 3MF in plaats van STL, met behoud van kleuren, materialen en ontwerpgeschiedenis
  * Verbeterde ondersteuning voor slepen en neerzetten van bestanden en mappen in de 3D-weergave

* **Workflow**
  * De dialoogvensters Opslaan als en Verplaatsen onthouden je laatste maplocatie
  * Expressievelden ondersteunen nu `pi`, `tau`, `e` en `count`
  * De Esc-toets maakt bewerkingen ongedaan in ontwerpcontexten
  * 3D-besturingselementen blijven zichtbaar wanneer de muis de scène verlaat

* **Prestaties en stabiliteit**
  * Crashes bij het opstarten en problemen met recursief laden opgelost
  * Renderfouten bij belichting en mipmapping opgelost
  * Verbeterde updates van de boomweergave van de bibliotheek
  * Dynamische berekening van het nabije en verre vlak voor beter zoomgedrag
  * Bijgewerkt naar .NET 10

---

# MatterCAD 2.2025.6 (20 juni 2025)
[Windows-download](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## Nieuwe functies

* **Ondersteuning voor SVG-bestanden**  
  * Volledige ondersteuning voor slepen en neerzetten van SVG-bestanden
  * Directe conversie van SVG-afbeeldingen naar 3D-objecten
  * Naadloze integratie met bestaande CAD-workflows

* **Geavanceerde verwerking van OBJ-bestanden**  
  * Ondersteuning voor het laden van materialen uit ZIP-archieven
  * Verbeterde verwerking van OBJ-bestanden en materiaalafhandeling
  * Betere ondersteuning voor complexe 3D-modellen met meerdere materialen

* **Verbeterd systeem voor tabbladbeheer**
  * Tabbladen van de cloudbibliotheek blijven nu correct bewaard — je werk blijft precies waar je het achterliet
  * Verbeterde ordening en navigatie van tabbladen
  * Automatisch herstel van geopende tabbladen tussen sessies

## Verbeteringen in de gebruikerservaring

* **Gestroomlijnde interface**
  * Opnieuw ingedeeld menu Recent voor snellere toegang
  * Betere visuele terugkoppeling tijdens langdurige bewerkingen
  * Verbeterde opstarttijd en reactiesnelheid van de toepassing

* **Betrouwbaarheid**
  * Kritieke crashes bij interacties in de 3D-scène opgelost
  * Problemen met geheugenbeheer verholpen
  * Verbeterde stabiliteit van de toepassing op alle platformen

---

# MatterCAD 2.21.5 (13 feb. 2025)

[Windows-download](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# Bestaande functies

*De volgende functies vormen de basis waarop MatterCAD voortbouwt vanuit de erfenis van MatterControl:*

* Functie Hol toegevoegd  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* Polygonen verkleinen toegevoegd  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* Mesh repareren toegevoegd  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* Volledig automatische ondersteuning (verouderde ondersteuning) toegevoegd als optie naast de nieuwe optie voor handmatige ondersteuning
* Ondersteuning toegevoegd voor gsSlicer (experimentele nieuwe slice-engine)
* Fouten opgelost

## Wijzigingen

* Verbeterd degroeperen van meshes (splitsen in meerdere meshes)
    * Ontaarde facetten worden weggelaten
    * Microscopisch kleine losse kenmerken worden weggelaten

## Wijzigingen

* Zoekbalk toegevoegd aan de toepassing
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* Verbeterde ontwerpwerkbalk
    * Groepering toegevoegd aan sommige items
    * Dubbele uitlijnknop toegevoegd
    * Knop Alles rangschikken toegevoegd
* Items op het bed verschuiven met de pijltoetsen
* De map Downloads is gesorteerd op datum

## Wijzigingen

* Verbeteringen in de gebruikersinterface
    * Snellere updates in mappen van de Cloudbibliotheek
    * Gebruikersinterface wordt hersteld bij opnieuw openen
    * Betere ondersteuning voor toetsenbordnavigatie
* Nieuw systeem voor foutdetectie en waarschuwingen
    * Meer hardwarefouten worden afgehandeld
* Verbeteringen en optimalisaties van ontwerpgereedschappen
    * Nieuwe Twist-gereedschappen 
    * Verbeterd Curve-gereedschap
    * Verbeterd Uitlijnen


## Wijzigingen

* Verbeterd afvlakken
* Verbeterde ondersteuning voor ongedaan maken
* Verbeterde ontwerpgeschiedenis

## Wijzigingen
* Versiebeheer: overstap naar een versienummer volgens (versie).(jaar).(maand). Eenvoudiger te lezen en informatiever.
* Nieuwe, ultramoderne Aftrekken, Combineren en Doorsnede (alleen Windows)
* We starten nu met een 'Rondleiding langs functies' om nieuwe gebruikers op weg te helpen

## Wijzigingen
* Ontwerpgereedschappen - de mogelijkheid om in 3D te modelleren met een complete set modelleerprimitieven
* Gebruik een primitief om je eigen aangepaste ondersteuning te maken
* Ontwerpapps - Ontwerpapps: geavanceerde, aanpasbare ontwerpen
* 64-bits Verwerken
