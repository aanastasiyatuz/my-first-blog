from django.urls import path
from mysite.blog import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]