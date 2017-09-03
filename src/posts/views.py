from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
		FormView,
		ListView,
		DetailView,
		CreateView,
		UpdateView,
		DeleteView,
	)


from .models import Post
from .forms import PostForm

# Create your views here.
class PostListView(ListView):
	model = Post

	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		return context

class PostCreateView(FormView):
	template_name = 'posts/post_form.html'
	model = Post
	form_class = PostForm
	success_url = reverse_lazy("posts:list")
	# fields = ['title', 'content', 'publish', 'language']

	def form_valid(self, form):
		form.save()
		return super(PostCreateView, self).form_valid(form)


class PostDetailView(DetailView):
	model = Post

	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		print(dir(context['object']))
		return context

class PostUpdateView(UpdateView):
	template_name = 'posts/post_form.html'
	model = Post
	form_class = PostForm
	success_url = reverse_lazy("posts:list")

	def form_valid(self, form):
		form.save()
		return super(PostUpdateView, self).form_valid(form)


class PostDeleteView(DeleteView):
	model = Post
	success_url = reverse_lazy("posts:list")