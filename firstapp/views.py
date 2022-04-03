from django.shortcuts import render
from django.http import *
from django.template.response import TemplateResponse
from .forms import UserForm, UserForm1

def index_app1(request):
    if request.method == "POST":
        userform1 = UserForm1(request.POST)
        if userform1.is_valid():
            name = userform1.cleaned_data["name"]
            return HttpResponse('<h2>True - {0}</h2>'.format(name))
        else:
            return HttpResponse('False')
    else:
        userform1 = UserForm1
        return render(request, 'firstapp/index_app1.html',{'form1':userform1})

def index(request):
    userform = UserForm()
    return render(request, 'firstapp/index.html', {'form': userform})

def home(request):
    return render(request, 'firstapp/home.html')

def about(request):
    return HttpResponse("<h2>about</h2>")

def contact(request):
    cat = ['Ноутбуки','Принтеры','Диски','Шнуры']
    return render(request, 'firstapp/contact.html',context={'cat': cat})

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

