from django.urls import path
from . import views
app_name='feedback'

urlpatterns = [
    path('review/', views.review_page, name='review_page'),
    path('thankyou/', views.thankyou_page, name='thankyou_page')

]