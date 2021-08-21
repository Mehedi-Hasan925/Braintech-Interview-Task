from app_user_activity import views
from django.urls import path

app_name = 'app_user_activity'

urlpatterns = [
    path('home/', views.home, name='home'),
    
]
