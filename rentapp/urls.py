from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger/OpenAPI schema setup
schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="API documentation for Your Project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourproject.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),

    # Маршруты для API
    path('api/user/', include('user_service.urls')),
    path('api/property/', include('property_service.urls')),
    path('api/booking/', include('booking_service.urls')),
    path('api/notifications/', include('notifications_service.urls')),
    path('api/analytics/', include('analytics_service.urls')),
    path('api/reviews/', include('review_service.urls')),

    # Swagger и ReDoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Маршруты для HTML (шаблоны)
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('notifications/', views.notification_list, name='notification_list'),

    # Маршруты для объектов недвижимости
    path('properties/', views.property_list, name='property_list'),
    path('properties/add/', views.property_create, name='property_create'),
    path('properties/edit/<int:pk>/', views.property_edit, name='property_edit'),
    path('properties/delete/<int:pk>/', views.property_delete, name='property_delete'),
    path('properties/<int:pk>/', views.property_detail, name='property_detail'),

    # Маршрут для создания бронирования
    path('properties/<int:property_id>/booking/', views.create_booking, name='create_booking'),

    # Маршруты для подтверждения/отмены бронирования
    path('booking/confirm/<int:booking_id>/', views.confirm_booking, name='confirm_booking'),
    path('booking/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('bookings/success/<int:booking_id>/', views.booking_success, name='booking_success'),

    # Django-Allauth
    path('accounts/', include('allauth.urls')),

    # Дополнительные страницы
    path('dashboard/', views.dashboard, name='user_dashboard'),
    path('analytics/', views.analytics, name='analytics'),
    path('search/', views.search_results, name='search_results'),
]

# Настройки для статических и медиа файлов
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
