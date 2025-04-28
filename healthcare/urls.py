from rest_framework.routers import DefaultRouter
from .views import HealthProfessionalViewSet, MedicalAppointmentViewSet

router = DefaultRouter()
router.register(r'professionals', HealthProfessionalViewSet, basename='professional')
router.register(r'appointments', MedicalAppointmentViewSet, basename='appointment')

urlpatterns = router.urls