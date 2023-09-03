from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginTestCase(TestCase):

    def setUp(self):
     
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_login_get(self):
        
        response = self.client.get(reverse('login'))

        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Logowanie")  

    def test_login_post(self):
      
        data = {
            'username': self.username,
            'password': self.password,
        }

     
        response = self.client.post(reverse('login'), data)

      
        self.assertEqual(response.status_code, 302)

 
        user = self.client.get(reverse('dashboard')).context['user']
        self.assertTrue(user.is_authenticated)
