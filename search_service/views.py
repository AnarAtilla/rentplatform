from django.db.models import Q
from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from property_service.models import Property
from property_service.serializers import PropertySerializer
from rest_framework import generics
from .filters import PropertyFilter
from .models import SearchQuery


class PropertySearchView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PropertyFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('q', None)

        if search_query:
            queryset = queryset.filter(
                title__icontains=search_query
            )
            if self.request.user.is_authenticated:
                SearchQuery.objects.create(user=self.request.user, query=search_query, results_count=queryset.count())

        return queryset

class SearchResultsView(ListView):
    model = Property
    template_name = 'search_service/search_results.html'
    context_object_name = 'properties'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Property.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
