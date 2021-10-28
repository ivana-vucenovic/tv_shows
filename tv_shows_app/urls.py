from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('show/<int:show_id>', views.show),
    path('show/<int:show_id>/edit', views.edit),
]