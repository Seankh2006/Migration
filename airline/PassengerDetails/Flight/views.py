from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Flight2, Passenger
from django.urls import reverse

# Create your views here.
def first(request):
    return render(request, 'page.html', {'details': Flight2.objects.all()})

def second(request, flightid):
    flight = Flight2.objects.get(id = flightid)
    passengerdetails = Passenger.objects.get(id = flightid)
    passengerdetails = flight.Passenger.all()
    passengerlist = Passenger.objects.exclude(flight = flight).all()
    return render(request, 'details.html', {'flights': flight, 'd': passengerdetails, 'list': passengerlist})

def book(request, flightid):
    if request.method == "POST":
        flight = Flight2.objects.get(id = flightid)
        passengerid = int(request.POST["passenger"])
        passengerlist = Passenger.objects.get(id = passengerid)
        passengerlist.flight.add(flight)
    return HttpResponseRedirect(reverse ("flight", args=(2)))
