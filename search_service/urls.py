from django.urls import path
from search_service import views

urlpatterns = [
    path('search-analytics/', views.SearchAnalyticsListCreateView.as_view(), name='search_analytics'),
    path('property-view-analytics/', views.PropertyViewAnalyticsListCreateView.as_view(), name='property_view_analytics'),
    path('search_history/', views.UserSearchHistoryView.as_view(), name='search_history'),
    path('view_history/', views.UserViewHistoryView.as_view(), name='view_history'),
]
