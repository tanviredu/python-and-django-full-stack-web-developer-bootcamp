from .models import Post
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentForm, MyRegistrationForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def sign_up(request):
    form = MyRegistrationForm()
    registered = False
    if request.method == "POST":
        form = MyRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    # when the page load
    fdict = {'form': form, 'registered': registered}

    return render(request, 'blog/signup.html', fdict)


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

    # WHY ADDING THIS ?
    # IN THE MODELS WE HAVE THREE FIELD THAT CANT BE NULL AND HAVE TO
    # BE ADDED .ONE IS THE USER OBJECT BUT WE DONT GIVE USER TO SET THE AUTHOR FIELD
    # THE CURRENT USER WILL BE THE VALUE
    # SO THIS METHOD WE OVERRITE AND SET THE LOGGED USER TO THE CURRENT AUTHOR
    # OTHER WISE THESE FILED WILL BE EMPTY
    # SO WE SET THE VALUE AND THE TITLE AND TEXT WILL BE FILLED WITH USER

    def form_valid(self, form):

        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    template_name = "blog/post_form.html"
    model = Post


# same thing we will do but this time
# for all the unpublished
# so we change the queryset
class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # reverse lazy  will be done only after the post is
    # deleted successfully
    # it will wait untill it is done

    success_url = reverse_lazy('blog:post_list')
