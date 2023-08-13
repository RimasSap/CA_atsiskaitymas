from django.db import models

# Create your models here.
class ElectricityPrice(models.Model):
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    hour = models.PositiveIntegerField()
    electricity_price = models.DecimalField(max_digits=10, decimal_places=2)
    earnings_per_hour = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    daily_average_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def calculate_daily_average_price(self):
        if self.daily_average_price is None:
            # receive all one day records
            daily_records = ElectricityPrice.objects.filter(year=self.year, month=self.month, day=self.day)

            # calculate day average price
            total_price = sum(record.electricity_price for record in daily_records)
            average_price = total_price / len(daily_records)

            # record in db
            self.daily_average_price = average_price
            self.save()

    def calculate_earnings(self, ivado_galingumas_kW):


        # check, if dayly_average_price already exist
        if self.daily_average_price is None:
            self.calculate_daily_average_price()

        # calculate price difference
        if self.electricity_price < self.daily_average_price:
            self.earnings_per_hour = -1 * ivado_galingumas_kW * self.electricity_price / 1000
        elif self.electricity_price > self.daily_average_price:
            self.earnings_per_hour = ivado_galingumas_kW * self.electricity_price / 1000
        else:
            self.earnings_per_hour = 0

        # Įrašome apskaičiuotą uždarbį į lauką
        self.save()

        return self.earnings_per_hour

