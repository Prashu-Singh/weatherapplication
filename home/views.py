from django.shortcuts import render
import requests
from datetime import datetime

# Create your views here.

def home(request):
    city= request.GET.get('city','Lucknow')
    # city="Lucknow"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c7b19738f530601016afb63e6d0c77f8'
    data= requests.get(url).json()

    payload = {'city':data['name'],
                'weather':data['weather'][0]['main'],
               'icon':data['weather'][0]['icon'], 
               'kelvin_temperature':data['main']['temp'],
               'celcius_temperature':int(data['main']['temp']) - 273,
                'pressure':data['main']['pressure'],
                'humidity':data['main']['humidity'],
                'description':data['weather'][0]['description']
            }
    today = datetime.now()
    context = {'data': payload, 'today1':today}
    # print(context)
    
    return render(request,'home.html',context,)
