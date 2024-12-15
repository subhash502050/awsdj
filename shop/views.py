import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.request import Request

from shop.forms import ArticlesForm, CustomerForm
from shop.models import Article, Customers


# Create your views here.

def shop_home(request):
    id = request.GET.get("id",1)
    art_id = int(id)
    try:
        articles = Article.objects.all()[art_id:art_id+1]
        customers = Customers.objects.all()[:3]
    except:
        return render(request,'404.html')
    return render(request, 'index.html',{"customers":customers,"articles":articles})


def shop_cart(request):
    forms = CustomerForm()
    if request.method == "POST": 
        name = request.POST.get('name')
        email = request.POST.get('email')
        a = request.POST.get('age')
        age = int(a)
        customer = Customers(name=name, email=email, age=age)
        customer.save()
        return redirect('/')
    else:
        return render(request, 'cart.html',{"form":forms})


def upload(request):
    if request.method == "POST":
        fr = ArticlesForm(request.POST,request.FILES)
        if fr.is_valid():
            fr.save()
            return HttpResponseRedirect("/")

    form = ArticlesForm()
    return render(request,"upload.html",{"form":form})


def upload_data(request):
    data = request.GET.get("id")
    id = int(data)
    try:
        article = Article.objects.get(id=id)
    except:
        return render(request,"404.html")
        print(article)
    return render(request,"details.html",{"article":article})