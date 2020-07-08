from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    title = models.CharField(max_length=256, verbose_name="Title :", unique=True, blank=False, null=False)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=256, verbose_name="Title :", unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=256, verbose_name="Slug :", unique=True, null=False, blank=False)
    thumbnail = models.ImageField(upload_to='blog/thumbnail/', verbose_name="Thumbnail :")
    publish = models.BooleanField(verbose_name="Publish :", default=True, help_text="Will this post be published?")
    category = models.ManyToManyField(Category)
    content = RichTextUploadingField()

    def display_category(self):
        return ', '.join([cat.title for cat in self.category.all()])

    def __str__(self):
        return self.title



