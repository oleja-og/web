from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

def index(request):
    return render(request, 'firstapp/home.html')

def about(request):
    return HttpResponse("<h2>about</h2>")

def contact(request):
    return HttpResponseRedirect('/about')

def products(request,productid= 1):
    category = request.GET.get('cat', '')
    output = "<h2>Продукт № {0} Категория: {1}</h2>".format(productid,category)
    return HttpResponse(output)

def users(request, id= 1, name='Oleg'):
    id = request.GET.get('id', 1)
    name = request.GET.get('name', 'Oleg')
    output = "<h2>Пользователь</h2><h3>id: {0}" \
             " Имя: {1}</h3>".format(id,name)
    return HttpResponse(output)

def details(request):
    return HttpResponsePermanentRedirect('/')

