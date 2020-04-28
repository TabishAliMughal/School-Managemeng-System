from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('hello/', views.hello),
    ### exam model....
    path('form/', views.form , name = 'exam_form'),
    path('list_view/', views.list_view, name = 'exam_list_view'),
    path('edit/<exam_code>+/', views.edit, name='edit_exam'),
    path('delete/<exam_code>+/', views.delete, name='delete_exam'),
    path('detail/<exam_code>/', views.detail, name = 'exam_detail'),
   
    ### SEMESTER MODEL
    path('semester_form/', views.semester_form , name = 'semester_form'),
    path('semester_list_view/', views.semester_list_view, name = 'semester_list_view'),
    path('semester_edit/<semester_code>+/', views.semester_edit, name='edit_semester'),
    path('semester_delete/<semester_code>+/', views.semester_delete, name='delete_semester'),
    path('semester_detail/<semester_code>/', views.semester_detail, name = 'semester_detail'),
    path('semester_upload/', views.semester_upload , name = 'semester_upload'),
    ### SEMESTER Breakup MODEL
    path('semesterB_form/', views.semesterBform , name = 'semesterB_form'),
    path('semesterB_list_view/', views.semesterB_list_view, name = 'semesterB_list_view'),
    path('semesterB_detail/<semesterbreakup_code>/', views.semesterB_detail, name = 'semesterB_detail'),
    path('semesterB_edit/<semesterbreakup_code>+/', views.semesterB_edit, name='edit_semesterB'),
    path('semesterB_delete/<semesterbreakup_code>+/', views.semesterB_delete, name='delete_semesterB'),
    path('semesterB_upload/', views.semesterB_upload , name = 'semesterB_upload'),
    ####Quaters
    path('quater_form/', views.quaterform , name = 'quater_form'),
    path('quater_list_view/', views.quater_list_view, name = 'quater_list_view'),
    path('quater_detail/<quater_code>/', views.quater_detail, name = 'quater_detail'),
    path('quater_edit/<quater_code>+/', views.quater_edit, name='edit_quater'),
    path('quater_delete/<quater_code>+/', views.quater_delete, name='delete_quater'),
    path('quater_upload/', views.quater_upload , name = 'quater_upload'),
    ####Assesment
    path('assesment_form/', views.assesmentform , name = 'assesment_form'),
    path('assesment_list_view/', views.assesment_list_view, name = 'assesment_list_view'),
    path('assesment_detail/<assesment_code>/', views.assesment_detail, name = 'assesment_detail'),
    path('assesment_edit/<assesment_code>+/', views.assesment_edit, name='edit_assesment'),
    path('assesment_delete/<assesment_code>+/', views.assesment_delete, name='delete_assesment'),
    path('assesment_upload/', views.assesment_upload , name = 'assesment_upload'),
    ####Mark
    path('mark_form/', views.markform , name = 'mark_form'),
    path('mark_print/', views.markprint , name = 'mark_print'),
    path('mark_list_view/', views.mark_list_view, name = 'mark_list_view'),
    path('mark_detail/<id>+/', views.mark_detail, name = 'mark_detail'),
    path('mark_edit/<id>+/', views.mark_edit, name='edit_mark'),
    path('mark_delete/<id>+/', views.mark_delete, name='delete_mark'),
    path('mark_upload/', views.mark_upload , name = 'mark_upload'),
    path('download_mark/', views.mark_download , name = 'mark_download')

]
    