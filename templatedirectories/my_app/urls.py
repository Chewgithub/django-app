from django.urls import path
from . import views

# register the app namespace
app_name="my_app" #special variable ("app_name") django look for in urls.py 

urlpatterns = [
    path('', views.example_view,name="example"),
    path('variable/', views.variable_view, name="variable"),
]