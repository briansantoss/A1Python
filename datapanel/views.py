import csv
from shutil import rmtree
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings


@login_required(login_url='login')
def data_panel(request):
    return render(request, 'data_panel/data_panel.html')