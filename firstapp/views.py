from django.shortcuts import render
from django.http import *


from .models import Person


def index(request):
    people = Person.objects.all()
    return render(request, 'firstapp/index.html', {'people': people})


def create(request):
    if request.method == 'POST':
        klient = Person()
        klient.name = request.POST.get('name')
        klient.age = request.POST.get('age')
        klient.save()
    return HttpResponseRedirect('/')


def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == 'POST':
            person.name = request.POST.get('name')
            person.age = request.POST.get('age')
            person.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'firstapp/edit.html', {'person': person})
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Клиент не найден</h2>')


def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect('/')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Клиент не найден</h2>')
