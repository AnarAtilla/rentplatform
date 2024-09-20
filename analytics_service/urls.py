from django.urls import path
from . import views

urlpatterns = [
    path('search-analytics/', views.SearchAnalyticsListCreateView.as_view(), name='search_analytics'),
    path('popular-property-analytics/', views.PopularPropertyAnalyticsListCreateView.as_view(), name='popular_property_analytics'),
]
