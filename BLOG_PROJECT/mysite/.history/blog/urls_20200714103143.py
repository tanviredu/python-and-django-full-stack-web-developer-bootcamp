from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # home page will be the list of the post
    path('', views.PostListView.as_view(), name="post_list"),
    path('about/', views.AboutView.as_view(), name='about'),
    path('detail/', views.DetailView.as_view(), name='post_detail'),
]
