from analytics_service.models import PopularPropertyAnalytics, PropertyViewAnalytics
from analytics_service.serializers import PopularPropertyAnalyticsSerializer, PropertyViewAnalyticsSerializer
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from property_service.models import Property
from property_service.serializers import PropertySerializer
from rest_framework import generics
from django.views.generic import ListView
from .models import Property
from django.db.models import Q

class PropertySearchView(ListView):
    model = Property
    template_name = 'property_service/property_search.html'
    context_object_name = 'properties'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Property.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        return Property.objects.all()


# Property views
class PropertyCreateView(CreateView):
    model = Property
    template_name = 'property_service/property_form.html'
    fields = ['title', 'description', 'location', 'price', 'rooms', 'bathrooms', 'property_type', 'amenities', 'photos']
    success_url = reverse_lazy('property_list')

# Analytics views
class PropertyViewAnalyticsListCreateView(generics.ListCreateAPIView):
    queryset = PropertyViewAnalytics.objects.all()
    serializer_class = PropertyViewAnalyticsSerializer

class PropertyViewAnalyticsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyViewAnalytics.objects.all()
    serializer_class = PropertyViewAnalyticsSerializer

class PopularPropertyAnalyticsListCreateView(generics.ListCreateAPIView):
    queryset = PopularPropertyAnalytics.objects.all()
    serializer_class = PopularPropertyAnalyticsSerializer

class PopularPropertyAnalyticsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PopularPropertyAnalytics.objects.all()
    serializer_class = PopularPropertyAnalyticsSerializer

class PropertyListView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyUpdateView(generics.UpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDeleteView(generics.DestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
