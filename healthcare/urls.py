from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HealthProfessionalViewSet, MedicalAppointmentViewSet

router = DefaultRouter()
router.register(r'professionals', HealthProfessionalViewSet)

urlpatterns = [
    path('', include(router.urls))
]