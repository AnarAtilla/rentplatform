from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from search_service.filters import SearchAnalyticsFilter
from search_service.models import SearchAnalytics, PropertyViewAnalytics, SearchHistory, ViewHistory
from search_service.serializers import SearchAnalyticsSerializer, PropertyViewAnalyticsSerializer, SearchHistorySerializer, ViewHistorySerializer
from property_service.models import Property
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from user_service.forms import UserProfileForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Личный кабинет пользователя
@login_required
def user_dashboard(request):
    return render(request, 'user_service/dashboard.html')


# Редактирование профиля пользователя
@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш профиль был успешно обновлен!')
            return redirect('user_dashboard')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'user_service/edit_profile.html', {'form': form})


# Изменение пароля пользователя
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Ваш пароль был успешно изменен!')
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'user_service/change_password.html', {'form': form})


# История поисков пользователя
class UserSearchHistoryView(generics.ListAPIView):
    serializer_class = SearchHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SearchHistory.objects.filter(user=self.request.user)


# История просмотров пользователя
class UserViewHistoryView(generics.ListAPIView):
    serializer_class = ViewHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ViewHistory.objects.filter(user=self.request.user)


# Аналитика поисков
class SearchAnalyticsListCreateView(generics.ListCreateAPIView):
    queryset = SearchAnalytics.objects.all()
    serializer_class = SearchAnalyticsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SearchAnalyticsFilter


# Аналитика просмотров недвижимости
class PropertyViewAnalyticsListCreateView(generics.ListCreateAPIView):
    queryset = PropertyViewAnalytics.objects.all()
    serializer_class = PropertyViewAnalyticsSerializer


# Список истории поисков
class SearchHistoryListView(generics.ListAPIView):
    serializer_class = SearchHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SearchHistory.objects.filter(user=self.request.user)


# Список истории просмотров
class ViewHistoryListView(generics.ListAPIView):
    serializer_class = ViewHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ViewHistory.objects.filter(user=self.request.user)


# Логирование поисков
def log_search(user, keyword):
    search_history, created = SearchHistory.objects.get_or_create(user=user, keyword=keyword)
    if not created:
        search_history.search_count += 1
    search_history.save()


# Логирование просмотров
def log_view(user, property):
    view_history, created = ViewHistory.objects.get_or_create(user=user, property=property)
    if not created:
        view_history.view_count += 1
    view_history.save()


# Генерация рекомендаций
def get_recommendations(user):
    viewed_properties = ViewHistory.objects.filter(user=user).values_list('property', flat=True)
    search_keywords = SearchHistory.objects.filter(user=user).values_list('keyword', flat=True)

    recommendations = Property.objects.filter(
        title__icontains=search_keywords.first()
    ).exclude(id__in=viewed_properties)[:10]  # 10 рекомендованных объектов
    return recommendations


# Представление для отображения аналитики пользователя
@login_required
def user_analytics_view(request):
    search_history = SearchHistory.objects.filter(user=request.user)
    view_history = ViewHistory.objects.filter(user=request.user)

    # Генерация рекомендаций
    recommendations = get_recommendations(request.user)

    context = {
        'search_history': search_history,
        'view_history': view_history,
        'recommendations': recommendations,
    }
    return render(request, 'search_service/analytics.html', context)
