from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.views import redirect_to_login

from django.http import HttpResponseRedirect

from django.views.generic import UpdateView, DeleteView,FormView, DetailView, ListView

from . forms import UserProfileForm, UserRegisterForm
from . models import UserProfile
from house.models import House
from house.mixins import UserOwnerMixin


User = get_user_model()
# Create your views here.


class RegisterForm(FormView):
    template_name = 'profile/user_register.html'
    form_class = UserRegisterForm
    success_url = "/login"
    
    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return super(RegisterForm, self).form_valid(form)

class EditUserProfileView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "profile/create_user_profile.html"
    success_url = "/"
  
    def get_object(self, *args, **kwargs):
      user = get_object_or_404(User, username=self.kwargs['username'])
      return user.profile

    # def user_passes_test(self, request):
    #   if request.user.is_authenticated():
    #       return self.object == request.user.profile
    #   return False

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.user_passes_test(request):
    #       return redirect_to_login(request.get_full_path())
    #     return super(EditUserProfileView, self).dispatch(
    #         request, *args, **kwargs)

class UserHouseLists(ListView): 
    
    template_name = "houses/user_listings.html"
    model = House

    def get_queryset(self, *args, **kwargs): 
        profile_name = self.kwargs.get("username")
        profile = UserProfile.objects.filter(user__username=profile_name)
        qs = House.objects.filter(owner__username=profile[0])
        return qs
        
         


    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        #context['owner'] =  
        return context