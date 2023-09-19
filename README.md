# carrental

Projekt "CarRental" to system zarządzania wypożyczalnią samochodów. Głównym celem tego projektu jest umożliwienie użytkownikom rezerwacji i wynajmowania samochodów na określony okres czasu.

Podstawowe funkcje projektu "CarRental" mogą obejmować:

1. **Rejestracja i Logowanie:** Użytkownicy mogą tworzyć konta i logować się, aby korzystać z usług wypożyczalni samochodów.

2. **Wyszukiwanie Samochodów:** Użytkownicy mogą przeszukiwać dostępne samochody na podstawie różnych kryteriów, takich jak rodzaj samochodu, cena, dostępność, marka itp.

3. **Rezerwacja Samochodu:** Użytkownicy mogą rezerwować samochody na określony okres czasu. Mogą także anulować rezerwacje.

4. **Wynajmowanie Samochodu:** Po dokonaniu rezerwacji użytkownicy mogą odebrać wynajęty samochód w wybranym punkcie wypożyczalni i korzystać z niego przez określony czas.

5. **Zwrot Samochodu:** Po zakończeniu okresu wynajmu użytkownicy muszą zwrócić samochód w wybranym punkcie wypożyczalni.

6. **Płatności:** System obsługuje płatności za wynajem samochodów, z uwzględnieniem różnych metod płatności.

7. **Zarządzanie Samochodami:** Administratorzy systemu mogą dodawać, edytować i usuwać samochody z oferty wypożyczalni.

8. **Zarządzanie Użytkownikami:** Administratorzy mogą zarządzać kontami użytkowników, nadawać uprawnienia i monitorować aktywność użytkowników.

9. **Historia Wynajmu:** Użytkownicy mogą przeglądać historię swoich wynajmów samochodów.

10. **Raporty i Statystyki:** System może generować raporty i statystyki dotyczące działalności wypożyczalni samochodów, takie jak przychody, ilość wynajmów itp.

Projekt "CarRental" ma na celu ułatwienie zarządzania wypożyczalnią samochodów i poprawę doświadczenia użytkowników podczas wynajmowania pojazdów. Może być wykorzystywany zarówno przez klientów, którzy chcą wynająć samochód, jak i przez personel wypożyczalni do zarządzania flotą samochodów oraz obsługi klientów.

Użyte Biblioteki

Django: Framework webowy Pythona.
python-decouple: Biblioteka do obsługi zmiennych środowiskowych.
Pillow: Biblioteka do obsługi obrazów w Pythonie.
Contributing


Licencja

Ten projekt jest udostępniany na licencji 

Instalacja:

python -m venv venv
source venv/bin/activate  # Dla systemów Unix/macOS
# lub
.\venv\Scripts\activate  # Dla systemu Windows

pip install -r requirements.txt

Skonfiguruj zmienne środowiskowe w pliku .env. Przykładowy plik .env może wyglądać tak:
DEBUG=True
SECRET_KEY=your_secret_key_here
DATABASE_URL=your_database_url_here

Wykonaj migrację:
python manage.py migrate

Uruchom serie:
python manage.py runserver


