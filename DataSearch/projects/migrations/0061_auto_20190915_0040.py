# Generated by Django 2.2.3 on 2019-09-15 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0060_projectlog_update_history_review_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='nrmrl_qapp_requirement',
            field=models.ManyToManyField(blank=True, to='projects.NRMRLQAPPRequirement'),
        ),
        migrations.AlterField(
            model_name='project',
            name='programs',
            field=models.ManyToManyField(blank=True, to='projects.Program'),
        ),
    ]
