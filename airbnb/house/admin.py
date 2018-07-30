from django.contrib import admin
from . models import House, Booking, Review
from . forms import HouseForm


admin.site.register(House)
admin.site.register(Booking)
admin.site.register(Review)

