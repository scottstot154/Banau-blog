import requests
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import PostForm

class HomeView(ListView):
	model = Post
	template_name = 'home.html'

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_posts.html'
	#fields = ('author','image','description','private')

def search_bar(request):
	if request.method == 'POST':
		searched = request.POST.get('searched',False)
		users = Post.objects.filter(author__username__icontains=searched, private=False)

		return render(request,'search_bar.html',{'searched':searched,'users':users})
	else:
		return render(request,'search_bar.html',{})