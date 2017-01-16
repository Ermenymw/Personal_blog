from django.shortcuts import render
from django.views import generic

from .models import Post

# Create your views here.
class BlogView(generic.ListView):
    template_name = "blog/blog.html"

    def queryset(self):
        return Post.objects.all().order_by("-date")[:25]

class PostView(generic.DetailView):
    template_name = 'blog/post.html'
    model = Post
