from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.blog, name='blog'),
    path('logout/', views.logout_view, name='logout'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<slug:slug>/edit/',views.post_edit,name='post_edit'),
    path('post/<slug:slug>/',views.post_detail,name='post_detail'),
    path('post/<slug:slug>/delete/',views.post_delete,name='post_delete'),
]