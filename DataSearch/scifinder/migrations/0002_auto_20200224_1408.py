# Generated by Django 3.0.3 on 2020-02-24 19:08

import constants.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scifinder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=constants.utils.get_scifinder_storage_path),
        ),
    ]
