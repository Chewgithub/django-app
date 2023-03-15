from django.urls import path
from .views import HomeView,ThankYouView,ContactFormView,TeacherCreateView,TeacherListView,TeacherDetailView,TeacherUpdateView,TeacherDeleteView

app_name='classroom'


urlpatterns = [
    path('', HomeView.as_view(),name='home'), #path expect function
    path('thankyou/', ThankYouView.as_view(),name='thankyou'),
    path('contact/', ContactFormView.as_view(),name='contact'),
    path('teacher/', TeacherCreateView.as_view(),name='teacher'),
    path('listteacher/', TeacherListView.as_view(),name='listteacher'),
    path('detailteacher/<int:pk>', TeacherDetailView.as_view(),name='detailteacher'),
    path('updateteacher/<int:pk>', TeacherUpdateView.as_view(),name='updateteacher'),
    path('deleteteacher/<int:pk>', TeacherDeleteView.as_view(),name='deleteteacher'),
    ]