from django.urls import path
from review_service import views

urlpatterns = [
    path('create/', views.ReviewCreateView.as_view(), name='create_review'),
    path('list/', views.ReviewListView.as_view(), name='list_review'),
    path('<int:pk>/', views.ReviewDetailView.as_view(), name='detail_review'),
]
