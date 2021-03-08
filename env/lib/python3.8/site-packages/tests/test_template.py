from django.test import TestCase, RequestFactory
from django.template import Template, RequestContext


class TemplateTagTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        request = self.factory.get('/teste')
        context = RequestContext(request=request)
        template_to_render = Template(
            '{% load flags %}'
            '{% languages %}'
        )
        self.rendered_template = template_to_render.render(context)

    def test_has_tags(self):
        """Must contains the tags in HTML"""
        tags = (
            '<li',
            '<a href="#pt-br"',
            '<a href="#en"',
            '<span class="flag-icon flag-icon-pt-br',
            '<span class="flag-icon flag-icon-en'
        )
        for text in tags:
            with self.subTest():
                self.assertIn(text, self.rendered_template)

    def test_has_link_css(self):
        """Must have the link tag with css registration"""
        contents = [
            '<link rel="stylesheet" type="text/css" href="/static/css/django-translation-flags.min.css">'
        ]

        for expected in contents:
            with self.subTest():
                self.assertIn(expected, self.rendered_template)

    def test_has_jquery_function(self):
        """Must have the script tag with jQuery registration"""
        contents = [
            '<script type="text/javascript">',
            'function set_language(language) {',
            '$(\'input[name="language"]\').val(language);',
            '$(\'form#setlang\').submit();',
            '}',
            '</script>',
        ]

        for expected in contents:
            with self.subTest():
                self.assertIn(expected, self.rendered_template)

    def test_has_no_class_square(self):
        """Don't Must contains the class 'flag-icon-square' in HTML"""
        self.assertNotIn('flag-icon-square', self.rendered_template)


class TemplatetagWithSquareTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        request = self.factory.get('/teste')
        context = RequestContext(request=request)
        template_to_render = Template(
            '{% load flags %}'
            "{% languages 'square'  %}"
        )
        self.rendered_template = template_to_render.render(context)

    def test_has_class(self):
        """Must contains the class 'flag-icon-square' in HTML"""
        icon_class = 'flag-icon-square'
        self.assertIn(icon_class, self.rendered_template)

    def test_count_class(self):
        """Must count the class 'flag-icon-square' in HTML"""
        self.assertEqual(2, self.rendered_template.count('flag-icon-square'))


class TemplatetagWithKwargsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        request = self.factory.get('/teste')
        context = RequestContext(request=request)
        template_to_render = Template(
            '{% load flags %}'
            "{% languages 'square' li_class='your-li-class' a_class='your-a-class' %}"
        )
        self.rendered_template = template_to_render.render(context)

    def test_has_class(self):
        """Must contains the classes in HTML"""
        kw_classes = ['your-li-class', 'your-a-class']

        for expected in kw_classes:
            with self.subTest():
                self.assertIn(expected, self.rendered_template)

    def test_count_li_class(self):
        """Must count the class 'your-li-class' in HTML"""
        self.assertEqual(2, self.rendered_template.count('your-li-class'))

    def test_count_a_class(self):
        """Must count the class 'flag-icon-square' in HTML"""
        self.assertEqual(2, self.rendered_template.count('your-a-class'))
