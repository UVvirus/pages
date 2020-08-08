from django.urls import path
from . import views

urlpatterns=[
    path('',views.Homepageview.as_view(),name='home'),
    path('about/',views.Aboutpageview.as_view(),name='about'),
            ]