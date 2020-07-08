from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=256, verbose_name="Title :")

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=256, verbose_name="Title :")
    slug = models.SlugField(max_length=256, verbose_name="Slug :")
    thumbnail = models.ImageField(upload_to='blog/thumbnail/', verbose_name="Thumbnail :")
    category = models.ManyToManyField(Category)

    def display_category(self):
        return ', '.join([cat.title for cat in self.category.all()])

    def __str__(self):
        return self.title



