import csv, pytz
import pandas as pd
from beers.models import Store
from django.utils import timezone
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        url = "https://www.vinmonopolet.no/medias/sys_master/locations/locations/h3c/h4a/8834253946910/8834253946910.csv"

        df = pd.read_csv(url, sep=';')
        
        for index, row in df.iterrows():
            try:
                store = Store.objects.get(storeid=int(row['Butikknummer']))
                store.name = row['Butikknavn']
                store.address = row['Gateadresse']
                store.zipcode = int(row['Gate_postnummer'])
                store.phone = row['Telefonnummer']
                store.category = row['Kategori']
                store.gps_lat = float(row['GPS_breddegrad'])
                store.gps_long = float(row['GPS_lengdegrad'])
                store.save()

            except Store.DoesNotExist:
                store = Store.objects.create(
                storeid = int(row['Butikknummer']),
                name = row['Butikknavn'],
                address = row['Gateadresse'],
                zipcode = int(row['Gate_postnummer']),
                phone = row['Telefonnummer'],
                category = row['Kategori'],
                gps_lat = float(row['GPS_breddegrad']),
                gps_long = float(row['GPS_lengdegrad']),
                )

        self.stdout.write(self.style.SUCCESS('Successfully updated stores from Vinmonpolet CSV'))