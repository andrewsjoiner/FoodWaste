# Generated by Django 2.1.2 on 2018-11-14 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_office_designation_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
