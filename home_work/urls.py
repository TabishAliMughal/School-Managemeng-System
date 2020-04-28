from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('home_work/', views.home_work, name="home_work_main"),
    # path('home_work/calender/', views.home_work_calender, name="home_work_calender"),
    path('homework/list/', views.homeWork_listWise, name='home_work_listWise'),
    path('homework/add/', views.homeWork_add, name='homeWork_add'),
    path('homework/update/<homework_ID>', views.homeWork_update, name='homeWork_update'),
    path('delete_class/<homework_ID>+/', views.homeWork_delete, name = 'delete_class'),
]
