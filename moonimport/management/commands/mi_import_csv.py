import csv
import json

from django.core.management.base import BaseCommand
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from tqdm import tqdm

from ...models import Moon, MoonOres


class Command(BaseCommand):
    help = 'Import Moon CSV'
    
    def add_arguments(self, parser):
        parser.add_argument("-t", type=int)

    def handle(self, *args, **options):
        total_lines = options.get("t", 225080)
        with open('moon_scans.csv') as csvfile:
            reader = list(csv.DictReader(csvfile))
            print(f"Clear tables {Moon.objects.all().delete()}")
            print("Load data")
            with tqdm(total=total_lines, unit=" Moons") as t:
                for row in reader:
                    if len(row["moon_dist_ore"]) > 5:
                        _m = Moon.objects.create(
                            moon_id = int(row["moon_id"]),
                            moon_name = row["moon_name"],
                            moon_system_id = int(row["moon_system_id"]),
                            moon_system_name = row["moon_system_name"],
                            moon_constellation_id = int(row["moon_constellation_id"]),
                            moon_constellation_name = row["moon_constellation_name"],
                            moon_region_id = int(row["moon_region_id"]),
                            moon_region_name = row["moon_region_name"],
                            moon_r_rating = int(row["moon_r_rating"])
                        )
                        
                        dist = json.loads(row["moon_dist_ore"])
                        for _d in dist.values():
                            _mo = MoonOres.objects.create(
                                moon_id_id = int(row["moon_id"]),
                                type_id = _d["type_id"],
                                type_name = _d["name"],
                                distribution = _d["distribution"],
                                volume = _d["volume"],
                                portion_size = _d["portionSize"],
                                extraction_per_hour_m3 = _d["extraction_per_hour_m3"],
                                units_per_hour = _d["units_per_hour"]
                            )

                    else:
                        pass
                        #print(f"No Data {row['moon_region_name']} {row['moon_constellation_name']} {row['moon_system_name']} {row['moon_name']}")
                    t.update(1)

