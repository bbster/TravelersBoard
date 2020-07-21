from django.conf import settings
from test_plus import TestCase
from apps.account.models import User
from apps.board.models import Board, Post, Comment


class PostCreateTest(TestCase):
    def setUp(self):
        self.user = self.make_user(username='test_case_user', password='test')

    def api_create_board(self):
        self.post(
            "/api/board/",
            data={
                'unique_title': 'test_case',
            }
        )
        board = self.last_response.json()
        return board

    def api_create_post(self):
        res_board = self.api_create_board()

        # When
        self.post(
            "/api/post/",
            data={
                'board': res_board['id'],
                'title': 'title',
                'content': 'content',
                'creator': self.user.id,
            }
        )
        post = self.last_response.json()
        return post

    def api_create_comment(self):
        res_post = self.api_create_post()

        self.post(
            "/api/comment/",
            data={
                'post': res_post['id'],
                'content': 'test_content',
                'creator': self.user.id,
            }
        )
        comment = self.last_response.json()
        return comment

    def api_create_sub_comment(self):
        res_comment = self.api_create_comment()

        self.post(
            "/api/comment/",
            data={
                'content': 'test_content',
                'creator': self.user.id,
                'parent': res_comment['id']
            }
        )
        comment_parent = self.last_response.json()
        return comment_parent

    def test_board_create(self):
        self.login(username='test_case_user', password='test')

        res = self.api_create_board()

        self.response_201()
        assert res['id']
        assert res['unique_title']

    def test_post_create(self):
        # Case
        self.login(username='test_case_user', password='test')

        # When
        res = self.api_create_post()

        # Then
        self.response_201()
        assert res['id']
        assert res['board']
        assert res['title']
        assert res['content']
        assert res['creator']

    def test_comment_create(self):
        self.login(username='test_case_user', password='test')

        self.api_create_sub_comment()

        res = self.last_response.json()
        self.response_201()
        breakpoint()
        assert res['id']
        assert res['content']
        assert res['creator']
        assert res['parent']
