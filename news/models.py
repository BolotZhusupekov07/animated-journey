from django.db import models


class News(models.Model):
    """News model."""

    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)
    no_of_votes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=250)

    def upvote(self) -> None:
        """Increments number of votes of post."""
        self.no_of_votes += 1
        self.save(update_fields=("no_of_votes",))

    def __str__(self) -> str:
        return f"Author:{self.author_name}, Title:{self.title}"


class Comment(models.Model):
    """News comment model."""

    author_name = models.CharField(max_length=250)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
