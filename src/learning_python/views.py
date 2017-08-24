from django.shortcuts import render
from django.views import View

class Home(View):
	def get(self, request, *args, **kwargs):
		template = "home.html"
		context = {"task_list": ["Create Book Model", 
		"Crud Book", "Admin", "API Book Model",\
		"account user: send mail", "post app (Viblo)",\
 		"project app (video content tutorial) ", "Regex",\
		"Multi language", "Docker, pusher, notification",\
		"Markdown - Comment", "Tag App"
		]}
		return render(request, template, context)

class Contact(View):
	def get(self, request, *args, **kwargs):
		template = "contact.html"
		context = {}
		return render(request, template, context)