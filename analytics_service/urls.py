from django.urls import path
from .views import (
    PropertyViewListView,
    SearchQueryListView,
    PropertyStatsView,
    BookingStatsView,
    UserActivityView,
    PopularPropertiesView
)

urlpatterns = [
    path('property-views/', PropertyViewListView.as_view(), name='property_view_list'),
    path('search-queries/', SearchQueryListView.as_view(), name='search_query_list'),
    path('property-stats/', PropertyStatsView.as_view(), name='property_stats'),
    path('booking-stats/', BookingStatsView.as_view(), name='booking_stats'),
    path('user-activity/', UserActivityView.as_view(), name='user_activity'),
    path('popular-properties/', PopularPropertiesView.as_view(), name='popular_properties'),
]
