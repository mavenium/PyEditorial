from django.contrib import admin

from . import models


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_category']
    models.Blog.display_category.short_description = 'Categories'
    prepopulated_fields = {'slug': ('title',)}


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_category']
    models.Videocast.display_category.short_description = 'Categories'
    prepopulated_fields = {'slug': ('title',)}


class PodcastAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_category']
    models.Podcast.display_category.short_description = 'Categories'
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Blog, PostAdmin)

admin.site.register(models.BlogCategory)

admin.site.register(models.Videocast, VideoAdmin)

admin.site.register(models.VideocastCategory)

admin.site.register(models.Podcast, PodcastAdmin)

admin.site.register(models.PodcastCategory)

admin.site.register(models.Skill)
