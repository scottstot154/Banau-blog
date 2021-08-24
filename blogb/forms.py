from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author','image','description','private')

		widgets = {
			'author': forms.TextInput(attrs={'class':'form-control','value':'', 'id':'legal', 'type':'hidden'}),
			'description': forms.Textarea(attrs={'class':'form-control'}),
			
		}
