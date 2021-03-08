from django.test import TestCase
from django_translation_flags import app_settings


class AppSettingsTest(TestCase):
    def test_has_defined(self):
        """Must have the MIDDLEWARE defined in app_settings.py"""
        self.assertTrue(hasattr(app_settings, 'MIDDLEWARE'))
