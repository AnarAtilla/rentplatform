from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from booking_service.models import Booking
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=Booking)
def booking_saved(sender, instance, created, **kwargs):
    """
    Отправляет уведомление арендодателю после создания нового бронирования.
    """
    if created:
        send_mail(
            subject='Новое бронирование!',
            message=f'Пользователь {instance.guest.email} забронировал объект "{instance.property.title}".',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.property.owner.email],
            fail_silently=False,
        )
