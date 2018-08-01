from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import CreateView, UpdateView, DeleteView,ListView,FormView, DetailView
from django.views.generic.edit import FormMixin, SingleObjectMixin
from django.urls import reverse, reverse_lazy
from django.db.models import Q

from . mixins import FormUserNeededMixin, AjaxFormMixin
from . models import House, Booking, Review
from . forms import HouseForm, BookingForm, SearchForm
from accounts.models import UserProfile



def form_redirect(request):
  return render(request, 'home')



class HouseCreate(LoginRequiredMixin, CreateView):
  form_class =  HouseForm
  template_name = "houses/create_view.html" 
  success_url= "/"
  login_url ="/login/"

  def form_valid(self, form):
      form.instance.owner = self.request.user
      return super(HouseCreate, self).form_valid(form)

class HouseList(ListView): 
    model = House
    template_name = "houses/list_houses.html"

    def get_queryset(self, *args, **kwargs):
        qs = House.objects.all()
        
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
    

    def get_context_data(self, **kwargs): 
        context = super(HouseDetail, self).get_context_data(**kwargs)
        context['form'] = BookingForm()
        return context
    

class BookingView(LoginRequiredMixin, FormView):
    form_class = BookingForm
    model = Booking
    success_url = ''
    login_url = '/login'

    
    def form_valid(self, form):
        guest = self.request.user
        no_guests = form.cleaned_data.get('no_guests')
        start = form.cleaned_data.get('start')
        stop = form.cleaned_data.get('stop')
        extra_info = form.cleaned_data.get('extra_info')

        booking = Booking.objects.create(guest=guest, no_guests=no_guests,
        start=start ,stop=stop,extra_info=extra_info)

        if form.is_valid:
            form.save(commit = False)
            form.guest= self.request.user

        return super(BookingView, self).form_valid(form)


class HouseUpdateView(UpdateView): 
    model = House
    form_class =  HouseForm
    template_name = "houses/create_view.html"
    slug_field = 'slug'

    def get_success_url(self, **kwargs):         
        return self.object.get_absolute_url()

class HouseDeleteView(DeleteView):
    model = House
    template_name = "houses/delete_view.html"
    success_url = reverse_lazy("house:my_lists")
    slug_field ='slug'


class SearchView(ListView):
    model = House 
    template_name = "houses/list_houses.html"
    
    def get_queryset(self, *args, **kwargs):
        qs = House.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(adtitle__icontains=query) |
                Q(house_type__icontains=query)
            )
        return qs

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context


        
