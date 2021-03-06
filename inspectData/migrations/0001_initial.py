# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestHealth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspection_uid', models.IntegerField()),
                ('inspection_status', models.BooleanField()),
                ('facility_name', models.CharField(max_length=200)),
                ('address_field', models.CharField(max_length=200)),
                ('cuisine', models.CharField(max_length=200)),
            ],
        ),
    ]
