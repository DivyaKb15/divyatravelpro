from django.shortcuts import render
from django.http import HttpResponse
from .models import place, blog


# Create your views here.
def fun(request):
    ob = place.objects.all()
    obj = blog.objects.all()
    return render(request, "index.html", {'results': ob, 'products': obj})
from django.shortcuts import render

# Create your views here.
