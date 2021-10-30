from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('show/new', views.new),
    path('create', views.create),
    path('show/<int:show_id>/edit', views.edit),
    path('show/<int:show_id>/delete', views.delete),
    path('back', views.back),
    path('show/<int:show_id>/update', views.update),
    path('show/<int:show_id>', views.show),
]