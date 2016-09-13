# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('image', models.ImageField(upload_to='client/images')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=512)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('short_desc', models.CharField(max_length=256)),
                ('desc', models.TextField()),
                ('project_start', models.DateField(blank=True, null=True)),
                ('project_end', models.DateField(blank=True, null=True)),
                ('location', models.CharField(max_length=256)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='home.Client')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('primary', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='projects/images')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=128)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='services/images')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('visible', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to='slider/images')),
                ('short_desc', models.CharField(blank=True, max_length=256, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.Slider')),
            ],
        ),
    ]
