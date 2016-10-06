from django.shortcuts import render
from django.views.generic import TemplateView

from core.tasks import parse_habr


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def post(self, request, *args, **kwargs):
        parse_habr.delay()


def error404(request):
    return render(request, 'core/404.html', status=404)
