# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 23:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_cancion', models.CharField(max_length=500)),
                ('artista', models.CharField(max_length=250)),
                ('audio', models.FileField(default='', upload_to='')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_lista', models.CharField(max_length=500)),
                ('artista', models.CharField(max_length=250)),
                ('cancion', models.ManyToManyField(default=None, to='MyMusic.Cancion')),
                ('user_l', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
