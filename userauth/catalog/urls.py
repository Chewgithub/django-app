from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('createbook/', views.BookCreate.as_view(), name='createbook'),
    path('bookdetail/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('my_view/', views.my_view, name='my_view'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('profile/', views.CheckOutBookbyUserView.as_view(), name='profile'),
]