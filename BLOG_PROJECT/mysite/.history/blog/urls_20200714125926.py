from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # home page will be the list of the post
    path('', views.PostListView.as_view(), name="post_list"),
    path('about/', views.AboutView.as_view(), name='about'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name="post_new"),
    path('post/new/', views.CreatePostView.as_view(), name="post_new"),
    path('post/edit/<int:pk>', views.PostUpdateView.as_view(), name='post_edit'),
]
