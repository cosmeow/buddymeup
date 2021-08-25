from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('<int:users_id>/', views.home, name='home')
]
