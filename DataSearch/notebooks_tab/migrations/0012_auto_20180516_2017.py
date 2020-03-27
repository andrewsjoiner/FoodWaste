# Generated by Django 2.0.5 on 2018-05-16 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks_tab', '0011_auto_20180515_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebookstabreviewattachment',
            name='include_in_email',
            field=models.CharField(choices=[('', ''), ('Y', 'Yes'), ('N', 'No')], default='N', max_length=2),
        ),
        migrations.AddField(
            model_name='notebookstabreviewattachment',
            name='is_review_file',
            field=models.CharField(choices=[('', ''), ('Y', 'Yes'), ('N', 'No')], default='N', max_length=2),
        ),
    ]
