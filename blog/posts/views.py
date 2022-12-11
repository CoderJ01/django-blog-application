from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts}) # dynamically retrieve objects from posts

def post(request, pk): # id of the post will be passed to the function
    posts = Post.objects.get(id=pk), # get id of post
    return render(request, 'posts.html', {'posts': posts}) 