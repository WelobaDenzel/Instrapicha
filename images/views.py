from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import *
# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request,"home.html",{"images":images})
