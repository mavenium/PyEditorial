from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('blog/', views.Blog.as_view(), name='blog'),
]
