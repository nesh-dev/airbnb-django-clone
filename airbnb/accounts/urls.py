from django.urls import path
from django.contrib import admin

admin.autodiscover()

app_name = 'accounts'

from . views import (
  RegisterForm, EditUserProfileView,UserHouseLists
  
)

urlpatterns = [

    # path('create/', ProfileForm.as_view(), name='create'),
    path('edit/<username>', EditUserProfileView.as_view(), name='update'),
    path('user_lists/<username>/' , UserHouseLists.as_view(), name='user_lists'),

    
    
    
   
    
    
]
