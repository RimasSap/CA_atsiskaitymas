Title: Electricity purchase - sale calculator
Problem: Electricity prices are different during the day and often depend on the effect of the environment - presence of wind or sun light.

Solving: Various high-capacity batteries (household, electric car) can be used to equalize electricity demand and prices, i.e. using batteries, electricity can be bought and stored by household consumers when it is cheap and sold when it is expensive.

Description: the project offers a simple calculator that uses electricity prices on the stock exchange and calculates the profit a household consumer would receive when buying cheap energy and selling expensive energy. In the calculator, you can choose to enter the power of the electricity input in kilowatts and receive a daily profit.

Installation:

    pip install django
    Download zipped project
    pip install -r requirements.txt
    transfer files to the newly created Django project
    python manage.py makemigrations
    python manage.py migrate
    python manage.py data_import
    python manage.py runserver
    Go to: http://127.0.0.1:8000/charge_sharing/


# CA_atsiskaitymas
