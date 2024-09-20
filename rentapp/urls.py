from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from search_service import views  # Импортируем views из search_service

# Swagger и Redoc схема
schema_view = get_schema_view(
    openapi.Info(
        title="RentApp API",
        default_version='v1',
        description="API для системы аренды недвижимости",
        terms_of_service="https://www.rentapp.com/terms/",
        contact=openapi.Contact(email="contact@rentapp.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Функция для главной страницы
def homepage(request):
    return render(request, 'homepage.html')

# Функция для страницы "О программе"
def about_view(request):
    return render(request, 'about.html')

# URL паттерны
urlpatterns = [
    path('', homepage, name='home'),  # Главная страница
    path('about/', about_view, name='about'),  # Страница "О программе"
    path('admin/', admin.site.urls),  # Панель администратора

    # Подключение сервисов
    path('user/', include('user_service.urls')),
    path('property/', include('property_service.urls')),
    path('booking/', include('booking_service.urls')),
    path('notifications/', include('notification_service.urls')),
    path('analytics/', include('analytics_service.urls')),
    path('reviews/', include('review_service.urls')),

    # URL для аналитики пользователя
    path('user/analytics/', views.user_analytics_view, name='user_analytics'),

    # Сервис поиска
    path('search/', include('search_service.urls')),

    # Swagger и Redoc UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # API документация
    path('docs/', include_docs_urls(title='RentApp API Documentation')),
]

# Если режим DEBUG включен, добавить URL для статических и медиа файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
