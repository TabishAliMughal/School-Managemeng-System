from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('book_list/',views.book_list, name = 'book_list'),
    path('book_form/',views.books, name = 'book_form'),
    path('book_upload/',views.book_upload, name = 'book_upload'),
    path('book_download/', views.book_download, name = 'book_download'),
    path('edit_book/<book_code>+/', views.edit_book, name = 'edit_book'),
    path('book_detail/<book_code>/', views.book_detail, name = 'book_detail'),
    path('delete_book/<book_code>+/', views.delete_book, name = 'delete_book'),
    path('print/<clas>/<subj>/<publ>/',views.ManageBookPrintPdfView, name="book_print"),



    path('publisher_list/',views.publisher_list, name = 'publisher_list'),
    path('publisher_form/',views.publishers, name = 'publisher_form'),
    path('publisher_upload/',views.publisher_upload, name = 'publisher_upload'),
    path('publisher_download/', views.publisher_download, name = 'publisher_download'),
    path('edit_publisher/<publisher_code>+/', views.edit_publisher, name = 'edit_publisher'),
    path('delete_publisher/<publisher_code>+/', views.delete_publisher, name = 'delete_publisher'),
    path('publisher_print/',views.ManagePublisherPrintPdfView, name="publisher_print"),


    path('chapter_list/',views.chapter_list, name = 'chapter_list'),
    path('chapter_form/',views.chapters, name = 'chapter_form'),
    path('chapter_upload/',views.chapter_upload, name = 'chapter_upload'),
    path('chapter_download/', views.chapter_download, name = 'chapter_download'),
    path('edit_chapter/<chapter_code>+/', views.edit_chapter, name = 'edit_chapter'),
    path('delete_chapter/<chapter_code>+/', views.delete_chapter, name = 'delete_chapter'),
    path('chapter_print/',views.ManageChapterPrintPdfView, name="chapter_print"),


    path('question_type_list/',views.question_type_list, name = 'question_type_list'),
    path('question_type_form/',views.questions_types, name = 'question_type_form'),
    path('question_type_upload/',views.question_type_upload, name = 'question_type_upload'),
    path('Q_type_download/', views.Q_type_download, name = 'Q_type_download'),
    path('edit_question_type/<Q_type_code>+/', views.edit_question_type, name = 'edit_question_type'),
    path('delete_question_type/<Q_type_code>+/', views.delete_question_type, name = 'delete_question_type'),


    path('question_bank_list/',views.question_bank_list, name = 'question_bank_list'),
    path('question_bank_filtered/',views.filtered_Questions, name = 'question_bank_filter'),
    path('question_bank_form/',views.question_banks, name = 'question_bank_form'),
    path('question_bank_upload/',views.question_bank_upload, name = 'question_bank_upload'), 
    path('Q_bank_download/', views.Q_bank_download, name = 'Q_bank_download'),   
    path('edit_question_bank/<question_code>+/', views.edit_question_bank, name = 'edit_question_bank'),
    path('question_bank_detail/<question_code>/', views.question_bank_detail, name = 'question_bank_detail'),
    path('delete_question_bank/<question_code>+/', views.delete_question_bank, name = 'delete_question_bank'),
    path('question_print/',views.ManageQuestionPrintPdfView, name="question_print"),

]