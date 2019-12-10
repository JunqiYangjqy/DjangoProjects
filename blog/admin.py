from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    """
    Self remind notes
    发布文章的过程实际上是一个 HTTP 请求过程，
    此前提到，django 将 HTTP 请求封装在 HttpRequest 对象中，
    然后将其作为第一个参数传给视图函数
    （这里我们没有看到新增文章的视图，
    因为 django admin 已经自动帮我们生成了），
    若用户登录了我们的站点，
    django 就会将这个用户实例绑定到 request.user 属性上，
    我们可以通过 request.user 取到当前请求用户，
    然后将其关联到新创建的文章即可。

    Postadmin 继承自 ModelAdmin，
    它有一个 save_model 方法，
    这个方法只有一行代码：obj.save()。
    它的作用就是将此 Modeladmin 关联注册的 model 实例
    （这里 Modeladmin 关联注册的是 Post）保存到数据库。
    这个方法接收四个参数，其中前两个，一个是 request，
    即此次的 HTTP 请求对象，第二个是 obj，
    即此次创建的关联对象的实例，
    于是通过复写此方法，
    就可以将 request.user 关联到创建的 Post 实例上，
    然后将 Post 数据再保存到数据库：
    """

    def save_model(self,request,obj,form,change):
        obj.author = request.user
        super().save_model(request,obj,form,change)

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)