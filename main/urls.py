from django.urls import path
from . import views

urlpatterns = [    
    path('', views.ManageMainScreenView, name='MainScreen_url'),
    path('main/', views.ManageAfterLoginView, name='after_login_url'),
    path('about/', views.ManageAboutView, name='about_url'),
    path('school/', views.ManageSchoolView, name='school_url'),
    path('contact/', views.ManageContactView, name='contact_url'),
    path('team/', views.ManageTeamView, name='team_url'),
    path('detail/', views.ManageDetailView, name='detail_url'),

    path('usertype/list', views.ManageUserTypeListView, name='usertype_url'),
    path('usertype/edit/<TypeCode>', views.ManageUserTypeEditView, name='usertypeedit_url'),
    path('usertype/create/', views.ManageUserTypeCreateView, name='usertypecreate_url'),

    path('userprofile/list', views.ManageUserProfileListView, name='userprofilelist_url'),
    path('userprofile/detail/<UserCode>/', views.ManageUserProfileDetailView, name='userprofiledetail_url'),
    path('userprofile/edit/<UserCode>/', views.ManageUserProfileEditView, name='userprofileedit_url'),
    path('userprofile/create/', views.ManageUserProfileCreateView, name='userprofilecreate_url'),
]
