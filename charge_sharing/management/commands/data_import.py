from bs4 import BeautifulSoup
import requests
from datetime import datetime
from django.utils import timezone
from charge_sharing.models import ElectricityPrice
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import data'

    def handle(self, *args, **options):

        # pasidarome data stringo formatu, kad isatatvtume kasdien i linka
        today_date = datetime.now().strftime('%d.%m.%Y')

        url = f'https://transparency.entsoe.eu/transmission-domain/r2/dayAheadPrices/show?name=&defaultValue=false&viewType=TABLE&areaType=BZN&atch=false&dateTime.dateTime={today_date}+00:00|CET|DAY&biddingZone.values=CTY|10YLT-1001A0008Q!BZN|10YLT-1001A0008Q&resolution.values=PT60M&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)'

        html_data = requests.get(url).text
        soup = BeautifulSoup(html_data, 'html.parser')

        # >
        current_year = datetime.now().year
        current_month = datetime.now().month
        current_day = datetime.now().day
        # iteration through table rows
        for row in soup.find_all('tr'):
            columns = row.find_all('td')
            if len(columns) >= 2:
                time_range = columns[0].text.strip()
                electricity_price = float(columns[1].text.strip())

                start_time_str, end_time_str = time_range.split(' - ')
                start_time = datetime.strptime(start_time_str, '%H:%M')

                # making Django time:
                start_time = timezone.make_aware(datetime(current_year, current_month, current_day, start_time.hour), timezone.get_default_timezone())

                # Atskiriam metus, mėnesį ir dieną iš laiko
                year = start_time.year
                month = start_time.month
                day = start_time.day
                #
                # # Sukuriame ir įrašome į Django duomenų bazę
                electricity_price_record = ElectricityPrice(year=year, month=month, day=day, hour=start_time.hour, electricity_price=electricity_price)
                electricity_price_record.save()
        pass




print("Duomenys įrašyti į Django duomenų bazę.")