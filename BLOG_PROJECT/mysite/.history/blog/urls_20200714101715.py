from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
]
