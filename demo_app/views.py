from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from .models import *



def index(request):
    # return HttpResponse("Hello, world. This is your first Django")
    cats_list = Cat.objects.all()
    from django.template import loader
    template = loader.get_template('demo_app/index.html')
    context = {
        'cats_list': cats_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    try:
        cat = Cat.objects.get(id = id)
    except Cat.DoesNotExist:
        raise Http404("Cat does not exist")
    return render(request, 'demo_app/detail.html',{'cat':cat})


def add(request):
    if request.method == 'GET':
        return render(request, 'demo_app/add.html',{})
    else:
        name = request.get['name']
        age = int(request.get['age'])
        cat = Cat(name=name, age=age)
        cat.save()
        cats_list = Cat.objects.all()
        return render(request,'demo_app/index.html',{'cats_list':cats_list})



def hello_country(request, country_name):
    return HttpResponse("Hello,%s" % country_name)