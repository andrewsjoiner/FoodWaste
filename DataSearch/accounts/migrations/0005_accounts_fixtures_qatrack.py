# Generated by Django 2.2.4 on 2019-08-02 18:18
# pylint: skip-file

import os
from django.core import serializers
from django.db import migrations, transaction
from django.db.utils import IntegrityError

fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_user = 'user.json'
fixture_accounts = 'accounts.json'

def load_fixture_custom(_apps, _schema_editor, fixture_filename):
    """Load data from a fixture when running migrations"""
    fixture_file = os.path.join(fixture_dir, fixture_filename)
    fixture = open(fixture_file, 'rb')
    objects = serializers.deserialize('json', fixture, ignorenonexistent=True)
    for obj in objects:
        try:
            with transaction.atomic():
                obj.save()
        except IntegrityError:
            pass    # Ignore if duplicate obj already exists in db
    fixture.close()


def load_fixture(_apps, _schema_editor):
    """Load data from a fixture when running migrations"""
    # Load users first
    load_fixture_custom(_apps, _schema_editor, fixture_user)
    # Then load accounts/profiles
    load_fixture_custom(_apps, _schema_editor, fixture_accounts)


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200327_1416'),
        ('branches', '0001_initial'),
        ('divisions', '0001_initial'),
        ('immediate_offices', '0001_initial'),
        ('labs', '0002_lab_designation_code'),
        ('offices', '0001_initial'),
        ('organization', '0009_auto_20190218_1816'),
        ('persons', '0004_auto_20180406_1916'),
        ('projects', '0051_remove_ordatwork'),
        ('rms', '0011_auto_20180413_2312'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
