# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import RestHealth

# Create your views here.

def results(request, facility_name):
    rst = get_object_or_404(RestHealth, facility_name=facility_name)
    return render(request, 'inspectData/details.html',
                  {'pass/fail': rst.inspection_status})
