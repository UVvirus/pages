from django.test import TestCase
from django.test import SimpleTestCase
# Create your tests here.

class Simpletests(SimpleTestCase):
    def home_test(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)

    def about_test(self):
        response=self.client.get('/about/')
        self.assertEqual(response.status_code,200)
