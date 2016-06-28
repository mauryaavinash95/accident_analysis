from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import *

# INDEX
def index(request):
    template = loader.get_template('forms/form1.html')
    context = None
    return HttpResponse(template.render(context, request))

def form2(request):
    template = loader.get_template('forms/form2.html')
    return HttpResponse(template.render(None, request))

def submit1(request):
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
        return HttpResponse("Saved into database")
    else:
        return HttpResponse("SOME ISSUE, PLEASE TRY AGAIN LATER")

def submit2(request):
    if request.method == 'POST':
        b = AccidentDetail()
        b.town = request.POST.get('town')
        b.road_name = request.POST.get('road_name')
        b.road_type = request.POST.get('road_type')
        b.road_number = request.POST.get('road_number')
        b.no_lanes = request.POST.get('no_lanes')
        b.physical_divider = request.POST.get('physical_divider')
        b.road_surface = request.POST.get('road_surface')
        b.accident_spot = request.POST.get('accident_spot')
        b.road_chainage = request.POST.get('road_chainage')
        b.latitude = request.POST.get('latitude')
        b.longitude = request.POST.get('longitude')
        b.property_damage = request.POST.get('property_damage')
        b.save()
        return HttpResponse('Save Successful... Hurray')

    else:
        return HttpResponse("SOME ISSUE, PLEASE TRY AGAIN LATER")