from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index,name='my_cv'),
    path('bootstrap', views.bootstrap,name='bootstrap'),
    path('tindog', views.tindog,name='tindog'),
    path('dom', views.dom,name='dom'),
    path('dice', views.dice,name='dice'),
    path('drumroll', views.drumroll,name='drumroll'),
    path('jquery', views.jquery,name='jquery'),
    path('simon', views.simon,name='simon'),

]