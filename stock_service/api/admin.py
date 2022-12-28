# register models for admin interface
from api.models import RequestLog
from django.contrib import admin


@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'status', 'date', 'user', 'extra_data')
