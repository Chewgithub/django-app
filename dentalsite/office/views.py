from django.shortcuts import render
from . import models

def patientview(request):
    context={'patients':models.Patient.objects.all()}
    return render(request,'office/list.html',context=context)