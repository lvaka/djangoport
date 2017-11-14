from django import forms
from .models import Post
from .models import Project

class PostForm(forms.ModelForm):

	class Media:
		css = {
			'all' : ('style.css')
		}

	class Meta:
		model = Post
		fields = ('title', 'text')

class ProjectForm(forms.ModelForm):

	class Media:
		css = {
			'all' : ('style.css')
		}

	class Meta:
		model = Project
		fields = ('image', 'site_name', 
			'site_url', 'site_git', 'languages',)