# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GrabHindiSongs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hindisong',
            name='album',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='GrabHindiSongs.HindiSongAlbum'),
        ),
    ]
