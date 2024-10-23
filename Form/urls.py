from django.urls import path
from . import views 

urlpatterns = [
    path('form/', views.PersonView, name='form_view'),  
]
