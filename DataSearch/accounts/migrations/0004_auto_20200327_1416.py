# Generated by Django 3.0.4 on 2020-03-27 18:16

import accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0009_auto_20190218_1816'),
        ('accounts', '0003_auto_20190802_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDropdownInfo',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'db_table': 'app_user_dropdown',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=255, null=True)),
                ('last_modified_by', models.CharField(blank=True, max_length=255, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to=accounts.models.get_contact_request_path)),
                ('the_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email_address', models.CharField(blank=True, max_length=255, null=True)),
                ('greenscope_response', models.CharField(blank=True, max_length=255, null=True)),
                ('response_date', models.DateField(blank=True, null=True)),
                ('the_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequestSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=255, null=True)),
                ('last_modified_by', models.CharField(blank=True, max_length=255, null=True)),
                ('the_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email_address', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.CharField(blank=True, choices=[('', ''), ('Y', 'Yes'), ('N', 'No')], max_length=5, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='state',
            name='country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='address_line1',
            new_name='mail_to_address',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='city',
            new_name='mail_to_city',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='zipcode',
            new_name='mail_to_zipcode',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address_line2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='affiliation',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='job_title',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_modified',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='state',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=accounts.models.get_profile_photo_storage_path),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Branch'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='can_create_users',
            field=models.CharField(blank=True, choices=[('', ''), ('Y', 'Yes'), ('N', 'No')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='can_edit',
            field=models.CharField(blank=True, choices=[('', ''), ('Y', 'Yes'), ('N', 'No')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='code_kept',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='created_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_epa_separation',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='display_in_dropdowns',
            field=models.CharField(choices=[('', ''), ('Y', 'Yes'), ('N', 'No')], db_index=True, default='Y', max_length=2),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Division'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email_address_epa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email_address_other',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_reviewer',
            field=models.CharField(blank=True, choices=[('', ''), ('Y', 'Yes'), ('N', 'No')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_technical_lead',
            field=models.CharField(blank=True, choices=[('', ''), ('Y', 'Yes'), ('N', 'No')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lab',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Lab'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_modified_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mail_to_mailstop',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mail_to_name',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mail_to_note',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mail_to_state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Office'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='permissions',
            field=models.CharField(choices=[('READER', 'READER'), ('EDITOR', 'EDITOR'), ('ADMIN', 'ADMIN')], default='READER', max_length=45),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='telephone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='telephone_extension',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_branch_one',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_division_one',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_lab_one',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('', ''), ('SUPER', 'SUPER USER'), ('ALL', 'ALL LABS'), ('LAB', 'SINGLE LAB'), ('DIVISION', 'DIVISION USER'), ('BRANCH', 'BRANCH USER')], max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='Sector',
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.AddField(
            model_name='contactrequest',
            name='request_subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.RequestSubject'),
        ),
    ]
