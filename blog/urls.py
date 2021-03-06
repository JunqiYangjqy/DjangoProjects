from django.urls import path
from . import views

# Assign namespace to avoid NoMatchReserved error
app_name = 'blog'

# Design RESTful URL
"""
    int:pk is django URL routing match rules
    which means capture all the int numbers from user request
    and the transit it to 'pk', then to 'detail' (view) function
    Calling detail function resembles: 
    detail(request, pk=255)
"""
urlpatterns = [
    path('',views.index,name='index'),
    path('posts/<int:pk>',views.detail,name='detail'),
]