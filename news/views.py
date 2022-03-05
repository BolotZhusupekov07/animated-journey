from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Comment, News
from .serializers import CommentSerializer, NewsSerializer


class NewsViewSet(ModelViewSet):
    """News model viewset."""

    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(methods=["patch"], detail=True)
    def upvote(self, request, pk):
        """Extra action to upvote post."""
        news = self.get_object()
        news.upvote()
        serializer = self.serializer_class(news)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class CommentViewSet(ModelViewSet):
    """News comment model viewset."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter]
    search_fields = ["news__id"]
