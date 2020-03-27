# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_division_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
