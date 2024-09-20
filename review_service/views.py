from rest_framework import generics, permissions
from review_service.models import Review
from review_service.serializers import ReviewSerializer
from review_service.permissions import IsOwnerOrReadOnly

# View для создания нового отзыва
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Создаем отзыв для текущего пользователя
        serializer.save(guest=self.request.user)

# View для списка всех отзывов
class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# View для редактирования и удаления отзывов
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
