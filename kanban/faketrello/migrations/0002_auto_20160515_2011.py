# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faketrello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faketrello',
            name='priority',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]