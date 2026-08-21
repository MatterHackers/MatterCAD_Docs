---
title: Wybierz element podrzędny
articleKey: SelectChildObject3D
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: f6f71d2b457b82126f272ea9354f877c36570df0
source_lang: en
---
# Wybierz element podrzędny

Operacja Wybierz element podrzędny wybiera jeden element podrzędny z grupy obiektów na podstawie numeru indeksu lub nazwy. Jest to szczególnie przydatne w projektach skryptowych i parametrycznych, w których chcesz dynamicznie decydować, który obiekt ma być wyświetlany.

<!-- IMAGE: Screenshot showing Select Child operation with multiple children and one selected by index -->
![20260506 080526 paste 20260506 080526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080526-paste-20260506-080526.jpg)


## Sposób użycia

1. Zaznacz dwa lub więcej obiektów
2. Zastosuj operację **Wybierz element podrzędny** z menu Duplikacja
3. Wybierz **Wg indeksu** lub **Wg nazwy**, aby określić sposób wyboru elementu podrzędnego
4. Ustaw numer indeksu lub nazwę do dopasowania

## Parametry

- **Metoda zaznaczania** — wybierz pomiędzy **Wg indeksu** (wybór według pozycji) a **Wg nazwy** (wybór według nazwy obiektu). Wyświetlane jako przyciski.
- **Indeks podrzędny** — liczony od zera indeks elementu podrzędnego do wybrania (widoczny przy użyciu opcji Wg indeksu). Obsługuje [wyrażenia](../../workspace/expressions.md).
- **Nazwa podrzędna** — nazwa elementu podrzędnego do wybrania (widoczna przy użyciu opcji Wg nazwy). Obsługuje [wyrażenia](../../workspace/expressions.md).

Jeśli indeks wykracza poza zakres lub nazwa nie pasuje do żadnego elementu podrzędnego, zwracany jest pierwszy element podrzędny jako wartość zastępcza. Jeśli nie ma elementów podrzędnych, nic nie zostaje zwrócone.

## Zastosowanie w skryptach

Operacja Wybierz element podrzędny została zaprojektowana do pracy z wyrażeniami i funkcją `rand()` w celu tworzenia dynamicznych projektów sterowanych danymi. Możesz na przykład zbudować scenę z kilkoma wariantami obiektów jako elementami podrzędnymi i użyć wyrażenia takiego jak `rand(42)` jako ziarna indeksu, aby losowo wybrać jeden z nich.

**Przykład: losowe rekwizyty książkowe do przedstawienia scenicznego**

1. Importuj 5 różnych siatek książek jako elementy podrzędne operacji Wybierz element podrzędny
2. Ustaw Metoda zaznaczania na **Wg indeksu**
3. Użyj wyrażenia dla parametru Indeks podrzędny, na przykład `floor(rand(seed) * 5)`, gdzie `seed` jest zmienną arkusza
4. Duplikuj operację Wybierz element podrzędny wielokrotnie, za każdym razem z inną wartością ziarna
5. Każde wystąpienie losowo wybiera inną książkę z zestawu

Ten schemat sprawdza się w każdej sytuacji, w której musisz wybrać element z zestawu wariantów: meble, dekoracje, elementy architektoniczne lub dowolny zbiór wymiennych części.

## Wskazówki

- Połącz z operacją [Szyk](array.md), aby tworzyć zróżnicowane wzory, w których każda kopia wybiera inny element podrzędny
- Używaj zmiennych arkusza dla indeksu lub nazwy, aby sterować wyborem z arkusza kalkulacyjnego
- Zachowanie polegające na powrocie do pierwszego elementu podrzędnego sprawia, że projekt nigdy się nie psuje, nawet jeśli indeks lub nazwa są błędne

## Powiązane

- [Szyk](array.md) — duplikowanie obiektów we wzorach liniowych, promienistych, po krzywej oraz z transformacją
