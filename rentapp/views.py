from booking_service.models import Booking
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from notifications_service.models import Notification
from property_service.forms import PropertyForm
from property_service.models import Property
from datetime import datetime
from django.contrib import messages


# Главная страница с фильтром и 5 объектами недвижимости
def home(request):
    properties = Property.objects.all()[:5]
    property_types = Property.PROPERTY_TYPES  # Передаём список типов недвижимости

    return render(request, 'base/index.html', {
        'properties': properties,
        'property_types': property_types,  # Передаём список типов недвижимости
        'title': 'Welcome to RentApp',
    })


# Страница "О нас"
def about(request):
    return render(request, 'base/about.html', {
        'title': 'About Us',
    })


# Страница контактов
def contact(request):
    return render(request, 'base/contact.html', {
        'title': 'Contact Us',
    })


# Личный кабинет пользователя
@login_required
def profile(request):
    bookings = Booking.objects.filter(guest=request.user)
    notifications = Notification.objects.filter(recipient=request.user, read=False)
    return render(request, 'base/profile.html', {
        'bookings': bookings,
        'notifications': notifications,
        'title': 'Your Profile',
    })


# Панель управления для владельцев недвижимости
@login_required
def dashboard(request):
    properties = Property.objects.filter(owner=request.user)
    return render(request, 'dashboard/dashboard_home.html', {
        'properties': properties,
        'title': 'Dashboard',
    })


# Список объектов недвижимости пользователя
@login_required
def property_list(request):
    properties = Property.objects.filter(owner=request.user)
    return render(request, 'properties/property_list.html', {
        'properties': properties,
        'title': 'Your Properties',
    })


# Добавление объекта недвижимости
@login_required
def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property_obj = form.save(commit=False)
            property_obj.owner = request.user
            property_obj.save()
            return redirect('property_list')
    else:
        form = PropertyForm()

    return render(request, 'properties/property_create.html', {'form': form})


# Редактирование объекта недвижимости
@login_required
def property_edit(request, pk):
    property_obj = get_object_or_404(Property, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_obj)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property_obj)

    return render(request, 'properties/property_edit.html', {'form': form})


# Удаление объекта недвижимости
@login_required
def property_delete(request, pk):
    property_obj = get_object_or_404(Property, pk=pk, owner=request.user)

    if request.method == 'POST':
        property_obj.delete()
        return redirect('property_list')

    return render(request, 'properties/property_delete.html', {
        'property': property_obj,
    })


# Подробности объекта недвижимости
def property_detail(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)

    # Вычисляем максимальное количество гостей (например, 2 гостя на каждую комнату)
    max_guests = property_obj.rooms * 2

    # Проверяем, что текущий пользователь является владельцем объекта
    if request.user == property_obj.owner:
        # Получаем бронирования со статусом 'pending'
        pending_bookings = Booking.objects.filter(rental_property=property_obj, status='pending')
    else:
        pending_bookings = None

    return render(request, 'properties/property_detail.html', {
        'property': property_obj,
        'pending_bookings': pending_bookings,
        'max_guests': max_guests,  # Передаем максимальное количество гостей в шаблон
    })


