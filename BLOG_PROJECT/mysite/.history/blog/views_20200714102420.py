from .models import Post
from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class AboutView(TemplateView):
    template_name = "blog/about.html"


class PostListView(ListView):
    model = Post

    # customize the query

    def get_queryset(self):
        return Post.objects.order_by('-published_date')
