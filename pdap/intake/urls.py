from . import views
from django.urls import path

urlpatterns = [
    path('plain', views.plain),
    path('schema', views.schema),
    path('ajax/get_agencies/<str:state_iso>/', views.get_agencies, name="state_iso"),
    path('ajax/get_datasets/<str:id>/', views.get_datasets, name="id"),
]
