from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Flight

# Create your views here.
def index(request):
    #return render(request, "App1/index.html")
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, "App1/index.html", context)
 
def flight(request,x):
    try:
        flight = Flight.objects.get(pk=x)
    except Flight.DoesNotExist:
        raise Http404("Flight dosenot exist")
    context = {
        "flight": flight #<-above flight object is passed 
    }
    return render(request, "App1/flight.html", context)