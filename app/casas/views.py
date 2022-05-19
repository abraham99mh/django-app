from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import HouseForm
from .models import House

# Create your views here.


def index(request):
    return HttpResponse("Casa guardada")


class HouseCreation(LoginRequiredMixin, View):
    def get(self, request):
        form = HouseForm()
        context = {'form': form, 'cosa': 'hola'}
        return render(request, 'casas/casas-form.html', context)

    def post(self, request):
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            print("FORMULARIO VALIDO")
            form.save()
            return redirect('index')
        else:
            print("FORM INVALIDO")
            return redirect('house_create')


class CasasList(LoginRequiredMixin, View):
    def get(self, request):
        context = {'casas': House.objects.all()}
        return render(request, 'casas/casas-list.html', context)


class CasasUpdate(LoginRequiredMixin, View):
    def get(self, request, nombre):
        house = House.objects.get(nombre=nombre)

        form = HouseForm(instance=house)
        context = {'form': form}
        return render(request, 'casas/casas-form.html', context)

    def post(self, request, nombre):
        house = House.objects.get(nombre=nombre)
        form = HouseForm(request.POST, request.FILES, instance=house)
        if form.is_valid():
            print("FORMULARIO VALIDO")
            form.save()
            return redirect('house_list')
        else:
            print("FORM INVALIDO")
            return redirect('house_list')
