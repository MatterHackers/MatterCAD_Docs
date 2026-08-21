---
title: Najczęściej zadawane pytania
nav_order: 101
source_hash: 929ea9e89d3f5008996615341418ba715d3f6075
source_lang: en
---
# Dlaczego moje obiekty mają nieprawidłową skalę?
- Pliki STL nie przechowują informacji o jednostkach. MatterCAD oczekuje wymiarów STL w milimetrach, podczas gdy większość oprogramowania CAD eksportuje je w swoich jednostkach natywnych (zazwyczaj w calach). Powoduje to rozbieżności skali podczas importowania projektów.

- Najlepszym rozwiązaniem jest skonfigurowanie oprogramowania projektowego tak, aby eksportowało pliki STL w milimetrach. Na przykład w programie SolidWorks użyj przycisku Opcje w oknie dialogowym Zapisz jako, aby ustawić parametry eksportu STL.

- Możesz też przeskalować część bezpośrednio w MatterCAD. W Widoku 3D przejdź do trybu Edytuj i wybierz SKALA na prawym pasku narzędzi. Skorzystaj z listy rozwijanej z typowymi współczynnikami przeliczeniowymi lub wpisz konkretne wymiary w polach osi.

# Jak wyczyścić dane aplikacji?

- Jeśli ponowna instalacja nie rozwiązuje problemu, może być konieczne usunięcie danych zapisanych przez MatterCAD. Dane te pozostają na dysku po odinstalowaniu. Aby całkowicie przywrócić ustawienia domyślne, usuń folder aplikacji. Możesz również tymczasowo zmienić nazwę pliku bazy danych SQLite (MatterCAD.db), aby sprawdzić, czy przyczyną problemów są ustawienia.
![20260318 194137 paste 20260318 194137](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194137-paste-20260318-194137.jpg)

![20260318 194200 paste 20260318 194200](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194200-paste-20260318-194200.jpg)

![20260318 194218 paste 20260318 194218](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194218-paste-20260318-194218.jpg)


- Windows
  - Biblioteka użytkownika i ustawienia są przechowywane w C:\Users\{user}\AppData\Local\MatterCAD.
