from django.urls import path
from . import views

urlpatterns = [
    path('',views.ManageSmsView, name="sms_create"),
]
