from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
		ListView,
		DetailView,
		CreateView,
		UpdateView,
		DeleteView,
	)


from .models import Post

# Create your views here.
class PostListView(ListView):
	model = Post

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class PostCreateView(CreateView):
	model = Post
	fields = ['title', 'content', 'publish', 'language']

class PostDetailView(DetailView):
	model = Post

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print(dir(context['object']))
		return context

class PostUpdateView(UpdateView):
	model = Post
	fields = ['title', 'content', 'language']
	template_name_suffix = '_update_form'

class PostDeleteView(DeleteView):
	model = Post
	success_url = reverse_lazy("posts:list")