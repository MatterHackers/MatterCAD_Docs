---
title: Udgivelsesnoter
nav_order: 104
source_hash: 3ac9ea595f4f14d23496f8e287ff115f5a7738ff
source_lang: en
---
# MatterCAD 2.2026.8 (13. august 2026)
[Windows-download](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## Nye funktioner

* **Rediger underelementer**
  * Dobbeltklik på et objekt på pladen eller i scenetræet for at gå ind i det og redigere de dele, det er bygget af — uden separat vindue eller fane
  * Ved operationer som Træk fra redigerer du kildedelene, og resultatet genopbygges, når du går ud igen
  * En brødkrummesti øverst i scenetræet viser hele stien; et klik på et niveau folder dine redigeringer sammen til ét trin, der kan fortrydes, og hvert niveau har sin egen fortrydelseshistorik
  <!-- Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->
  * ![Drill In](https://www.matterhackers.com/r/qgG4VA)

* **Ét boolesk værktøj**
  * Kombinér, Træk fra, Skær samt Træk fra og erstat er nu én enkelt operation med en ikonrække øverst i panelet — skift tilstand med et klik i stedet for at slette og anvende på ny
  * Den samme operation håndterer både 3D-masker og 2D-stier og viser fremdrift, mens en tung boolesk operation kører
  * Design gemt med de tidligere separate booleske objekter åbner fortsat som normalt
  <!-- Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->
  * ![20260810 181041 paste 20260810 181041](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)


* **Booleske operationer der bare virker**
  * Booleske operationer kører på en ny indbygget motor, der er hurtigere og lykkes på masker, som tidligere fejlede
  * Kombinér reparerer dele med huller automatisk: rene reparationer indgår i foreningen, dele der ikke kan sammenføjes sikkert, bevares ved siden af og navngives for dig, og en del, der ikke kunne repareres, beholder din oprindelige geometri
  * Planskæring er nu en ægte solid skæring, så resultatet er vandtæt og kan printes i stedet for at være en åben skal
  * Nye indstillinger Behold vrangvendt geometri og Reparer viklingsrækkefølge til problematiske importerede masker


## Forbedringer

* **2D-stieditor**
  * Fire punkttilstande — Skarp, Symmetrisk, Justeret og Fri — anvendes med ét klik, både i 2D-editoren og i 3D-visningen
  * Spejl er nu en live symmetritilstand: redigeringer spejles omkring midten, mens du foretager dem, og trækker du et spejlet par ind på aksen, flettes det til ét punkt
  * Vælg punkter ved at trække en markeringsramme, flyt dem som en gruppe, fastgør til gitteret, og tryk på Esc for at annullere et træk
  * Udjævn tilpasser en kurve gennem de punkter, du har klikket ud, i ét trin
  <!-- gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

* **Visning og navigation**
  * Tryk på Z med en flad sti markeret for at animere til en redigeringsvisning lige ovenfra, tilpasset stien
  * Subpixel-tekstgengivelse er nu slået til automatisk, når din skærm understøtter det, og kan stadig slås til eller fra under indstillingerne Avanceret

* **Modellering**
  * Lineær ekstrudering kan affase den nederste kant med sin egen stil, radius og segmentantal
  * Objekter kun til editoren (3D-kurve, Måleværktøj, Beskrivelse, Ark) vises fortsat, men udelades fra eksport

## Vigtigste fejlrettelser

  * En gemning, der mislykkedes undervejs, kunne afkorte den fil, den erstattede, og samtidig melde succes. Gemninger fuldføres nu helt og erstatter derefter destinationen atomisk — den samme beskyttelse gælder gemninger i biblioteket og eksporter
  * En mislykket gemning efterlader designet markeret som ikke gemt, så lukning af appen ikke i stilhed kan kassere dit arbejde
  * Gemning af et skyelement til disk beholdt det gamle fanenavn og mistede fanen ved genstart
  * Rettede at 3MF-undermodeller i stilhed blev droppet ved indlæsning, og at 3MF-filer indlæst samtidig forurenede hinanden
  * Rettede nedbrud, et defekt histogramfilter og kopier af en billeddel, der ikke forblev synkroniseret med originalen
  * Rettede et nedbrud ved sletning af et kurvepunkt samt at punkter ved en lukket stis søm nulstillede den tilstand, du havde valgt
  * Stop-knappen på en kørende opgave kan nu klikkes og annullerer rent faktisk

---

# MatterCAD 2.2026.5 (8. maj 2026)
[Windows-download](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMiMyt-ICwwLEgZVcGxvYWQYgIDI7IHKkwoM)

## Nye funktioner

* **Redesignet array-værktøj**
  * En enkelt samlet array-operation erstatter det tidligere Lineært array, Radialt array og Avanceret array
  * Tilstanden **Lineær**: kopier langs en retning med valgfri rotation og progressiv skalering
  * Tilstanden **Radial**: kopier omkring en central akse med konfigurerbar radius, sveppvinkel samt bue- eller helcirkelmønstre
  * Tilstanden **Transformér**: trinvise kopier med en manuel transformation eller et navngivet søskendeobjekts transformation
  * Rotationstilstanden Sammensætning i Lineær skaber spiraler, vifter og helixer helt naturligt
  * Indstillingen Skalering påvirker forskydning til layouts som nautilusskaller og geometriske progressioner
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **Favoritter i biblioteket**
  * Stjernemarkér ethvert bibliotekselement for at føje det til en permanent Favoritter-mappe
  * Få hurtigt adgang til dine mest brugte primitiver, generatorer og gemte dele ét sted
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## Forbedringer

* **Justér**
  * Stablet justering er nu en direkte tilstandsknap i stedet for en rullemenuindstilling
  * Tilføjet tydeligere tilstande Simpel, Forskydning og Stablet til at rette kanter ind, tilføje præcise mellemrum og bygge ordnede stakke
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **Filunderstøttelse**
  * Tilføjet understøttelse af billedformatet WEBP i billedbaserede operationer
  * Forbedret fortolkning af SVG-filer for mere pålidelige importer

* **Pålidelighed**
  * Forbedret hastighed og pålidelighed ved indlæsning af 3MF-filer
  * Bedre gendannelse af faner mellem sessioner

## Vigtigste fejlrettelser

* **Login og adgang til Skybibliotek**
  * Login og adgang til Skybibliotek er gendannet, efter at en opgradering af backend-serveren ødelagde login.
  * MatterCAD beder dig nu om at log ind igen, når skyadgang finder udløbne eller ugyldige loginoplysninger.

* **Markering i scenetræet**
  * Rettede inkonsistent markeringsadfærd ved valg af objekter i scenetræet.

* **Navigation i hjælpen**
  * Rettede navigationsproblemer i den medfølgende hjælp og udgivelsesdokumentation.

* **Højreklik i biblioteket**
  * Rettede højrekliksadfærd i bibliotekets trævisning.

* **Ark**
  * Rettede et nedbrud, der kunne opstå under arbejde med ark.

---

# MatterCAD 2.2026.3 (12. marts 2026)
[Windows-download](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## Nye funktioner

* **Helt ny Direct3D 11-renderingsmotor**
  * Fuldstændig migrering fra OpenGL til Direct3D 11 for markant bedre ydelse
  * FXAA-kantudjævning for skarpe, rene kanter
  * Dual depth peeling for korrekt rækkefølgeuafhængig gennemsigtighed
  * Hardwareaccelererede skygger på pladen
  * Forbedrede objektkonturer og markeringsvisninger
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **Gennemsigtighed for objekter**
  * Angiv alfa/gennemsigtighed på ethvert enkelt objekt i scenen
  * Masker med farve pr. flade understøtter alfa uden farveskade
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **Lås og skjul objekter**
  * Lås objekter for at forhindre utilsigtet markering eller redigering
  * Skjul objekter for at reducere visuelt rod, mens du arbejder på bestemte dele
  * Kommandoerne Vis alle og Lås alle op til hurtigt at gendanne synlighed
  * Låste og skjulte objekter udelades korrekt fra strålebaseret markering
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **Forbedret boolesk Træk fra**
  * Multi-subtraktioner er markant mere pålidelige og præcise

## Forbedringer

* **Filhåndtering**
  * Projekter gemmes nu som 3MF som standard i stedet for STL, hvilket bevarer farver, materialer og designhistorik
  * Forbedret understøttelse af træk-og-slip af filer og mapper ind i 3D-visningen

* **Arbejdsgang**
  * Dialogerne Gem som og Flyt husker din senest anvendte mappeplacering
  * Udtryksfelter understøtter nu `pi`, `tau`, `e` og `count`
  * Esc-tasten udfører fortryd i designredigeringskontekster
  * 3D-kontrollerne forbliver synlige, når musen forlader scenen

* **Ydelse og stabilitet**
  * Rettede nedbrud ved opstart og problemer med rekursiv indlæsning
  * Rettede renderingsfejl i belysning og mipmapping
  * Forbedrede opdateringer af bibliotekets trævisning
  * Dynamisk beregning af nær/fjern-planer for bedre zoomadfærd
  * Opgraderet til .NET 10

---

# MatterCAD 2.2025.6 (20. juni 2025)
[Windows-download](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## Nye funktioner

* **Understøttelse af SVG-fil**  
  * Fuld understøttelse af træk-og-slip for SVG-filer
  * Direkte konvertering fra SVG-grafik til 3D-objekter
  * Problemfri integration med eksisterende CAD-arbejdsgange

* **Avanceret håndtering af OBJ-fil**  
  * Understøttelse af indlæsning af materialer fra ZIP-arkiver
  * Forbedret fortolkning af OBJ-filer og materialehåndtering
  * Bedre understøttelse af komplekse 3D-modeller med flere materialer

* **Forbedret system til fanehåndtering**
  * Faner fra skybiblioteket bevares nu korrekt — dit arbejde bliver præcis, hvor du slap
  * Forbedret organisering af og navigation mellem faner
  * Automatisk gendannelse af åbne faner mellem sessioner

## Forbedringer af brugeroplevelsen

* **Strømlinet brugerflade**
  * Omorganiseret Seneste-menu for hurtigere adgang
  * Bedre visuel tilbagemelding under lange operationer
  * Forbedret opstartstid og reaktionsevne for programmet

* **Pålidelighed**
  * Rettede kritiske nedbrud i interaktioner med 3D-scenen
  * Løste problemer med hukommelseshåndtering
  * Forbedret programstabilitet på alle platforme

---

# MatterCAD 2.21.5 (13. feb. 2025)

[Windows-download](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# Eksisterende funktioner

*Følgende funktioner udgør det fundament, som MatterCAD bygger videre på fra MatterControls arv:*

* Tilføjet funktionen Hul  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* Tilføjet Reducér polygoner  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* Tilføjet Reparer maske  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* Indført fuldautomatisk support (ældre support) som en mulighed ud over den nye manuelle supportmulighed
* Tilføjet understøttelse af gsSlicer (eksperimentel ny slicer-motor)
* Rettede fejl

## Ændringer

* Forbedret opdeling af maske (opsplitning i flere masker)
    * Kasserer degenererede flader
    * Kasserer mikroskopiske diskrete detaljer

## Ændringer

* Tilføjet søgefelt til programmet
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* Forbedret designværktøjslinje
    * Tilføjet gruppering af nogle elementer
    * Tilføjet dobbelt justeringsknap
    * Tilføjet knappen Arrangér alle
* Flyt emner på pladen med piletasterne
* Mappen Downloads sorteres efter dato

## Ændringer

* Forbedringer af brugerfladen
    * Hurtigere opdateringer i mapper i Skybibliotek
    * Gendan brugerfladen ved genåbning
    * Bedre understøttelse af tastaturnavigation
* Nyt system til fejlregistrering og advarsler
    * Flere hardwarefejl håndteres
* Forbedringer og optimeringer af designværktøjer
    * Nye Twist-værktøjer 
    * Forbedret Kurve-værktøj
    * Forbedret Justér


## Ændringer

* Forbedret udfladning
* Forbedret understøttelse af fortryd
* Forbedret designhistorik

## Ændringer
* Versionering: Overgang til et versionsnummer på formen (version).(år).(måned). Nemmere at læse og mere informativt.
* Nye avancerede Træk fra, Kombinér og Skæring (kun Windows)
* Vi starter nu op med en "funktionsrundvisning" for at hjælpe nye brugere på vej

## Ændringer
* Designværktøjer – Muligheden for at 3D-modellere med et komplet sæt modelleringsprimitiver
* Brug en primitiv til at oprette dine egne tilpassede supporter
* Designapps – Designapps: avancerede designs, der kan tilpasses
* 64-bit behandling
