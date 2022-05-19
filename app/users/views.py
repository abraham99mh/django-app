from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm

# Create your views here.
def index(request):
    return HttpResponse("Hola mundo!")

def la_dos(request):
    return HttpResponse("Hola mundo 2!")

class UserCreation(LoginRequiredMixin, View):
    def get(self, request):
        form = UserForm()
        context = {'form':form, 'cosa':'hola'}
        return render(request, 'users/user-form.html', context)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            print("FORMULARIO VALIDO")
            print(form)
            form.save()
            return redirect('index')
        else:
            print("FORM INVALIDO")
            return redirect('user_create')