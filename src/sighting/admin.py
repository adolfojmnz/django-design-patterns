from django.contrib import admin

from .models import Origin, Location, Sighting


admin.site.register(Origin)
admin.site.register(Location)
admin.site.register(Sighting)
