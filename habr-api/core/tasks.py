from celery import shared_task

from core.habr import parse


@shared_task(name='parse_habr')
def parse_habr():
    parse()