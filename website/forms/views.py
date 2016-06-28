from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import *

# INDEX
def index(request):
    template = loader.get_template('forms/f1.html')
    context = None
    return HttpResponse(template.render(context, request))

def f2(request):
    template = loader.get_template('forms/form2.html')
    return HttpResponse(template.render(None, request))

def submit_f1(request):
    if request.method == 'POST':
        a = AccidentIdentification()
        a.state = request.POST.get('state')
        a.district = request.POST.get('district')
        a.fir_no = request.POST.get('fir_no')
        a.police_station = request.POST.get('police_station')
        a.date = request.POST.get('date')
        a.time = request.POST.get('time')
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
        #a.save()
		
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
        b.lattitude = request.POST.get('lattitude')
        b.longitude = request.POST.get('longitude')
        b.property_damage = request.POST.get('property_damage')
        #b.save()

        c = VehiclesInvolved()
        c.sr_no = request.POST.get('sr_no')
        c.type = request.POST.get('type')
        c.reg_no = request.POST.get('reg_no')
        c.disposition = request.POST.get('disposition')
        c.load_condition = request.POST.get('load_condition')
        c.traffic_violation = request.POST.get('traffic_violation')
        c.mechanical_failure = request.POST.get('mechanical_failure')
        #c.save()

        d = VictimsInvolved()
        d.sr_no = request.POST.get('victim_sr_no')
        d.type = request.POST.get('victim_type')
        d.sex = request.POST.get('victim_sex')
        d.age = request.POST.get('victim_age')
        d.vehicle_occupant = request.POST.get('victim_vehicle_occupant')
        d.license_no = request.POST.get('victim_license_no')
        d.impacted_by = request.POST.get('victim_impacted_by')
        d.injury_type = request.POST.get('injury_type')
        d.using_safety_device = request.POST.get('victim_using_safety_device')
        d.alcohol_drug = request.POST.get('victim_alcohol_drug')
        
		
        a.save()
        b.save()
        c.save()
        d.save()

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