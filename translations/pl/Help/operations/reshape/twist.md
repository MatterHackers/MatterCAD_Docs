---
title: Skręcenie
articleKey: TwistObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: 8ea8d2017c16f20dc42b433bcf91815262bb5380
source_lang: en
---
# Skręcenie

Skręcenie obraca górę obiektu względem jego dołu, tworząc efekt spirali lub skręcenia wzdłuż wysokości. Domyślnie obrót narasta równomiernie od dołu do góry; w sekcji Zaawansowane możesz narysować, w którym miejscu na wysokości skręcanie faktycznie następuje.

<!--  Before and after showing a cube being twisted into a spiral column -->
![20260506 155620 paste 20260506 155620](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155620-paste-20260506-155620.jpg)

## Sposób użycia

1. Wybierz obiekt
2. Zastosuj operację **Skręcenie** z menu Przekształć
3. Ustaw kąt skręcenia i dostosuj liczbę przekrojów, aby uzyskać gładkość
4. Włącz opcję **Zaawansowane**, jeśli chcesz narysować, jak skręcenie rozkłada się wzdłuż części

## Profil skręcenia

W sekcji Zaawansowane krzywa **Profil skręcenia** decyduje o tym, gdzie następuje skręcenie. Całkowita wielkość skręcenia nadal jest ustawiana kontrolką Kąt (lub Odległość obrotu) — krzywa jedynie ją rozkłada:

- **W górę krzywej** odkładana jest wysokość na części w procentach — 0 na dole, 100 na górze. Linia pomocnicza w poprzek edytora oznacza 100 procent i jest opisana rzeczywistą wysokością części w mm.
- **W poprzek krzywej** odkładany jest procent całkowitego skręcenia osiągnięty na tej wysokości — 0 oznacza brak skręcenia, 100 oznacza całe skręcenie.

Nowe Skręcenie zaczyna się od prostej przekątnej od 0 do 100, co odpowiada zwykłemu równomiernemu skręceniu, które otrzymujesz bez włączania opcji Zaawansowane.

Płaski odcinek krzywej to pas części, który nie jest skręcany. Tam, gdzie krzywa nie obejmuje pełnej wysokości, utrzymywana jest jej najbliższa wartość skrajna, więc krzywa narysowana tylko pomiędzy 40 a 60 procent pozostawia część sztywną poniżej i powyżej tego zakresu — w ten sposób rozpoczynasz i kończysz skręcenie na wybranej wysokości.

Odcinek, który opada w miarę wznoszenia się, rozkręca część: ten pas obraca się w drugą stronę, z powrotem w kierunku położenia początkowego. Narysowanie profilu powyżej 100, a następnie z powrotem w dół, pozwala przekroczyć wartość całkowitą i wrócić do niej.

## Parametry

- **Typ obrotu** — Wybierz spośród:
  - **Kąt** — Określ całkowity kąt skręcenia w stopniach (3-360)
  - **Odległość** — Określ skręcenie jako odległość wzdłuż obwodu
- **Przekroje** — Liczba poziomych cięć dodawanych dla gładkiego skręcenia, rozmieszczonych równomiernie wzdłuż części. Więcej przekrojów = gładsze skręcenie
- **Minimalna liczba boków** — Najmniejsza liczba boków, jaką część powinna mieć wokół osi skręcenia. Zgrubny kształt, taki jak sześcian, nie ma na obwodzie geometrii, która przeniosłaby obrót, więc jego płaskie ściany załamują się zamiast wyginać; ta opcja dodaje pionowe cięcia przechodzące przez oś skręcenia, aby ściany mogły podążać za skręceniem. Wartość 0 (domyślna) pozostawia część bez zmian
- **Skręć w prawo** — Kierunek skręcenia: w prawo (zgodnie z ruchem wskazówek zegara) lub w lewo (przeciwnie do ruchu wskazówek zegara)
- **Preferowany promień** — Tylko do odczytu: promień zgłaszany przez samą część lub wynikający z jej kształtu, względem którego mierzona jest odległość skręcenia (tylko w trybie Odległość)
- **Edytuj promień** — Wyłącz zgłaszany promień, aby ustawić własny (tylko w trybie Odległość i tylko wtedy, gdy część zgłasza promień)
- **Zastąp promień** — Niestandardowy promień do obliczenia skręcenia (tylko w trybie Odległość)

### Parametry zaawansowane

- **Profil skręcenia** — Opisany powyżej edytor krzywej: procent całkowitego skręcenia osiągnięty na każdej wysokości podanej w procentach
- **Przesunięcie obrotu** — Przesuń środek, wokół którego obracana jest część, poza środek części

## Wskazówki

- Wyższe wartości Przekrojów dają gładsze wyniki, ale generują więcej geometrii
- Jeśli skręcony sześcian lub inny kształt o płaskich ścianach wygląda na załamany zamiast wygiętego, zwiększ Minimalną liczbę boków
- Narysuj profil płasko na dole i wznoszący się powyżej, aby pozostawić prostą podstawę pod skręconą kolumną
- Skręcenie o 90 stopni na kwadratowej kolumnie tworzy elegancki efekt architektoniczny
- Narysuj dwa płaskie odcinki połączone krótkim wzniesieniem, aby skręcić środek części i pozostawić oba końce sztywne

## Powiązane

- [Krzywa](curve.md) — Wygina obiekt w łuk
- [Zwężenie](pinch.md) — Ściska w kierunku środka
- [Ściśnięcie promieniowe](radial-pinch.md) — Kształtuje profil za pomocą krzywej w ten sam sposób
