from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.order_by('created_date')
	print(posts)
	return render(request, 'microblog/post_list.html', {"posts" : posts})
