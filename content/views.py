from django.views import generic

from django.db.models import Q

from content import models as ContentModels

from constance import config

from .forms import SearchForm


class Base(generic.ListView):
    template_name = 'base.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs_categories'] = ContentModels.BlogCategory.objects.all()
        context['videocasts_categories'] = ContentModels.VideocastCategory.objects.all()
        context['podcast_categories'] = ContentModels.PodcastCategory.objects.all()
        context['podcasts'] = ContentModels.Podcast.objects.order_by('-pk').filter(publish=True)[:2]
        context['config'] = config
        return context

    def get_queryset(self):
        pass


class Index(Base):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_blog'] = ContentModels.Blog.objects.order_by('-pk').filter(publish=True)[:1]
        context['skills'] = ContentModels.Skill.objects.all()
        context['blogs'] = ContentModels.Blog.objects.order_by('-pk').filter(publish=True)[1:5]
        context['videocasts'] = ContentModels.Videocast.objects.order_by('-pk').filter(publish=True)[:4]
        return context


class Search(Base):
    template_name = 'search.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            context['blogs'] = ContentModels.Blog.objects.order_by('-pk').filter(Q(title__icontains=query) | Q(content__icontains=query))
            context['videocasts'] = ContentModels.Videocast.objects.order_by('-pk').filter(Q(title__icontains=query) | Q(content__icontains=query))
            context['podcasts'] = ContentModels.Podcast.objects.order_by('-pk').filter(Q(title__icontains=query) | Q(content__icontains=query))
        return context


class Blog(Base):
    template_name = 'archive.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archives'] = ContentModels.Blog.objects.all()
        return context


class BlogArchiveByCategoryPK(Base):
    template_name = 'archive.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archives'] = ContentModels.Blog.objects.filter(category=self.kwargs['pk'])
        return context


class BlogSingle(Base):
    template_name = 'single.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['single_content'] = ContentModels.Blog.objects.filter(slug=self.kwargs['slug'])
        return context


class Videocast(Base):
    template_name = 'archive.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archives'] = ContentModels.Videocast.objects.all()
        return context


class VideocastArchiveByCategoryPK(Base):
    template_name = 'archive.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archives'] = ContentModels.Videocast.objects.filter(category=self.kwargs['pk'])
        return context


class VideocastSingle(Base):
    template_name = 'single.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['single_content'] = ContentModels.Videocast.objects.filter(slug=self.kwargs['slug'])
        return context


class Podcast(Base):
    template_name = 'archive.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archives'] = ContentModels.Podcast.objects.all()
        return context


class PodArchiveByCategoryPK(Base):
    template_name = 'archive.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archives'] = ContentModels.Podcast.objects.filter(category=self.kwargs['pk'])
        return context


class PodSingle(Base):
    template_name = 'single.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['single_content'] = ContentModels.Podcast.objects.filter(slug=self.kwargs['slug'])
        return context
