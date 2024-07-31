from django.shortcuts import render
import urllib.request
import json

def home(request):
    data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            try:
                api_key = '971671e92d424632abc185630243107'
                source = urllib.request.urlopen(f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}').read()
                list = json.loads(source)
                data = {
                    "city": city,
                    "country_code": str(list['location']['country']),
                    "temp": str(list['current']['temp_c']) + ' °C',
                    "humidity": str(list['current']['humidity']),
                    "description": str(list['current']['condition']['text']),
                    "icon": list['current']['condition']['icon'],
                }
            except:
                data = {"error": "City not found."}
    return render(request, 'index.html', {'data': data})
