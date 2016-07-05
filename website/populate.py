from django.core.management import setup_environ
from mysite import settings

setup_environ(settings)

from forms.models import RoadLocation
import csv
with('~/Downloads/accident_analysis/temp-nodes.csv') as f:
    for row in csv.reader(f):
        _, created = RoadLocation.objects.get_or_create(road_id=row[0],rlongitute=row[1],rlatitude=row[2])
print 'done'