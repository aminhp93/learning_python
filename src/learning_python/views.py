from django.shortcuts import render
from django.views import View

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework.views import exception_handler
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.exceptions import (
		APIException, 
		NotFound, 
		ParseError, 
		PermissionDenied
	)

from books.api.serializers import BookListSerializer
from books.models import Book

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
		return Response({
				"books": reverse('books-api:list', request=request, format=format), 
				"comments": reverse('comments-api:list', request=request, format=format),
			})


@api_view()
def error400(request):
	raise ParseError('Bad request')

@api_view()
def error403(request):
	raise PermissionDenied('PermissionDenied')

@api_view()
def error404(request):
	raise NotFound('Not found')

@api_view()
def error500(request):
	raise APIException(detail='Server error')
