from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('search/', views.Search.as_view(), name='search'),
    path('blog/', views.Blog.as_view(), name='blog'),
    path('create/blog/', views.BlogCreateView.as_view(), name='blog_create'),
    path('create/blog_category/', views.BlogCategoryCreateView.as_view(), name='blog_category_create'),
    path('blog/<int:pk>/', views.BlogArchiveByCategoryPK.as_view(), name='blog_archive_by_category_pk'),
    path('blog/<str:slug>/', views.BlogSingle.as_view(), name='blog_single'),
    path('create/videocast_category/', views.VideocastCategoryCreateView.as_view(), name='videocast_category_create'),
    path('videocast/', views.Videocast.as_view(), name='videocast'),
    path('create/videocast/', views.VideocastCreateView.as_view(), name='videocast_create'),
    path('videocast/<int:pk>/', views.VideocastArchiveByCategoryPK.as_view(), name='videocast_archive_by_category_pk'),
    path('videocast/<str:slug>/', views.VideocastSingle.as_view(), name='videocast_single'),
    path('create/podcast_category/', views.PodcastCategoryCreateView.as_view(), name='podcast_category_create'),
    path('podcast/', views.Podcast.as_view(), name='podcast'),
    path('create/podcast/', views.PodcastCreateView.as_view(), name='podcast_create'),
    path('podcast/<int:pk>/', views.PodArchiveByCategoryPK.as_view(), name='podcast_archive_by_category_pk'),
    path('podcast/<str:slug>/', views.PodSingle.as_view(), name='podcast_single'),
    path('create/skill/', views.SkillCreateView.as_view(), name='skill_create'),
]
