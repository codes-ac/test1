from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('gallery/', views.gallery, name='gallery'),
    path('eSamachar/', views.samachar, name='eSamachar'),
    path('staff/', views.staff, name='staff'),
    path('atl/', views.atl, name='atl'),
    path('showcase/', views.showcase, name='showcase'),
    path('contact/', views.contact, name='contact'),
    path('notice/', views.notice, name='notice'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
    path('purchase_form/', views.purchase_form, name='purchase-form'),
]
