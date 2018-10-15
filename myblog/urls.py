from django.urls import path
from .views import stub_view
from .views import list_view
from myapp.feeds import DreamrealCommentsFeed
from django.conf.urls import patterns, url


urlpatterns = [
    path('',stub_view,name = "blog_index"),
    path('posts/', stub_view, name="blog_detail"),
    path('',list_view,name ="blog_index"),
    url(r'^latest/comments/', DreamrealCommentsFeed()),
    url(r'^comment/(?P\w+)/', 'comment', name='comment'),
]