# models.py (scifinder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301,E1101,W0611,C0411


"""Definition of models."""

from django.db import models
from constants.utils import get_scifinder_storage_path
from teams.models import User

class Upload(models.Model):
    """
    Class representing a scifinder file Upload.
    These files are stored in the MEDIA directory, but references
    to the location and other metadata are stored in the database.
    """
    name = models.CharField(max_length=255, blank=True)
    file = models.FileField(null=True, blank=True,
                            upload_to=get_scifinder_storage_path)
    uploaded_by = models.ForeignKey(User, blank=False,
                                    related_name='scifinder_uploaded_by',
                                    on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Override str method to display name instead of stringified obj."""
        return self.name