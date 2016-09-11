from restaurants.models import Food
from django.conf.urls import url, patterns
from django.views.generic import ListView
from django.conf.urls.static import static
from django.conf import settings
from restaurants import views

urlpatterns =[
                url(r'^$',ListView.as_view(model=Food, template_name='restaurants/new.html')),
               url(r'^food/(?P<food_id>\d+)/$', views.choose_town, name = 'choose_town'),
               url(r'^food/(?P<food_id>\d+)/town/(?P<town_id>\d+)/$', views.choose_restaurant, name = 'choose_restaurant'),
               url(r'^rest/(?P<rest_id>\d+)/$', views.restaurant, name = 'restaurant'),
            ]
                       

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
