from django.views import generic

from content import models as ContentModels

from constance import config


class Index(generic.ListView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_blog_post'] = ContentModels.Blog.objects.order_by('-pk').filter(publish=True)[:1]
        context['blog_posts'] = ContentModels.Blog.objects.order_by('-pk').filter(publish=True)[1:5]
        context['config'] = config
        return context

    def get_queryset(self):
        pass
