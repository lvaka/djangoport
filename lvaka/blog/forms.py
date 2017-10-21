from django import forms
from .models import Post

class PostForm(forms.ModelForm):

	class Media:
		css = {
			'all' : ('style.css')
		}

	class Meta:
		model = Post
		fields = ('title', 'text')