from django.views import generic

from constance import config


class Index(generic.ListView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['config'] = config
        return context

    def get_queryset(self):
        pass
