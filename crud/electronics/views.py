from django.shortcuts import render,HttpResponseRedirect
from .models import Product
from .forms import ProductForm

# Create your views here.

def home(request):
    if request.method == "POST":
        fm = ProductForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = ProductForm()
    else:
        fm = ProductForm()

    prod = Product.objects.all()
    
    return render(request, 'electronics/home.html', {'prod':prod, "form": fm})

def update_data(request, id):
    if request.method =="POST":
        pi = Product.objects.gets(pk=id)
        fm = ProductForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Product.objects.get(pk=id)
        fm = ProductForm(instance=pi)
    return render(request, 'electronics/update.html',{'form': fm})

def delete_data(request, id):
    if request.method == "POST":
        pi = Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")


