from django.urls import path

from .views import home, aboutus, family, contactus,news,stores

urlpatterns = [

    path('', home, name='home'),

    path('about', aboutus, name='aboutus'),

    path('family', family, name='family'),

    path('contactus', contactus, name='contactus'),

    path('news', news, name='news'),

    path('stores', stores, name='stores'),

]