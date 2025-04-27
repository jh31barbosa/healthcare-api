from django.db import models

from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

class HealthProfessional(models.Model):
    class Profession(models.TextChoices):
        DOCTOR = 'DR', _('Médico(a)') 
        NURSE =  'NR', _('Enfermeiro(a)')
        PSYCHOLOGIST = 'PS', _('Psicólogo(a)')
        DENTIST = 'DT', _('Dentista')
        NUTRITIONIST = 'NT', _('Nutricionista')

    social_name = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(2)],
        verbose_name=_('Nome Social')
    )
    profession = models.CharField(
        max_length=2,
        choices=Profession.choices,
        verbose_name=_('Profissão')
    )
    address = models.TextField(verbose_name=_('Endereço'))
    contact = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(8)],
        verbose_name=_('Contato')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Profissional de Saúde')
        verbose_name_plural = _('Profissional de Saúde')
        ordering = ['social_name']

    def __str__(self):
        return f"{self.social_name}({self.get_profession_display()})"

class MedicalAppointment(models.Model):
    professional = models.ForeignKey(
        HealthProfessional,
        on_delete=models.PROTECT,
        related_name='appointments',
        verbose_name=_('Professional')
    )
    date = models.DateTimeField(verbose_name=_('Data e Hora'))
    patient_name = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(2)],
        verbose_name=_('Nome do Paciente')
    )
    notes = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Observações')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Consulta Médica')
        verbose_name_plural = _('Consultas Médicas')
        ordering = ['-date']

    def __str__(self):
        return f"Consulta com {self.professional} em {self.date}"
        