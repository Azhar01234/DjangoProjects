from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Flight, Passenger
from django.urls import reverse


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
        "flight": flight, #<-above flight object is passed 
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    }
    return render(request, "App1/flight.html", context)

def book(request, x):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=x)
    except Passenger.DoesNotExist:
        return render(request, "flights/error.http", {"message": "No Passenger."})
    except Flight.DoesNotExist:
        return render(request, "flights/error.http", {"message": "No Flight."})
    except KeyError:
        return render(request, "flight/error.html", {"message": "No selection"}) 
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(x,)))

