import django
from celery import shared_task
from celery.utils.log import get_task_logger

from .models import News

django.setup()

logger = get_task_logger(__name__)


@shared_task
def reset_votes() -> None:
    """
    Resets all post votes.

    Used as recurring job running once a day
    """
    news = News.objects.all()
    news.update(no_of_votes=0)
    logger.info("News votes reset!")
