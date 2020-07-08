from django.contrib import admin

from . import models


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_category']
    models.Post.display_category.short_description = 'Categories'
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Post, PostAdmin)

admin.site.register(models.Category)
