import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    """
    return HttpResponse("Welcome to this page")
    return render(request,'blog/index.html',context={
        'title':'Homepage of My Blog',
        'welcome':'Welcome to My Blog'
    }) 
    """

    # '-' means 'reverse=True'
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    
    """
    视图函数很简单，
    它根据我们从 URL 捕获的文章 id（
    也就是 pk，这里 pk 和 id 是等价的）
    获取数据库中文章 id 为该值的记录，然后传递给模板(Model)
    post.get_absolute_url 最终会被替换成该 post 自身的 URL。
    This function will match the id we got from URL(aka pk) with the 
    id in database, and forward to model
    """

    # get_object_or_404() will return 404 error if requested resources 
    # (in this situation is article) not exist.
    
    """
    将 Markdown 格式的文本解析成 HTML 文本非常简单，
    只需调用这个库的 markdown 方法。
    我们书写的博客文章内容存在 Post 的 body 属性里，
    回到我们的详情页视图函数，
    对 post 的 body 的值做一下解析，
    把 Markdown 文本转为 HTML 文本再传递给模板
    """
    post.body = markdown.markdown(
        post.body,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )

    return render(request,'blog/detail.html',context={'post': post})