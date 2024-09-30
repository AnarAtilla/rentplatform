from analytics_service.models import PropertyView, SearchQuery
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Property
from .permissions import IsOwnerOrReadOnly, IsActiveUser
from .serializers import PropertySerializer


# Создание нового объекта недвижимости
class PropertyCreateView(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated, IsActiveUser]

    def perform_create(self, serializer):
        # Указываем текущего пользователя как владельца при создании
        serializer.save(owner=self.request.user)

# Список и поиск объектов недвижимости
class PropertySearchView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Реализуем логику фильтрации и поиска по нескольким параметрам.
        """
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('q', None)
        location = self.request.query_params.get('location', None)
        property_type = self.request.query_params.get('property_type', None)

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
            # Сохраняем поисковый запрос
            SearchQuery.objects.create(
                user=self.request.user,
                query=search_query,
                results_count=queryset.count(),
            )

        if location:
            queryset = queryset.filter(location__icontains=location)

        if property_type:
            queryset = queryset.filter(property_type=property_type)

        return queryset


# Получение информации об объекте недвижимости
class PropertyDetailView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)

        # Сохраняем просмотр объекта
        property_instance = self.get_object()
        PropertyView.objects.create(property=property_instance, user=request.user)

        return response

# Обновление объекта недвижимости
class PropertyUpdateView(generics.UpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

# Удаление объекта недвижимости
class PropertyDeleteView(generics.DestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
