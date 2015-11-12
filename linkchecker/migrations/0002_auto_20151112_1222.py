# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkchecker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brokenlink',
            old_name='link_to',
            new_name='object_url',
        ),
    ]
