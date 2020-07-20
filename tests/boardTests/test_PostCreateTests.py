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
                'unique_title': 'QnA',
            }
        )
        board = self.last_response.json()
        return board

    def test_board_create(self):
        self.login(username='test_case_user', password='test')

        res = self.api_create_board()

        self.response_201()
        assert res['unique_title']

    def test_post_create(self):
        # Case
        self.login(username='test_case_user', password='test')
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

        # Then
        self.response_201()
        res = self.last_response.json()
        assert res['board']
        assert res['title']
        assert res['content']
        assert res['creator']

    # def test_board_not_exist_unique_title_create(self):
    #     board = Board.objects.create(unique_title='QnA')
    #     self.post(
    #         "/api/board/",
    #         data={
    #             "board": board,
    #             'title': 'title',
    #             'content': 'content',
    #             'creator': 'admin',
    #         }
    #     )
    #     # breakpoint()
    #     self.response_200()
    #     res = self.last_response.json()
    #     assert res['board']
    #     assert res['title']
    #     assert res['content']
    #     assert res['creator']
    #
    # def test_board_not_exist_user_create(self):
    #     board = Board.objects.create(unique_title='QnA')
    #     self.post(
    #         "/api/board/",
    #         data={
    #             "board": "QnA",
    #             'title': 'title',
    #             'content': 'content',
    #         }
    #     )
    #     # breakpoint()
    #     self.response_200()
    #     res = self.last_response.json()
    #     assert res['board']
    #     assert res['title']
    #     assert res['content']
    #     assert res['creator']
