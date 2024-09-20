from analytics_service.filters import SearchAnalyticsFilter, PopularPropertyAnalyticsFilter
from analytics_service.models import SearchAnalytics, PopularPropertyAnalytics
from analytics_service.serializers import SearchAnalyticsSerializer, PopularPropertyAnalyticsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class SearchAnalyticsListCreateView(generics.ListCreateAPIView):
    """
    API View для создания и просмотра поисковой аналитики
    """
    queryset = SearchAnalytics.objects.all()
    serializer_class = SearchAnalyticsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SearchAnalyticsFilter

    def get_queryset(self):
        """
        Получить список объектов SearchAnalytics, с возможностью фильтрации
        """
        queryset = super().get_queryset()
        # Можно добавить дополнительную логику фильтрации или сортировки
        return queryset


class PopularPropertyAnalyticsListCreateView(generics.ListCreateAPIView):
    """
    API View для создания и просмотра аналитики популярных объектов недвижимости
    """
    queryset = PopularPropertyAnalytics.objects.all()
    serializer_class = PopularPropertyAnalyticsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PopularPropertyAnalyticsFilter

    def get_queryset(self):
        """
        Получить список объектов PopularPropertyAnalytics с возможностью фильтрации
        """
        queryset = super().get_queryset()
        # Можно добавить дополнительную логику фильтрации или сортировки
        return queryset
