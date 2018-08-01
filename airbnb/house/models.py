from django.db import models
from django.conf import settings
from django.urls import reverse 
from django.template.defaultfilters import slugify

from . utils import get_unique_slug

# Create your models here.

TYPES = (
        ('APPARTMENTS', 'APPARTMENTS'), 
        ('STUDIO', 'STUDIO'), 
        ('CABIN', 'CABIN'),
        ('BUNGALOW', 'BUNGALOW'), 
        ('EARTHHOUSE', 'EARTHHOUSE'),
)

SPACES = (

        ('KITHCHEN', 'KITHCHEN'),
        ('LAUNDRY', 'KITHCHEN'),
        ('POOL', 'POOL'),
        ('GYM', 'GYM'),
        ('PARKING', 'PARKING'), 

)
def upload_location(instance, filename):
	filebase, extension = filename.split(".")
	return "%s/%s.%s" %(instance.id, instance.id, extension)

class House(models.Model):
        adtitle =  models.CharField(max_length=253)
        slug = models.SlugField(unique=True, max_length=253, blank=True)
        owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        location = models.CharField(max_length = 50)
        description =models.TextField(null=True, blank=True)
        house_type = models.CharField(max_length = 50, choices=TYPES ) 
        no_beds = models.IntegerField(default=0)
        no_bedrooms = models.IntegerField(default=0)
        no_baths = models.IntegerField(default =0) 
        price = models.PositiveIntegerField(default = 0, null=True, blank=True)
        images = models.ImageField(upload_to=upload_location, null=True, blank=True)
        wifi = models.BooleanField(default= False)
        essential = models.BooleanField(default= False)
        shampoo = models.BooleanField(default= False)
        closet = models.BooleanField(default= False)
        tv = models.BooleanField(default= False)
        smoke_detector = models.BooleanField(default= False)
        first_aid = models.BooleanField(default= False)
        fire_extinguisher = models.BooleanField(default= False)
        kitchen = models.BooleanField(default= False)
        laundry = models.BooleanField(default= False)
        pool = models.BooleanField(default= False)
        gym = models.BooleanField(default= False)
        parking = models.BooleanField(default= False)
        pub_date = models.DateTimeField(auto_now_add=True)
        mod_date = models.DateTimeField(auto_now=True)
        

        objects = models.Manager()
        
        def __str__(self):
                return str(self.adtitle)


        def save(self, *args, **kwargs):
                if not self.slug:
                        self.slug = get_unique_slug(self,'adtitle', 'slug')
                        super().save(*args, **kwargs)
        
        def get_absolute_url(self): 
                return reverse('house:detail', kwargs={'slug':self.slug})


class Booking(models.Model):
        house = models.ForeignKey(House, related_name="booked", on_delete=models.CASCADE)
        guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        no_guests = models.SmallIntegerField(default=0,null=False, blank=False)
        nights = models.SmallIntegerField(default=0, null=False, blank=True)
        start = models.DateField()
        end = models.DateField()
        extra_info = models.CharField(max_length = 100, blank=True, null=True)
        payment_notification_date = models.DateTimeField(null=True, blank=True)
        payment_confirmation_date = models.DateTimeField(null=True, blank=True)
        timestamp = models.DateTimeField(auto_now_add=True)
        mod_date = models.DateTimeField(auto_now_add=True)

        objects = models.Manager()

        def __str__(self):
                return str(self.house)

class Review(models.Model): 
        reviewer =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        house = models.ForeignKey(House, related_name="reviewed", on_delete=models.CASCADE)
        text = models.TextField()
        overall_rating = models.SmallIntegerField(blank=True, null=True)
        clean_rating = models.SmallIntegerField()
        comfort_rating = models.SmallIntegerField()
        location_rating = models.SmallIntegerField()
        value_money_rating = models.SmallIntegerField()

        def __str__(self):
                return "review from {}".format(self.reviewer)

        def save(self, *args, **kwargs):
                self.overall_rating = int(round(float(self.clean_rating + self.comfort_rating + self.location_rating + self.value_money_rating ) / 4))
                super(Review, self).save(*args, **kwargs)

        


        







        
