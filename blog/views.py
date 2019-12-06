from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
    #return HttpResponse("Welcome to this page")
    # return render(request,'blog/index.html',context={
    #     'title':'Homepage of My Blog',
    #     'welcome':'Welcome to My Blog'
    # })

    # '-' means 'reverse=True'
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})