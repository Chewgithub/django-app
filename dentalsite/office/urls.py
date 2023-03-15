from django.urls import path
from . import views

urlpatterns = [
    path('', views.patientview,name="listofpatient")
]
