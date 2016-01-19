# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-18 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mturk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mturkassignment',
            name='hit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mturk_assignments', to='mturk.MTurkHIT'),
        ),
        migrations.AlterField(
            model_name='mturkhit',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='mturkhit',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mturk_hits', to='crowdsourcing.Task'),
        ),
    ]