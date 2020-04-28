"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('Query/', include('Query.urls')),
    path('fees/', include('fees.urls')),
    path('students/', include('student_information.urls')),
    path('dependencies/', include('dependencies.urls')),
    path('Exam/', include('Exam.urls')),    
    path('homework/', include('home_work.urls')),
    path('Question_Bank/', include('Question_Bank.urls')),
    path('sms/', include('sms.urls')),
    path('attendence/', include('attendence.urls'))
]

