# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrokenLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entity', models.CharField(default='', max_length=255, verbose_name='Entity', blank=True)),
                ('field_name', models.CharField(default='', max_length=200, verbose_name='Field', blank=True)),
                ('last_checked', models.DateTimeField(auto_now_add=True, verbose_name='last_checked')),
                ('url', models.URLField(max_length=5000, verbose_name='Broken link')),
                ('status_code', models.PositiveSmallIntegerField(null=True, verbose_name='Status code', blank=True)),
                ('link_to', models.URLField(null=True, verbose_name='Go to Object', blank=True)),
            ],
            options={
                'ordering': ('-last_checked',),
                'verbose_name': 'Broken link',
                'verbose_name_plural': 'Broken links',
            },
        ),
    ]
