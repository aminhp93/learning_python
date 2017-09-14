try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass

from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import (
	FormView,
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
)

from comments.models import Comment
from comments.forms import CommentForm
from .models import Post
from .forms import PostForm
from tags.models import Tag

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

	def dispatch(self, request, *args, **kwargs):
		if not self.request.user.is_authenticated:
			raise Http404
		return super(PostCreateView, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		# self.object = form.save(commit=False)
		# if form.cleaned_data["tag"]:
		# 	new_tag = Tag.objects.create(tag=form.cleaned_data["tag"])
		# 	post.tags.append(new_tag)
		# 	post.save()
		return super(PostCreateView, self).form_valid(form)

class PostDetailView(DetailView):
	model = Post

	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		print(dir(context['object']))
		return context

def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	# if instance.publish > timezone.now().date() or instance.draft:
		# if not request.user.is_staff or not request.user.is_superuser:
			# raise Http404
	# share_string = quote_plus(instance.content)

	initial_data = {
			"content_type": instance.get_content_type,
			"object_id": instance.id
	}
	form = CommentForm(request.POST or None, initial=initial_data)
	if form.is_valid() and request.user.is_authenticated():
		c_type = form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = form.cleaned_data.get('object_id')
		content_data = form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()


		new_comment, created = Comment.objects.get_or_create(
							user = request.user,
							content_type= content_type,
							object_id = obj_id,
							content = content_data,
							parent = parent_obj,
						)
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

	comments = instance.comments
	context = {
		"title": instance.title,
		"object": instance,
		# "share_string": share_string,
		"comments": comments,
		"comment_form":form,
	}
	return render(request, "posts/post_detail.html", context)

class PostUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'posts/post_form.html'
	model = Post
	form_class = PostForm
	success_url = reverse_lazy("posts:list")

	def dispatch(self, request, *args, **kwargs):
		instance = self.get_object()
		if instance.user != self.request.user:
			raise Http404
		return super(PostUpdateView, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		form.save()
		return super(PostUpdateView, self).form_valid(form)


class PostDeleteView(DeleteView):
	model = Post
	success_url = reverse_lazy("posts:list")

	def dispatch(self, request, *args, **kwargs):
		instance = self.get_object()
		if instance.user != self.request.user:
			raise Http404
		return super(PostDeleteView, self).dispatch(request, *args, **kwargs)