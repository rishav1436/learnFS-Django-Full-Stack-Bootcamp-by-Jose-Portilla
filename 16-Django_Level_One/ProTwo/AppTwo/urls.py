from django.urls import path
from AppTwo import views

urlpatterns = [
    path('', views.index, name='index'), # for homepage, no path is needed
    path('help/', views.help, name='index'),
]