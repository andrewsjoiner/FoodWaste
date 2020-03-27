# Generated by Django 2.0.5 on 2018-06-04 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20180525_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('', ''), ('SUPER', 'SUPER USER'), ('ALL', 'ALL LABS'), ('LAB', 'SINGLE LAB'), ('DIVISION', 'DIVISION USER'), ('BRANCH', 'BRANCH USER')], max_length=45, null=True),
        ),
    ]
