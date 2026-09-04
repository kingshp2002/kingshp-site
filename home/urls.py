from django.urls import path
from .views import *


app_name = "home"
urlpatterns = [
    path('',index,name="index"),
    path('skills/',skills,name="skills"),
    path('contact/',contact,name="contact"),
    path('experience/',experience,name="experience"),
]
