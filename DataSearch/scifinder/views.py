# views.py (scifinder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301,E1101,R0901,W0613,W0622,C0411


"""Definition of views."""

from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from scifinder.forms import UploadForm
from scifinder.models import Upload


class ScifinderIndex(LoginRequiredMixin, TemplateView):
    """
    Class to return the main scifinder page along with a list of all
    scifinder uploaded files available to this user as well as a form for
    uploading new scifinder files. This class also handles the POSTs
    for new file uploads.
    """

    template_name = 'scifinder.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """
        Return a view with an empty form for uploading new scifinder files
        in addition to a list of scifinder files available to the current user.
        """
        files_list = Upload.objects.filter(uploaded_by=request.user)
        return render(request, self.template_name,
                      {'form': UploadForm(), 'files': files_list})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """Process the post request with a new scifinder file upload."""
        form = UploadForm(request.POST, self.request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.uploaded_by = request.user
            file.save()
            data = {'is_valid': True, 'name': file.file.name, 
                    'url': file.file.url}
        else:
            data = {'is_valid': False}

        return JsonResponse(data)