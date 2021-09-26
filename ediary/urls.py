from django.urls import path

from . import views

app_name = 'ediary'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.users_new, name='users_new'),
    path('register/<int:pk>/', views.users_reg_success, name='users_reg_success'),
    path('register/<int:pk>/edit/', views.users_edit, name='users_edit'),
    path('<int:users_id>/home/', views.home, name='home'),
    path('new_activity/', views.new_activity, name='new_activity'),
]
