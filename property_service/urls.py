from django.urls import path
from property_service import views

urlpatterns = [
    path('create/', views.PropertyCreateView.as_view(), name='property_create'),
    path('list/', views.PropertyListView.as_view(), name='property_list'),
    path('search/', views.PropertySearchView.as_view(), name='property_search'),
    path('edit/<int:pk>/', views.PropertyUpdateView.as_view(), name='property_edit_'),
    path('delete/<int:pk>/', views.PropertyDeleteView.as_view(), name='property_delete'),
]
