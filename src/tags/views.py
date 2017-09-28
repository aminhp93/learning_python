from django.shortcuts import render
from django.shortcuts import redirect

from tags.models import Tag

def tag_list(request):
	template = "tags/tag_list.html"
	queryset = Tag.objects.all()
	context = {"tag_list": queryset}
	return render(request, template, context)

def tag_related(request, slug):
	template = "tags/tag_related.html"
	tag_instance = Tag.objects.filter(tag=slug)[0]
	if tag_instance.tag == "hango":
		if not request.user.is_superuser:
			return redirect('home')
	context = {"tag_instance": tag_instance}
	return render(request, template, context)
