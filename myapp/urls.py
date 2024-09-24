from django.urls import path
from .views import index, contact, display_contacts
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('display-contacts/', display_contacts, name='display_contacts'),
]