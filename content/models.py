from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField


class BlogCategory(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _('Blog Category')
        verbose_name_plural = _('Blog Categories')

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        null=False,
        blank=False
    )
    slug = models.SlugField(
        max_length=256,
        verbose_name=_('Slug :'),
        unique=True,
        null=False,
        blank=False
    )
    thumbnail = models.ImageField(
        upload_to='content/blog/thumbnail/',
        verbose_name=_('Thumbnail :')
    )
    publish = models.BooleanField(
        verbose_name=_('Publish :'),
        default=True,
        help_text=_('Will this post be published?')
    )
    category = models.ManyToManyField(
        BlogCategory
    )
    content = RichTextUploadingField()

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def display_category(self):
        return ', '.join([cat.title for cat in self.category.all()])

    def __str__(self):
        return self.title


class VideocastCategory(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _('Video Cast Category')
        verbose_name_plural = _('Video Cast Categories')

    def __str__(self):
        return self.title


class Videocast(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        null=False,
        blank=False
    )
    slug = models.SlugField(
        max_length=256,
        verbose_name=_('Slug :'),
        unique=True,
        null=False,
        blank=False
    )
    thumbnail = models.ImageField(
        upload_to='content/video/thumbnail/',
        verbose_name=_('Thumbnail :')
    )
    publish = models.BooleanField(
        verbose_name=_('Publish :'),
        default=True,
        help_text=_('Will this video be published?')
    )
    video = models.CharField(
        max_length=256,
        verbose_name=_('Video link :')
    )
    category = models.ManyToManyField(
        VideocastCategory
    )
    content = RichTextUploadingField()

    class Meta:
        verbose_name = _('Video Cast')
        verbose_name_plural = _('Video Casts')

    def display_category(self):
        return ', '.join([cat.title for cat in self.category.all()])

    def __str__(self):
        return self.title


class PodcastCategory(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _('Podcast Category')
        verbose_name_plural = _('Podcast Categories')

    def __str__(self):
        return self.title


class Podcast(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        null=False,
        blank=False
    )
    slug = models.SlugField(
        max_length=256,
        verbose_name=_('Slug :'),
        unique=True,
        null=False,
        blank=False
    )
    thumbnail = models.ImageField(
        upload_to='content/podcast/thumbnail/',
        verbose_name=_('Thumbnail :')
    )
    publish = models.BooleanField(
        verbose_name=_('Publish :'),
        default=True,
        help_text=_('Will this audio be published?')
    )
    audio = models.FileField(
        upload_to='content/podcast/audio/',
        verbose_name=_('Audio :')
    )
    category = models.ManyToManyField(
        PodcastCategory
    )
    content = RichTextUploadingField()

    class Meta:
        verbose_name = _('Podcast')
        verbose_name_plural = _('Podcasts')

    def display_category(self):
        return ', '.join([cat.title for cat in self.category.all()])

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name=_('Description :'),
        null=False,
        blank=False
    )
    icon = models.CharField(
        max_length=30,
        verbose_name=_('Icon name :'),
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')

    def __str__(self):
        return self.title

