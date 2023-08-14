
from datetime import datetime

current_date = datetime.now().strftime('%d.%m.%Y')
today_date = datetime.now()
# html_data = requests.get('https://transparency.entsoe.eu/transmission-domain/r2/dayAheadPrices/show?name=&defaultValue=false&viewType=TABLE&areaType=BZN&atch=false&dateTime.dateTime=01.08.2023+00:00|CET|DAY&biddingZone.values=CTY|10YLT-1001A0008Q!BZN|10YLT-1001A0008Q&resolution.values=PT60M&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)').text
html_data = f'https://transparency.entsoe.eu/transmission-domain/r2/dayAheadPrices/show?name=&defaultValue=false&viewType=TABLE&areaType=BZN&atch=false&dateTime.dateTime={current_date}+00:00|CET|DAY&biddingZone.values=CTY|10YLT-1001A0008Q!BZN|10YLT-1001A0008Q&resolution.values=PT60M&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)'


print(html_data )
print(int(today_date.year), type(int(today_date.year)))
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)