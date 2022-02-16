from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from django.views.generic import DeleteView, DetailView



def about(request):
    appid = '0b80fcc0703f18d00f2190f49cdcdd27'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0b80fcc0703f18d00f2190f49cdcdd27&lang=ru'

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()


    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'id': city.id,
            'city': city.name,
            'temp': res["main"]["temp"],
            'wind': res["wind"]["speed"],
            'humidity': res["main"]["humidity"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}


    return render(request, 'main/about.html', context)

def delete(request, id):
    model = City
    try:
        person = model.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/about")
    except model.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def contacts(request):
    return render(request, 'main/contacts.html')

def faq(request):
    return render(request, 'main/faq.html')

def index(request):
    return render(request, 'main/index.html')





