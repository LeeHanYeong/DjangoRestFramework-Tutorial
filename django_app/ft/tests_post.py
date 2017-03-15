import random

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APILiveServerTestCase

from snippets.models import Snippet


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
        num = random.randrange(1, 20)
        self.create_snippet(num)
        self.assertEqual(Snippet.objects.count(), num)
        # values_list를 사용해서 필요한 항목만 가져올 경우
        for index, snippet_value_tuple in enumerate(Snippet.objects.values_list('title', 'code')):
            self.assertEqual(snippet_value_tuple[0], self.test_title.format(index + 1))
            self.assertEqual(snippet_value_tuple[1], self.test_code.format('!' * (index + 1)))

        # 쿼리가 매우 커서 일부만 사용할 경우
        for index, snippet in enumerate(Snippet.objects.all().iterator()):
            self.assertEqual(snippet.title, self.test_title.format(index + 1))
            self.assertEqual(snippet.code, self.test_code.format('!' * (index + 1)))

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
