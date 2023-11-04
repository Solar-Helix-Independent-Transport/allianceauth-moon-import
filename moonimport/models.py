
from django.db import models


class Moon(models.Model):
    """
    Basic Moon Model
    """
    moon_id = models.BigIntegerField(primary_key=True)
    moon_name = models.CharField(max_length=150)
    moon_system_id = models.BigIntegerField(db_index=True)
    moon_system_name = models.CharField(max_length=150)
    moon_constellation_id = models.BigIntegerField(db_index=True)
    moon_constellation_name = models.CharField(max_length=150)
    moon_region_id = models.BigIntegerField(db_index=True)
    moon_region_name = models.CharField(max_length=150)
    moon_r_rating = models.IntegerField(db_index=True)

    class Meta:
        default_permissions = ()

    
class MoonOres(models.Model):
    """
    basic Moon Ore Model
    """
    moon_id = models.ForeignKey(Moon, on_delete=models.CASCADE)
    type_id = models.BigIntegerField(db_index=True)
    type_name = models.CharField(max_length=150)
    distribution = models.FloatField()
    volume = models.FloatField()
    portion_size = models.FloatField()
    extraction_per_hour_m3 = models.FloatField()
    units_per_hour = models.FloatField()
    
    class Meta:
        default_permissions = ()


