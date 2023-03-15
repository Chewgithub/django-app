from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView,FormView,CreateView, ListView, DetailView, UpdateView, DeleteView
from classroom.forms import ContactForm
from classroom.models import Teacher

# Create your views here.
# def home_view(request):
#     return render(request,"classroom/home.html")



class HomeView(TemplateView):
    template_name = "classroom/home.html"

class ThankYouView(TemplateView):
    template_name="classroom/thankyou.html"

class TeacherCreateView(CreateView):
    model = Teacher
    #model_form.html
    fields="__all__"
    success_url=reverse_lazy('classroom:thankyou')


class TeacherListView(ListView):
    #model_list.html
    model = Teacher
    queryset = Teacher.objects.order_by('last_name')
    context_object_name='teacher_list'

class TeacherDetailView(DetailView):

    #model_detail
    model = Teacher

class TeacherUpdateView(UpdateView):

    #share model_form.html
    model = Teacher
    fields = '__all__'

    success_url=reverse_lazy('classroom:listteacher')

class TeacherDeleteView(DeleteView):
    model = Teacher

    success_url=reverse_lazy('classroom:listteacher')

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # success URL? URL, not template
    success_url = reverse_lazy('classroom:thankyou') 

    # What to do with form?
    def form_valid(self, form):
        print(form.cleaned_data)
        # ContactForm(request.POST)
        return super().form_valid(form)

