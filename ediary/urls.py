from django.urls import path

from . import views

app_name = 'ediary'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register, name='register'),
    path('<int:users_id>/', views.home, name='home')
]
