from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField


class BlogCategory(models.Model):
    title = models.CharField(max_length=256, verbose_name="Title :", unique=True, blank=False, null=False)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=256, verbose_name="Title :", unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=256, verbose_name="Slug :", unique=True, null=False, blank=False)
    thumbnail = models.ImageField(upload_to='content/blog/thumbnail/', verbose_name="Thumbnail :")
    publish = models.BooleanField(verbose_name="Publish :", default=True, help_text="Will this post be published?")
    category = models.ManyToManyField(BlogCategory)
    content = RichTextUploadingField()

    def display_category(self):
        return ', '.join([cat.title for cat in self.category.all()])

    def __str__(self):
        return self.title


class VideocastCategory(models.Model):
    title = models.CharField(max_length=256, verbose_name="Title :", unique=True, blank=False, null=False)

    def __str__(self):
        return self.title


class Videocast(models.Model):
    title = models.CharField(max_length=256, verbose_name="Title :", unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=256, verbose_name="Slug :", unique=True, null=False, blank=False)
    thumbnail = models.ImageField(upload_to='content/video/thumbnail/', verbose_name="Thumbnail :")
    publish = models.BooleanField(verbose_name="Publish :", default=True, help_text="Will this video be published?")
    video = models.CharField(max_length=256, verbose_name="Video link :")
    category = models.ManyToManyField(VideocastCategory)
    content = RichTextUploadingField()

    def display_category(self):
        return ', '.join([cat.title for cat in self.category.all()])

    def __str__(self):
        return self.title


class PodcastCategory(models.Model):
    title = models.CharField(max_length=256, verbose_name="Title :", unique=True, blank=False, null=False)

    def __str__(self):
        return self.title


class Podcast(models.Model):
    title = models.CharField(max_length=256, verbose_name="Title :", unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=256, verbose_name="Slug :", unique=True, null=False, blank=False)
    thumbnail = models.ImageField(upload_to='content/podcast/thumbnail/', verbose_name="Thumbnail :")
    publish = models.BooleanField(verbose_name="Publish :", default=True, help_text="Will this audio be published?")
    audio = models.FileField(upload_to='content/podcast/audio/', verbose_name="Audio :")
    category = models.ManyToManyField(PodcastCategory)
    content = RichTextUploadingField()

    def display_category(self):
        return ', '.join([cat.title for cat in self.category.all()])

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=256, verbose_name="Title :", unique=True, null=False, blank=False)
    description = models.TextField(verbose_name="Description :", null=False, blank=False)
    icon = models.CharField(max_length=30, verbose_name="Icon name :", null=False, blank=False)

    def __str__(self):
        return self.title

