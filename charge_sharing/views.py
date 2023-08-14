import os
from django.shortcuts import render
from .models import ElectricityPrice
from datetime import datetime
from decimal import Decimal
import seaborn as sns
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import base64
from django.http import FileResponse
from django.conf import settings



def index(request):
    if request.method == 'POST':
        # nesusiderina decimal su float, keiciu:
        # ivado_galingumas_kW = float(request.POST.get('ivado_galingumas_kW'))
        ivado_galingumas_kW = Decimal(request.POST.get('ivado_galingumas_kW'))
        calculation_date_str = request.POST.get('calculation_date')

        try:
            calculation_date = datetime.strptime(calculation_date_str,'%Y-%m-%d').date()  # Konvertuoti į datetime.date objektą
            # Gauti visus tos dienos įrašus
            daily_records = ElectricityPrice.objects.filter(year=calculation_date.year, month=calculation_date.month, day=calculation_date.day)

            total_earnings = 0
            for record in daily_records:
                total_earnings += record.calculate_earnings(ivado_galingumas_kW)

            hourly_earnings = []
            for record in daily_records:
                hourly_earnings.append(record.calculate_earnings(ivado_galingumas_kW))

            sns.set(style="whitegrid")
            plt.figure(figsize=(10, 6))
            plt.title("Elektros kainų diagrama")
            sns.lineplot(x=range(24), y=hourly_earnings)
            plt.xlabel("Valanda")
            plt.ylabel("Uždarbis")
            plt.tight_layout()

            # Generate a unique filename for the image
            image_filename = f'price_chart_{datetime.now().strftime("%Y%m%d%H%M%S")}.png'
            # pakitimas 1 buvo:
            image_path = os.path.join(settings.MEDIA_ROOT, image_filename)
            # tapo:
            # image_path = os.path.join(settings.MEDIA_ROOT, 'charge_sharing', image_filename)
            plt.savefig(image_path)
            plt.close()




            return render(request, 'index.html', {'total_earnings': total_earnings,  'price_chart_image': image_filename})

        except ElectricityPrice.DoesNotExist:
            return render(request, 'index.html', {'error_message': 'Nėra įrašų šiai dienai'})

    return render(request, 'index.html')



