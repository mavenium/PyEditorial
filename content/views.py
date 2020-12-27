from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views import generic, View
from django.db.models import Q

from . import models
from .forms import SearchForm


class Index(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'last_blog': models.Blog.objects.order_by('-pk').filter(publish=True)[:1],
            'skills': models.Skill.objects.all(),
            'blogs': models.Blog.objects.order_by('-pk').filter(publish=True)[1:5],
            'video_casts': models.VideoCast.objects.order_by('-pk').filter(publish=True)[:4]
        }
        return render(request, self.template_name, context)


class Search(View):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            print('valid')
            query = form.cleaned_data['query']
            context = {
                'blogs': models.Blog.objects.order_by('-pk').filter(
                    Q(title__icontains=query) | Q(content__icontains=query)
                ),
                'videocasts': models.VideoCast.objects.order_by('-pk').filter(
                    Q(title__icontains=query) | Q(content__icontains=query)
                ),
                'podcasts': models.Podcast.objects.order_by('-pk').filter(
                    Q(title__icontains=query) | Q(content__icontains=query)
                )
            }
        else:
            return redirect('content:index')
        return render(request, self.template_name, context)


class Blog(generic.ListView):
    model = models.Blog
    template_name = 'blog_archive.html'


class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = models.Blog
    fields = '__all__'
    success_message = 'Blog was created successfully'
    success_url = '/create/blog/'


class BlogArchiveByCategoryPK(generic.ListView):
    model = models.Blog
    template_name = 'blog_archive.html'

    def get_queryset(self):
        return self.model.objects.filter(category=self.kwargs['pk'])


class BlogSingle(generic.DetailView):
    model = models.Blog
    template_name = 'single.html'

    def get_queryset(self):
        return self.model.objects.filter(slug=self.kwargs['slug'])


class VideoCast(generic.ListView):
    model = models.VideoCast
    template_name = 'video_cast_archive.html'


class VideoCastArchiveByCategoryPK(generic.ListView):
    model = models.VideoCast
    template_name = 'video_cast_archive.html'

    def get_queryset(self):
        return self.model.objects.filter(category=self.kwargs['pk'])


class VideoCastSingle(generic.DetailView):
    model = models.VideoCast
    template_name = 'single.html'

    def get_queryset(self):
        return self.model.objects.filter(slug=self.kwargs['slug'])


class Podcast(generic.ListView):
    model = models.Podcast
    template_name = 'podcast_archive.html'


class PodArchiveByCategoryPK(generic.ListView):
    model = models.Podcast
    template_name = 'podcast_archive.html'

    def get_queryset(self):
        return self.model.objects.filter(category=self.kwargs['pk'])


class PodSingle(generic.DetailView):
    model = models.Podcast
    template_name = 'single.html'

    def get_queryset(self):
        return self.model.objects.filter(slug=self.kwargs['slug'])
