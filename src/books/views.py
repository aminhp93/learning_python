from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from comments.forms import CommentForm
from comments.models import Comment
# from .forms import BookForm
from .models import Book

from django.urls import reverse_lazy
from django.views.generic import (
		ListView,
		DetailView,
		CreateView,
		UpdateView,
		DeleteView,
	)

from .models import Book

# Create your views here.
class BookListView(ListView):
	model = Book

	def get_context_data(self, **kwargs):
		context = super(BookListView, self).get_context_data(**kwargs)
		return context

class BookCreateView(CreateView):
	model = Book
	fields = ['title', 'review']

# class BookDetailView(DetailView):
# 	model = Book

# 	def get_context_data(self, *args, **kwargs):
# 		context = super().get_context_data(*args, **kwargs)
# 		context['form'] = CommentForm()
# 		return context

# 	def post(self, request, *args, **kwargs):
# 		object = self.get_object()
# 		initial_data = {
# 			"content_type": "book",
# 			"object_id": object.id
# 		}
# 		print(initial_data)
# 		form = CommentForm(request.POST or None, initial=initial_data)
# 		print(form)
# 		print(form.is_valid())
# 		print(form.errors)
# 		if form.is_valid() and request.user.is_authenticated():
# 			print("60")
# 			c_type = form.cleaned_data.get("content_type")
# 			content_type = ContentType.objects.get(model=c_type)
# 			obj_id = form.cleaned_data.get('object_id')
# 			content_data = form.cleaned_data.get("content")
# 			parent_obj = None
# 			try:
# 				parent_id = int(request.POST.get("parent_id"))
# 			except:
# 				parent_id = None
# 			if parent_id:
# 				parent_qs = Comment.objects.filter(id=parent_id)
# 				if parent_qs.exists() and parent_qs.count() == 1:
# 					parent_obj = parent_qs.first()

# 			new_comment, created = Comment.objects.get_or_create(
# 								user = request.user,
# 								content_type= content_type,
# 								object_id = obj_id,
# 								content = content_data,
# 								parent = parent_obj,
# 							)
# 			print("DONE")
# 			return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

# 		comments = object.comments
# 		context = {
# 			"title": object.title,
# 			"object": object,
# 			"comments": comments,
# 			"form":form,
# 		}
# 		return render(request, "books/book_detail.html", context)



def book_detail(request, slug=None):
	object = get_object_or_404(Book, slug=slug)

	initial_data = {
			"content_type": object.get_content_type,
			"object_id": object.id
	}
	form = CommentForm(request.POST or None, initial=initial_data)
	print(form)
	print(form.is_valid())
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


	comments = object.comments
	context = {
		"title": object.title,
		"object": object,
		"comments": comments,
		"form":form,
	}
	return render(request, "books/book_detail.html", context)

class BookUpdateView(UpdateView):
	model = Book
	fields = ['title', 'review']
	template_name_suffix = '_update_form'

class BookDeleteView(DeleteView):
	model = Book
	success_url = reverse_lazy("books:list")