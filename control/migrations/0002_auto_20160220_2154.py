# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inacistencia',
            name='estado',
            field=models.CharField(blank=True, choices=[('1', 'ASISTENTE PUNTUAL'), ('2', 'INASISTENCIA JUSTIFICADA'), ('3', 'INASISTENCIA INJUSTIFICADA'), ('4', 'ASISTENTE RETARDO')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='inacistencia',
            name='tipo',
            field=models.CharField(blank=True, choices=[('1', 'ASISTENTE PUNTUAL'), ('2', 'INASISTENCIA JUSTIFICADA'), ('3', 'INASISTENCIA INJUSTIFICADA'), ('4', 'ASISTENTE RETARDO')], max_length=2, null=True),
        ),
    ]
