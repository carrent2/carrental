from django.test import TestCase
from django.urls import reverse

class UserLoginViewTest(TestCase):
    def test_get_request(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_post_request_with_valid_credentials(self):
        data = {
            'username': 'your_username',
            'password': 'your_password',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)

    def test_post_request_with_invalid_credentials(self):
        data = {
            'username': 'invalid_username',
            'password': 'invalid_password',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)
