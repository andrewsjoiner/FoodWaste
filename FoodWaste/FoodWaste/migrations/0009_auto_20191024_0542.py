# Generated by Django 2.2.6 on 2019-10-24 09:42

import FoodWaste.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FoodWaste', '0008_auto_20191023_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(blank=True, null=True, upload_to=FoodWaste.models.get_attachment_storage_path)),
            ],
        ),
        migrations.CreateModel(
            name='DataAttachmentMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachment_secondary_data', to='FoodWaste.Attachment')),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary_data_attachments', to='FoodWaste.TrackingTool')),
            ],
        ),
        migrations.AddField(
            model_name='trackingtool',
            name='attachments',
            field=models.ManyToManyField(through='FoodWaste.DataAttachmentMap', to='FoodWaste.Attachment'),
        ),
    ]