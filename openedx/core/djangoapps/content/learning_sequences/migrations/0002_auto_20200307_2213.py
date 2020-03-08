# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-07 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_sequences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseoutline',
            name='learning_context',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_outline', to='learning_sequences.LearningContext', unique=True),
        ),
    ]
