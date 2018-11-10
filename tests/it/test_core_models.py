import os

import django
from django.test import TestCase, utils


def setup_module():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'management.settings')
    django.setup()
    utils.setup_test_environment()


def teardown_module():
    utils.teardown_test_environment()


class QuestionTests(TestCase):
    def test_question(self):
        self.assertTrue(True)
