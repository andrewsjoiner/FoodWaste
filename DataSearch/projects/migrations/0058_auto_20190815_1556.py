# Generated by Django 2.2.3 on 2019-08-15 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0057_project_update_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_update_history',
            name='projectlead',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projhist_lead', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project_update_history',
            name='qa_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projhist_qa_manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ProjectLog_update_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('modified', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('created_by', models.CharField(blank=True, max_length=255, null=True)),
                ('last_modified_by', models.CharField(blank=True, max_length=255, null=True)),
                ('date_approved', models.DateField(blank=True, db_index=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('project_log', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.ProjectLog')),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projloghist_reviewer', to=settings.AUTH_USER_MODEL)),
                ('technical_lead', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projloghist_lead', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projloghist_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
