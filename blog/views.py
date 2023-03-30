from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import *
from .models import Post
from .decorators import allowed_users


def home(request):
	posts = Post.objects.all()
	return render(request, 'blog/home.html', {'posts': posts})


class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html'
  context_object_name = 'posts'
  ordering = ['-date_posted']
  paginate_by = 5


@login_required
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	comments = Comment.objects.filter(post=post).order_by("-pk")

	is_favourite = False
	if post.favourite.filter(pk=request.user.id).exists():
		is_favourite = True

	likes_connected = get_object_or_404(Post, id=pk)
	liked = False

	if likes_connected.likes.filter(id=request.user.id).exists():
		liked = True
  
	total_likes = likes_connected.total_likes()
	post_is_liked = liked

	if request.method == 'POST':
		comment_form = CommentForm(request.POST or None)
		if comment_form.is_valid():
			content = request.POST.get('content')
			comment = Comment.objects.create(post=post, user=request.user, content=content)
			comment.save()
			messages.success(request, f'Comment posted successfully!')
			return redirect(post.get_absolute_url())

	else:
		comment_form = CommentForm()

	context = {
		'post': post,
		'comments': comments,
		'is_favourite': is_favourite,
		'comment_form': comment_form,
    'total_likes': total_likes,
    'post_is_liked': post_is_liked
	}
	return render(request, 'blog/post_detail.html', context)


def postLike(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
	else:
		post.likes.add(request.user)

	return HttpResponseRedirect(reverse('post-detail', args=[int(pk)]))


class PostCreateView(LoginRequiredMixin, CreateView, SuccessMessageMixin):
  model = Post
  fields = ['title', 'content','image', 'category']
  success_message = "Your post was successfully created!"

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, SuccessMessageMixin):
  model = Post
  fields = ['title', 'content', 'image', 'category']
  success_message = "Your post was successfully updated!"

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView, SuccessMessageMixin):
  model = Post
  success_url = '/'
  success_message = "Your post has been successfully deleted!"

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False


@login_required
def favourite_post(request, id):
	post = get_object_or_404(Post, id=id)
	if post.favourite.filter(id=request.user.id).exists():
		post.favourite.remove(request.user)
	else:
		post.favourite.add(request.user)
	return HttpResponseRedirect(post.get_absolute_url())


@login_required
def favourite_posts(request):
	favourite_posts = request.user.favourite.all()
	return render(request, 'blog/favourite_posts.html', {"favourite_posts": favourite_posts})


@login_required
def delete_comment(request, id):
	comment = get_object_or_404(Comment, id=id)
	comment.delete()
	messages.success(request, f'Comment deleted successfully!')
	return redirect(comment.post.get_absolute_url())


class UserPostListView(ListView):
  model = Post
  template_name = 'blog/user_posts.html'
  context_object_name = 'posts'
  paginate_by = 5

  def get_queryset(self):
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('-date_posted')


class PostCategoryListView(ListView):
	model = Post
	template_name = 'blog/posts_by_category.html'
	paginate_by = 5

	def get_queryset(self):
		self.category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
		return Post.objects.filter(category=self.category).order_by('-date_posted')

	def get_context_data(self, **kwargs):
		context = super(PostCategoryListView, self).get_context_data(**kwargs)
		context['category'] = self.category
		return context


class CategoryDetailView(DetailView):
	model = Category


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Category
	fields = ['name']
	success_message = "Your category was successfully created!"

	def form_valid(self, form):
		form.instance.catrgory_author = self.request.user
		return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
	model = Category
	fields = ['name']
	success_message = "Your category was successfully updated!"

	def form_valid(self, form):
		form.instance.catrgory_author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		category = self.get_object()
		if self.request.user == category.catrgory_author:
			return True
		return False


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
	model = Category
	success_url = '/'
	success_message = "Your category has been successfully deleted!"

	def test_func(self):
		category = self.get_object()
		if self.request.user == category.catrgory_author:
			return True
		return False


@allowed_users(allowed_roles=['admin', 'staff'])
def show_categories(request):
	categories = Category.objects.all()
	return render(request, 'blog/categories.html', {'categories': categories})


def last_five_posts(request):
	last_five_posts = Post.objects.all().order_by('-date_posted')[:5]
	return render(request, 'blog/last_five_posts.html', {'last_five_posts': last_five_posts})


def latest_jobs(request):
	category_num = Category.objects.filter(name="Jobs").first()
	latest_jobs = Post.objects.filter(category=category_num).order_by('-date_posted')[:5]
	return render(request, 'blog/latest_jobs.html', {'latest_jobs': latest_jobs})


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
    return redirect('home')
  return render(request, 'blog/contact.html')


def subscribe(request):
  if request.method == "POST":
    form = NewsletterForm(request.POST or None)
    instance = form.save(commit=False)
    if Newsletter.objects.filter(email=instance.email).exists():
      messages.warning(request,('Sorry! this email is already exist'), extra_tags='warning')
      return redirect('home')
    else:
      instance.save()
      messages.success(request,('Thank you for subscribing to our newsletter'), extra_tags='success')
      return redirect('home')
  return render(request, 'home')


def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})

# By default Class based views search for the template like the following way of convenition
# <app>/<model>_<viewtype>.html
# blog/home_list.html