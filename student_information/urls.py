from django.urls import path
from . import views

urlpatterns = [
    path('',views.ManageGrListView, name="gr_list"),
    path('download/', views.ManageGrDataDownloadView, name = 'gr_data_download'),
    path('print/<clas>/<sect>/',views.ManageGrPrintPdfView, name="gr_print"),
    path('create/',views.ManageGrCreateView, name="gr_create"),
    path('create/autofill/<query>',views.ManageGrCreateView, name="gr_create"),
    path('create/bulk/download/', views.ManageGrBulkSampleDownloadView, name = 'gr_bulk_download'),
    path('create/bulk/', views.ManageGrUploadView, name = 'gr_bulk'),
    path('<int:gr_number>/',views.ManageGrDetailView,name='gr_detail'),
    path('edit/<gr_number>/', views.ManageGrEditView, name = 'gr_edit'),
    path('delete/<gr_number>/', views.ManageGrDeleteView, name = 'gr_delete'),
]
