from django import forms
from django.utils.text import slugify

from .models import Post


class PostForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={"id": "post_content"}), required=False)
	publish = forms.DateField(widget=forms.SelectDateWidget)
	tag = forms.CharField(required=False)

	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"draft",
			"publish",
			"tags",
			"tag",
		]

	def clean_tag(self):
		return slugify(self.cleaned_data['tag'])
