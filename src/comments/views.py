from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
		CreateView,
		ListView,
		DetailView,
		DeleteView,
		UpdateView
	)

from .models import Comment

# Create your views here.
# class CommentListView(ListView):
# 	model = Comment

# class CommentCreateView(CreateView):
# 	model = Comment
# 	fields = ['content']

class CommentDetailView(DetailView):
	model = Comment
	pk_url_kwarg = 'id'

	def get_context_data(self, **kwargs):
		context = super(CommentDetailView, self).get_context_data(**kwargs)
		print(context)
		return context

# class CommentUpdateView(UpdateView):
# 	model = Comment
# 	fields = ['content']
# 	template_name_suffix = '_update_form'
# 	pk_url_kwarg = 'id'

class CommentDeleteView(DeleteView):
	model = Comment
	success_url = reverse_lazy("posts:list")
