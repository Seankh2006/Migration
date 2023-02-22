from django.shortcuts import render
from .models import Airport, Flight

# Create your views here.
def index(request):
    return render(request, "index.html")

def Airport(request):
    
    return render(request, "index.html", {'Fli': Flight.objects.all()})

def Flight2(request, flight_id):
    return render(request, "index.html", {'flight_id': Flight.objects.get(id = flight_id)})

def flightdetails(request, flight_id):
    return render(request, "flightdetails.html", {'flight_id': Flight.objects.get(id = flight_id)})
