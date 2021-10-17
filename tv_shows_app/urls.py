from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/<int:show_id>', views.show)
]