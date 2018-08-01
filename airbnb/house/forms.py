from django import forms 
from . models import House, Booking, Review
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

class HouseForm(forms.ModelForm):
  adtitle = forms.CharField(
    label='Lising Title', 
    required = 'True',
    widget=forms.TextInput(attrs={'class':'fa fa-briefcase'})
  )
  description = forms.CharField(
    label='Description', 
    required = 'True',
    widget=forms.Textarea(attrs={'placeholder': 'Description'})
  )
  location = forms.CharField(
    label='Location', 
    required = 'True',
    widget=forms.TextInput()
  )
  house_type = forms.ChoiceField(choices=TYPES,
    label='House Type', 
    required = 'True',
    widget=forms.Select(attrs={'class':' chosen-select  nice-select-search'})
  )
  
  no_beds = forms.IntegerField(
    label='Number of Beds',
    required = 'True',
   widget=forms.NumberInput(attrs={'type':'text', } )
  )
  no_baths = forms.IntegerField(
    label='Number of Baths',
    required = 'True',
    widget=forms.NumberInput(attrs={'type':'text'})
  )
  no_bedrooms = forms.IntegerField(
    label='Number of Rooms',
    required = 'True',
    widget=forms.NumberInput(attrs={'type':'text'})
  )
  price = forms.IntegerField(
    label='Price',
    required = 'True',
    widget=forms.NumberInput(attrs={'type':'text'})
    )
  images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
  
  wifi = forms.BooleanField(label='Wifi',
  required=False, 
  widget=forms.CheckboxInput(attrs={'type':'checkbox' ,'class':''})
  )
  essential = forms.BooleanField(label='Essential',
  required=False, 
  widget=forms.CheckboxInput(attrs={'type':'checkbox' })
  )
  shampoo  = forms.BooleanField(label='shampoo',
  required=False, 
  widget=forms.CheckboxInput(attrs={'type':'checkbox'})
  )
  closet = forms.BooleanField(label='Closet',
  required=False, 
  widget=forms.CheckboxInput(attrs={'type':'checkbox' ,})
  )
  tv = forms.BooleanField(label='TV',
  required=False, 
  widget=forms.CheckboxInput(attrs={'type':'checkbox'})
  )
  smoke_detector = forms.BooleanField(label='Smoke Detector',
  required=False, 
  widget=forms.CheckboxInput(attrs={'type':'checkbox'})
  )
  first_aid = forms.BooleanField(label='First Aid',
  required=False, 
  widget=forms.CheckboxInput(attrs={'type':'checkbox'})
  )
  laundry = forms.BooleanField(label='Fire Extinguisher',
  required=False, 
  widget=forms.CheckboxInput(attrs={'type':'checkbox'})
  )
  pool = forms.BooleanField(label='Fire Extinguisher',
  required=False, 
  widget=forms.CheckboxInput(attrs={'type':'checkbox'})
  )
  kitchen = forms.BooleanField(label='Fire Extinguisher',
  required=False, 
  widget=forms.CheckboxInput(attrs={'type':'checkbox'})
  )
  gym = forms.BooleanField(label='Fire Extinguisher',
  required=False, 
  widget=forms.CheckboxInput(attrs={'type':'checkbox'})
  )
  parking = forms.BooleanField(label='Fire Extinguisher',
  required=False, 
  widget=forms.CheckboxInput(attrs={'type':'checkbox'})
  )
  fire_extinguisher = forms.BooleanField(label='Fire Extinguisher',
  required=False, 
  widget=forms.CheckboxInput(attrs={'type':'checkbox'})
  )
  
  class Meta:
    model = House
    fields = ['adtitle', 'description', 'location', 'house_type', 'wifi', 'no_baths', 'no_bedrooms', 'no_beds', 'price', 'images', 'kitchen', 'fire_extinguisher', 'first_aid', 'parking', 'gym', 'kitchen', 'pool', 'laundry', 'smoke_detector']
 
  
class BookingForm(forms.ModelForm):
  no_guests = forms.IntegerField(label='Guests', required=True)
  start = forms.DateField(label="Start", 
  required=True, 
  widget=forms.SelectDateWidget(attrs={'type':'text', 'class':'datepick', 'data-large-mode':'true', 'data-large-default':"true"}))
  end = forms.DateField(label="End", required=True)
  extra_info = forms.CharField(label="Additional info", required=False)

  class Meta:
    model = Booking 
    fields = ['no_guests', 'start', 'end', 'extra_info']




class SearchForm(forms.Form):
  keyword = forms.CharField(required=False)
  house_type = forms.ChoiceField(choices=TYPES,
    label='House Type', 
    required = 'True',
    widget=forms.Select(attrs={'class':' chosen-select  nice-select-search'})
  )













