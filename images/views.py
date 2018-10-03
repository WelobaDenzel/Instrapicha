from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import *
# Create your views here.
def home(request):
    images = Image.objects.all()
    
    return render(request,"home.html",{"images":images})

def search_results(request):

    if 'image' in request.GET and request.GET['image']:
        search_images = request.GET.get("image")
        searched_images = Image.search_by_category(search_images)
        message = f"{search_images}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})

def get_image_by_id(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})
