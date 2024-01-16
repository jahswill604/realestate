# listings/urls.py
from django.urls import path
from . import views 
from.views import  initiate_payment

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('single/<int:item_id>/', views.single_view, name='single'),
    path('property/', views.property, name='property'),
    path('paystack', views.paystack, name='paystack'),
    path('pay/<int:listing_id>/', initiate_payment, name='initiate_payment'),
]



