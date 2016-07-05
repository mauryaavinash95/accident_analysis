from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(AccidentIdentification)
admin.site.register(AccidentDetail)
admin.site.register(VehiclesInvolved)
admin.site.register(VictimsInvolved)
admin.site.register(RoadLocation)