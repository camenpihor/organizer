import os
import django
from django.test import TestCase, utils
from django.urls import reverse
from organizer import views


def setup_module():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'management.settings')
    django.setup()
    utils.setup_test_environment()


def teardown_module():
    utils.teardown_test_environment()


class HomeViewTests(TestCase):
    def test_view_resoulution(self):
        for core_object_type in views.CORE_OBJECT_TYPES:
            url = reverse('home', kwargs={'core_object_type': core_object_type})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, f'{url} should be resolvable')

    def test_bad_request(self):
        url = reverse('home', kwargs={'core_object_type': 'bad-request'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404, f'{url} should not be resolvable')

    def test_default_home(self):
        url = '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, f'{url} should be resolvable')
        self.assertEqual(response.context['page_name'], 'Home')


class ArchiveViewTests(TestCase):
    def test_view_resoulution(self):
        for core_object_type in views.CORE_OBJECT_TYPES:
            url = reverse('archive', kwargs={'core_object_type': core_object_type})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, f'{url} should be resolvable')

    def test_bad_request(self):
        url = reverse('archive', kwargs={'core_object_type': 'bad-request'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404, f'{url} should not be resolvable')


class StatsViewTests(TestCase):
    def test_view_resoulution(self):
        for core_object_type in views.CORE_OBJECT_TYPES:
            url = reverse('stats', kwargs={'core_object_type': core_object_type})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, f'{url} should be resolvable')

    def test_bad_request(self):
        url = reverse('stats', kwargs={'core_object_type': 'bad-request'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404, f'{url} should not be resolvable')


class ItemViewTests(TestCase):
    def test_view_resoulution(self):
        for core_object_type in views.CORE_OBJECT_TYPES:
            url = reverse('item', kwargs={'core_object_type': core_object_type, 'object_id': 1})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, f'{url} should be resolvable')

    def test_bad_request(self):
        url = reverse('item', kwargs={'core_object_type': 'bad-request', 'object_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404, f'{url} should not be resolvable')
