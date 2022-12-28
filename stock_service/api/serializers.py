# encoding: utf-8

from api.models import RequestLog
from rest_framework import serializers


class RequestLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestLog
        exclude = ['id', 'user_id', 'symbol', 'status', 'extra_data']


class StockPriceSerializer(serializers.Serializer):
    open = serializers.DecimalField(max_digits=14, decimal_places=4, read_only=True)
    high = serializers.DecimalField(max_digits=14, decimal_places=4, read_only=True)
    low = serializers.DecimalField(max_digits=14, decimal_places=4, read_only=True)
    close = serializers.DecimalField(max_digits=14, decimal_places=4, read_only=True)
    variation = serializers.DecimalField(max_digits=14, decimal_places=4, read_only=True)
