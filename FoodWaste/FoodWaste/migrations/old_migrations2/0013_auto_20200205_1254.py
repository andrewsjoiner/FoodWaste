# Generated by Django 3.0.2 on 2020-02-05 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FoodWaste', '0012_qualityassuranceprojectplan_tracking_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QualityAssuranceProjectPlan',
            new_name='Qapp',
        ),
        migrations.RenameModel(
            old_name='QualityAssuranceProjectLead',
            new_name='QappLead',
        ),
    ]
