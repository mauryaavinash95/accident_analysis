from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import *

# INDEX
def index(request):
    template = loader.get_template('forms/f1.html')
    context = None
    return HttpResponse(template.render(context, request))

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
        a.no_vehicles = int(request.POST.get('no_vehicles'))

        a.no_fatalities = 0
        a.no_injured_hospitalisation = 0
        a.no_injured_not_hospitalisation = 0
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

        #print a.no_vehicles
        if(a.no_vehicles > 0):
            for i in range(1, int(a.no_vehicles)):
                c = VehiclesInvolved()
                c.sr_no = i
                c.type = request.POST.get('type_'+str(i))
                c.reg_no = request.POST.get('reg_no_'+str(i))
                c.disposition = request.POST.get('disposition_'+str(i))
                c.load_condition = request.POST.get('load_condition_'+str(i))
                c.traffic_violation = request.POST.get('traffic_violation_'+str(i))
                c.mechanical_failure = request.POST.get('mechanical_failure_'+str(i))
                c.save()

        no_victims_involved = int(request.POST.get("no_victims_involved"))
        if(no_victims_involved > 0):
            for i in range(0, no_victims_involved):
                d = VictimsInvolved()
                d.sr_no = i+1
                d.type = request.POST.get('victim_type_'+str(i))
                d.sex = request.POST.get('victim_sex_'+str(i))
                d.age = int(request.POST.get('victim_age_'+str(i)))
                d.vehicle_occupant = request.POST.get('victim_vehicle_occupant_'+str(i))
                d.license_no = request.POST.get('victim_license_no_'+str(i))
                d.impacted_by = request.POST.get('victim_impacted_by_'+str(i))
                d.injury_type = request.POST.get('victim_injury_type_'+str(i))

                if(d.injury_type == 'Fatal'):
                    a.no_fatalities += 1
                elif(d.injury_type == 'Injury Needing Hospitalisation'):
                    a.no_injured_hospitalisation += 1
                elif(d.injury_type == 'Injury Not Needing Hospitalisation' or d.injury_type == 'No Injury'):
                    a.no_injured_not_hospitalisation += 1

                d.using_safety_device = request.POST.get('victim_using_safety_device_'+str(i))
                d.alcohol_drug = request.POST.get('victim_alcohol_drug_'+str(i))
                d.save()


        a.save()
        b.save()
        #c.save()
        #d.save()

        return HttpResponse("Saved into database")

    else:
        return HttpResponse("SOME ISSUE, PLEASE TRY AGAIN LATER")