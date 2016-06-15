from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *

# INDEX
def index(request):
    template = loader.get_template('forms/index.html')
    context = None
    return HttpResponse(template.render(context, request))

def submit(request):
    if request.method == 'POST':
        a = AccidentIdentification()
        a.state = request.POST.get('state')
        a.district = request.POST.get('district')
        a.fir_no = request.POST.get('fir_no')
        a.police_station = request.POST.get('police_station')
        a.date_time = request.POST.get('date_time')
        a.area_type = request.POST.get('area_type')
        a.accident_type = request.POST.get('accident_type')
        a.no_vehicles = request.POST.get('no_vehicles')
        a.no_fatalities = request.POST.get('no_fatalities')
        a.no_injured_hospitalisation = request.POST.get('no_injured_hospitalisation')
        a.no_injured_not_hospitalisation = request.POST.get('no_injured_not_hospitalisation')
        a.hit_run = request.POST.get('hit_run')
        a.ongoing_road_work = request.POST.get('ongoing_road_work')
        a.weather_type = request.POST.get('weather_type')
        a.collision_type = request.POST.get('collision_type')
        a.save()
        return HttpResponse("SAVE SUCCESSFUL")
    else:
        return HttpResponse("SOME ISSUE, PLEASE TRY AGAIN LATER")