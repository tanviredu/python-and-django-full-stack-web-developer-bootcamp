from .models import Post
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView


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
    # login mixin wants wo know
    # where they will prompt you for login
    # so provide a url
    login_url = '/login/'
    # after login where they will redirect
    # this variable name cant be changed
    redirect_field_name = 'blog/post_detail.html'
    # for creating you need a form
    form_class = PostForm
    template_name = "blog/post_form.html"


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    forms = PostForm
    template_name = "blog/post_form.html"
