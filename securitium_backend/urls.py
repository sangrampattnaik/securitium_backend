from django.urls import path, include,re_path
from django.contrib import admin
from users import views
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="SSecuritium back end test API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('person', views.PersonAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(router.urls)),
]

if settings.DEBUG:

    api_urls = [
        re_path(r'^swagger/$', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),
    ]
    urlpatterns += api_urls