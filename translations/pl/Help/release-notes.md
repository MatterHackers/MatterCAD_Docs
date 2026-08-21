---
title: Informacje o wydaniu
nav_order: 104
source_hash: 3ac9ea595f4f14d23496f8e287ff115f5a7738ff
source_lang: en
---
# MatterCAD 2.2026.8 (13 sierpnia 2026)
[Pobieranie dla Windows](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## Nowe funkcje

* **Edytuj elementy podrzędne**
  * Kliknij dwukrotnie obiekt na stole roboczym lub w drzewie sceny, aby wejść do jego wnętrza i edytować części, z których jest zbudowany — bez osobnego okna czy karty
  * W przypadku operacji takich jak Odejmij edytujesz części źródłowe, a wynik jest przebudowywany po wyjściu
  * Ścieżka nawigacji u góry drzewa sceny pokazuje pełną ścieżkę; kliknięcie poziomu scala Twoje edycje w jeden krok możliwy do cofnięcia, a każdy poziom zachowuje własną historię cofania
  <!-- Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->
  * ![Drill In](https://www.matterhackers.com/r/qgG4VA)

* **Jedno narzędzie boolowskie**
  * Połącz, Odejmij, Część wspólna oraz Odejmij i zamień to teraz jedna operacja z rzędem ikon u góry panelu — tryby przełączasz kliknięciem, zamiast usuwać i ponownie stosować operację
  * Ta sama operacja obsługuje zarówno siatki 3D, jak i ścieżki 2D, a podczas wymagającej operacji boolowskiej pokazuje postęp
  * Projekty zapisane ze starszymi, oddzielnymi obiektami boolowskimi nadal otwierają się normalnie
  <!-- Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->
  * ![20260810 181041 paste 20260810 181041](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)


* **Operacje boolowskie, które po prostu działają**
  * Operacje boolowskie działają na nowym natywnym silniku, który jest szybszy i radzi sobie z siatkami, na których wcześniej zawodziły
  * Połącz automatycznie naprawia części z dziurami: poprawnie naprawione dołączają do sumy, części, których nie da się bezpiecznie scalić, pozostają obok niej z nadanymi nazwami, a część, której nie udało się naprawić, zachowuje oryginalną geometrię
  * Cięcie płaszczyzną jest teraz prawdziwym przecięciem brył, więc wynik jest szczelny i gotowy do druku, a nie otwartą powłoką
  * Nowe opcje Zachowaj geometrię odwróconą na lewą stronę i Napraw kolejność nawijania dla problematycznych importowanych siatek


## Ulepszenia

* **Edytor ścieżek 2D**
  * Cztery tryby punktów — Ostry, Symetryczny, Wyrównany i Swobodny — stosowane jednym kliknięciem, zarówno w edytorze 2D, jak i w widoku 3D
  * Odbicie lustrzane jest teraz aktywnym trybem symetrii: edycje są odbijane względem środka na bieżąco, a przeciągnięcie odbitej pary na oś scala ją w jeden punkt
  * Zaznaczaj punkty przeciągnięciem ramki, przesuwaj je grupowo, przyciągaj do siatki i naciśnij Esc, aby anulować przeciąganie
  * Wygładzanie dopasowuje krzywą do wyklikanych punktów w jednym kroku
  <!-- gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

* **Widok i nawigacja**
  * Naciśnij Z przy zaznaczonej płaskiej ścieżce, aby płynnie przejść do widoku edycji z góry dopasowanego do ścieżki
  * Renderowanie tekstu z dokładnością subpikselową jest teraz włączane automatycznie, gdy ekran to obsługuje, i nadal można je włączyć lub wyłączyć w ustawieniach Zaawansowane

* **Modelowanie**
  * Wyciągnięcie liniowe może fazować dolną krawędź z własnym stylem, promieniem i liczbą segmentów
  * Obiekty istniejące tylko w edytorze (Krzywa 3D, Narzędzie pomiaru, Opis, Arkusz) nadal są wyświetlane, ale są wykluczane z eksportu

## Najważniejsze poprawki błędów

  * Zapis, który nie powiódł się w połowie, mógł obciąć zastępowany plik, zgłaszając jednocześnie sukces. Zapisy są teraz w pełni kończone, a następnie atomowo zastępują plik docelowy — ta sama ochrona obejmuje zapisy do biblioteki i eksporty
  * Nieudany zapis pozostawia projekt oznaczony jako niezapisany, więc zamknięcie aplikacji nie może po cichu odrzucić Twojej pracy
  * Zapisanie elementu z chmury na dysku zachowywało starą nazwę karty i powodowało utratę karty po ponownym uruchomieniu
  * Naprawiono ciche pomijanie podmodeli 3MF podczas wczytywania oraz wzajemne zanieczyszczanie się plików 3MF wczytywanych jednocześnie
  * Naprawiono awarie, niedziałający filtr histogramu oraz brak synchronizacji kopii części obrazu z oryginałem
  * Naprawiono awarię przy usuwaniu punktu krzywej oraz cofanie wybranego trybu przez punkty na szwie zamkniętej ścieżki
  * Przycisk Stop przy uruchomionym zadaniu jest teraz klikalny i faktycznie anuluje zadanie

---

# MatterCAD 2.2026.5 (8 maja 2026)
[Pobieranie dla Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMiMyt-ICwwLEgZVcGxvYWQYgIDI7IHKkwoM)

## Nowe funkcje

* **Przeprojektowane narzędzie szyku**
  * Pojedyncza, ujednolicona operacja szyku zastępuje dawne Szyk liniowy, Szyk kołowy i Zaawansowany szyk
  * Tryb **Liniowy**: kopie wzdłuż kierunku z opcjonalnym obrotem i progresywną skalą
  * Tryb **Promieniowy**: kopie wokół osi centralnej z konfigurowalnym promieniem, kątem rozwarcia oraz wzorami łuku lub pełnego okręgu
  * Tryb **Przekształć**: kopie krokowe z użyciem ręcznego przekształcenia lub przekształcenia nazwanego obiektu równorzędnego
  * Tryb obrotu Łączenie w trybie Liniowy w naturalny sposób tworzy spirale, wachlarze i helisy
  * Opcja Skala wpływa na offset dla układów typu muszla łodzika i postęp geometryczny
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **Ulubione w bibliotece**
  * Oznacz gwiazdką dowolny element biblioteki, aby dodać go do trwałego folderu Ulubione
  * Szybki dostęp z jednego miejsca do najczęściej używanych prymitywów, generatorów i zapisanych części
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## Ulepszenia

* **Wyrównaj**
  * Wyrównanie Ułożone w stos jest teraz bezpośrednim przyciskiem trybu zamiast opcji na liście rozwijanej
  * Dodano czytelniejsze tryby Proste, Przesunięcie i Ułożone w stos do wyrównywania krawędzi, dodawania precyzyjnych odstępów i budowania uporządkowanych stosów
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **Obsługa plików**
  * Dodano obsługę formatu obrazu WEBP w operacjach opartych na obrazach
  * Ulepszono analizę plików SVG dla bardziej niezawodnego importu

* **Niezawodność**
  * Poprawiono szybkość i niezawodność wczytywania plików 3MF
  * Lepsze przywracanie kart między sesjami

## Najważniejsze poprawki błędów

* **Logowanie i dostęp do Biblioteki w chmurze**
  * Przywrócono logowanie i dostęp do Biblioteki w chmurze po tym, jak aktualizacja serwera zaplecza uniemożliwiła logowanie.
  * MatterCAD prosi teraz, abyś ponownie zalogował się, gdy dostęp do chmury napotka wygasłe lub nieprawidłowe dane logowania.

* **Zaznaczenie w drzewie sceny**
  * Naprawiono niespójne zachowanie zaznaczania podczas wybierania obiektów z drzewa sceny.

* **Nawigacja w pomocy**
  * Naprawiono problemy z nawigacją w dołączonej pomocy i dokumentacji wydania.

* **Kliknięcie prawym przyciskiem w bibliotece**
  * Naprawiono zachowanie kliknięcia prawym przyciskiem myszy w widoku drzewa biblioteki.

* **Arkusze**
  * Naprawiono awarię, która mogła wystąpić podczas pracy z arkuszami.

---

# MatterCAD 2.2026.3 (12 marca 2026)
[Pobieranie dla Windows](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## Nowe funkcje

* **Zupełnie nowy silnik renderowania Direct3D 11**
  * Pełna migracja z OpenGL na Direct3D 11 dla znacznie lepszej wydajności
  * Antyaliasing FXAA dla ostrych, czystych krawędzi
  * Podwójne depth peeling dla poprawnej przezroczystości niezależnej od kolejności
  * Sprzętowo przyspieszane cienie na stole
  * Ulepszone obrysy obiektów i wizualizacja zaznaczenia
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **Przezroczystość obiektów**
  * Ustaw kanał alfa/przezroczystość dla dowolnego pojedynczego obiektu w scenie
  * Siatki z kolorami na poszczególnych ścianach obsługują kanał alfa bez utraty kolorów
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **Blokowanie i ukrywanie obiektów**
  * Blokuj obiekty, aby zapobiec przypadkowemu zaznaczeniu lub edycji
  * Ukrywaj obiekty, aby ograniczyć bałagan wizualny podczas pracy nad konkretnymi częściami
  * Polecenia Pokaż wszystko i Odblokuj wszystko szybko przywracają widoczność
  * Zablokowane i ukryte obiekty są prawidłowo wykluczane z zaznaczania promieniem
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **Ulepszona operacja Odejmij**
  * Operacje wielokrotnego odejmowania są znacznie bardziej niezawodne i dokładne

## Ulepszenia

* **Obsługa plików**
  * Projekty są teraz domyślnie zapisywane w formacie 3MF zamiast STL, zachowując kolory, materiały i historię projektu
  * Ulepszona obsługa przeciągania i upuszczania plików oraz folderów do widoku 3D

* **Przepływ pracy**
  * Okna dialogowe Zapisz jako i Przenieś zapamiętują ostatnią lokalizację folderu
  * Pola wyrażeń obsługują teraz `pi`, `tau`, `e` i `count`
  * Klawisz Esc cofa operację w kontekstach edycji projektu
  * Elementy sterujące 3D pozostają widoczne, gdy kursor opuści scenę

* **Wydajność i stabilność**
  * Naprawiono awarie przy uruchamianiu i problemy z rekurencyjnym wczytywaniem
  * Naprawiono błędy renderowania oświetlenia i mipmapowania
  * Ulepszono aktualizacje widoku drzewa biblioteki
  * Dynamiczne obliczanie płaszczyzn bliskiej i dalekiej dla lepszego zachowania przybliżania
  * Zaktualizowano do .NET 10

---

# MatterCAD 2.2025.6 (20 czerwca 2025)
[Pobieranie dla Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## Nowe funkcje

* **Obsługa plików SVG**  
  * Pełna obsługa przeciągania i upuszczania plików SVG
  * Bezpośrednia konwersja grafiki SVG na obiekty 3D
  * Płynna integracja z istniejącymi przepływami pracy CAD

* **Zaawansowana obsługa plików OBJ**  
  * Obsługa wczytywania materiałów z archiwów ZIP
  * Ulepszona analiza plików OBJ i obsługa materiałów
  * Lepsza obsługa złożonych modeli 3D z wieloma materiałami

* **Ulepszony system zarządzania kartami**
  * Karty biblioteki w chmurze są teraz prawidłowo zachowywane — Twoja praca pozostaje dokładnie tam, gdzie ją zostawiłeś
  * Lepsza organizacja kart i nawigacja
  * Automatyczne przywracanie otwartych kart między sesjami

## Ulepszenia obsługi

* **Uproszczony interfejs**
  * Zreorganizowane menu Ostatnie dla szybszego dostępu
  * Lepsza informacja zwrotna podczas długich operacji
  * Skrócony czas uruchamiania aplikacji i lepsza responsywność

* **Niezawodność**
  * Naprawiono krytyczne awarie w interakcjach ze sceną 3D
  * Rozwiązano problemy z zarządzaniem pamięcią
  * Poprawiono stabilność aplikacji na wszystkich platformach

---

# MatterCAD 2.21.5 (13 lutego 2025)

[Pobieranie dla Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# Istniejące funkcje

*Poniższe funkcje stanowią fundament, na którym MatterCAD opiera się, czerpiąc z dziedzictwa MatterControl:*

* Dodano funkcję Wydrążenie  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* Dodano Zmniejsz liczbę wielokątów  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* Dodano Napraw siatkę  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* Dodano w pełni automatyczne podpory (podpory starszego typu) jako opcję obok nowej opcji podpór ręcznych
* Dodano obsługę gsSlicer (eksperymentalny nowy silnik cięcia)
* Naprawiono błędy

## Zmiany

* Ulepszone rozgrupowywanie siatki (dzielenie na wiele siatek)
    * Odrzucanie zdegenerowanych ścian
    * Odrzucanie mikroskopijnych, oddzielnych elementów

## Zmiany

* Dodano pasek wyszukiwania w aplikacji
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* Ulepszono pasek narzędzi projektowych
    * Dodano grupowanie niektórych elementów
    * Dodano przycisk podwójnego wyrównania
    * Dodano przycisk Rozmieść wszystko
* Przesuwanie elementów na stole klawiszami strzałek
* Folder Pobrane jest sortowany według daty

## Zmiany

* Ulepszenia interfejsu
    * Szybsze aktualizacje w folderach Biblioteki w chmurze
    * Przywracanie interfejsu po ponownym otwarciu
    * Lepsza obsługa nawigacji klawiaturą
* Nowy system wykrywania błędów i ostrzeżeń
    * Obsługa większej liczby błędów sprzętu
* Ulepszenia i optymalizacje narzędzi projektowych
    * Nowe narzędzia Skręcanie 
    * Ulepszone narzędzie Krzywa
    * Ulepszone Wyrównaj


## Zmiany

* Ulepszone spłaszczanie
* Ulepszona obsługa cofania
* Ulepszona historia projektu

## Zmiany
* Wersjonowanie: przejście na numer wersji w formacie (wersja).(rok).(miesiąc). Łatwiejszy do odczytania i bardziej informacyjny.
* Nowe, najnowocześniejsze Odejmij, Połącz i Przecięcie (tylko Windows)
* Aplikacja uruchamia się teraz z „Przewodnikiem po funkcjach”, który pomaga nowym użytkownikom się odnaleźć

## Zmiany
* Narzędzia projektowe - możliwość modelowania 3D z pełnym zestawem prymitywów modelowania
* Użyj prymitywu, aby stworzyć własne, dostosowane podpory
* Aplikacje projektowe - Aplikacje projektowe: zaawansowane, konfigurowalne projekty
* 64-bitowe Przetwarzanie
