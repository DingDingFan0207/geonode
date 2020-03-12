import json
import decimal
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Polygon


class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Polygon):
            return {
                '__type__':'__polygon__',
                'ewkt': obj.ewkt
            }
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        
        return json.JSONEncoder.default(self, obj)


def my_decoder(obj):
    if '__type__' in obj:
        if obj['__type__'] == '__polygon__':
            return GEOSGeometry.from_ewkt(obj)
    return obj

# Encoder function
def my_dumps(obj):
    return json.dumps(obj, cls=MyEncoder)

# Decoder funtion
def my_loads(obj):
    return json.loads(obj, object_hook=my_decoder)