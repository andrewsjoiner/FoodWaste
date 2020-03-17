# Generated by Django 3.0.3 on 2020-03-17 16:17

import constants.utils
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowsa', '0005_auto_20200316_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/uploads', location='/home/user/Repos/DataSearch/FoodWaste/DataSearch/DataSearch/uploads'), upload_to=constants.utils.get_flowsa_storage_path),
        ),
    ]
