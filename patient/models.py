from django.db import models


class Patient(models.Model):
    """Patient model"""
    class Meta:
        ordering = ['-created_at']

    name = models.CharField(max_length=100, verbose_name="Nome do paciente")
    address = models.CharField(max_length=300, verbose_name="Endereço")
    phone = models.CharField(max_length=100, verbose_name="Telefone")
    birthdate = models.DateField(verbose_name="Data de nascimento")
    prostate_history = models.NullBooleanField(
        verbose_name="Tem alguém na família com problemas na próstata")
    trouble_urinating = models.NullBooleanField(
        verbose_name="Problemas para urinar?")
    suspicious_nodule = models.NullBooleanField(
        verbose_name="Possui nódulo suspeito?")
    notes = models.CharField(
        max_length=300, verbose_name="Observações", null=True)
    created_at = models.DateTimeField(auto_now_add=True)


