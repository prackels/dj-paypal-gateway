from django.shortcuts import render
from .models import *
def products(request,id):
    product = Product.objects.get(id= id)
    return render(request, 'product.html', {'product':product})