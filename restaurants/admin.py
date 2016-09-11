from django.contrib import admin
from restaurants.models import Restaurant, Food, Town, Type

class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields': ['name','menu','restaurant_type']}),
                 ('Address',{'fields':['address','town']}),
                 ('Contact',{'fields':['phone']}),
                 ('Food',{'fields':['food']}),
                 ('Pictures',{'fields':['picture','map']}),
                 ('Cost',{'fields':['cost']})]

admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Food)
admin.site.register(Town)
admin.site.register(Type)
