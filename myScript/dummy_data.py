from apps.board.models import Board, Post
from apps.account.models import User

board = Board.objects.get(pk=1)
creator = User.objects.get(pk=1)

for i in range(1, 1000):
    Post.objects.create(board=board, title="test", content="test", creator=creator)
