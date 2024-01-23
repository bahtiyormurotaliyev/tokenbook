<<<<<<< HEAD
from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('data', GetMethod, basename='data')
urlpatterns = router.urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, HaridListView

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('haridlar/<int:customer_id>/', HaridListView.as_view({'get': 'list'}), name='haridlar-list'),
]

urlpatterns += router.urls
=======
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="352a3225-a8d8-4823-bd41-4288f1b3f2d8",
        default_version="v1",
        description="Sizning API-niz uchun Swagger skhema",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("your_app.urls")),  # your_app ning yo'lidan o'zgartiring
    url(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    url(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    url(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
>>>>>>> 1c6cdc514e0bb30688edc5859b6680c1478779fd
