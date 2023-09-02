from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginTestCase(TestCase):

    def setUp(self):
        # Tworzenie użytkownika do testów
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_login_get(self):
        # Wysłanie żądania GET do formularza logowania
        response = self.client.get(reverse('login'))

        # Sprawdzenie, czy formularz logowania jest dostępny (oczekujemy statusu 200)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Logowanie")  # Sprawdzenie, czy widok zawiera tytuł "Logowanie"

    def test_login_post(self):
        # Przygotowanie danych do testu
        data = {
            'username': self.username,
            'password': self.password,
        }

        # Wysłanie żądania POST do widoku logowania
        response = self.client.post(reverse('login'), data)

        # Sprawdzenie, czy logowanie się powiodło (oczekujemy przekierowania, czyli statusu 302)
        self.assertEqual(response.status_code, 302)

        # Sprawdzenie, czy użytkownik jest teraz zalogowany
        user = self.client.get(reverse('dashboard')).context['user']
        self.assertTrue(user.is_authenticated)
