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
