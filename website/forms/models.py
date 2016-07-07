from __future__ import unicode_literals

from django.db import models
import datetime


#DATABASE FOR TABLE A
class AccidentIdentification(models.Model):
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    fir_no = models.CharField(max_length=30)
    police_station = models.CharField(max_length=30)
    date = models.DateField(default=datetime.date.today)       
    time = models.TimeField(default='00:00:00')
    area_type = models.CharField(max_length=30)
    accident_type = models.CharField(max_length=30)
    no_vehicles = models.IntegerField()
    no_fatalities = models.IntegerField()
    no_injured_hospitalisation = models.IntegerField()
    no_injured_not_hospitalisation = models.IntegerField()
    hit_run = models.BooleanField()
    ongoing_road_work = models.BooleanField()
    weather_type = models.CharField(max_length=30)
    collision_type = models.CharField(max_length=50)

    def __str__(self):
        #for i in range(0, )
        return str(str(self.pk) + '-' +self.state + '-' + self.district + '-' + self.fir_no + '-' + str(self.date) + '-' + str(self.time))


#DATABASE FOR TABLE B
class AccidentDetail(models.Model):
    uid = models.ForeignKey(AccidentIdentification, on_delete=models.CASCADE, default=0)
    town = models.CharField(max_length= 500)
    road_name = models.CharField(max_length= 500)
    road_type = models.CharField(max_length=100)
    road_number = models.CharField(max_length=100)
    no_lanes = models.IntegerField()
    physical_divider = models.BooleanField()
    road_surface = models.CharField(max_length=50)
    accident_spot = models.CharField(max_length=100)
    road_chainage = models.CharField(max_length=100)
    longitude = models.FloatField()
    lattitude = models.FloatField()
    #COMBINING THE FIELD OF TABLE C - Has a single attribute
    property_damage = models.CharField(max_length=100)

    def __str__(self):
        return str(self.town+ '-' + self.road_name+ '-' + str(self.lattitude)+ '-' +str(self.longitude))



#DATABASE FOR TABLE D
class VehiclesInvolved(models.Model):
    uid = models.ForeignKey(AccidentIdentification, on_delete=models.CASCADE, default=0)
    sr_no = models.IntegerField(default=0)
    type = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    disposition = models.CharField(max_length=100)
    load_condition = models.CharField(max_length=100)
    traffic_violation = models.CharField(max_length=100)
    mechanical_failure = models.BooleanField()

    def __str__(self):
        return str(str(self.sr_no) + '-' + self.type+ '-' + self.reg_no)


#DATABASE FOR TABLE E
class VictimsInvolved(models.Model):
    uid = models.ForeignKey(AccidentIdentification, on_delete=models.CASCADE, default=0)
    sr_no = models.IntegerField(default=0)
    type = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    vehicle_occupant = models.CharField(max_length=100)
    license_no = models.CharField(max_length=100)
    impacted_by = models.CharField(max_length=100)
    injury_type = models.CharField(max_length=100)
    using_safety_device = models.BooleanField()
    alcohol_drug = models.BooleanField()

    def __str__(self):
        return str(str(self.sr_no) + '-' + self.type+ '-' + self.license_no)



