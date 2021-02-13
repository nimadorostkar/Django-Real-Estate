from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('property-detail/<slug:slug>',views.propertyDetail,name='property_detail'),
    path('properties-list/',views.propertiesList,name='properties_list'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.searchResult,name='search'),
    path('services/',views.Services,name='services'),
    path('quick-contact/',views.Quick_Contact,name='quickcontact'),
    path('contact-agent/',views.UserAgentContact,name='agentcontact')
]