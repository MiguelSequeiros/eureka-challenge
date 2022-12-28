# encoding: utf-8
import logging
from decimal import Decimal

from api.exceptions import ErrorResponse
from api.models import RequestLog
from api.serializers import RequestLogSerializer, StockPriceSerializer
from api.stock_info_providers.alphavantage.api_client import AlphavantageApiClient
from api.utils import retrieve_last_two_days
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class StockPriceView(APIView):
    """
    View to retrieve the stock price for a given symbol.
    """
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    @swagger_auto_schema(
        operation_description="Retrieve the stock price for a given symbol.",
        responses={
            200: StockPriceSerializer,
            400: "Missing symbol in query params.",
        },
        manual_parameters=[
            openapi.Parameter(
                'symbol',
                openapi.IN_QUERY,
                description="Stock symbol",
                type=openapi.TYPE_STRING
            )
        ]
    )
    def get(self, request, format=None):
        """
        Retrieve the stock price for a given symbol.
        """
        symbol = request.query_params.get('symbol', None)
        request_log = RequestLog(
            user=request.user,
            symbol=symbol,
        )
        # at least symbol is required
        if symbol is None:
            raise ValidationError("Missing symbol in query params.")

        # performs the request to the third api
        try:
            stock_info_from_api = AlphavantageApiClient().get_stock_info({
                "symbol": symbol,
            })
            last_day, previous_day = retrieve_last_two_days(stock_info_from_api)
        except ErrorResponse as e:
            raise ValidationError(e)

        # calculates the variation between the last two days
        last_day['variation'] = Decimal(last_day['close']) - Decimal(previous_day['close'])

        request_log.status = RequestLog.STATUS_SUCCESS
        request_log.save()

        return Response(
            status=200,
            data=StockPriceSerializer(last_day).data
        )


class RequestLogsView(APIView):
    """
    View to retrieve the logs.
    """
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        queryset = RequestLog.objects.all()
        serializer = RequestLogSerializer(queryset, many=True)
        return Response(serializer.data)
