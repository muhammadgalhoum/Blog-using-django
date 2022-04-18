from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db.models import Q
from .forms import *
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content','image']    #edited

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content','image']    #edited

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def search(request):
    if request.method == 'POST':
        search_content = request.POST['search_content']
        lookup = (Q(title__icontains=search_content) or Q(content__icontains=search_content))
        posts = Post.objects.filter(lookup)
        return render(request, 'blog/post_search_result.html', {'search_content': search_content, 'posts': posts})
    else:
        return render (request,'blog/post_search_result.html',{})


def contact(request):
    if request.method == "POST":
        form  = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            messages.warning(request,('There was an error in your form! try again...'), extra_tags='warning')
            return render(request, 'blog/contact.html')
        messages.success(request,('Thank you for contacting us'), extra_tags='success')
        return redirect('blog-home')
    return render(request, 'blog/contact.html')


def subscribe(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST or None)
        instance = form.save(commit=False)
        if Newsletter.objects.filter(email=instance.email).exists():
            messages.warning(request,('Sorry! this email is already exist'), extra_tags='warning')
            return redirect('blog-home')
        else:
            instance.save()
            messages.success(request,('Thank you for subscribing to our newsletter'), extra_tags='success')
            return redirect('blog-home')
    return render(request, 'blog-home')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


# By default Class based views search for the template at the following image of convenition
# <app>/<model>_<viewtype>.html
# blog/home_list.html