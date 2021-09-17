from django.urls import path

from . import views

app_name = 'ediary'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/new',views.users_new, name='users_new'),
    path('register/<int:pk>/', views.users_detail, name='users_detail'),
    path('register/<int:pk>/edit/', views.users_edit, name='users_edit'),
    path('<int:users_id>/home/', views.home, name='home'),
]
