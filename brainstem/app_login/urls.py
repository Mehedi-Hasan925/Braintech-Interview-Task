from django.urls import path
from app_login import views

app_name = 'app_login'

urlpatterns = [
    path('', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),

    
    path('add_profile_info/', views.Add_Profile_Info, name='add_profile_info'),
    path('change_profile_photo/', views.change_profile_pic, name='change_profile_photo'),
    path('profile/', views.profile_page, name='profile'),
]