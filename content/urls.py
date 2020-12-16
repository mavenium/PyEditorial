from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('search/', views.Search.as_view(), name='search'),
    path('blog/', views.Blog.as_view(), name='blog'),
    path('blog/<int:pk>/', views.BlogArchiveByCategoryPK.as_view(), name='blog_archive_by_category_pk'),
    path('blog/<str:slug>/', views.BlogSingle.as_view(), name='blog_single'),
    path('blog/<int:pk>/<str:slug>/', views.BlogSingle.as_view(), name='blog_single'),
    path('videocast/', views.Videocast.as_view(), name='videocast'),
    path('videocast/<int:pk>/', views.VideocastArchiveByCategoryPK.as_view(), name='videocast_archive_by_category_pk'),
    path('videocast/<str:slug>/', views.VideocastSingle.as_view(), name='videocast_single'),
    path('videocast/<int:pk>/<str:slug>/', views.VideocastSingle.as_view(), name='videocast_single'),
    path('podcast/', views.Podcast.as_view(), name='podcast'),
    path('podcast/<int:pk>/', views.PodArchiveByCategoryPK.as_view(), name='podcast_archive_by_category_pk'),
    path('podcast/<str:slug>/', views.PodSingle.as_view(), name='podcast_single'),
    path('podcast/<int:pk>/<str:slug>/', views.PodSingle.as_view(), name='podcast_single'),
]
