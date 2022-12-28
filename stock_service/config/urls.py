# encoding: utf-8

from api import views as api_views
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.contrib import admin
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="Stock API",
        default_version="v1",
        description="Simple api to retrieve stock data",
        contact=openapi.Contact(email="miguel.sequeiros.net@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[JWTAuthentication]
)

swagger_urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]

auth_urlpatterns = [
    path('register', RegisterView.as_view(), name="user-auth-registration"),
    path('login', LoginView.as_view(), name="user-login"),
    path('logout', LogoutView.as_view(), name='user-logout'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('password/reset', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("stock-info/", api_views.StockPriceView.as_view()),
] + swagger_urlpatterns + auth_urlpatterns
