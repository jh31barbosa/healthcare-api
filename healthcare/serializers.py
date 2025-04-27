from rest_framework import serializers
from .models import HealthProfessional, MedicalAppointment

class HealthProfessionalSerializer(serializers.ModelSerializer):
    profession_display = serializers.CharField(
        source='get_profession_display',
        read_only=True
    )

    class Meta:
        model = HealthProfessional
        fields = [
            'id',
            'social_name',
            'profession_display',
            'address',
            'contact',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at','updated_at']

class MedicalAppointmentSerializer(serializers.ModelSerializer):
    professional = HealthProfessionalSerializer(read_only=True)
    professional_id = serializers.PrimaryKeyRelatedField(
        queryset=HealthProfessional.objects.all(),
        source='professional',
        write_only=True
    )

    class Meta:
        model = MedicalAppointment
        fields = [
            'id',
            'professional',
            'professional_id',
            'date',
            'patient_name'
            'notes',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate_date(self, value):
        if value.date() < timezone.now().date():
            raise serializers.ValidationError("A data da consulta não pode ser no passado")
        return value