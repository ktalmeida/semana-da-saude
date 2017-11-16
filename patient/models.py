from django.db import models
from datetime import datetime


CHARACTER_CHOICES = ['ELETIVO', 'URGÊNCIA']
REFERAL_PLACES = ['Clínica da família', 'Policlínica Piquet Carneiro', 'Outro']

class Patient(models.Model):
    """Patient model"""
    name = models.CharField(max_length=100, verbose_name="Nome do paciente")
    mother_name = models.CharField(max_length=100, verbose_name="Nome da mãe")
    address = models.CharField(max_length=300, verbose_name="Endereço")
    phone = models.CharField(max_length=100, verbose_name="Telefone")
    birthdate = models.DateField(verbose_name="Data de nascimento")
    exame_number = models.CharField(
        verbose_name="Número do exame laboratorial", max_length=40,
        null=True, blank=True)
    notes = models.CharField(
        max_length=300, verbose_name="Observações", null=True, blank=True)
    prostate_history = models.NullBooleanField(
        verbose_name="Tem alguém na família com problemas na próstata")
    trouble_urinating = models.NullBooleanField(
        verbose_name="Problemas para urinar?")
    suspicious_nodule = models.NullBooleanField(
        verbose_name="Possui nódulo suspeito?")

    has_referral = models.NullBooleanField(
        verbose_name="Encaminhamento", default=False)

    referral_character = models.CharField(
        max_length=100,
        verbose_name="Caráter",
        null=True,
        blank=True,
        choices=[(str(i), CHARACTER_CHOICES[i]) for i in range(len(CHARACTER_CHOICES))])

    referral_place = models.CharField(
        max_length=100,
        verbose_name="Local de encaminhamento",
        null=True,
        blank=True,
        choices=[(str(i), REFERAL_PLACES[i]) for i in range(len(REFERAL_PLACES))])

    other_referral_place = models.CharField(
        max_length=100, verbose_name="Especificar local",
        null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_age(self):
        today = datetime.now().date()
        age = today.year - self.birthdate.year
        if today.month < self.birthdate.month:
            age = age - 1
        elif today.month == self.birthdate.month and \
                today.day >= self.birthdate.day:
            age = age - 1
        return age


    class Meta:
        ordering = ['-created_at']
