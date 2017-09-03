from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post

class PostForm(forms.ModelForm):
	# content = forms.CharField(widget=PagedownWidget(show_preview=False, template='posts/pagedown.html'))
	publish = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"draft",
			"publish",
			"image",
		]

		def clean_content(request, obj):
			print('clean contnet')
			print(request, obj)
