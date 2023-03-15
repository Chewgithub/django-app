from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.urls import reverse
# Create your views here.

def review_page(request):

    # POST REQEUST --> FORM CONTENTS --> THANK YOU
    if request.method =='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            #feedback:{name of url instead of path}
            return redirect(reverse('feedback:thankyou_page'))
    # ELSE, Render form
    else:
        form = ReviewForm()
    return render(request, 'feedback/review.html', context={'form':form})



def thankyou_page(request):

    return render(request, 'feedback/thankyou.html')