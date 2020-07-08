from django.dispatch import receiver
from django.views import generic

from blog import models as BlogModels

from constance import config


class Index(generic.ListView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_blog_post'] = BlogModels.Post.objects.order_by('-pk')[:1]
        context['config'] = config
        return context

    def get_queryset(self):
        pass
