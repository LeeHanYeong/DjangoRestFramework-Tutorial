import json

from django.urls import reverse
from rest_framework.test import APILiveServerTestCase


class SnippetTest(APILiveServerTestCase):
    def test_snippet_list(self):
        pass

    def test_snippet_create(self):
        test_title = 'Test Snippet Title'
        test_code = 'print("Hello, world!")'
        default_linenos = False
        default_language = 'python'
        default_style = 'friendly'
        url = reverse('snippet:list')
        data = {
            'title': test_title,
            'code': test_code,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(test_title, response.data.get('title'))
        self.assertEqual(test_code, response.data.get('code'))
        self.assertEqual(default_linenos, response.data.get('linenos'))
        self.assertEqual(default_language, response.data.get('language'))
        self.assertEqual(default_style, response.data.get('style'))

    def test_snippet_retrieve(self):
        pass

    def test_snippet_update_partial(self):
        pass

    def test_snippet_update(self):
        pass

    def test_snippet_delete(self):
        pass