# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mamdaniAllocator', '0002_ramusage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPUusage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage', models.IntegerField()),
                ('SMALL', models.IntegerField(default=0)),
                ('MEDIUM', models.IntegerField(default=0)),
                ('LARGE', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Diskusage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage', models.IntegerField()),
                ('SMALL', models.IntegerField(default=0)),
                ('MEDIUM', models.IntegerField(default=0)),
                ('LARGE', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='ramusage',
            name='usage',
            field=models.IntegerField(),
        ),
    ]
