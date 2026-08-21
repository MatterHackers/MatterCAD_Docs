---
title: Poznámky k verzi
nav_order: 104
source_hash: 3ac9ea595f4f14d23496f8e287ff115f5a7738ff
source_lang: en
---
# MatterCAD 2.2026.8 (13. srpna 2026)
[Stáhnout pro Windows](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## Nové funkce

* **Upravit potomky**
  * Dvojklikem na objekt na podložce nebo ve stromu scény do něj vstoupíte a upravíte části, ze kterých je sestaven — bez samostatného okna nebo karty
  * U operací jako Odečíst upravujete zdrojové části a výsledek se po návratu ven znovu přestaví
  * Drobečková navigace v horní části stromu scény zobrazuje celou cestu; kliknutím na úroveň se vaše úpravy sloučí do jednoho vratného kroku a každá úroveň si udržuje vlastní historii kroků zpět
  <!-- Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->
  * ![Drill In](https://www.matterhackers.com/r/qgG4VA)

* **Jeden booleovský nástroj**
  * Sloučit, Odečíst, Průnik a Odečíst a nahradit jsou nyní jediná operace s řádkem ikon v horní části panelu — režimy přepnete kliknutím místo mazání a opětovného použití
  * Stejná operace zvládá jak 3D sítě, tak 2D cesty, a zobrazuje průběh, když běží náročná booleovská operace
  * Návrhy uložené se staršími samostatnými booleovskými objekty se nadále otevírají normálně
  <!-- Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->
  * ![20260810 181041 paste 20260810 181041](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)


* **Booleovské operace, které prostě fungují**
  * Booleovské operace běží na novém nativním jádru, které je rychlejší a uspěje i u sítí, jež dříve selhávaly
  * Sloučit automaticky opravuje části s dírami: čisté opravy se připojí ke sjednocení, části, které nelze bezpečně sloučit, zůstanou vedle něj a budou za vás pojmenovány, a část, kterou nebylo možné opravit, si ponechá vaši původní geometrii
  * Řez rovinou je nyní skutečný průnik těles, takže výsledek je vodotěsný a tisknutelný místo otevřené skořepiny
  * Nové volby Ponechat obrácenou geometrii a Opravit orientaci ploch pro problematické importované sítě


## Vylepšení

* **2D editor cesty**
  * Čtyři režimy bodů — Ostrý, Symetrický, Zarovnaný a Volný — použitelné jedním kliknutím, jak ve 2D editoru, tak ve 3D pohledu
  * Zrcadlit je nyní živý režim symetrie: úpravy se během provádění zrcadlí přes střed a přetažením zrcadleného páru na osu se sloučí do jediného bodu
  * Body vyberete tažením gumovým rámečkem, posunete je jako skupinu, přichytíte k mřížce a stisknutím Esc tažení zrušíte
  * Vyhlazení proloží vašimi naklikanými body křivku v jediném kroku
  <!-- gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

* **Zobrazení a navigace**
  * Stisknutím Z s vybranou plochou cestou přejdete animací do kolmého pohledu shora přizpůsobeného cestě
  * Subpixelové vykreslování textu je nyní automaticky zapnuté, pokud to displej podporuje, a stále jej lze zapnout nebo vypnout v nastavení Rozšířené

* **Modelování**
  * Lineární extruze umí zkosit spodní hranu s vlastním stylem, poloměrem a počtem segmentů
  * Objekty určené pouze pro editor (3D křivka, Nástroj měření, Popis, List) se stále zobrazují, ale jsou vyloučeny z exportu

## Nejdůležitější opravy chyb

  * Uložení, které selhalo v půli, mohlo zkrátit soubor, jejž nahrazovalo, a přitom hlásit úspěch. Uložení se nyní dokončí celé a teprve poté atomicky nahradí cíl — stejná ochrana platí pro ukládání do knihovny a exporty
  * Neúspěšné uložení ponechá návrh označený jako neuložený, takže zavření aplikace nemůže tiše zahodit vaši práci
  * Uložení cloudové položky na disk zachovávalo starý název karty a po restartu se karta ztratila
  * Opraveno tiché zahazování dílčích modelů 3MF při načítání a vzájemné znehodnocování souborů 3MF načtených současně
  * Opraveny pády, nefunkční filtr histogramu a kopie obrázkové části, které nezůstávaly synchronizované s originálem
  * Opraven pád při mazání bodu křivky a body na švu uzavřené cesty, které vracely zvolený režim zpět
  * Tlačítko Zastavit u běžící úlohy je nyní klikatelné a úlohu skutečně zruší

---

# MatterCAD 2.2026.5 (8. května 2026)
[Stáhnout pro Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMiMyt-ICwwLEgZVcGxvYWQYgIDI7IHKkwoM)

## Nové funkce

* **Přepracovaný nástroj Pole**
  * Jediná sjednocená operace Pole nahrazuje dřívější Lineární pole, Radiální pole a Rozšířené pole
  * Režim **Lineární**: kopie podél směru s volitelnou rotací a postupným měřítkem
  * Režim **Radiální**: kopie kolem centrální osy s nastavitelným poloměrem, úhlem rozevření a vzory oblouku či plné kružnice
  * Režim **Transformace**: krokové kopie pomocí ruční transformace nebo transformace pojmenovaného sourozeneckého objektu
  * Režim rotace Skládání v Lineární přirozeně vytváří spirály, vějíře a šroubovice
  * Volba Měřítko ovlivňuje offset pro rozvržení typu lastury nautila a geometrické posloupnosti
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **Oblíbené v knihovně**
  * Označte hvězdičkou libovolnou položku knihovny a přidejte ji do trvalé složky Oblíbené
  * Rychlý přístup k nejpoužívanějším primitivům, generátorům a uloženým dílům z jednoho místa
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## Vylepšení

* **Zarovnat**
  * Skládané zarovnání je nyní přímé tlačítko režimu místo volby v rozbalovací nabídce
  * Přidány přehlednější režimy Jednoduché, Odsazení a Skládaný pro zarovnávání hran, přidávání přesných mezer a stavbu uspořádaných stohů
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **Podpora souborů**
  * Přidána podpora obrazového formátu WEBP v operacích založených na obrázcích
  * Vylepšeno zpracování souborů SVG pro spolehlivější import

* **Spolehlivost**
  * Vylepšena rychlost a spolehlivost načítání souborů 3MF
  * Lepší obnovení karet mezi relacemi

## Nejdůležitější opravy chyb

* **Přihlášení a přístup do Cloudové knihovny**
  * Přihlášení a přístup do Cloudové knihovny jsou obnoveny poté, co upgrade serveru rozbil přihlašování.
  * MatterCAD vás nyní vyzve, abyste se znovu přihlásili, když přístup do cloudu narazí na vypršené nebo neplatné přihlašovací údaje.

* **Výběr ve stromu scény**
  * Opraveno nekonzistentní chování výběru při volbě objektů ze stromu scény.

* **Navigace v nápovědě**
  * Opraveny problémy s navigací v přiložené nápovědě a dokumentaci k verzím.

* **Kliknutí pravým tlačítkem v knihovně**
  * Opraveno chování pravého tlačítka ve stromovém zobrazení knihovny.

* **Listy**
  * Opraven pád, ke kterému mohlo dojít při práci s listy.

---

# MatterCAD 2.2026.3 (12. března 2026)
[Stáhnout pro Windows](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## Nové funkce

* **Zcela nové vykreslovací jádro Direct3D 11**
  * Kompletní přechod z OpenGL na Direct3D 11 pro výrazně lepší výkon
  * Vyhlazování FXAA pro ostré, čisté hrany
  * Dvojité depth peeling pro správnou průhlednost nezávislou na pořadí
  * Hardwarově akcelerované stíny na podložce
  * Vylepšené obrysy objektů a vizuály výběru
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **Průhlednost objektu**
  * Nastavte alfu/průhlednost u libovolného jednotlivého objektu ve scéně
  * Sítě s barvou po plochách podporují alfu bez poškození barev
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **Zamknutí a skrytí objektů**
  * Zamkněte objekty, abyste zabránili náhodnému výběru nebo úpravám
  * Skryjte objekty a omezte vizuální nepořádek při práci na konkrétních částech
  * Příkazy Zobrazit vše a Odemknout vše pro rychlé obnovení viditelnosti
  * Zamknuté a skryté objekty jsou správně vyloučeny z výběru paprskem
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **Vylepšené booleovské Odečíst**
  * Operace vícenásobného odečtení jsou výrazně spolehlivější a přesnější

## Vylepšení

* **Práce se soubory**
  * Projekty se nyní ve výchozím nastavení ukládají jako 3MF místo STL, čímž se zachovají barvy, materiály a historie návrhu
  * Vylepšená podpora přetahování souborů a složek do 3D pohledu

* **Pracovní postup**
  * Dialogy Uložit jako a Přesunout si pamatují poslední umístění složky
  * Pole s výrazy nyní podporují `pi`, `tau`, `e` a `count`
  * Klávesa Esc provádí krok zpět v kontextech úprav návrhu
  * 3D ovládací prvky zůstávají viditelné, když myš opustí scénu

* **Výkon a stabilita**
  * Opraveny pády při spuštění a problémy s rekurzivním načítáním
  * Opraveny chyby vykreslování osvětlení a mipmapování
  * Vylepšeny aktualizace stromového zobrazení knihovny
  * Dynamický výpočet blízké/vzdálené roviny pro lepší chování přiblížení
  * Přechod na .NET 10

---

# MatterCAD 2.2025.6 (20. června 2025)
[Stáhnout pro Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## Nové funkce

* **Podpora souborů SVG**  
  * Plná podpora přetahování souborů SVG
  * Přímý převod z grafiky SVG na 3D objekty
  * Bezproblémové zapojení do stávajících CAD pracovních postupů

* **Pokročilá práce se soubory OBJ**  
  * Podpora načítání materiálů z archivů ZIP
  * Vylepšené zpracování souborů OBJ a práce s materiály
  * Lepší podpora složitých 3D modelů s více materiály

* **Vylepšený systém správy karet**
  * Karty cloudové knihovny nyní správně přetrvávají – vaše práce zůstane přesně tam, kde jste ji nechali
  * Vylepšené uspořádání karet a navigace mezi nimi
  * Automatické obnovení otevřených karet mezi relacemi

## Vylepšení uživatelského prostředí

* **Zjednodušené rozhraní**
  * Reorganizovaná nabídka Nedávné pro rychlejší přístup
  * Lepší vizuální zpětná vazba během dlouhých operací
  * Zlepšená doba spuštění aplikace a odezva

* **Spolehlivost**
  * Opraveny kritické pády při interakcích s 3D scénou
  * Vyřešeny problémy se správou paměti
  * Zlepšena stabilita aplikace na všech platformách

---

# MatterCAD 2.21.5 (13. února 2025)

[Stáhnout pro Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# Stávající funkce

*Následující funkce představují základ, na kterém MatterCAD staví z dědictví MatterControl:*

* Přidána funkce Dutý  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* Přidáno Zmenšit počet polygonů  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* Přidáno Opravit síť  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* Přidána plně automatická podpora (starší podpory) jako volba navíc k nové možnosti ručních podpor
* Přidána podpora pro gsSlicer (Experimentální nové jádro slicování)
* Opraveny chyby

## Změny

* Vylepšeno rozdělování skupiny sítě (rozdělení na více sítí)
    * Zahození degenerovaných ploch
    * Zahození mikroskopických samostatných prvků

## Změny

* Přidán vyhledávací panel pro aplikaci
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* Vylepšena lišta návrhových nástrojů
    * Přidáno seskupení některých položek
    * Přidáno tlačítko dvojitého zarovnání
    * Přidáno tlačítko Uspořádat vše
* Posouvání položek na podložce pomocí kláves se šipkami
* Složka Stažené soubory je řazena podle data

## Změny

* Vylepšení uživatelského rozhraní
    * Rychlejší aktualizace ve složkách Cloudové knihovny
    * Obnovení uživatelského rozhraní při opětovném otevření
    * Lepší podpora navigace klávesnicí
* Nový systém detekce chyb a varování
    * Ošetřeno více hardwarových chyb
* Vylepšení a optimalizace návrhových nástrojů
    * Nové nástroje Zkroucení 
    * Vylepšený nástroj Křivka
    * Vylepšené Zarovnat


## Změny

* Vylepšeno zploštění
* Vylepšená podpora kroku zpět
* Vylepšená historie návrhu

## Změny
* Verzování: Přechod na číslo verze ve tvaru (verze).(rok).(měsíc). Snazší na čtení a informativnější.
* Nové špičkové Odečíst, Sloučit a Průsečík (pouze Windows)
* Nově startujeme s „Prohlídkou funkcí“, která novým uživatelům pomůže se zorientovat

## Změny
* Návrhové nástroje – Možnost 3D modelovat s kompletní sadou modelovacích primitiv
* Použijte primitivum k vytvoření vlastních přizpůsobených podpor
* Návrhové aplikace – Návrhové aplikace: sofistikované přizpůsobitelné návrhy
* 64bitové Zpracování
