from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import CreateView, UpdateView, DeleteView,ListView,FormView, DetailView
from django.views.generic.edit import FormMixin, SingleObjectMixin
from django.urls import reverse, reverse_lazy
from . mixins import FormUserNeededMixin, AjaxFormMixin
from . models import House, Booking, Review
from . forms import HouseForm, BookingForm
from accounts.models import UserProfile



def form_redirect(request):
  return render(request, 'home')



class HouseCreate(LoginRequiredMixin, FormView):
  form_class =  HouseForm
  template_name = "houses/create_view.html" 
  success_url= "/"
  login_url ="/login/"
#   def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('images')
    
#         if form.is_valid():
#             for f in files:
#                 f.save()
#                 ...  # Do something with each file.
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

  def form_valid(self, form):
    adtitle = form.cleaned_data.get( 'adtitle')
    owner = self.request.user
    description = form.cleaned_data.get('description')
    location = form.cleaned_data.get('location')
    no_baths = form.cleaned_data.get('no_baths')
    no_beds = form.cleaned_data.get('no_beds')
    no_bedrooms = form.cleaned_data.get('no_bedrooms')
    house_type = form.cleaned_data.get('house_type')
    price = form.cleaned_data.get('price')
    images = form.cleaned_data.get('images')
    wifi = form.cleaned_data.get( 'wifi')
    essential = form.cleaned_data.get('essential')
    shampoo = form.cleaned_data.get('shampoo')
    closet = form.cleaned_data.get('closet')
    tv = form.cleaned_data.get('tv')
    smoke_detector = form.cleaned_data.get('smoke_detector')
    first_aid = form.cleaned_data.get('first_aid')
    
    house = House.objects.create(adtitle=adtitle, owner=owner, description=description, location=location, no_beds=no_beds, no_baths =no_baths, no_bedrooms=no_bedrooms, house_type=house_type, price=price,wifi=wifi, essential=essential, shampoo=shampoo, closet=closet, tv =tv, smoke_detector=smoke_detector, first_aid=first_aid, images=images )

    if form.is_valid:
        form.save(commit = False)
        form.owner= self.request.user
    return super(HouseCreate, self).form_valid(form)

class HouseList(ListView): 
    model = House
    template_name = "houses/list_houses.html"

    def get_queryset(self, *args, **kwargs):
        qs = House.objects.all()
        qs2 = House.objects.filter()
        return qs

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        return context

class MyHouseList(ListView): 
    model = House
    template_name = "houses/my_listings.html"

    def get_queryset(self, *args, **kwargs): 
        qs = House.objects.filter(owner=self.request.user)
        return qs

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        return context



class HouseDetail(DetailView):
    model = House
    template_name = 'houses/house_detail.html'
    form_class = BookingForm

    def get_context_data(self, **kwargs): 
        context = super(HouseDetail, self).get_context_data(**kwargs)
        context['form'] = BookingForm()
        return context
    
class BookHouse(SingleObjectMixin, FormView):
    template_name = 'houses/house_detail.html'
    form_class = BookingForm
    model = House

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('house-detail', kwargs={'pk': self.object.pk})
        




class HouseUpdateView(UpdateView): 
    model = House
    form_class =  HouseForm
    template_name = "houses/create_view.html"
    success_url =  "/house/user_lists"
    slug_field = 'slug'

    def form_valid(self, form):
        form.save(commit=True)
        return super(HouseUpdateView, self).form_valid(form)

class HouseDeleteView(DeleteView):
    model = House
    template_name = "houses/delete_view.html"
    success_url = "/"
    slug_field ='slug'



    

        
