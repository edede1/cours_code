import pytz
from datetime import datetime

t = datetime(2023, 7, 7, 10, 30)  

timezone_douala = pytz.timezone('Africa/Douala')
timezone_paris = pytz.timezone('Europe/Paris')
timezone_jerusalem = pytz.timezone('Asia/Jerusalem')

heure_douala = t.astimezone(timezone_douala)
heure_paris = t.astimezone(timezone_paris)
heure_jerusalem = t.astimezone(timezone_jerusalem)


print("Heure à Douala :", heure_douala.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
print("Heure à Paris :", heure_paris.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
print("Heure à Jerusalem :", heure_jerusalem.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
