from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.account.views import UserViewSet
from apps.board.views import BoardViewSet, CommentViewSet, PostViewSet

router = DefaultRouter()
router.register('board', BoardViewSet, basename='board')
router.register('post', PostViewSet, basename='post')
router.register('comment', CommentViewSet, basename='comment')
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
