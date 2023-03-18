from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.index,name='my_cv'),
    path('bootstrap', views.bootstrap,name='bootstrap'),
    path('tindog', views.tindog,name='tindog'),

]