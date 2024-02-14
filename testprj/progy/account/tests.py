from django.test import TestCase, Client
from django.urls import reverse
from .models import Name


class HelloWorldViewTest(TestCase):
    def test_hello_world(self):
        url = reverse('account:hello_world')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Hello World!")


class AddNumbersViewTest(TestCase):
    def test_add_numbers_get(self):
        url = reverse('account:add_numbers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Введите 2 числа и нажмите Submit")

    def test_add_numbers_post(self):
        url = reverse('account:add_numbers')
        data = {'num1': '5', 'num2': '3'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Сумма чисел 5 и 3 равна 8")


class NameIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:name_list')

    def test_name_list_integration(self):
        # Create test data
        Name.objects.create(name='John', description='John Doe')
        Name.objects.create(name='Jane', description='Jane Smith')

        # Send a GET request to the URL
        response = self.client.get(self.url)

        # Assert the response status code and content
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John')
        self.assertContains(response, 'Jane')
