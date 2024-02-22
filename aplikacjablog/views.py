from django.shortcuts import render

from aplikacjablog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return 'test 123'
   # return render(request,'')