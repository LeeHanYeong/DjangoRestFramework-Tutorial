import random

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APILiveServerTestCase

from snippets.models import Snippet

User = get_user_model()


class SnippetTest(APILiveServerTestCase):
    test_title = 'Test Snippet[{}] Title'
    test_code = 'print("Hello, world{}")'
    default_linenos = False
    default_language = 'python'
    default_style = 'friendly'

    test_username = 'test_username'
    test_password = 'test_password'

    def create_user(self):
        user = User.objects.create_user(
            username=self.test_username,
            password=self.test_password,
        )
        return user

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
            url = reverse('snippets:snippet_list')
            data = {
                'title': test_title,
                'code': test_code,
            }
            response = self.client.post(url, data, format='json')
            if num == 1:
                return response

    def test_snippet_list(self):
        # Snippet목록을 생성하기 전에 인증을 위해 유저를 생성하고 로그인
        self.create_user()
        self.client.login(username=self.test_username, password=self.test_password)

        # 1~20개중 랜덤하게 Snippet을 생성
        num = random.randrange(1, 20)
        self.create_snippet(num)

        # num값과 일치하는 개수만큼 Snippet이 생성되었는지 확인
        self.assertEqual(Snippet.objects.count(), num)

        # values_list를 사용해서 필요한 항목만 가져올 경우
        for index, snippet_value_tuple in enumerate(Snippet.objects.values_list('title', 'code')):
            self.assertEqual(snippet_value_tuple[0], self.test_title.format(index + 1))
            self.assertEqual(snippet_value_tuple[1], self.test_code.format('!' * (index + 1)))

        # 쿼리가 매우 커서 일부만 사용할 경우
        for index, snippet in enumerate(Snippet.objects.all().iterator()):
            self.assertEqual(snippet.title, self.test_title.format(index + 1))
            self.assertEqual(snippet.code, self.test_code.format('!' * (index + 1)))

    def test_snippet_cannot_create_no_authenticate(self):
        # Snippet생성 요청
        response = self.create_snippet()
        # 생성 후 response가 올바른지 테스트
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_snippet_create(self):
        # Create이전에 인증을 위해 유저를 생성하고 로그인 시킴
        self.create_user()
        self.client.login(username=self.test_username, password=self.test_password)

        # Snippet생성 요청
        response = self.create_snippet()

        # 생성 후 response가 올바른지 테스트
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

    def test_snippet_highlight(self):
        """
        Snippet의 save()메서드를 참조해서
        만들어진 Snippet인스턴스의 highlighted필드의 값이
        pygments를 사용해서 만들어낸
        syntax highlighted HTML과 같은지 (assertEqual)확인
        """
        pass
