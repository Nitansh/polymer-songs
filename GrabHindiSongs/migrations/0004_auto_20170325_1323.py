# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrabHindiSongs', '0003_auto_20170224_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='hindisongalbum',
            name='album_type',
            field=models.TextField(default='hindi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hindisongartist',
            name='artist_type',
            field=models.TextField(default='hindi'),
            preserve_default=False,
        ),
    ]
