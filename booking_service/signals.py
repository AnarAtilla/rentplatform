from django.db.models.signals import post_save
from django.dispatch import receiver
from booking_service.models import Booking
from django.core.mail import send_mail
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()


@receiver(post_save, sender=Booking)
def booking_saved_or_updated(sender, instance, created, **kwargs):
    """
    Обрабатывает создание нового бронирования и обновление его статуса.
    """
    try:
        if created:
            # Сформируем ссылку для подтверждения бронирования
            confirm_url = f"{settings.SITE_URL}/bookings/{instance.id}/confirm/"

            # Уведомление владельцу недвижимости о новом бронировании
            send_mail(
                subject='Новое бронирование!',
                message=f'Пользователь {instance.guest.email} забронировал объект "{instance.rental_property.title}". '
                        f'Подтвердите бронирование по ссылке: {confirm_url}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[instance.rental_property.owner.email],
                fail_silently=False,
            )

            # Уведомление гостю о том, что его бронирование ожидает подтверждения
            send_mail(
                subject='Бронирование в ожидании!',
                message=f'Ваше бронирование объекта "{instance.rental_property.title}" находится в ожидании подтверждения владельцем.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[instance.guest.email],
                fail_silently=False,
            )

            # Устанавливаем срок для подтверждения бронирования владельцем
            instance.confirmation_deadline = timezone.now() + timedelta(hours=2)
            instance.save()

        # Проверяем изменения статуса и отправляем соответствующие уведомления
        elif not created and 'status' in instance.get_dirty_fields():
            if instance.status == 'confirmed':
                # Уведомление гостю о подтверждении бронирования
                send_mail(
                    subject='Бронирование подтверждено!',
                    message=f'Ваше бронирование объекта "{instance.rental_property.title}" подтверждено владельцем.',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[instance.guest.email],
                    fail_silently=False,
                )
            elif instance.status == 'cancelled':
                # Уведомление гостю о том, что бронирование было отклонено
                send_mail(
                    subject='Бронирование отклонено',
                    message=f'Ваше бронирование объекта "{instance.rental_property.title}" было отклонено владельцем.',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[instance.guest.email],
                    fail_silently=False,
                )
    except Exception as e:
        # Логируем исключения, чтобы в случае ошибок уведомления не нарушали работу системы
        print(f"Ошибка при отправке email: {e}")
