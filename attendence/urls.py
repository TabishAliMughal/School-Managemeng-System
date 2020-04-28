from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('attend/', views.attendance_select, name="attendence_list_template"),
    path('attendence/', views.attendance_add, name="attendence_list_template"),
    path('attendence/print', views.attendance_print, name="attendence_print"),
    path('attendence/ask/print', views.attendance_ask_print, name="attendance_ask_print"),
    path('attendence/save', views.attendance_save, name="attendence_save_template"),
    # path('list_attend/', views.student_attend_list, name="create_attendence")

]