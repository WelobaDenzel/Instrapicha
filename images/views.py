from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()

    return render(request,"home.html",{"images":images})

@login_required(login_url='/accounts/profile/')
def profile(request,profile_id):

    profile = Profile.objects.get(id = profile_id)

    return render(request,"profile.html",{"profile":profile})


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
