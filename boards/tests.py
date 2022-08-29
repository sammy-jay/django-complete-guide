from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from .views import home

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('boards:home')
        response = self.client.get(url)
        self.assertTemplateUsed('home.html')
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
