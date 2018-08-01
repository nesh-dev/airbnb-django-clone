from django.urls import path
from django.contrib import admin

admin.autodiscover()

from . views import (
  HouseCreate, HouseList, HouseDetail, MyHouseList, 
  HouseUpdateView, HouseDeleteView, BookingView, SearchView
)

app_name = 'house'

urlpatterns = [
    path('create/', HouseCreate.as_view(), name='create'),
    path('' , HouseList.as_view(), name='list'),
    path('my_lists/' , MyHouseList.as_view(), name='my_lists'),
    path('<slug:slug>/', HouseDetail.as_view(), name='detail'),
    path('edit/<slug:slug>', HouseUpdateView.as_view(), name='update_house'),
    path('delete/<slug:slug>', HouseDeleteView.as_view(), name='delete_house'),
    path('book/', BookingView.as_view(), name='book'),

]
