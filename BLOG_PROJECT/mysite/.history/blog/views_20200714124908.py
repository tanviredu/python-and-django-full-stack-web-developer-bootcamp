from .models import Post
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView, ListView, DetailView, CreateView


class AboutView(TemplateView):
    template_name = "blog/about.html"


class PostListView(ListView):
    model = Post

    # customize the query

    def get_queryset(self):
        return Post.objects.order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


# in the create View we also use the mixin
# it is the same as the @login_required in the function
# based views
# and the  class based view for Create View
class CreatePostView(LoginRequiredMixin, CreateView):
    pass
