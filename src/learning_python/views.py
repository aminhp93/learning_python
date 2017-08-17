from django.shortcuts import render
from django.views import View

class Home(View):
	def get(self, request, *args, **kwargs):
		template = "home.html"
		context = {}
		return render(request, template, context)

class Contact(View):
	def get(self, request, *args, **kwargs):
		template = "contact.html"
		context = {}
		return render(request, template, context)