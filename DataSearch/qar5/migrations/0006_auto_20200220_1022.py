# Generated by Django 3.0.3 on 2020-02-20 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qar5', '0005_auto_20200219_0830'),
    ]

    operations = [
        migrations.CreateModel(
            name='References',
            fields=[
                ('qapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='qar5.Qapp')),
                ('references', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='qapp',
            name='prepared_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
