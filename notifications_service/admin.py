from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'recipient_type', 'message', 'created_at', 'read')
    list_filter = ('recipient_type', 'read', 'created_at')
    search_fields = ('recipient__email', 'message')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    def __str__(self):
        return self.message