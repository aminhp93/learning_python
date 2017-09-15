from django import forms

from .models import Post

class PostForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={"id": "post_content"}))
	publish = forms.DateField(widget=forms.SelectDateWidget)
	tag = forms.CharField(required=False)
	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"draft",
			"publish",
			"image",
			"tags",
			"tag",
		]

		def clean_content(request, obj):
			print('clean contnet')
			print(request, obj)
