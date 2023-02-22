from django.contrib import admin
from .models import Flight, Airport, Flight2, Passenger

# Register your models here.
admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Flight2)
admin.site.register(Passenger)