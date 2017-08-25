from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.serializers import (
	HyperlinkedIdentityField,
	)

from books.models import Book

from books.api.serializers import BookListSerializer
from rest_framework import status


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

class RootAPIView(APIView):
	def get(self, request, format=None):
		book_api_url = "http://localhost:8000/api/books/"
		comment_api_url = "http://localhost:8000/api/comments/"
		return Response({"books": book_api_url, "comments": comment_api_url, "status":status.HTTP_201_CREATED})
