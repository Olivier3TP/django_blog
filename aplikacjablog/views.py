from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from aplikacjablog.models import Post


# Create your views here.

def post_list(request):
    posts = Post.objects.all().filter(status='published')
    return render(request, 'blog/post/list.html',
                  {'posts': posts})
def post_detail(request, year, month, day, slug):
    post = get_object_or_404()



