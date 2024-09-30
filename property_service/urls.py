from django.urls import path
from .views import PropertyCreateView, PropertyDetailView, PropertyUpdateView, PropertyDeleteView, PropertySearchView

urlpatterns = [
    path('property/<int:pk>/', PropertyDetailView.as_view(), name='property_detail'),
    path('create/', PropertyCreateView.as_view(), name='property_create'),
    path('list/', PropertySearchView.as_view(), name='property_list'),
    path('search/', PropertySearchView.as_view(), name='property_search'),
    path('edit/<int:pk>/', PropertyUpdateView.as_view(), name='property_edit'),
    path('delete/<int:pk>/', PropertyDeleteView.as_view(), name='property_delete'),
]
