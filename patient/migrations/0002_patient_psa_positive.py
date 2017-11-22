# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='psa_positive',
            field=models.NullBooleanField(default=False, verbose_name='Exame de PSA Positivo?'),
        ),
    ]
