from django.db import models


CHARACTER_CHOICES = ['ELETIVO', 'URGÊNCIA']
REFERAL_PLACES = ['Clínica da família', 'Policlínica Piquet Carneiro', 'Outro']

class Patient(models.Model):
    """Patient model"""
    name = models.CharField(max_length=100, verbose_name="Nome do paciente")
    mother_name = models.CharField(max_length=100, verbose_name="Nome da mãe")
    address = models.CharField(max_length=300, verbose_name="Endereço")
    phone = models.CharField(max_length=100, verbose_name="Telefone")
    birthdate = models.DateField(verbose_name="Data de nascimento")
    notes = models.CharField(
        max_length=300, verbose_name="Observações", null=True)
    prostate_history = models.NullBooleanField(
        verbose_name="Tem alguém na família com problemas na próstata")
    trouble_urinating = models.NullBooleanField(
        verbose_name="Problemas para urinar?")
    suspicious_nodule = models.NullBooleanField(
        verbose_name="Possui nódulo suspeito?")
    has_referral = models.NullBooleanField(verbose_name="Encaminhamento")

    referral_character = models.CharField(
        max_length=100,
        verbose_name="Caráter",
        choices=[(str(i), CHARACTER_CHOICES[i]) for i in range(len(CHARACTER_CHOICES))])

    referral_place = models.CharField(
        max_length=100,
        verbose_name="Local de encaminhamento",
        choices=[(str(i), REFERAL_PLACES[i]) for i in range(len(REFERAL_PLACES))])
    other_referral_place = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
