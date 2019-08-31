from django.urls import path
from . import views as home_view

urlpatterns = [
    path('', home_view.home, name = 'home'),
]