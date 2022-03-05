from rest_framework import serializers

from .models import Comment, News


class CommentSerializer(serializers.ModelSerializer):
    """News comment model serializer."""

    class Meta:
        model = Comment
        fields = ["news", "author_name", "content", "creation_date"]


class NewsSerializer(serializers.ModelSerializer):
    """News model serializer."""

    comments = CommentSerializer(
        many=True, source="comment_set", read_only=True
    )

    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "link",
            "creation_date",
            "no_of_votes",
            "author_name",
            "comments",
        ]
