from django.shortcuts import render
from django.views.generic import TemplateView

from core.habr import parse


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        parse()
        return self.render_to_response(context)


def error404(request):
    return render(request, 'core/404.html', status=404)