# Представление для поиска недвижимости с фильтрацией
def search_results(request):
    location = request.GET.get('location')
    property_type = request.GET.get('property_type')
    checkin = request.GET.get('checkin')
    checkout = request.GET.get('checkout')

    # Преобразуем даты в формат Python
    try:
        checkin = datetime.strptime(checkin, '%Y-%m-%d').date()
        checkout = datetime.strptime(checkout, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        checkin = checkout = None

    # Начальная выборка всех объектов недвижимости
    properties = Property.objects.all()

    # Фильтрация по местоположению
    if location:
        properties = properties.filter(location__icontains=location)

    # Фильтрация по типу недвижимости
    if property_type:
        properties = properties.filter(property_type=property_type)

    # Фильтрация по датам бронирования
    if checkin and checkout:
        # Исключаем объекты с пересекающимися бронированиями
        properties = properties.exclude(
            id__in=Booking.objects.filter(
                check_in__lt=checkout,
                check_out__gt=checkin,
                status='confirmed'
            ).values_list('rental_property_id', flat=True)
        )

        # Проверяем доступность по ограничениям владельца
        properties = [p for p in properties if p.is_available_for_dates(checkin, checkout)]

    # Передаем список типов недвижимости и результаты поиска
    context = {
        'properties': properties,
        'property_types': Property.PROPERTY_TYPES,
    }

    return render(request, 'search/search_results.html', context)


# Список бронирований пользователя
@login_required
def booking_list(request):
    bookings = Booking.objects.filter(guest=request.user)
    return render(request, 'bookings/booking_list.html', {
        'bookings': bookings,
        'title': 'Your Bookings',
    })


# Список уведомлений пользователя
@login_required
def notification_list(request):
    notifications = Notification.objects.filter(recipient=request.user)
    return render(request, 'notifications/notification_list.html', {
        'notifications': notifications,
        'title': 'Your Notifications',
    })


# Пример представления для получения аналитики
@login_required
def analytics(request):
    properties = Property.objects.filter(owner=request.user)
    bookings = Booking.objects.filter(rental_property__in=properties)
    total_views = Property.objects.filter(owner=request.user).count()

    context = {
        'properties': properties,
        'bookings': bookings,
        'total_views': total_views,
    }
    return render(request, 'analytics/analytics.html', context)


# Вспомогательная функция для отметки всех уведомлений как прочитанных
@login_required
def mark_all_notifications_as_read(request):
    notifications = Notification.objects.filter(recipient=request.user, read=False)
    notifications.update(read=True)
    return redirect('profile')


# Создание бронирования
@login_required
def create_booking(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')

        try:
            checkin = datetime.strptime(checkin, '%Y-%m-%d').date()
            checkout = datetime.strptime(checkout, '%Y-%m-%d').date()

            if checkin >= checkout:
                messages.error(request, "Дата заезда должна быть раньше даты выезда.")
                return redirect('property_detail', pk=property_obj.id)

            # Проверяем, нет ли пересекающихся бронирований
            existing_bookings = Booking.objects.filter(
                rental_property=property_obj,
                check_in__lt=checkout,
                check_out__gt=checkin,
                status='confirmed'
            )
            if existing_bookings.exists():
                messages.error(request, "На эти даты жильё уже забронировано.")
                return redirect('property_detail', pk=property_obj.id)

            # Создаем бронирование
            booking = Booking.objects.create(
                rental_property=property_obj,
                guest=request.user,
                check_in=checkin,
                check_out=checkout,
                total_price=(checkout - checkin).days * property_obj.price,
                status='pending'  # Ставим статус ожидания подтверждения
            )
            messages.success(request, "Бронирование успешно создано и ожидает подтверждения.")
            return redirect('booking_success', booking_id=booking.id)

        except ValueError:
            messages.error(request, "Некорректные данные для даты.")
            return redirect('property_detail', pk=property_obj.id)

    return redirect('property_detail', pk=property_obj.id)


# Бронирования для владельца
@login_required
def owner_bookings(request):
    bookings = Booking.objects.filter(rental_property__owner=request.user, status='pending')
    return render(request, 'bookings/owner_bookings.html', {
        'bookings': bookings,
        'title': 'Ваши бронирования'
    })


# Подтверждение бронирования
@login_required
def confirm_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, rental_property__owner=request.user)

    if request.method == 'POST':
        booking.status = 'confirmed'
        booking.save()
        messages.success(request, f'Бронирование для {booking.guest.email} подтверждено.')
        return redirect('owner_bookings')

    return render(request, 'bookings/confirm_booking.html', {'booking': booking})


# Отмена бронирования
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, rental_property__owner=request.user)

    if request.method == 'POST':
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, f'Бронирование для {booking.guest.email} отклонено.')
        return redirect('owner_bookings')

    return render(request, 'bookings/cancel_booking.html', {'booking': booking})

@login_required
def booking_success(request, booking_id):
    """
    Отображает страницу успешного бронирования.
    """
    booking = get_object_or_404(Booking, id=booking_id, guest=request.user)
    return render(request, 'bookings/booking_success.html', {'booking': booking})

