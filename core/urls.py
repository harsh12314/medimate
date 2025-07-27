from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    # Medicine routes
    path('medicines/', views.medicine_list, name='medicine_list'),
    path('medicines/add/', views.add_medicine, name='add_medicine'),
    path('medicines/<int:pk>/edit/', views.edit_medicine, name='edit_medicine'),
    path('medicines/<int:pk>/delete/', views.delete_medicine, name='delete_medicine'),
    
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),
    path('appointments/<int:pk>/edit/', views.edit_appointment, name='edit_appointment'),
    path('appointments/<int:pk>/delete/', views.delete_appointment, name='delete_appointment'),
    
    path('vitals/', views.vitals_list, name='vitals_list'),
    path('vitals/add/', views.add_vitals, name='add_vitals'),
    path('vitals/graph/', views.vitals_graph, name='vitals_graph'),

]
