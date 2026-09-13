from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.index, name="index"),
    path('skills/', views.skills, name="skills"),
    path('contact/', views.contact, name="contact"),
    path('experience/', views.experience, name="experience"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio/<int:id>/', views.portfolio_detail, name="portfolio_detail"),
]
