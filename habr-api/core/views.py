from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

from core.tasks import parse_habr


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def post(self, request, *args, **kwargs):
        parse_habr.delay()
        return HttpResponse("PARSING STARTED")


def error404(request):
    return render(request, 'core/404.html', status=404)
