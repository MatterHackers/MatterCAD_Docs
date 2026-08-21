---
title: Versjonsmerknader
nav_order: 104
source_hash: 3ac9ea595f4f14d23496f8e287ff115f5a7738ff
source_lang: en
---
# MatterCAD 2.2026.8 (13. august 2026)
[Nedlasting for Windows](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## Nye funksjoner

* **Rediger underelementer**
  * Dobbeltklikk på et objekt på byggeplaten eller i scenetreet for å gå inn i det og redigere delene det er bygd opp av – uten et eget vindu eller en egen fane
  * For operasjoner som Trekk fra redigerer du kildedelene, og resultatet bygges opp på nytt når du går ut igjen
  * En brødsmulesti øverst i scenetreet viser hele stien; å klikke på et nivå slår endringene dine sammen til ett angrbart trinn, og hvert nivå har sin egen angrehistorikk
  <!-- Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->
  * ![Drill In](https://www.matterhackers.com/r/qgG4VA)

* **Ett booleansk verktøy**
  * Kombiner, Trekk fra, Skjæring og Trekk fra og erstatt er nå én enkelt operasjon med en ikonrad øverst i panelet – bytt modus med et klikk i stedet for å slette og bruke på nytt
  * Den samme operasjonen håndterer både 3D-mesher og 2D-baner, og viser fremdrift mens en tung boolsk operasjon kjører
  * Design som er lagret med de eldre, separate boolske objektene, åpnes fortsatt som normalt
  <!-- Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->
  * ![20260810 181041 paste 20260810 181041](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)


* **Boolske operasjoner som bare virker**
  * Boolske operasjoner kjører på en ny innebygd motor som er raskere og lykkes med mesher som tidligere feilet
  * Kombiner reparerer deler med hull automatisk: rene reparasjoner blir med i unionen, deler som ikke kan slås trygt sammen beholdes ved siden av og navngis for deg, og en del som ikke kunne repareres beholder den opprinnelige geometrien din
  * Plankutt er nå et ekte solid snitt, slik at resultatet blir vanntett og utskrivbart i stedet for et åpent skall
  * Nye alternativer Behold geometri med invertert innside og Reparer viklingsrekkefølge for problematiske importerte mesher


## Forbedringer

* **2D-baneredigering**
  * Fire punktmoduser – Skarp, Symmetrisk, Justert og Fri – brukes med ett klikk, både i 2D-redigeringen og i 3D-visningen
  * Speil er nå en levende symmetrimodus: endringer speiles over midten mens du gjør dem, og å dra et speilet par inn på aksen slår det sammen til ett punkt
  * Dra-velg punkter med et gummibånd, flytt dem som en gruppe, fest til rutenettet, og trykk Esc for å avbryte en draoperasjon
  * Jevn ut tilpasser en kurve gjennom punktene du har klikket ut, i ett trinn
  <!-- gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

* **Visning og navigasjon**
  * Trykk Z med en flat bane valgt for å animere til en redigeringsvisning rett ovenfra, tilpasset banen
  * Subpiksel-tekstgjengivelse er nå automatisk på når skjermen din støtter det, og kan fortsatt slås av eller på under Avansert-innstillingene

* **Modellering**
  * Lineær ekstrudering kan avfase den nederste kanten med egen stil, radius og antall segmenter
  * Objekter som bare finnes i redigeringen (3D-kurve, Måleverktøy, Beskrivelse, Ark) vises fortsatt, men utelates fra eksport

## Viktigste feilrettinger

  * En lagring som feilet halvveis, kunne avkorte filen den erstattet, samtidig som den meldte om vellykket lagring. Lagringer fullføres nå helt, og erstatter deretter målet atomisk – den samme beskyttelsen gjelder lagringer til biblioteket og eksporter
  * En mislykket lagring lar designet stå merket som ulagret, slik at lukking av appen ikke i stillhet kan forkaste arbeidet ditt
  * Lagring av et skyelement til disk beholdt det gamle fanenavnet og mistet fanen ved omstart
  * Rettet at 3MF-undermodeller ble forkastet i stillhet ved innlasting, og at 3MF-filer som ble lastet samtidig, forurenset hverandre
  * Rettet krasj, et ødelagt histogramfilter, og at kopier av en bildedel ikke holdt seg synkronisert med originalen
  * Rettet en krasj ved sletting av et kurvepunkt, og at punkter i skjøten på en lukket bane tilbakestilte modusen du valgte
  * Stopp-knappen på en kjørende oppgave er nå klikkbar og avbryter faktisk

---

# MatterCAD 2.2026.5 (8. mai 2026)
[Nedlasting for Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMiMyt-ICwwLEgZVcGxvYWQYgIDI7IHKkwoM)

## Nye funksjoner

* **Redesignet matriseverktøy**
  * Én samlet Matrise-operasjon erstatter de gamle Lineær matrise, Radiell matrise og Avansert matrise
  * **Lineær**-modus: kopier langs en retning med valgfri rotasjon og progressiv skalering
  * **Radiell**-modus: kopier rundt en sentral akse med konfigurerbar radius, sveipvinkel og bue- eller helsirkelmønstre
  * **Transformer**-modus: trinnvise kopier ved hjelp av en manuell transformasjon eller transformasjonen til et navngitt søskenobjekt
  * Rotasjonsmodusen Sammensetting i Lineær lager spiraler, vifter og helikser helt naturlig
  * Alternativet Skalering påvirker forskyvning for oppsett med nautilusskall og geometrisk progresjon
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **Bibliotekfavoritter**
  * Stjernemerk et hvilket som helst bibliotekelement for å legge det i en permanent Favoritter-mappe
  * Få rask tilgang til de primitivene, generatorene og lagrede delene du bruker mest, fra ett sted
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## Forbedringer

* **Juster**
  * Stablet justering er nå en direkte modusknapp i stedet for et nedtrekksalternativ
  * Lagt til tydeligere moduser – Enkel, Forskyvning og Stablet – for å stille opp kanter, legge til presise mellomrom og bygge ordnede stabler
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **Filstøtte**
  * Lagt til støtte for bildeformatet WEBP i bildebaserte operasjoner
  * Forbedret tolking av SVG-filer for mer pålitelige importer

* **Pålitelighet**
  * Forbedret hastighet og pålitelighet ved lasting av 3MF-filer
  * Bedre gjenoppretting av faner mellom økter

## Viktigste feilrettinger

* **Innlogging og tilgang til Skybibliotek**
  * Innlogging og tilgang til Skybibliotek er gjenopprettet etter at en oppgradering av serveren i bakkant ødela innloggingen.
  * MatterCAD ber deg nå om å logge inn på nytt når skytilgangen finner utløpt eller ugyldig påloggingsinformasjon.

* **Valg i scenetreet**
  * Rettet inkonsekvent valgatferd når objekter velges fra scenetreet.

* **Hjelpenavigasjon**
  * Rettet navigasjonsproblemer i den medfølgende hjelpen og utgivelsesdokumentasjonen.

* **Høyreklikk i biblioteket**
  * Rettet høyreklikkatferd i bibliotekets trevisning.

* **Ark**
  * Rettet en krasj som kunne oppstå under arbeid med ark.

---

# MatterCAD 2.2026.3 (12. mars 2026)
[Nedlasting for Windows](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## Nye funksjoner

* **Helt ny Direct3D 11-gjengivelsesmotor**
  * Fullstendig overgang fra OpenGL til Direct3D 11 for dramatisk bedre ytelse
  * FXAA-kantutjevning for skarpe, rene kanter
  * Dobbel dybdeavskalling for korrekt rekkefølgeuavhengig gjennomsiktighet
  * Maskinvareakselererte skygger på byggeplaten
  * Forbedrede objektkonturer og utvalgsvisning
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **Objektgjennomsiktighet**
  * Angi alfa/gjennomsiktighet på et hvilket som helst enkeltobjekt i scenen
  * Mesher med farge per flate støtter alfa uten fargeskade
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **Lås og skjul objekter**
  * Lås objekter for å hindre utilsiktet valg eller redigering
  * Skjul objekter for å redusere visuell rot mens du jobber med bestemte deler
  * Kommandoene Vis alle og Lås opp alle for raskt å gjenopprette synlighet
  * Låste og skjulte objekter utelates korrekt fra strålebasert valg
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **Forbedret boolsk Trekk fra**
  * Operasjoner med flere subtraksjoner er betydelig mer pålitelige og nøyaktige

## Forbedringer

* **Filhåndtering**
  * Prosjekter lagres nå som 3MF som standard i stedet for STL, noe som bevarer farger, materialer og designhistorikk
  * Forbedret dra-og-slipp-støtte for filer og mapper inn i 3D-visningen

* **Arbeidsflyt**
  * Dialogene Lagre som og Flytt husker den sist brukte mappeplasseringen
  * Uttrykksfelt støtter nå `pi`, `tau`, `e` og `count`
  * Esc-tasten utfører angre i designredigeringssammenhenger
  * 3D-kontrollene forblir synlige når musen forlater scenen

* **Ytelse og stabilitet**
  * Rettet oppstartskrasj og problemer med rekursiv lasting
  * Rettet gjengivelsesfeil for lyssetting og mipmapping
  * Forbedrede oppdateringer av bibliotekets trevisning
  * Dynamisk beregning av nær-/fjernplan for bedre zoomatferd
  * Oppgradert til .NET 10

---

# MatterCAD 2.2025.6 (20. juni 2025)
[Nedlasting for Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## Nye funksjoner

* **Støtte for SVG-fil**  
  * Full dra-og-slipp-støtte for SVG-filer
  * Direkte konvertering fra SVG-grafikk til 3D-objekter
  * Sømløs integrasjon med eksisterende CAD-arbeidsflyter

* **Avansert håndtering av OBJ-fil**  
  * Støtte for lasting av materialer fra ZIP-arkiver
  * Forbedret tolking av OBJ-filer og materialhåndtering
  * Bedre støtte for komplekse 3D-modeller med flere materialer

* **Forbedret system for fanehåndtering**
  * Faner fra Skybibliotek beholdes nå korrekt – arbeidet ditt blir værende nøyaktig der du forlot det
  * Forbedret organisering og navigering av faner
  * Automatisk gjenoppretting av åpne faner mellom økter

## Forbedringer i brukeropplevelsen

* **Strømlinjeformet grensesnitt**
  * Omorganisert Nylig-meny for raskere tilgang
  * Bedre visuell tilbakemelding under lange operasjoner
  * Forbedret oppstartstid og respons i applikasjonen

* **Pålitelighet**
  * Rettet kritiske krasj i 3D-sceneinteraksjoner
  * Løst problemer med minnehåndtering
  * Forbedret programstabilitet på alle plattformer

---

# MatterCAD 2.21.5 (13. feb. 2025)

[Nedlasting for Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# Eksisterende funksjoner

*Følgende funksjoner utgjør grunnlaget som MatterCAD bygger videre på fra arven etter MatterControl:*

* Lagt til Hul-funksjonen  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* Lagt til Reduser polygoner  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* Lagt til Reparer mesh  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* Lagt inn fullstendig automatisk støtte (eldre støtte) som et alternativ i tillegg til det nye manuelle støttealternativet
* Lagt til støtte for gsSlicer (eksperimentell ny skjæremotor)
* Rettet feil

## Endringer

* Forbedret oppheving av gruppering av mesh (deling i flere mesher)
    * Forkaster degenererte flater
    * Forkaster mikroskopiske diskrete detaljer

## Endringer

* Lagt til søkefelt for applikasjonen
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* Forbedret designverktøylinje
    * Lagt til gruppering for enkelte elementer
    * Lagt til knapp for dobbel justering
    * Lagt til knappen Ordne alle
* Dytt elementer på byggeplaten med piltastene
* Nedlastinger-mappen sorteres etter dato

## Endringer

* Forbedringer i brukergrensesnittet
    * Raskere oppdateringer i mapper i Skybibliotek
    * Gjenoppretting av grensesnittet ved ny åpning
    * Bedre støtte for tastaturnavigasjon
* Nytt system for feiloppdaging og varsling
    * Flere maskinvarefeil håndteres
* Forbedringer og optimaliseringer av designverktøy
    * Nye Vri-verktøy 
    * Forbedret Kurve-verktøy
    * Forbedret Juster


## Endringer

* Forbedret utflating
* Forbedret angrestøtte
* Forbedret designhistorikk

## Endringer
* Versjonering: Går over til versjonsnummeret (versjon).(år).(måned). Enklere å lese og mer informativt.
* Nye toppmoderne Trekk fra, Kombiner og Snitt (kun Windows)
* Vi starter nå opp med en «funksjonsomvisning» for å hjelpe nye brukere å finne fram

## Endringer
* Designverktøy – Muligheten til å 3D-modellere med et komplett sett med modelleringsprimitiver
* Bruk en primitiv til å lage dine egne tilpassede støtter
* Designapper – Designapper: sofistikerte, tilpassbare design
* 64-biters behandling
