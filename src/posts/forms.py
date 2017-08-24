from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post

from codemirror import CodeMirrorTextarea

codemirror_widget = CodeMirrorTextarea(
	mode="python",
	theme="cobalt",
	config={
		'fixedGutter': True
	},
)
# document = forms.TextField(widget=codemirror_widget)


class PostForm(forms.ModelForm):
	# content = forms.CharField(widget=codemirror_widget)

	content = forms.CharField(widget=PagedownWidget(show_preview=False))
	publish = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"draft",
			"publish",
		]