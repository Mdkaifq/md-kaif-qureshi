from django.urls import path
from . import views

urlpatterns = [
    path('', views.uploadFile, name='upload_file'),
    path('send-email/', views.sendEmail, name='send_email'),
]
