from django.contrib import admin

from .models import Flight1, Airport, Flight2, Passenger

# Register your models here.
admin.site.register(Flight1)
admin.site.register(Passenger)
admin.site.register(Airport)
admin.site.register(Flight2)
