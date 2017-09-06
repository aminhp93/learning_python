from django.shortcuts import render

# Create your views here.
def tag_list(request):
	template = "tags/tag_list.html"
	context = {}
	return render(request, template, context)

def tag_related(request):
	template = "tags/tag_related.html"
	context = {}
	return render(request, template, context)
