# encoding: utf-8

from django.contrib.auth import get_user_model
from django.db import models

AppUser = get_user_model()

STATUS_CHOICES = (
    ('COM', 'Success'),
    ('ERR', 'Error'),
)


class RequestLog(models.Model):
    """
    Model to store the requests done by each user.
    """
    STATUS_ERROR = 'ERR'
    STATUS_SUCCESS = 'COM'

    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    symbol = models.CharField(max_length=20, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3, null=True)
    extra_data = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-date']
        indexes = [
            models.Index(fields=['symbol']),
        ]
