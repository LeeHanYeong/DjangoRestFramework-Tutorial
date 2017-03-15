import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APILiveServerTestCase


class SnippetTest(APILiveServerTestCase):
    test_title = 'Test Snippet[{}] Title'
    test_code = 'print("Hello, world{}")'
    default_linenos = False
    default_language = 'python'
    default_style = 'friendly'

    def create_snippet(self, num=1):
        """
        주어진 num값 (기본값 1)만큼의 snippet을 만든다
        num이 1일경우, 생성 후 response를 리턴
        :param num: 만들 Snippet 개수
        :return: num이 1일 경우, 생성요청 후 response
        """
        for i in range(num):
            test_title = self.test_title.format(i + 1)
            test_code = self.test_code.format('!' * (i + 1))
            url = reverse('snippet:list')
            data = {
                'title': test_title,
                'code': test_code,
            }
            response = self.client.post(url, data, format='json')
            if num == 1:
                return response

    def test_snippet_list(self):
        pass

    def test_snippet_create(self):
        response = self.create_snippet()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('title'), self.test_title.format(1))
        self.assertEqual(response.data.get('code'), self.test_code.format('!'))
        self.assertEqual(response.data.get('linenos'), self.default_linenos)
        self.assertEqual(response.data.get('language'), self.default_language)
        self.assertEqual(response.data.get('style'), self.default_style)

    def test_snippet_retrieve(self):
        pass

    def test_snippet_update_partial(self):
        pass

    def test_snippet_update(self):
        pass

    def test_snippet_delete(self):
        pass