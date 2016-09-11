from django.shortcuts import render
from restaurants.models import Food, Restaurant, Type, Town
from django.http import HttpResponse

def search(request):
    error = False
    if 'search' in request.GET:
        q = request.GET['search']
        if not q:
            error = True
        else:
            restaurants = Restaurants.ojects.filter(title__icontains=search)
            return render(request, 'choose_restaurant.html',{'rests' : restaurants, 'query':q})
    return render(request, 'new.html',{'error':error})

def choose_town(request, food_id):
    rest_list = Restaurant.objects.filter(food=food_id)
    town_list = []
    for r in rest_list:
        t = Town.objects.get(id = r.town.id)
        if t not in town_list:
            town_list.append(t)
    return render(request, 'restaurants/choose_town.html',{'food_id':food_id, 'town_list': town_list})

def choose_restaurant(request, food_id, town_id):
    rests = Restaurant.objects.filter(food__id = food_id, town__id = town_id)
    return render(request, 'restaurants/choose_restaurant.html',{'rests':rests})
        
def restaurant(request, rest_id):
    rest = Restaurant.objects.get(id = rest_id)
    return render(request, 'restaurants/restaurant.html',{'restaurant':rest})
            
    
# Create your views here.
