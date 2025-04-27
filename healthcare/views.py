from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import HealthProfessional, MedicalAppointment
from .serializers import (
    HealthProfessionalSerializer,
    MedicalAppointmentSerializer
)

class HealthProfessionalViewSet(viewsets.ModelViewSet):
    queryset = HealthProfessional.objects.all()
    serializer_class = HealthProfessionalSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['profession']
    search_fields = ['social_name','contact']
    ordering_fields = ['social_name', 'created_at']
    ordering = ['social_name']

class MedicalAppointmentViewSet(viewsets.ModelViewSet):
    queryset = MedicalAppointment.objects.select_related('professional').all()
    serializer_class = MedicalAppointmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['professional', 'date']
    search_fields = ['patient_name','professional__social_name']
    ordering_fields = ['date', 'created_at']
    ordering = ['-date']

    def get_queryset(self):
        queryset = super().get_queryset()
        professional_id = self.request.query_params.get('professional_id')
        if professional_id:
            queryset = queryset.filter(professional_id=professional_id)
            return queryset