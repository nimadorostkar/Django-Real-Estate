from django.template import Context, Template, RequestContext
from django.test import TestCase, RequestFactory

from django_translation_flags.templatetags.flags import languages


class TemplateTagFlagTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        request = self.factory.get('/teste')
        context = RequestContext(request=request)
        self.languages = languages(context)

    def test_languages_return_has_key(self):
        expected = ['icon_class', 'classes', 'redirect_to']
        self.assertListEqual(expected, list(self.languages.keys()))

    def test_languages_return_has_classes_key(self):
        expected = ['li_class', 'a_class']
        self.assertListEqual(expected, list(self.languages['classes'].keys()))

    def test_languages_return_flag_type(self):
        """Must return empty when given no param"""
        self.assertEqual('', self.languages['icon_class'])

    def test_languages_return_li_class(self):
        """Must return empty when given no param"""
        self.assertEqual('', self.languages['classes']['li_class'])

    def test_languages_return_a_class(self):
        """Must return empty when given no param"""
        self.assertEqual('', self.languages['classes']['a_class'])


class TemplateTagFlagTypeTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        request = self.factory.get('/teste')
        context = RequestContext(request=request)
        self.languages = languages(context, 'square')

    def test_languages_return_flag_type_square(self):
        """Must return the class flag-icon-square when given the string 'square' as param"""
        self.assertEqual('flag-icon-square', self.languages['icon_class'])


class TemplateTagKwargsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        template = Template(
            '{% load flags %}'
            "{% languages 'square' li_class='your-li-class' a_class='your-a-class' %}"
        )
        request = self.factory.get('/teste')
        context = RequestContext(request=request)
        self.languages = languages(context=context, li_class='your-li-class', a_class='your-a-class')

    def test_languages_return_li_class(self):
        """Must return class when given the key li_class"""
        self.assertEqual('your-li-class', self.languages['classes']['li_class'])

    def test_languages_return_a_class(self):
        """Must return class when given the key a_class"""
        self.assertEqual('your-a-class', self.languages['classes']['a_class'])
