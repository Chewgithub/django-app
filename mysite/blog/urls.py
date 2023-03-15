
from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.Home,name="blog-home"),
    path('about/', views.about,name="about-us"),
]