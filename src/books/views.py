from django.shortcuts import render
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
		context = super().get_context_data(**kwargs)
		return context

class BookCreateView(CreateView):
	model = Book
	fields = ['title', 'review']

class BookDetailView(DetailView):
	model = Book

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class BookUpdateView(UpdateView):
	model = Book
	fields = ['title', 'review']
	template_name_suffix = '_update_form'

class BookDeleteView(DeleteView):
	model = Book
	success_url = reverse_lazy("books:list")