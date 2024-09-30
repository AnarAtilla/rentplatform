from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .filters import PropertyViewFilter, SearchQueryFilter
from .serializers import PropertyViewSerializer, SearchQuerySerializer
from booking_service.models import Booking  # Импорт Booking из модуля booking_service
from property_service.models import Property  # Импорт Property из модуля property_service
from .models import PropertyView, SearchQuery  # Импорт остальных моделей из analytics_service


# Просмотры недвижимости для владельцев
class PropertyViewListView(generics.ListAPIView):
    serializer_class = PropertyViewSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PropertyViewFilter

    def get_queryset(self):
        """
        Возвращаем просмотры для объектов недвижимости текущего владельца.
        """
        return PropertyView.objects.filter(property__owner=self.request.user)


# Поисковые запросы всех пользователей (для админов)
class SearchQueryListView(generics.ListAPIView):
    serializer_class = SearchQuerySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SearchQueryFilter

    def get_queryset(self):
        """
        Администраторы могут видеть все поисковые запросы.
        """
        if self.request.user.is_staff:
            return SearchQuery.objects.all()
        return SearchQuery.objects.none()  # Не показывать ничего обычным пользователям


# Статистика по объектам недвижимости для владельцев
class PropertyStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        properties = Property.objects.filter(owner=request.user)
        stats = []

        for property in properties:
            views_count = PropertyView.objects.filter(property=property).count()
            bookings_count = Booking.objects.filter(property=property).count()

            stats.append({
                'property': property.title,
                'views_count': views_count,
                'bookings_count': bookings_count
            })

        return Response(stats)


# Статистика по бронированиям для владельцев
class BookingStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        properties = Property.objects.filter(owner=request.user)
        stats = []

        for property in properties:
            confirmed_bookings = Booking.objects.filter(property=property, status='confirmed').count()
            cancelled_bookings = Booking.objects.filter(property=property, status='cancelled').count()

            stats.append({
                'property': property.title,
                'confirmed_bookings': confirmed_bookings,
                'cancelled_bookings': cancelled_bookings
            })

        return Response(stats)


# Активность пользователя
class UserActivityView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        views = PropertyView.objects.filter(user=request.user)
        bookings = Booking.objects.filter(guest=request.user)

        data = {
            'viewed_properties': views.count(),
            'made_bookings': bookings.count()
        }

        return Response(data)


# Популярные объекты недвижимости
class PopularPropertiesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        popular_properties = Property.objects.annotate(view_count=Count('views')).order_by('-view_count')[:5]

        data = [{'property': prop.title, 'view_count': prop.view_count} for prop in popular_properties]

        return Response(data)
