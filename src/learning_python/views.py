from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework.views import exception_handler
from rest_framework.views import APIView
from rest_framework.reverse import reverse

from haystack.query import SearchQuerySet

from posts.api.serializers import PostListSerializer
from posts.models import Post


class Home(View):
	def get(self, request, *args, **kwargs):
		template = "home.html"
		context = {'count_space': range(7)}
		return render(request, template, context)

class Contact(View):
	def get(self, request, *args, **kwargs):
		template = "contact.html"
		context = {}
		return render(request, template, context)

class RootAPIView(APIView):
	def get(self, request, format=None):
		return Response({
				"users": reverse('users-api:list', request=request, format=format),
				"posts": reverse('posts-api:list', request=request, format=format), 
				"comments": reverse('comments-api:list', request=request, format=format),
			})

def translate(request):
	return render(request, 'contact.html', {})

def autocomplete(request):
	sqs = SearchQuerySet().autocomplete(
		content_auto=request.GET.get(
			'q',
			'')).highlight()
	s = []
	for result in sqs:
		if result.highlighted is not None:
			d = {"title": result.object.title, "slug": result.object.slug, "highlighted": result.highlighted[0], "date": result.object.timestamp}
			s.append(d)
	output = {'suggestions': s}
	response = JsonResponse(output)
	response['Access-Control-Allow-Origin'] = '*'
	return response


