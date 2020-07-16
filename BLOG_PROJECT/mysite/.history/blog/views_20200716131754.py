from .models import Post
from django.shortcuts import render, HttpResponsePermanentRedirect, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentForm, MyRegistrationForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# to do
# setting up the sign in page
# sign up page
# redirect to the necessary
# setting up form for sign in and sign up page


# make  asign up model
# this will be function based view
def sign_up(request):
    # import the Registration form
    form = MyRegistrationForm()
    registered = False
    if request.method == "POST":
        # fill the form
        form = MyRegistrationForm(data=request.POST)
        # validate
        if form.is_valid():
            form.save()
            registered = True

    # when the page
    fdict = {'form': form, 'registered': registered}
    return render(request, 'registration/register.html', fdict)


def login_user(request):
    form = AuthenticationForm()
    loggedin = False
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                loggedin = True
                return HttpResponsePermanentRedirect(reverse('blog:post_list'))

    return render(request, 'registration/login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponsePermanentRedirect(reverse('blog:post_list'))


# post will not be automatically publish
# until it is published so add the the publish method
# then add the publish method
# then add the comment method to add comment
# and then button to remove the comment
# thats it

# @login_required
# def post_publish(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.publish()
#     return redirect('post_detail', pk=pk)


# adding decorator

@login_required
def publish_post(request, pk):
    # fetch the post
    post = get_object_or_404(Post, pk=pk)
    # set the publish value
    post.publish()
    return HttpResponsePermanentRedirect(reverse('blog:post_list'))


class AboutView(TemplateView):
    template_name = "blog/about.html"


class PostListView(ListView):
    model = Post

    # customize the query

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


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
