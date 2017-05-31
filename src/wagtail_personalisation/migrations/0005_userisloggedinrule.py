# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-11 12:15
from __future__ import unicode_literals

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_personalisation', '0004_segment_persistent'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIsLoggedInRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_logged_in', models.BooleanField(default=False)),
                ('segment', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_personalisation_userisloggedinrule_related', related_query_name='wagtail_personalisation_userisloggedinrules', to='wagtail_personalisation.Segment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]