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
    template_name = 'archive.html'
    context_object_name = 'archives'


class BlogArchiveByCategoryPK(View):
    template_name = 'archive.html'

    def get(self, request, *args, **kwargs):
        context = {
            'archives': models.Blog.objects.filter(category=self.kwargs['pk']),
        }
        return render(request, self.template_name, context)


class BlogSingle(View):
    template_name = 'single.html'

    def get(self, request, *args, **kwargs):
        context = {
            'single_content': models.Blog.objects.filter(slug=self.kwargs['slug']),
        }
        return render(request, self.template_name, context)


class VideoCast(View):
    template_name = 'archive.html'

    def get(self, request, *args, **kwargs):
        context = {
            'archives': models.VideoCast.objects.all(),
        }
        return render(request, self.template_name, context)


class VideoCastArchiveByCategoryPK(View):
    template_name = 'archive.html'

    def get(self, request, *args, **kwargs):
        context = {
            'archives': models.VideoCast.objects.filter(category=self.kwargs['pk']),
        }
        return render(request, self.template_name, context)


class VideoCastSingle(View):
    template_name = 'single.html'

    def get(self, request, *args, **kwargs):
        context = {
            'single_content': models.VideoCast.objects.filter(slug=self.kwargs['slug']),
        }
        return render(request, self.template_name, context)


class Podcast(View):
    template_name = 'archive.html'

    def get(self, request, *args, **kwargs):
        context = {
            'archives': models.Podcast.objects.all(),
        }
        return render(request, self.template_name, context)


class PodArchiveByCategoryPK(View):
    template_name = 'archive.html'

    def get(self, request, *args, **kwargs):
        context = {
            'archives': models.Podcast.objects.filter(category=self.kwargs['pk']),
        }
        return render(request, self.template_name, context)


class PodSingle(View):
    template_name = 'single.html'

    def get(self, request, *args, **kwargs):
        context = {
            'single_content': models.Podcast.objects.filter(slug=self.kwargs['slug']),
        }
        return render(request, self.template_name, context)
