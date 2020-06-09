# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-23 10:50
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0002_bidding_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidding',
            name='bids',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)]),
            preserve_default=False,
        ),
    ]